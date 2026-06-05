def format_output(text: str, documents):
    """
    """
    try:
        ouput_json = {
            "text": text,
            "redacted_text": "",
            "entities": []
        }
        text_copy = text
        for ent in documents.ents:
            ouput_json["entities"].append({
                "text": ent.text,
                "label": ent.label_
            })
            text_copy = text_copy.replace(ent.text, "["+str(ent.label_)+"]")
        ouput_json["redacted_text"] = text_copy
        return ouput_json
    except Exception as e:
        ouput_json = {
            "text": text,
            "entities": []
        }
        print(e)
        return ouput_json