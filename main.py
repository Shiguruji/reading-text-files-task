def read_file_content(filename):
    with open(filename) as f:
        file_text = f.read() 
        return file_text


def count_words():
    text = read_file_content("./story.txt")
    clean_text = text.translate({ ord(c): None for c in ".,?" })
    counts = dict()
    words = clean_text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

# print(count_words())