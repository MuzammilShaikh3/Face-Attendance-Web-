import cv2
# from flask import request

path = 'Training_images'
cam = cv2.VideoCapture(0)
cv2.namedWindow("Enroll")
# img_counter = 0
# n= input("Enter Name: ")
m=0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Enroll", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "{}.png".format(m)
        cv2.imwrite(f'{path}/{img_name}', frame)
        print("{} written!".format(img_name))
        m=m+1


cam.release()

cv2.destroyAllWindows()
