import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text(book_filepath):
    """
    Write a new function called get_book_text. It takes a filepath as input and returns the contents of the file as a string.
    """
    if book_filepath is None:
        return None
    try:
        with open(book_filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {book_filepath}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    text = get_book_text(book_path)
    if text:
        num_words = get_num_words(text)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        
        char_counts = get_char_count(text)
        sorted_chars = sort_char_count(char_counts)
        
        print("--------- Character Count -------")
        for char_dict in sorted_chars:
            if char_dict["char"].isalpha():
                print(f"{char_dict['char']}: {char_dict['num']}")
        
        print("============= END ===============")

if __name__ == "__main__":
    main()