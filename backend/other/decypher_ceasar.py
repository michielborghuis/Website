def encode(message, shift, alphabet):
    result = ''
    for symbol in message.lower():
        if symbol in alphabet:
            result += alphabet[alphabet.index(symbol) - (26 - shift)]
        else:
            result += symbol
    return result


def decode(message, shift, alphabet):
    result = ''
    for symbol in message:
        if symbol in alphabet:
            result += alphabet[alphabet.index(symbol) - shift]
        else:
            result += symbol
    return result


def break_caesar(message):
    d = {'e': 11.1607, 'a': 8.4966, 'r': 7.5809, 'i': 7.5448, 'o': 7.1635, 't': 6.9509, 'n': 6.6544, 's': 5.7351, 'l': 5.4893, 'c': 4.5388, 'u': 3.6308, 'd': 3.3844, 'p': 3.1671, 'm': 3.0129, 'h': 3.0034, 'g': 2.4705, 'b': 2.0720, 'f': 1.8121, 'y': 1.7779, 'w': 1.2899, 'k': 1.1016, 'v': 1.0074, 'x': 0.2902, 'z': 0.2722, 'j': 0.1965, 'q': 0.1962}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for key, value in d.items():
        d[key] = value / 100

    errors = []
    for shift in range(26):
        temp_message = decode(message, shift, alphabet)
        d_shift = {}
        for letter in alphabet:
            d_shift[letter] = 1
        for letter in temp_message:
            if letter in alphabet:
                d_shift[letter] += 1

        value_sum_shift = sum(d_shift.values())
        for key, value in d_shift.items():
            d_shift[key] = value / value_sum_shift

        error = 0
        for letter in alphabet:
            error += (d[letter] - d_shift[letter])**2
        errors.append(error)
    return errors


text = 'I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father ' \
       'teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in ' \
       'school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from ' \
       'Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food! My ' \
       'family is very important to me. We do lots of things together. My brothers and I like to go on long walks in ' \
       'the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. ' \
       'We laugh and always have a good time. I love my family very much. '

decrypted_text = 'p spcl pu h ovbzl ulhy aol tvbuahpuz. p ohcl adv iyvaolyz huk vul zpzaly, huk p dhz ivyu shza. tf ' \
                 'mhaoly alhjolz thaolthapjz, huk tf tvaoly pz h ubyzl ha h ipn ovzwpahs. tf iyvaolyz hyl clyf zthya ' \
                 'huk dvyr ohyk pu zjovvs. tf zpzaly pz h ulycvbz npys, iba zol pz clyf rpuk. tf nyhuktvaoly hszv ' \
                 'spclz dpao bz. zol jhtl myvt pahsf dolu p dhz adv flhyz vsk. zol ohz nyvdu vsk, iba zol pz zapss ' \
                 'clyf zayvun. zol jvvrz aol ilza mvvk! tf mhtpsf pz clyf ptwvyahua av tl. dl kv svaz vm aopunz ' \
                 'avnlaoly. tf iyvaolyz huk p sprl av nv vu svun dhsrz pu aol tvbuahpuz. tf zpzaly sprlz av jvvr dpao ' \
                 'tf nyhuktvaoly. vu aol dllrlukz dl hss wshf ivhyk nhtlz avnlaoly. dl shbno huk hsdhfz ohcl h nvvk ' \
                 'aptl. p svcl tf mhtpsf clyf tbjo. '


def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # emma = open('emma.txt').read()
    # decrypted_emma = decode(emma, 4, alphabet)

    test = 'Je moeder'
    decrypted_test = decode(test, 8, 'abcdefghijklmnopqrstuvwxyz')
    print(decrypted_test)

    errors = break_caesar(decrypted_test)
    minimum = min(errors)
    minimum_shift = errors.index(minimum)
    for shift in range(26):
        print(f'shift: {shift}, error:{errors[shift]}')
    print(f'minimum error: {minimum}, decoding shift: {minimum_shift}, encoding shift: --> {26-minimum_shift} <--')
    print(f'second error: {sorted(errors)[1]}')
    print(f'Gives text:')
    print(decode(decrypted_test, minimum_shift, alphabet)[:500])


main()
