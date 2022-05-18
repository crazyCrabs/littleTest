import cv2
from tqdm import tqdm

from string_image import pixel2char, get_char_img

# 以下是opencv-python可以获取视频的相关信息，可以通过从0开始的序号获取
# CV_CAP_PROP_POS_MSEC 视频文件的当前位置（以毫秒为单位）或视频捕获时间戳。
# CV_CAP_PROP_POS_FRAMES 接下来要解码/捕获的帧的基于0的索引。
# CV_CAP_PROP_POS_AVI_RATIO 视频文件的相对位置：0 - 电影的开始，1 - 电影的结尾。
# CV_CAP_PROP_FRAME_WIDTH 视频流中帧的宽度。
# CV_CAP_PROP_FRAME_HEIGHT 视频流中帧的高度。
# CV_CAP_PROP_FPS 帧速率。
# CV_CAP_PROP_FOURCC 编解码器的4字符代码。
# CV_CAP_PROP_FRAME_COUNT 视频文件中的帧数。
# CV_CAP_PROP_FORMAT 返回的Mat对象的格式 retrieve() 。
# CV_CAP_PROP_MODE 指示当前捕获模式的特定于后端的值。
# CV_CAP_PROP_BRIGHTNESS 图像的亮度（仅适用于相机）。
# CV_CAP_PROP_CONTRAST 图像对比度（仅适用于相机）。
# CV_CAP_PROP_SATURATION 图像的饱和度（仅适用于相机）。
# CV_CAP_PROP_HUE 图像的色调（仅适用于相机）。
# CV_CAP_PROP_GAIN 图像的增益（仅适用于相机）。
# CV_CAP_PROP_EXPOSURE 曝光（仅适用于相机）。
# CV_CAP_PROP_CONVERT_RGB 布尔标志，指示是否应将图像转换为RGB。
# CV_CAP_PROP_WHITE_BALANCE_U 白平衡设置的U值（注意：目前仅支持DC1394 v 2.x后端）
# CV_CAP_PROP_WHITE_BALANCE_V 白平衡设置的V值（注意：目前仅支持DC1394 v 2.x后端）
# CV_CAP_PROP_RECTIFICATION 立体摄像机的整流标志（注意：目前仅支持DC1394 v 2.x后端）
# CV_CAP_PROP_ISO_SPEED摄像机 的ISO速度（注意：目前仅支持DC1394 v 2.x后端）
# CV_CAP_PROP_BUFFERSIZE 存储在内部缓冲存储器中的帧数（注意：目前仅支持DC1394 v 2.x后端）


def generate(input_video, output_video):
    # 1、读取视频
    cap = cv2.VideoCapture(input_video)

    # 2、获取视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 读取第一帧，获取转换成字符后的图片的尺寸
    ret, frame = cap.read()
    char_img = get_char_img(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 4)

    # 创建一个VideoWriter，用于保存视频
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_video, fourcc, fps,
                             (char_img.shape[1], char_img.shape[0]))
    total_time = cap.get(7) / cap.get(5) * 1000
    with tqdm(total=total_time) as pbar:
        while ret:
            # 读取视频的当前帧，如果没有则跳出循环
            ret, frame = cap.read()
            # print(f'>>> running: current frame {cap.get(1) / cap.get(5)}, current time {cap.get(0) / 1000} s , total time {cap.get(7) / cap.get(5)} s')
            # current_time = cap.get(0)
            pbar.update(42)  # 更新当前时间
            if not ret:
                break
            # 将当前帧转换成字符图
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            char_img = get_char_img(gray, 4)

            # 转换成BGR模式，便于写入视频
            char_img = cv2.cvtColor(char_img, cv2.COLOR_GRAY2BGR)
            writer.write(char_img)
        writer.release()

generate('1.mp4', 'string_1.mp4')