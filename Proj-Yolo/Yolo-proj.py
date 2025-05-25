from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8l.pt')
result = model("Images/3.png",show=True)
cv2.waitKey(0)