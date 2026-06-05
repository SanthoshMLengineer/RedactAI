def find_entity_from_diff(q_tokens, a_tokens):
    entities = []

    i = 0
    while i < len(q_tokens) and i < len(a_tokens):

        # SAME → move forward
        if q_tokens[i] == a_tokens[i]:
            i += 1
            continue

        # DIFFERENCE STARTS → entity detected
        start = i

        # skip until tokens match again
        while i < len(q_tokens) and i < len(a_tokens) and q_tokens[i] != a_tokens[i]:
            i += 1

        end = i

        entity_tokens = q_tokens[start:end]
        entity_text = " ".join(entity_tokens)

        entities.append(entity_text)

    return entities

raw_text = ["<s>[INST] I need a summary of the book Existential Therapy: 100 Key Points and Techniques for Van Kilback. Can you help? [/INST] I need a summary of the book Existential Therapy: 100 Key Points and Techniques for [FULLNAME]. Can you help? </s>",
            "<s>[INST] Please write a review of the book The Developing Mind by Daniel J. Siegel for Mr. Glen Padberg to share on their social media. [/INST] Please write a review of the book The Developing Mind by Daniel J. Siegel for [FULLNAME] to share on their social media. </s>",
            "<s>[INST] Please write a review of the book The Happiness Advantage by Shawn Achor for Gloria Reichert to post on their website. [/INST] Please write a review of the book The Happiness Advantage by Shawn Achor for [FULLNAME] to post on their website. </s>"]

#splits = raw_text[0].split("[/INST]")

formatted_text = []

for text in raw_text:
    splits = text.split("[/INST]")
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

    print(find_entity_from_diff(question_split, answer_split))