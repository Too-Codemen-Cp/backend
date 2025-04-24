from ultralytics import YOLO


model = YOLO("yolo11l.pt")

if __name__ == "__main__":
    model.train(
        data="museum-objects/data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        name="museum-objects",
        project="runs/train",
        device="cpu"
    )
