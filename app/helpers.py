from typing import Dict
from ai.model import go_to_ai

def recognize_static(file) -> Dict:
    return go_to_ai(file)