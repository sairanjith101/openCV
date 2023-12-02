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

# Rotate Operation

(h, w) = image_rgb.shape[:2]

c = (w/2, h/2)

angle = 90

m = cv2.getRotationMatrix2D(c, angle, 1.0)
rotate_90 = cv2.warpAffine(image_rgb, m, (w, h))

plt.imshow(rotate_90)
plt.show()