import os
import pandas as pd
from ai.model import go_to_ai
from data import data_lang

def make_csv():
    static = os.listdir("images")
    columns = ['object_id', 'group', 'img_name']
    data = []
    count = 0
    for name in static:
        if count > 2000:
            break
        images = os.listdir("images" + "/" + name)
        try:
            for image in images:
                    path = name + "/" + image
                    info = go_to_ai(path)
                    if len(info["predictions"]) > 0:
                        data.append([name, data_lang[info["predictions"][0]["predictions"][0]["class"]],image])
        except Exception as exc:
            print(str(exc))
        count += 1
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(r'trained1.csv', sep = ';', encoding = 'utf-8', index = False)

if __name__ == "__main__":
    make_csv()