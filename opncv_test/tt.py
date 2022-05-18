import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt
import time


img = scipy.misc.ascent()

plt.ion()
pic_figure = plt.figure(figsize=(4, 4))
# for degree in range(6):
degree = 1
while degree <= 360 *3:
    # plt.subplot(151+degree)
    degree *= 2
    rotated_img = ndimage.rotate(img, degree)
    plt.imshow(rotated_img, cmap=plt.cm.gray)
    plt.axis('off')
    # plt.plot()
    plt.pause(0.05)
    # plt.close(pic_figure)

plt.ioff()
plt.show()

# import pygame

# pygame.init()
# screen = pygame.display.set_mode([800, 800])
# pygame.display.set_caption('Rotating image example')
# clock = pygame.time.Clock()

# images = [r"C:\Users\tjliu\Desktop\wp\opncv_test\ice.png",
#           r"C:\Users\tjliu\Desktop\wp\opncv_test\1.jpg"]

# for img_str in images:
#     img = pygame.image.load(img_str).convert()
#     img_rect = img.get_rect(center=screen.get_rect().center)
#     degree = 0

#     while degree < 360:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()

#         # rotate image
#         rot_img = pygame.transform.rotate(img, degree)
#         img_rect = rot_img.get_rect(center=img_rect.center)

#         # copy image to screen
#         screen.fill((255, 255, 255))
#         screen.blit(rot_img, img_rect)
#         pygame.display.flip()

#         clock.tick(120)
#         degree += 1
