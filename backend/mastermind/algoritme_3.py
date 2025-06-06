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


def algoritme_3():
    print('Welkom bij mastermind!\n'
          'In deze versie van het spel moet jij de code verzinnen en gaat de computer deze proberen te kraken.\n'
          'De code bestaat uit 4 pinnen die 6 verschillende kleuren kunnen hebben.\n'
          'Veel succes!')
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

print(algoritme_3())

#de verandering in dit algoritme ten opzichte van algoritme 1 is dat het niet de eerste overgebleven element
#in de lijst met combinaties neemt, maar een willekeurige. De gedachte die hier achter zit is dat er op die manier
#meer variatie in de keuzes zou kunnen komen, waardoor er per gok meer mogelijkheden afvallen.
#Dit is te zien in line 71 en 79.