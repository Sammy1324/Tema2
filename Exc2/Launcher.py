def format_text(input_text):
    # Split the input text into sentences using '#' as the delimiter
    sentences = input_text.split('#')
    
    # Capitalize the first letter of each sentence and add appropriate punctuation
    formatted_sentences = []
    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if i == 0:
            # First sentence ends with "..."
            formatted_sentences.append(sentence.capitalize() + "...")
        else:
            # Other sentences end with "."
            formatted_sentences.append(sentence[0].upper() + sentence[1:] + ".")
    
    # Join the formatted sentences with a newline
    return "\n\n".join(formatted_sentences)