import pandas as pd
from os.path import join, dirname, abspath

import pickle

from tqdm import tqdm 
from converter.raw_to_spacy import format_text

# data folder path
BASE_DIR = dirname(abspath(__file__))
file_path = abspath(join(BASE_DIR, "..", "data", "raw_dataset.csv"))

# read raw data
data = pd.read_csv(file_path)

# convert text column to list
list_data_text = data["text"].tolist()

#print("Sample Text:", list_data_text[0])
#print("Raw Data Sample:", data.head())


if __name__ == "__main__":
    formatted_text = []
    failed_processed = []
    for text in tqdm(list_data_text):
        result = format_text(text)
        if result:
            formatted_text.append(result)
        else:
            failed_processed.append(text)

    
    formated_file_path = abspath(join(BASE_DIR, "..", "data", "train_data.pkl"))
    # save formatted data to pickle file

    print("Formatted Text Sample:", len(formatted_text))
    with open(formated_file_path, "wb") as f:
        pickle.dump(formatted_text, f)

    processed_file_path = abspath(join(BASE_DIR, "..", "data", "processed_data.csv"))
    df_processed = pd.DataFrame(formatted_text, columns=["text", "entities"])
    df_processed.to_csv(processed_file_path, index=False)

    failed_file_path = abspath(join(BASE_DIR, "..", "data", "failed_data_processed.csv"))
    df_failed = pd.DataFrame(failed_processed, columns=["text"])
    df_failed.to_csv(failed_file_path, index=False)
