import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("image/yellow_bus.jpg")

# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(type(image))
print(image.shape)

plt.imshow(image)
# plt.imshow(image_rgb)
plt.show()



