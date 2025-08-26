def number_words(file_text):
    words = file_text.split()
    return f"Found {len(words)} total words"
  
def num_unique_characters(text):
    text = text.lower()
    list_of_characters = dict()
    for char in text:
        if char in list_of_characters:
            list_of_characters[char] = list_of_characters[char] + 1
        if char not in list_of_characters:
            list_of_characters[char] = 1
    
    return list_of_characters
    

def sort_on(items):
    return items["num"]

def ret_list(dict):
    new_list = []
    for char in dict:
        new_list.append({"char" : char, "num" : dict[char]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list


def print_report(path_to_book):
    print("============ BOOKBOT ============ \nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(number_words(get_book_text(path_to_book)))
    print("--------- Character Count -------")
    new_dict = num_unique_characters(get_book_text(path_to_book))
    new_list = ret_list(new_dict)
    for item in new_list:
        if item["char"].isalpha():
            print(item["char"] + ": " + str(item["num"]))
    print("============= END ===============")

def get_book_text(file_path):
    file_content = ""
    with open(file_path) as file:
        file_content = file.read()
    return file_content  
