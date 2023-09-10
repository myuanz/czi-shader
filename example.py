import cv2
from czi_shader import CZIChannel, shading_czi

p = '/mnt/inner-data/sc-C057-146-O4213.czi'
[print(c) for c in CZIChannel.from_czi(p)]

res = shading_czi(p, scale_factor=0.01)
cv2.imwrite(p + '.png', cv2.cvtColor(res, cv2.COLOR_RGB2BGR))
