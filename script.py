import os
import csv
import pandas as pd
from ai.model import go_to_ai
from data import data_lang

def make_csv():
    static = os.listdir("images")
    columns = ['object_id', 'img_name', 'group']
    data = []
    with open('nontrain.csv', newline='', encoding="UTF-8") as f:
        reader = list(csv.reader(f, delimiter=';', quoting=csv.QUOTE_MINIMAL))
        for name in static:
            id = ''
            for row in reader[1:]:
                if name in row:
                    id = row[0]
            info = go_to_ai(name)
            data.append([id, name, data_lang[info["predictions"][0]["class"]]])
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(r'trained.csv', sep = ';', encoding = 'utf-8', index = False)

if __name__ == "__main__":
    make_csv()