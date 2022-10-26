import cv2
import cv2.aruco as aruco
 
 
cap = cv2.VideoCapture(0)
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #print(frame.shape) #480x640
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
 
    #print(parameters)
 
    '''    detectMarkers(...)
        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
        mgPoints]]]]) -> corners, ids, rejectedImgPoints
        '''
        #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    # print(corners)
 
    #It's working.
    # my problem was that the cellphone put black all around it. The alrogithm
    # depends very much upon finding rectangular black blobs
    backtorgb = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
    backtorgb = aruco.drawDetectedMarkers(backtorgb, corners)

    # cv2.line(backtorgb,100,100,[255,0,0])

    # backtorgb = cv.aruco.drawAxis(	gray, cameraMatrix, distCoeffs, rvec, tvec, length	)

 
    #print(rejectedImgPoints)
    # Display the resulting frame
    cv2.imshow('frame',backtorgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()