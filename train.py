from ultralytics import YOLO
model =YOLO("yolov8m.pt")

model.train(data="data_custom.yaml", batch=8, imgsz=640, epoch=100, workers=1)