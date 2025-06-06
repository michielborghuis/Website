from itertools import permutations

#morsecode = '.--..---..--.-.......-.-' #normaal
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


perm = permutations(['N', 'A', 'T', 'H', 'A', 'N', 'D', 'E', 'M', 'L'])
counter = 0
for i in list(perm):
    morsecode = '.--..---..--.-.......-.'  # normaal
    count = 0
    while count != 10:
        letter = i[count]
        substring = morse_code_dict.get(letter) #Miljuschka Witzenhausen
        if substring in morsecode:
            morsecode = morsecode.replace(substring, '/', 1)
        count += 1
    if morsecode == len(morsecode) * morsecode[0]:
        #print(i)
        counter += 1
print(counter)