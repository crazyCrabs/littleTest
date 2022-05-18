import cv2
import string
import numpy as np

# show img
# img = cv2.imread('1.jpg')

# # 灰度转换
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('this is title', gray)

# # 灰度转换2
# img2 = cv2.imread('1.jpg', 0)
# cv2.imshow('this is gray 2', img2)

# # 绘制文字
# cv2.putText(img, 'nana', (200, 200),
#             cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 0), 5)

# cv2.imshow('simple show', img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# 像素与字符的计算公式 颜色值/颜色表长度(256) = 字符所在字符串的index/字符表长度
def pixel2char(pixel):
    # char_list = string.ascii_letters + ' '
    char_list = "@#$%&erytuioplkszxcv=+---.     "
    index = int(pixel / 256 * len(char_list))
    return char_list[index]

# 生成字符串图片


def get_char_img(img, scale=4, font_size=5):
    h, w = img.shape
    re_im = cv2.resize(img, (w//scale, h//scale))
    char_img = np.ones((h//scale * font_size, w//scale *
                        font_size), dtype=np.uint8) * 255
    font = cv2.FONT_HERSHEY_SIMPLEX
    for y in range(0, re_im.shape[0]):
        for x in range(0, re_im.shape[1]):
            char_pixel = pixel2char(re_im[y][x])
            cv2.putText(char_img, char_pixel, (x*font_size,
                                               y*font_size), font, 0.5, (0, 0, 0))
    return char_img

if __name__ == "__main__":
    img = cv2.imread('ice.png', 0)
    res = get_char_img(img, scale=4, font_size=5)
    cv2.imwrite('hot.png', res)