from typing import Dict
import os
from roboflow import Roboflow
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("API", None)
root_dir = os.path.dirname(os.path.abspath(__file__)).replace("/ai", "")
folder = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "images",
)

def go_to_ai(image) -> Dict:
    rf = Roboflow(api_key=api)
    project = rf.workspace().project("museum-xvhrs")
    model = project.version(1).model
    info = model.predict(f'{folder}/{image}').json()
    return info