from ultralytics import YOLO
model= YOLO("yolov8_custom.pt")
model.predict(source="1.jpeg" ,)