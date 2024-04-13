from typing import Dict
import os
from roboflow import Roboflow
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("API", None)
root_dir = os.path.dirname(os.path.abspath(__file__)).replace("/ai", "")
folder = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "static",
)

def go_to_ai(image) -> Dict:
    rf = Roboflow(api_key=api)
    project = rf.workspace().project("museum-objects")
    model = project.version(1).model
    model.predict(f'{folder}/{image}', confidence=40, overlap=30).save(f'{folder}/new_{image}')
    info = model.predict(f'{folder}/{image}', confidence=40, overlap=30).json()
    os.remove(f'{folder}/{image}')
    return info