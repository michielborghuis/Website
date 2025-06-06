import random


def all_possibilities():
    lst1 = [1, 2, 3, 4, 5, 6]

    all_pos = [[a, b, c, d] for a in lst1 for b in lst1
               for c in lst1 for d in lst1]
    return all_pos


def black_pins(guess, solution):
    counter = 0
    for pin in range(len(guess)):
        if guess[pin] == solution[pin]:
            counter += 1
    return counter


def white_pins(guess, solution):
    temp_solution = solution[:]
    counter = 0
    for pin in guess:
        if pin in temp_solution:
            temp_solution.remove(pin) # voorkomt dat er een witte pin wordt  toegevoegddoordat een kleur die vaker
                                        # voorkomt in guess, een kleur is die minder vaak voorkomt in de solution
            counter += 1
    return counter


def feedback(guess, solution):
    white = white_pins(guess, solution)
    black = black_pins(guess, solution)
    white -= black  # voorkomt dat als een pin zwart is deze niet ook wit is
    return [black, white]


def remover(all_pos1, solution, guess):
    for i in all_pos1[:]:
        if feedback(guess, i) != feedback(guess, solution):
            all_pos1.remove(i)
    return all_pos1


def graph(all_pos1, all_pos2):
    maximum = {}
    for i in all_pos2:
        nul_nul = 0
        nul_een = 0
        nul_twee = 0
        nul_drie = 0
        nul_vier = 0
        een_nul = 0
        een_een = 0
        een_twee = 0
        een_drie = 0
        twee_nul = 0
        twee_een = 0
        twee_twee = 0
        drie_nul = 0
        vier_nul = 0
        for j in all_pos1:
            if feedback(i, j) == [0, 0]:
                nul_nul += 1
            if feedback(i, j) == [0, 1]:
                nul_een += 1
            if feedback(i, j) == [0, 2]:
                nul_twee += 1
            if feedback(i, j) == [0, 3]:
                nul_drie += 1
            if feedback(i, j) == [0, 4]:
                nul_vier += 1
            if feedback(i, j) == [1, 0]:
                een_nul += 1
            if feedback(i, j) == [1, 1]:
                een_een += 1
            if feedback(i, j) == [1, 2]:
                een_twee += 1
            if feedback(i, j) == [1, 3]:
                een_drie += 1
            if feedback(i, j) == [2, 0]:
                twee_nul += 1
            if feedback(i, j) == [2, 1]:
                twee_een += 1
            if feedback(i, j) == [2, 2]:
                twee_twee += 1
            if feedback(i, j) == [3, 0]:
                drie_nul += 1
            if feedback(i, j) == [4, 0]:
                vier_nul += 1
        update = {tuple(i) : max(nul_nul, nul_een, nul_twee, nul_drie, nul_vier, een_nul, een_een, een_twee, een_drie, twee_nul, twee_een, twee_twee, drie_nul, vier_nul)}
        maximum.update(update)
    next_guess = list(min(maximum, key=maximum.get))
    return next_guess


def solution_maker():
    solution = []
    solution_input = input('Geef de geheime code bv. 3635: ')
    for i in solution_input:
        solution.append(int(i))
    return solution

def guess_maker():
    guess = []
    guess_input = input('Doe een eerste gok: ')
    for i in guess_input:
        guess.append(int(i))
    return guess


def solve():
    print('Welkom bij Mastermind!\n'
          'In deze variant van het spel is het de bedoeling dat je de code kraakt van de computer.\n'
          'De computer heeft een random code gegenereerd.\n'
          'Deze code bevat getallen van 1 t/m 6 in een willekeurige volgorde.\n'
          'Kleuren kunnen meerdere malen voorkomen.\n'
          'Na iedere gok krijg je te weten hoeveel kleuren goed zijn en op de goede plek zitten en\n'
          'hoeveel kleuren goed zijn, maar op de verkeerde plek zitten.\n'
          'Veel succes!')
    count = 0
    all_pos = all_possibilities()
    solution = []
    all_guesses = []
    all_pins = []
    for i in range(0, 4):
        solution.append(random.randrange(1, 7))
    next_guess = []
    while next_guess != solution:
        next_guess = []
        count += 1
        guess_input = input('Speler 2, doe een gok (vb. 2534): ')
        for i in guess_input:
            next_guess.append(int(i))

        all_guesses.append(next_guess)
        all_pins.append(feedback(next_guess, solution))
        (remover(all_pos, solution, next_guess))
        print('--------------------------------------------\n|  Je huidige bord ziet er zo uit:         |')
        for i, j in zip(all_guesses, all_pins):
            print('|  Kleuren: {} feedback: {}  |'.format(i, j))
        print('--------------------------------------------')
    if count > 10:
        print('Helaas, je hebt de code niet kunnen kraken in 10 stappen.\n'
              'Wel heb je de code kunnen kraken in {} stappen.'.format(count))
    else:
        print('Heel goed!\nJe hebt de code weten te kraken in {} stap(pen).'.format(count))


