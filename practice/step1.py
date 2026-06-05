raw_text = ["<s>[INST] Write a summary of the book Cormier - Friesen on child psychology theories for Junius.Crooks@gmail.com. [/INST] Write a summary of the book [NAME] on child psychology theories for [EMAIL]. </s>",
            "<s>[INST] 1. A brief history of psychoanalysis, including the contributions of Allison Wolf and Dr. Jeanette Cartwright Jr.. [/INST] 1. A brief history of psychoanalysis, including the contributions of [FULLNAME] and [FULLNAME]. </s>"]

#splits = raw_text[0].split("[/INST]")

formatted_text = []

for text in raw_text:
    splits = text.split("[/INST]")
    for split in splits:
        if "[INST]" in split:
            question = split.split("[INST]")[1].strip()
        else:
            split = split.replace("</s>", "").strip()

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
                end_index = start_index + len(full_word_entity)

                #print("Entity Detected:", full_word_entity, "Start Index:", start_index, "End Index:", end_index, "Label:", "FULLNAME", "word", question[start_index:end_index+1])
                ent = word_entity[-1].replace("[", "").replace("]", "").replace(".", "").replace(",", "")
                entities.append((start_index, end_index, full_word_entity, ent))
                question_index += 1
                answer_index += 1
            else:
                word_entity.append(question_split[question_index])
                question_index += 1

    print(question_index, answer_index, len(question_split), len(answer_split))
        
    formatted_text.append((question, {"entities": entities}))

    
print(formatted_text)