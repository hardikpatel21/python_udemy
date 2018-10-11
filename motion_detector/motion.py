import cv2, time, pandas
from datetime import datetime

# store the first frame of the video in the variable to get the static background
first_frame=None
status_list=[None, None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])
# create video object to access webcam to capture video
video=cv2.VideoCapture(0)



while True:

    # create check and frame objects to check the video.read() and get the frames of images respectively
    check, frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # make the image blur for smoother results to get the delta frame
    gray=cv2.GaussianBlur(gray,(21,21),0)

    # check if first_frame is None or not
    if first_frame is None:
        first_frame=gray
        continue #this means continue from the top of the loop

    # create the delta frame image Capturing
    # absdiff checks absolute diffrence between first frame and the current frame
    delta_frame=cv2.absdiff(first_frame,gray)

    # create threshold frame with threshold value 30 and clor white(255) and THRESH_BINARY method
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # smoothen the threshold image frames
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    # find counters of the dilated frames
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.contourArea(countour) < 20000:
            continue
        status=1
        # store countour values into x, y, h,w
        (x,y,h,w)=cv2.boundingRect(countour)
        # build the rectangle using above values
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),3)

    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2]==1:
        times.append(datetime.now())

    # show the images
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1)
    # when 'q' is pressed it stops the while loop and closes the camera
    if key==ord('q'):
        times.append(datetime.now())
        break
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
# close or release the camera
video.release()
cv2.destroyAllWindows()
