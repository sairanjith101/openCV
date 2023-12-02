import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("image/yellow_bus.jpg")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(type(image))
print(image.shape)

# plt.imshow(image)
plt.imshow(image_rgb)
plt.show()


# spliting images
r,g,b = cv2.split(image_rgb)
# print('r', r.shape)
# print('g', g.shape)
# print('b', b.shape)

image_rgb = cv2.merge((r,g,b))

# Resize of image

s = 10
w = int(image_rgb.shape[1]*s/100)
h = int(image_rgb.shape[0]*s/100)
dim = (w,h)
re_size = cv2.resize(image_rgb, dim, interpolation=cv2.INTER_AREA)
print(re_size.shape)

