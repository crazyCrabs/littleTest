import json
import os
import re
import time
import warnings

import requests
from parsel import Selector

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78"
headers = {
    "User-Agent": user_agent,
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}


def extract_category_info(rsp: dict):
    _result = {}  # type: dict
    name_tag = []

    def extract_item_list(data: dict):
        item_list = data.get('itemList', [])
        for item in item_list:
            name_tag.append(item.get('name', ''))
            if item.get('child'):
                extract_item_list(item.get('child', [])[0])
                name_tag.pop()
            else:
                _result["".join(name_tag)] = ".".join(item.get("path", "").split(".")[2:])
                name_tag.pop()
    data = rsp.get('data', {})
    extract_item_list(data)
    return _result


def get_course_name_list(category: str, course_type: int = 1, page_num: int = 1, page_size: int = 5):
    course_list_url = f"https://basic.beijing.smartedu.cn/api/course/course_list?category={category}&type={course_type}&page_num={page_num}&page_size={page_size}"
    course_list_rsp = requests.get(course_list_url).json()
    course_list_data = course_list_rsp.get('data', {})
    print(f">>> 当前{category}类别共有{course_list_data.get('total', 0)}门课程")
    return [i.get("name") for i in course_list_data.get('dataList', [])]


def get_weike_id(course_name: str):
    """废弃使用支持不完善"""
    warnings.warn("废弃使用获取id可能会失败", DeprecationWarning)
    search_url = f"http://bdschool.cn/index.php?jsonVar=ajax&app=interface&mod=Search&act=getKnowledgeResource&keyword={course_name}&type=1&self_flag=0&page=1&num=10&token=&_={int(time.time() * 1000)}"
    search_text = requests.get(search_url, headers=headers).text.encode("utf-8").decode("unicode_escape")
    return re.findall(r'.*data":\[{"id":"(.*?)","clone_id".*', search_text)[0]


def get_course_content(weike_id: str) -> dict:
    """废弃使用支持不完善"""
    warnings.warn("获取内容可能不完善", DeprecationWarning)
    course_details_url = f"http://bdschool.cn/index.php?app=weike&mod=CloudSchool&act=weikeStudy&weike_id={weike_id}"
    course_details_rsp = requests.get(course_details_url, headers=headers)
    course_text = course_details_rsp.text
    course_html = Selector(course_text)
    # 判断是否可以直接拿到video的链接
    video_x_path = '//*[@id="video_cast"]/div[2]/video'
    video_url = course_html.xpath(video_x_path).xpath("./@src").get()
    if not video_url:
        course_text = course_text.replace(" ", "").replace("\n", "")
        video_url = re.findall(r'.*varglobal_weike_url="(.*?)";.*', course_text)[0]
    print(">>> video_url: ", video_url)
    # 获取附件的链接
    course_uls = course_html.xpath('//*[@id="course_fujian_list"]/li/a')
    download_url = 'http://bdschool.cn/index.php?app=interface&mod=Resource&act=download&id={}'
    download_urls = []
    for li in course_uls:
        _href = li.xpath("./@href").get()
        _text = li.xpath("./text()").get()
        download_urls.append((
            download_url.format(re.findall(r'.*id=(\d+).*', _href)[0]),
            _text
        ))
    print(">>> download_urls: ", download_urls)
    title = download_urls[0][1].split("-")[0]
    return {
        "video_url": video_url,
        "download_urls": download_urls,
        "title": title
    }


def new_get_course_contents(course_name: str, grade: str) -> dict:
    search_url = f"http://bdschool.cn/index.php?jsonVar=ajax&app=interface&mod=Search&act=getKnowledgeResource&keyword={course_name}&type=1&self_flag=0&page=1&num=10&token=&_={int(time.time() * 1000)}"
    search_text = requests.get(search_url, headers=headers).text.encode("utf-8").decode("unicode_escape")
    search_text = search_text.replace('var ajax=', "").replace("&quot", '').replace(
        '&gt', '').replace('&lt', '').replace('\r\n', '').replace('\\', '').replace('\t', '')
    rsp_data = json.loads(search_text)
    course_data = []
    head_url = "http://bdschool.cn"
    for data in rsp_data.get('data', []):
        _course_ware = [(f"{head_url}{i.get('download_url')}", i.get('name')) for i in data.get('courseware', [])]
        course_data.append(
            {
                "grade": data.get('grade'),
                "name": data.get('name', '').replace("?", "？"),
                "download_urls": _course_ware,
                "video_url": data.get("resources")[0].get("url")
            }
        )
    return next((data for data in course_data if data.get("grade") == grade), {})


def save_video(video_url: str, title: str, save_path: str = "./"):
    video_rsp = requests.get(video_url, headers=headers)
    with open(os.path.join(save_path, f"{title}.mp4"), "wb") as f:
        f.write(video_rsp.content)


def save_download_urls(download_urls: list, save_path: str = "./"):
    for url, name in download_urls:
        download_rsp = requests.get(url, headers=headers)
        with open(os.path.join(save_path, name), "wb") as f:
            f.write(download_rsp.content)


def download_course(course_name: str, grade: str, save_path: str = "./"):
    # weike_id = get_weike_id(course_name)
    # print(">>> weike_id: ", weike_id)
    # course_content = get_course_content(weike_id)
    course_content = new_get_course_contents(course_name, grade)
    print(f">>> 当前{course_name}的文件内容 course_content: {course_content}")
    save_video(course_content["video_url"], course_content["name"], save_path)
    save_download_urls(course_content["download_urls"], save_path)


def job(category_name: str, grade: str, save_path: str = "./"):
    course_list = get_course_name_list(category_details[category_name], page_num=1, page_size=120)
    error_course = []
    for course in course_list:
        try:
            download_course(course, grade, save_path=save_path)
        except Exception as e:
            print(f"!!!!! 下载 {course} 出错: {e}")
            error_course.append(course)
    if error_course:
        print("!@#$" * 10)
        print(f">>> 下载失败的课程: {error_course}")


if __name__ == '__main__':
    category_url = 'https://basic.beijing.smartedu.cn/api/course/category?type=1'
    category_rsp = requests.get(category_url, headers=headers).json()
    category_details = extract_category_info(category_rsp)

    # category_name = "小学三年级英语人教版上"
    grade = "高中一年级"

    categories = ["高中高一数学复习下", "高中高一数学人教A版上", "高中高一数学人教A版下"]
    categories = ["高中高一数学人教B版上", "高中高一数学人教B版下"]
    categories = ["高中高一数学人教B版下"]
    for category_name in categories:
        print(">>> 开始下载：", category_name)
        save_path = rf"D:\WORK\course\{category_name}"
        os.makedirs(save_path, exist_ok=True)
        job(category_name, grade, save_path=save_path)
