def get_number_of_words(filename):
    with open(filename) as f:
        file_content = f.read()
    return len(file_content.split())

def get_letter_count(filename):
    with open(filename) as f:
        file_content = f.read().lower()
    letter_count = dict()
    for ch in file_content:
        if not ch.isalpha():
            continue
        if ch not in letter_count:
            letter_count[ch] = 1
        else:
            letter_count[ch] += 1
    return letter_count

def sort_on(dict):
    return dict["num"]

def dict_sort(dic):
    sort_list = []
    for key in dic:
        sort_list.append({"char": key, "num": dic[key]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list