import itertools

morsecode = '.--..---..--.-.......-.-' #normaal
#morsecode = '-..--...--..-.-------.-.' #andersom
#morsecode = '.--.----..--.-.......-.-' #afhaalchinees
#morsecode = '-..-....--..-.-------.-.' #andersom
morse_code_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

letters = []
while morsecode != len(morsecode) * morsecode[0]:
    letter = input('Geef letter: ')
    substring = morse_code_dict.get(letter) #Miljuschka Witzenhausen
    if substring in morsecode:
        morsecode = morsecode.replace(substring, '/', 1)
        print(morsecode)
        letters.append(letter)
        print(letters)
    else:
        print('Deze letter kan niet meer uit de morsecode worden gehaald.')
print('Alles is uit de lijst.')