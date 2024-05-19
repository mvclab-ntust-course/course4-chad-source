from ultralytics import YOLO


model = YOLO("yolov8n.pt")
model.track(source="C:\\Users\\User\\Downloads\\argoverse.mp4", show=True, save=True, classes=[2])