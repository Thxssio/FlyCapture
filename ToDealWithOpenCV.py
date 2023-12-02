import cv2

print('bayer_fmt:', frame['bayer_fmt'])
img = cv2.cvtColor(arr, cv2.COLOR_BayerBGGR2BGR)  
cv2.imshow('image', img)
cv2.waitKey(0)
