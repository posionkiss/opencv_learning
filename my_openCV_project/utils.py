import cv2
def cv_show(win_name,pic,col,row):
    cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(win_name,col,row)
    cv2.imshow(win_name,pic)
    key=cv2.waitKey(0)
    if key==ord('q'):
        cv2.destroyAllWindows()