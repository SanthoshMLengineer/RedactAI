def format_text(raw_text):
    """
    This function takes in raw text and formats it into a structured format for training a NER model.
    It identifies the question and answer parts of the text, splits them into tokens, and detects entities by comparing the question and answer tokens.
    """
    try:
        splits = raw_text.split("[/INST]")
        for split in splits:
            if "[INST]" in split:
                question = split.split("[INST]")[1].strip()
                print("Question:", question)
            else:
                split = split.replace("</s>", "").strip()
                print("Answer:", split)

        entities = []

        question_split = question.split()
        answer_split = split.split()

        print("Question Split:", question_split)
        print("Answer Split:", answer_split)

        question_index = 0
        answer_index = 0

        word_entity = []
        while question_index+1 < len(question_split) and answer_index+1 < len(answer_split):
            if question_split[question_index] == answer_split[answer_index]:
                question_index += 1
                answer_index += 1
            else:
                if question_split[question_index+1] == answer_split[answer_index+1]:
                    # entities[answer_split[answer_index]].append(question_split[question_index])
                    word_entity.append(question_split[question_index])
                    word_entity.append(answer_split[answer_index])

                    full_word_entity = " ".join(word_entity[:-1])
                    start_index = question.find(full_word_entity)
                    if start_index == -1:
                        print("Error: Entity not found in question:", full_word_entity)
                        word_entity = []
                        question_index += 1
                        answer_index += 1
                        continue
                    end_index = start_index + len(full_word_entity)

                    #print("Entity Detected:", full_word_entity, "Start Index:", start_index, "End Index:", end_index, "Label:", "FULLNAME", "word", question[start_index:end_index+1])
                    ent = word_entity[-1].replace("[", "").replace("]", "").replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("'", "").replace('s', "")
                    entities.append((start_index, end_index, ent))
                    word_entity = []
                    question_index += 1
                    answer_index += 1
                else:
                    word_entity.append(question_split[question_index])
                    question_index += 1
        
        return (question, {"entities": entities})
    except Exception as e:
        print("Error processing text:", e)
        return False
    