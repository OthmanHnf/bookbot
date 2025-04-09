def number_of_words(text):
    return len(text.split())

def number_of_characters(text):
    characters_count = {}
    for character in text:
        if character.lower() in characters_count:
            characters_count[character.lower()] += 1
        else:
            characters_count[character.lower()] = 1
    return characters_count

def sort_with(dict):
    return dict["count"]

def get_sorted_list(characters_count):
    new_list = []
    for char, count in characters_count.items():
        new_list.append({"char": char, "count": count})
    new_list.sort(key=sort_with, reverse=True)
    return new_list