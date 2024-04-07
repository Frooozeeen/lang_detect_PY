def detect_language(input_text):
    # Counters for English and German words
    english_count = 0
    german_count = 0

    # Read English words from file
    with open('D:\Projects\python\LANGUAGE DETEXTTOR\data\lang\english.txt', 'r', encoding='utf-8') as english_file:
        english_words = set(english_file.read().splitlines())

    # Read German words from file
    with open('D:\Projects\python\LANGUAGE DETEXTTOR\data\lang\german.txt', 'r', encoding='utf-8') as german_file:
        german_words = set(german_file.read().splitlines())

    # Split input text into words and check language
    words = input_text.split()
    for word in words:
        if word.lower() in english_words:
            english_count += 1
        elif word.lower() in german_words:
            german_count += 1

    # Determine the language with the highest count
    if english_count > german_count:
        return "English"
    elif german_count > english_count:
        return "German"
    else:
        return "Unknown"  # If counts are equal or no recognized words found


# Example usage:
user_input = input("Enter text: ")
language = detect_language(user_input)
print("Detected language:", language)
