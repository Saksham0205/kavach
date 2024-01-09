from ultralytics import YOLO
model= YOLO("yolov8_custom.pt")
model.predict(source="image_path" ,conf=0.5,show=True, save=True)
