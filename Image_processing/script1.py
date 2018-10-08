import cv2

img=cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print (img.shape)

print(img.ndim)

# resise the image
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# display image
cv2.imshow("Galaxy", resized_image)
# store resized image into new file
cv2.imwrite("Galaxy_resized.jpg", resized_image)
# if you put 0 in place of 200 it will close window by pressing any keybord key
cv2.waitKey(0)
cv2.destroyAllWindows()
