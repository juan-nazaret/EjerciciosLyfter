
def sort_list(path):
    with open(path, 'r', encoding = 'utf-8') as file:    
        lines = file.readlines()
        lines.sort()

    return lines 
    

def songs_v2(path, text):
    with open(path, 'w', encoding = 'utf-8') as file:
        for number, line in enumerate(text, start=1):
            file.write(f"\n {number} {line.strip()} ") 
            


def print_songs2(path):
    with open(path, 'r', encoding='utf-8') as file:
        document = file.read()
    return document


text = sort_list("songs.txt")
print(songs_v2("songs2.txt", text))
print(print_songs2('songs2.txt'))