from ultralytics import YOLO

model = YOLO("TODO")

def predict_img(image: str) -> list:
    results = model(image, save=True)
    return results