import cv2
img=cv2.imread("love.jpg")
new1=cv2.pyrDown(img)
new2=cv2.pyrDown(new1)
new3=cv2.pyrDown(new2)
# new4=cv2.pyrDown(new3)
big=cv2.pyrUp(new3)
big2=cv2.pyrUp(big)

cv2.imshow("new1",big2)
# cv2.imshow("new2",new2)
# cv2.imshow("new3",new3)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()