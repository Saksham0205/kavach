from ultralytics import yolo 
model=yolo("yolov8m.pt")
model.train(data="data_custom.yaml",batch=8, imgsz=640 , epochs=11 ,workers=1)