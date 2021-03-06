import numpy as np
import cv2

cap = cv2.VideoCapture(1)
img_id=0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('/home/sriharsha/igvc/VO-master/kernel_sample/images2/'+str(img_id).zfill(6)+'.png',frame)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    img_id=img_id+1;
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
