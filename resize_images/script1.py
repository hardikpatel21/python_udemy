import cv2
import glob

# get all .jpg file names as a list in the project or current folder
images=glob.glob("*.jpg")

# go through all the files
for image in images:
    # read all image in the list images
    img=cv2.imread(image,0)
    # resize the image
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
