encryption = {'a': '!',
'b': "@",
'c': "#",
'd': '$',
'e': '%',
'f': '^',
'g': '&',
'h': '*',
'i': '(',
'j': ')',
'k': '_',
'l': '+',
'm': '{',
'n': '}',
'o': '[',
'p': ']',
'q': '|',
'r': '1',
's': '/',
't': ':',
'u': ';',
'v': '"',
'w': '<',
'x': '>',
'y': ',',
'z': '.',
'A': '?',
'B': '`',
'C': '~',
'D': '!',
'E': '@',
'F': '#',
'G': '$',
'H': '%',
'I': '^',
'J': '&',
'K': '*',
'L': '(',
'M': ')',
'N': '_',
'O': '+',
'P': '{',
'Q': '}',
'R': '[',
'S': ']',
'T': '||',
'U': '2',
'V': '/',
'W': '3',
'X': ';',
'Y': "'",
'Z': '4',
' ': ' '
}
readfile = open('info_security.txt', 'r')
outfile = open('encrypted.txt', 'w')

text_list = []
characters = []
new_list = []

for i in readfile:
    text_list.append(i)

for paragraph in text_list:
    for char in paragraph:
        characters.append(char)

for x in characters:
    for i in encryption:
        if i in x:
            new_list.append(encryption[i])

for i in new_list:
    outfile.write(i)

outfile.close()
