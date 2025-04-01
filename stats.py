def num_of_words(string):
    list = string.split()
    num_words = len(list)
    return num_words

def count_characters(string):
    string = string.lower()
    num_of_chars = {}
    for i in range(0, len(string)):
        if string[i] in num_of_chars:
            num_of_chars[string[i]] += 1
        else:
            num_of_chars[string[i]] = 1
    return num_of_chars 

def sort_on(dict):
    return dict["num"]

def sort_list(dict_of_chars_and_counts):
    list = []
    for element in dict_of_chars_and_counts:
        list.append({"char": element, "num": dict_of_chars_and_counts[element]})
    list.sort(reverse=True, key=sort_on)
    return list

