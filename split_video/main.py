from concurrent.futures import ThreadPoolExecutor, wait
from pathlib import Path

from moviepy.editor import VideoFileClip
from tqdm import tqdm


def run(
    video_file: str,
    segment_length: int,
    project_name: str,
    first_skip_time: int,
    use_thread: bool = True,
    max_workers: int = 6,
):
    """分割视频

    Args:
        video_file (str): 视频所在绝对路径
        segment_length (int): 片段间隔，单位秒
        project_name (str): 项目名称
    """
    p_path = Path(video_file).parent
    output_path = p_path / "output" / project_name
    output_path.mkdir(parents=True, exist_ok=True)
    # 打开视频文件
    clip = VideoFileClip(video_file)
    # 获取视频的总时长，单位是秒
    total_time = clip.duration
    # 计算片段的数量
    num_segments = int(total_time / segment_length)
    # 创建一个进度条
    pbar = tqdm(total=num_segments)

    # 定义一个函数来处理每个片段
    total_subclip = []

    for i in range(num_segments):
        start_time = i * segment_length
        if i == 0:
            start_time = first_skip_time
        end_time = (i + 1) * segment_length
        total_subclip.append((i, start_time, end_time))
        if not use_thread:
            subclip = clip.subclip(start_time, end_time)
            save_file_path = str(output_path / f"p_{i}.mp4")
            subclip.write_videofile(save_file_path)
            pbar.update(1)

    def save2file(i, start_time, end_time):
        clip = VideoFileClip(video_file)
        subclip = clip.subclip(start_time, end_time)
        save_file_path = str(output_path / f"p_{i}.mp4")
        subclip.write_videofile(save_file_path)
        pbar.update(1)

    if use_thread:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            tasks = [executor.submit(save2file, i, s, e) for i, s, e in total_subclip]
            done, _ = wait(tasks)
            if len(done) != len(tasks):
                print("任务失败")

    # 如果视频的总时长不能被片段的长度整除，那么最后还会剩下一部分
    if total_time % segment_length != 0:
        start_time = num_segments * segment_length
        subclip = clip.subclip(start_time, total_time)
        save_file_path = str(output_path / f"p_{num_segments}.mp4")
        subclip.write_videofile(save_file_path)

    pbar.close()


if __name__ == "__main__":
    run(r"D:\video\电影\海王2：失落的王国.mp4", segment_length=60 * 6, project_name="失落的王国", first_skip_time=32)
    # run(r"D:\video\电影\output\万圣节的新娘\p_0.mp4", segment_length=60, project_name="test")  # 3.07
    # run(r"D:\video\电影\output\万圣节的新娘\p_0.mp4", segment_length=60, project_name="test", use_thread=False)  # 3.07
