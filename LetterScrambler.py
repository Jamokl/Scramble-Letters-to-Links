import random

# Alle verfügbaren Buchstaben für die Generierung der URL
letters = "mllwstnhbo1urktlvcolweiomaspwcte"

# Mögliche Wortgruppen, die in der URL enthalten sein könnten
possible_inclusions = ["console", "ours", "vil1"]

# Funktion, um eine zufällige URL zu generieren, die eine der Wortgruppen enthält
def generate_random_url_with_inclusions(letters, inclusions):
    for inclusion in inclusions:
        if all(letter in letters for letter in inclusion):
            # Entferne die Buchstaben der Einfügung aus dem verfügbaren Buchstabenpool
            for letter in inclusion:
                letters = letters.replace(letter, '', 1)
            break
    else:
        # Wenn keines der Wörter passt, verwende das erste Wort als Standard
        inclusion = inclusions[0]
        for letter in inclusion:
            letters = letters.replace(letter, '', 1)
            
    # Mischen der verbleibenden Buchstaben für die zufällige Anordnung
    letters_list = list(letters)
    random.shuffle(letters_list)
    
    # Zusammensetzen der URL
    shuffled_letters = ''.join(letters_list)
    url = f"https://www.{shuffled_letters}.com/{inclusion}"
    
    return url

# Anzahl der zu generierenden URLs
num_urls = 300

# URLs generieren
random_urls_with_inclusions = [generate_random_url_with_inclusions(letters, possible_inclusions) for _ in range(num_urls)]

# Dateinamen festlegen
filename = "links.txt"

# Die generierten URLs in eine Datei schreiben
with open(filename, 'w') as file:
    for url in random_urls_with_inclusions:
        file.write(url + "\n")

# Information ausgeben, wo die Datei gespeichert wurde
print(f"URLs wurden in die Datei {filename} geschrieben.")
