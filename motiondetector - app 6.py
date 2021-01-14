import cv2, time, pandas
from datetime import datetime

video=cv2.VideoCapture(1)
first_frame=None
status_list=[None, None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

while True:
    status=0
    check, frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=3)

    (cnts,_) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contours in cnts:
        if cv2.contourArea(contours) < 1000:
            continue
        status = 1
        (x,y,w,h)=cv2.boundingRect(contours)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,355,0), 3)
    
    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())


    cv2.imshow("Gray",gray)
    cv2.imshow("Delta",delta_frame)
    cv2.imshow("Threshold",threshold_frame)
    cv2.imshow("Final1", frame)

    key=cv2.waitKey(1)

    if key==ord("q"):
        if status==1:
            times.append(datetime.now())
        break 
print(status_list)
print(times)

for i in range(0,len(times),2):
            df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
video.release() 
cv2.destroyAllWindows()

#print(check)
#print(frame)