def algoritme_1():  #Dit is het eerste algoritme uit het onderzoek van een student uit Groningen
    count = 0
    all_pos1 = all_possibilities()
    all_guesses = []
    all_pins = []
    solution = solution_maker()
    next_guess = all_pos1[0]
    while next_guess != solution:
        count += 1

        all_guesses.append(next_guess)
        all_pins.append(feedback(next_guess, solution))

        remover(all_pos1, solution, next_guess)
        next_guess = all_pos1[0]

        print('\n'*4)
        print('Poging {}'.format(count))
        print('--------------------------------------------\n|  Je huidige bord ziet er zo uit:         |')
        for i, j in zip(all_guesses, all_pins):
            print('|  Kleuren: {} feedback: {}  |'.format(i, j))
        print('--------------------------------------------')

    all_guesses.append(next_guess)
    all_pins.append(feedback(next_guess, solution))
    print('\n' * 4)
    print('Poging {}'.format(count+1))
    print('--------------------------------------------\n|  Je huidige bord ziet er zo uit:         |')
    for i, j in zip(all_guesses, all_pins):
        print('|  Kleuren: {} feedback: {}  |'.format(i, j))
    print('--------------------------------------------')

    if count > 10:
        print('Heel goed, de computer heeft de code niet kunnen kraken in 10 stappen.\n'
              'Wel heeft de computer de code kunnen kraken in {} stappen.'.format(count+1))
    else:
        print('Helaas!\nDe computer heeft de code weten te kraken in {} stap(pen).'.format(count+1))


def algoritme_2():  #Dit is het tweede algoritme uit het onderzoek van een student uit Groningen
                    #Ook wel de worst case methode genoemd.
    count = 0
    all_pos1 = all_possibilities()
    all_pos2 = all_possibilities()
    all_guesses = []
    all_pins = []
    solution = solution_maker()
    next_guess = [1, 1, 2, 2]   #Uit de eerste keus van het algoritme blijkt 1122 altijd de beste optie te zijn.
                                #Om tijd te besparen heb ik gekozen om deze niet te berekenen, maar deze altijd
                                #automatisch als eerste gok te kiezen.
    while next_guess != solution:
        count += 1

        all_guesses.append(next_guess)
        all_pins.append(feedback(next_guess, solution))

        remover(all_pos1, solution, next_guess)

        if len(all_pos1) == 1:
            next_guess = all_pos1[0]
        else:
            next_guess = graph(all_pos1, all_pos2)

        print('\n' * 4)
        print('Poging {}'.format(count))
        print('--------------------------------------------\n|  Je huidige bord ziet er zo uit:         |')
        for i, j in zip(all_guesses, all_pins):
            print('|  Kleuren: {} feedback: {}  |'.format(i, j))
        print('--------------------------------------------')

    all_guesses.append(next_guess)
    all_pins.append(feedback(next_guess, solution))
    print('\n' * 4)
    print('Poging {}'.format(count+1))
    print('--------------------------------------------\n|  Je huidige bord ziet er zo uit:         |')
    for i, j in zip(all_guesses, all_pins):
        print('|  Kleuren: {} feedback: {}  |'.format(i, j))
    print('--------------------------------------------')

    if count > 10:
        print('Heel goed, de computer heeft de code niet kunnen kraken in 10 stappen.\n'
              'Wel heeft de computer de code kunnen kraken in {} stappen.'.format(count+1))
    else:
        print('Helaas!\nDe computer heeft de code weten te kraken in {} stap(pen).'.format(count+1))


def algoritme_3():  #De verandering in dit algoritme ten opzichte van algoritme 1 is dat het niet de eerste overgebleven element
                    #in de lijst met combinaties neemt, maar een willekeurige. De gedachte die hier achter zit is dat er op die manier
                    #meer variatie in de keuzes zou kunnen komen, waardoor er per gok meer mogelijkheden afvallen.
                    #Dit is te zien in line 71 en 79.
    count = 0
    all_pos1 = all_possibilities()
    all_guesses = []
    all_pins = []
    solution = solution_maker()
    next_guess = random.choice(all_pos1)
    while next_guess != solution:
        count += 1

        all_guesses.append(next_guess)
        all_pins.append(feedback(next_guess, solution))

        remover(all_pos1, solution, next_guess)
        next_guess = random.choice(all_pos1)
        print('\n'*4)
        print('Poging {}'.format(count))
        print('--------------------------------------------\n|  Je huidige bord ziet er zo uit:         |')
        for i, j in zip(all_guesses, all_pins):
            print('|  Kleuren: {} feedback: {}  |'.format(i, j))
        print('--------------------------------------------')

    all_guesses.append(next_guess)
    all_pins.append(feedback(next_guess, solution))
    print('\n' * 4)
    print('Poging {}'.format(count+1))
    print('--------------------------------------------\n|  Je huidige bord ziet er zo uit:         |')
    for i, j in zip(all_guesses, all_pins):
        print('|  Kleuren: {} feedback: {}  |'.format(i, j))
    print('--------------------------------------------')

    if count > 10:
        print('Heel goed, de computer heeft de code niet kunnen kraken in 10 stappen.\n'
              'Wel heeft de computer de code kunnen kraken in {} stappen.'.format(count+1))
    else:
        print('Helaas!\nDe computer heeft de code weten te kraken in {} stap(pen).'.format(count+1))


def choose_algoritme():
    print('Welkom bij mastermind!\n'
          'In deze versie van het spel moet jij de code verzinnen en gaat de computer deze proberen te kraken.\n'
          'De code bestaat uit 4 pinnen die 6 verschillende kleuren kunnen hebben.\n'
          'Veel succes!')
    algoritme = input('Kies een algoritme. Type 1, 2 of 3: ')
    if algoritme == '1':
        algoritme_1()
    elif algoritme == '2':               #[1, 1]
        algoritme_2()
    elif algoritme == '3':
        algoritme_3()
    else:
        choose_algoritme()


def play():
    print('Welkom bij mastermind!')
    gamemode = input('Wilt u zelf een code bedenken en door de computer laten oplossen? Type c\n'
                     'Wilt u de code door de computer laten kiezen en zelf oplossen? Type z\n'
                     'Type c of z: ')
    if gamemode == 'c':
        choose_algoritme()
    elif gamemode == 'z':
        solve()
    else:
        play()


def main():
    play()

main()