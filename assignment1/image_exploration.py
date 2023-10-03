import numpy as np
import cv2 
import matplotlib.pyplot as plt

# entire output in console
import sys
np.set_printoptions(threshold=sys.maxsize)

# --- --- --- 

cat_img = cv2.imread("/Users/drozd/cs231n.github.io/assignments/2023/files/photo-of-kitty.jpeg")
# print(cat_img.shape) # (667, 1000, 3)

# https://stackoverflow.com/questions/23853632/which-kind-of-interpolation-best-for-resizing-image/51042104#51042104
cat_img_res = cv2.resize(cat_img, dsize=(32, 32), interpolation=cv2.INTER_AREA)
# print(cat_img_res.shape) # (32, 32, 3)

# flatten into 2D to 1D
cat_img_res_flat = cat_img_res.flatten()
print(cat_img_res_flat)

plt.imshow(cat_img_res)
plt.show()