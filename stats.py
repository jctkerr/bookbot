def get_num_words(text):
    """
    Write a new function that accepts the text from the book as a string, and returns the number of words in the string. The .split() method will be helpful here.
    """
    if text is None:
        return 0
    words = text.split()
    return len(words)

def get_char_count(text):
    """
    Takes the text from the book as a string, and returns the number of times each character appears in the string.
    """
    if text is None:
        return {}
    
    char_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in char_count:
            char_count[char_lower] += 1
        else:
            char_count[char_lower] = 1
    
    return char_count


def sort_char_count(char_count):
    """
    Takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
    Each dictionary has two key-value pairs: one for the character itself and one for that character's count.
    Sorts the list from greatest to least by the count.
    """
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list