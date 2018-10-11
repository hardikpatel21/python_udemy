import cv2, time

# create video object to access webcam to capture video
video=cv2.VideoCapture(0)

# calculate the number of frames generated
a = 0

while True:
    a = a + 1
    # create check and frame objects to check the video.read() and get the frames of images respectively
    check, frame = video.read()



    print(check)
    print(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # keep camera open for 3 seconds
    # time.sleep(3)

    # show the images
    cv2.imshow("Capturing", gray)


    key=cv2.waitKey(1)

    # when 'q' is pressed it stops the while loop and closes the camera
    if key==ord('q'):
        break

print("Number of frames generated: ",a)
# close or release the camera
video.release()
cv2.destroyAllWindows()
