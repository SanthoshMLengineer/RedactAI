import os
from os.path import join, dirname, abspath

import spacy

from format_predicted_output import format_output

model_folder = dirname(dirname(abspath(__file__)))
model_path = abspath(join(model_folder, "models", "model-best"))

model = spacy.load(model_path)
default_model = spacy.load("en_core_web_sm")

def get_prediction(text: str):
    """
    """
    try:
        doc = model(text)
        if len(doc.ents) == 0:
            doc = default_model(text)
        format_output_text = format_output(text, doc)
        return format_output_text
    except Exception as e:
        print(e)
        ouput_json = {
            "text": text,
            "entities": []
        }
        print(e)
        return ouput_json

