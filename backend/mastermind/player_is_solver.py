import random


def all_possibilities():
    lst1 = [1, 2, 3, 4, 5, 6]
    lst2 = [1, 2, 3, 4, 5, 6]
    lst3 = [1, 2, 3, 4, 5, 6]
    lst4 = [1, 2, 3, 4, 5, 6]

    all_pos = [[a, b, c, d] for a in lst1 for b in lst2
               for c in lst3 for d in lst4] # alle mogelijke 6**4 ofwel 1296 combinaties
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
            temp_solution.remove(pin) # voorkomt dat er een witte pin wordt toegevoegd doordat een kleur die vaker
                                        # voorkomt in guess een kleur is die minder vaak voorkomt in de solution
            counter += 1
    return counter


def feedback(guess, solution):
    white = white_pins(guess, solution)
    black = black_pins(guess, solution)
    white -= black  # als een pin zwart is hij in dit algoritme ook wit
    return [black, white]


def remover(all_pos, solution, guess):
    for i in all_pos[:]:
        if feedback(guess, i) != feedback(guess, solution):
            all_pos.remove(i)
    return all_pos


def play(all_pos):
    print('Welkom bij Mastermind!\n'
          'In deze variant van het spel is het de bedoeling dat je de code kraakt van de computer.\n'
          'De computer een random code gegenereerd.\n'
          'Deze code bevat getallen van 1t/m6 in een willekeurige volgorde.\n'
          'Kleuren kunnen meerdere malen voorkomen.\n'
          'Na iedere gok krijg je te weten hoeveel kleuren goed zijn en op de goede plek zitten en\n'
          'hoeveel kleuren goed zijn, maar op de verkeerde plek zitten.\n'
          'Veel succes!')
    count = 0
    solution = []
    all_guesses = []
    all_pins = []
    for i in range(0, 4):
        solution.append(random.randrange(1, 7))
    guess = []
    while guess != solution:
        guess = []
        count += 1
        guess_input = input('Speler 2, doe een gok (vb. 2534): ')
        for i in guess_input:
            guess.append(int(i))

        all_guesses.append(guess)
        all_pins.append(feedback(guess, solution))
        (remover(all_pos, solution, guess))
        print('------------------------------------------\n|  Je huidige bord ziet er zo uit:       |')
        for i, j in zip(all_guesses, all_pins):
            print('|  Kleuren: {} feedback: {}  |'.format(i, j))
        print('------------------------------------------')
    if count > 10:
        print('Helaas, je hebt de code niet kunnen kraken in 10 stappen.\n'
              'Wel heb je de code kunnen kraken in {} stappen.'.format(count))
    else:
        print('Heel goed!\nJe hebt de code weten te kraken in {} stap(pen).'.format(count))


def main():
    play(all_possibilities())
