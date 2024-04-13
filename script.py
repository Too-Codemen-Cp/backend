import os
import pandas as pd
from ai.model import go_to_ai
def make_csv():
    static = os.listdir("static")
    columns = ['object_id', 'object_name', 'group']
    data = []
    for name in static:
        info = go_to_ai(name)
        data.append(["", name, info["predictions"][0]["class"]])
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(r'trained.csv')

if __name__ == "__main__":
    make_csv()