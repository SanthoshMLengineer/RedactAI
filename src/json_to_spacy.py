import ast
from os.path import dirname, join, abspath

import pickle

import pandas as pd
from tqdm import tqdm

import spacy
from spacy.tokens import DocBin

# data folder path
BASE_DIR = dirname(abspath(__file__))
file_path = abspath(join(BASE_DIR, "..", "data", "cleaned_ner_data.csv"))


def load_csv_data(file_path):
    df = pd.read_csv(file_path)

    train_data = []

    for _, row in df.iterrows():
        text = row["text"]

        # convert string dict → python dict safely
        annot = ast.literal_eval(row["entities"])

        train_data.append((text, annot))

    return train_data


def convert_to_docbin(train_data):
    """
    This function takes in the raw data and formats it into the spacy format.
    Args:
        train_data: list of tuples containing the text and the entities
    Returns: None
    """
    # load the spacy model
    nlp = spacy.load("en_core_web_sm") 
    #print(nlp.pipe_names)
    
    # create a DocBin object to store the processed documents 
    db = DocBin() 
    processed_count = 0
    failed_count = 0
    for text, annot in tqdm(train_data): # data in previous format
        try:
            doc = nlp.make_doc(text) # create doc object from text
            ents = []
            for start, end, label in annot["entities"]: # add character indexes
                span = doc.char_span(start, end, label=label, alignment_mode="contract")
                if span is None:
                    print("Skipping entity")
                else:
                    ents.append(span)
            doc.ents = ents # label the text with the ents
            db.add(doc)
            processed_count += 1
        except Exception as e:
            print("Error processing text:", e)
            print("Text:", text)
            print("Annot:", annot)
            failed_count += 1
            continue

    print(f"Processed {processed_count} documents, failed to process {failed_count} documents.")
    spacy_filepath = abspath(join(BASE_DIR, "..", "data", "train_data.spacy"))
    db.to_disk(spacy_filepath) # save the docbin object


if __name__ == "__main__":
    train_data = load_csv_data(file_path)
    convert_to_docbin(train_data)


