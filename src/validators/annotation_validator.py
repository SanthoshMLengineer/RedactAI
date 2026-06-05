def validated_formatted_data(formatted_data):

    # if single sample is passed, wrap it
    if isinstance(formatted_data, tuple):
        formatted_data = [formatted_data]

    print("Validating formatted data...")

    for item in formatted_data:

        if not isinstance(item, tuple) or len(item) != 2:
            print(f"Invalid sample format: {item}")
            return False

        question, data = item

        if not isinstance(data, dict):
            print(f"Data must be dict: {data}")
            return False

        entities = data.get("entities", [])

        print(f"\nValidating text: {question}")
        print(f"Entities: {entities}")

        for entity in entities:

            # check tuple format
            if not isinstance(entity, tuple) or len(entity) != 3:
                print(f"Invalid entity format: {entity}")
                return False

            start, end, label = entity

            # type checks
            if not isinstance(start, int) or not isinstance(end, int):
                print(f"Non-integer span: {entity}")
                return False

            if start >= end or start < 0 or end > len(question):
                print(f"Invalid span (start >= end): {entity}")
                return False

    return True

#print(validated_formatted_data(("The F15 aircraft uses a lot of fuel", {"entities": [(4, 7, 'aircraft', 'AIRCRAFT')]})))

