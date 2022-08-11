import os
import ntpath
import shutil
import time
import zipfile

from watchdog.events import *
from watchdog.observers import Observer


def get_filename(filepath):
    return ntpath.basename(filepath)


class FileMoveHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()

    def on_created(self, event):
        if event.is_directory:
            print(f"directory created: {event.src_path}")
        else:
            print(f"file created: {event.src_path}")
            filename = get_filename(event.src_path)
            if filename in watch_tags:
                self.start(filename)

    def on_modified(self, event):
        if event.is_directory:
            print(f"directory modified: {event.src_path}")
        else:
            print(f"file modified: {event.src_path}")
            filename = get_filename(event.src_path)
            if filename in watch_tags:
                self.start(filename)

    def start(self, filename):
        try:
            filename_without_ext = filename.split('.')[0]
            source_file_path = f"{watch_folder}/{filename}"
            target_file_path = f"{target_folder}/{filename}"
            target_project_path = f"{target_folder}/{filename_without_ext}"
            print(f"拷贝源目录：{source_file_path}，目标文件夹：{target_folder}")
            if os.path.exists(target_file_path):
                os.remove(target_file_path)
            shutil.move(source_file_path, target_folder)
            if os.path.exists(target_project_path):
                shutil.rmtree(target_project_path, ignore_errors=True)
        except Exception as e:
            print(e)


class FileUnZipHandler(FileMoveHandler):
    def __init__(self) -> None:
        super().__init__()

    def start(self, filename):
        filename_without_ext = filename.split('.')[0]
        target_file_path = f"{target_folder}/{filename}"
        target_project_path = f"{target_folder}/{filename_without_ext}"
        if r := zipfile.is_zipfile(target_file_path):
            fz = zipfile.ZipFile(target_file_path, 'r')
            for file in fz.namelist():
                fz.extract(file, target_project_path)
        else:
            print(f"{target_file_path} is not a zip file")


if __name__ == "__main__":
    watch_tags = ['proj1.zip', 'proj2.zip', 'proj3.zip', 'proj4.zip']
    watch_folder = r"C:\Users\tjliu\Desktop\wp\littleTest\watchdog_test\tmp"
    target_folder = r"C:\Users\tjliu\Desktop\wp\littleTest\watchdog_test\object"

    watch_server = Observer()

    move_handler = FileMoveHandler()
    unzip_handler = FileUnZipHandler()

    watch_server.schedule(move_handler, watch_folder, recursive=True)
    watch_server.schedule(unzip_handler, target_folder, recursive=True)
    watch_server.start()
    try:
        print("start watching...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt, exiting...")
        watch_server.stop()
    watch_server.join()
