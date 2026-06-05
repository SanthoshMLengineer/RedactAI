import pandas as pd
from os.path import join, dirname, abspath

import pickle

from validators.annotation_validator import validated_formatted_data

# data folder path
BASE_DIR = dirname(abspath(__file__))
file_path = abspath(join(BASE_DIR, "..", "data", "train_data.pkl"))

# read raw data
with open(file_path, "rb") as f:
    data = pickle.load(f)

print("Sample Formatted Data:", data[0:5])

if __name__ == "__main__":
    list_failed_data = []
    for item in data:
        result = validated_formatted_data(item)
        if not result:
            list_failed_data.append(item)
        else:
            continue
    
    print("Failed Samples:", len(list_failed_data))
    dataframe = pd.DataFrame(list_failed_data, columns=["text", "entities"])
    csv_file_path = abspath(join(BASE_DIR, "..", "data", "failed_data.csv"))
    dataframe.to_csv(csv_file_path, index=False)



