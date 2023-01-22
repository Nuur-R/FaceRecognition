import cv2

# buka kamera daan tampilkan pada layar
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break