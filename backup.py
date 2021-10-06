import cv2
def snapshot():
    cameraObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=cameraObject.read()
        cv2.imwrite("richelle.png",frame)
        result=False


    cv2.destroyWindow() 
snapshot()