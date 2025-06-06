import streamlit as st
import random
import time
import pandas as pd


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


def guess_maker():
    guess = []
    guess_input = input('Doe een eerste gok: ')
    for i in guess_input:
        guess.append(int(i))
    return guess


def algoritme_1(solution):  #Dit is het eerste algoritme uit het onderzoek van een student uit Groningen
    count = 0
    all_pos1 = all_possibilities()
    all_guesses = []
    all_pins = []
    next_guess = all_pos1[0]
    while next_guess != solution:
        count += 1

        all_guesses.append(next_guess)
        all_pins.append(feedback(next_guess, solution))

        remover(all_pos1, solution, next_guess)
        next_guess = all_pos1[0]

    all_guesses.append(next_guess)
    all_pins.append(feedback(next_guess, solution))

    return all_guesses, all_pins, count

def algoritme_2(solution):  #Dit is het tweede algoritme uit het onderzoek van een student uit Groningen
                    #Ook wel de worst case methode genoemd.
    count = 0
    all_pos1 = all_possibilities()
    all_pos2 = all_possibilities()
    all_guesses = []
    all_pins = []
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


    all_guesses.append(next_guess)
    all_pins.append(feedback(next_guess, solution))

    return all_guesses, all_pins, count


def algoritme_3(solution):  #De verandering in dit algoritme ten opzichte van algoritme 1 is dat het niet de eerste overgebleven element
                    #in de lijst met combinaties neemt, maar een willekeurige. De gedachte die hier achter zit is dat er op die manier
                    #meer variatie in de keuzes zou kunnen komen, waardoor er per gok meer mogelijkheden afvallen.
                    #Dit is te zien in line 71 en 79.
    count = 0
    all_pos1 = all_possibilities()
    all_guesses = []
    all_pins = []
    next_guess = random.choice(all_pos1)
    while next_guess != solution:
        count += 1

        all_guesses.append(next_guess)
        all_pins.append(feedback(next_guess, solution))

        remover(all_pos1, solution, next_guess)
        next_guess = random.choice(all_pos1)

    all_guesses.append(next_guess)
    all_pins.append(feedback(next_guess, solution))

    return all_guesses, all_pins, count

def choose_algoritme():
    print('Welkom bij mastermind!\n'
          'In deze versie van het spel moet jij de code verzinnen en gaat de computer deze proberen te kraken.\n'
          'De code bestaat uit 4 pinnen die 6 verschillende kleuren kunnen hebben.\n'
          'Veel succes!')
    algoritme = input('Kies een algoritme. Type 1, 2 of 3: ')
    if algoritme == '1':
        algoritme_1()
    elif algoritme == '2':
        algoritme_2()
    elif algoritme == '3':
        algoritme_3()
    else:
        choose_algoritme()

def main():
    st.title("🎯 Mastermind Game - Computer Guesses")
    st.markdown("""
    Welcome to the **Mastermind** game!  
    In this version, you will input a secret code, and the computer will try to guess it using one of the algorithms.  
    - The secret code consists of 4 digits (1-6).
    - After each guess, you'll see feedback:
        - **⚪**: Correct color in the correct position.
        - **⚫**: Correct color, wrong position.
    """)

    # User input for secret code
    secret_code_input = st.text_input("Enter your secret code (4 digits, e.g., 1234):", "")
    
    # User input for selecting algorithm
    algorithm = st.selectbox("Select a guessing algorithm:", ["Algorithm 1", "Algorithm 2", "Algorithm 3"])

    if st.button("Start Guessing"):
        if len(secret_code_input) == 4 and secret_code_input.isdigit() and all(1 <= int(i) <= 6 for i in secret_code_input):
            secret_code = [int(i) for i in secret_code_input]

            guesses, pins, count = None, None, None

            if algorithm == "Algorithm 1":
                guesses, pins, count = algoritme_1(secret_code)
            elif algorithm == "Algorithm 2":
                guesses, pins, count = algoritme_2(secret_code)
            else:
                guesses, pins, count = algoritme_3(secret_code)

            # Prepare data for table
            table_data = []
            table_placeholder = st.empty()
            for i in range(count + 1):
                guess = guesses[i]
                feedback = pins[i]
                guess_str = " ".join(str(x) for x in guess)
                feedback_str = "⚪" * feedback[0] + "⚫" * feedback[1]
                table_data.append({"Guess": guess_str, "Feedback": feedback_str})

                # Show table up to current guess
                df = pd.DataFrame(table_data)
                df.index = df.index + 1
                table_placeholder.table(df)
                time.sleep(1)

            st.success(f"The computer cracked the code {secret_code} in {count+1} attempts.")
            st.caption("Guess: numbers, Feedback: ⚪ = white (correct color & position), ⚫ = black (correct color, wrong position).")
        else:
            st.error("Please enter a valid 4-digit secret code using numbers 1-6.")

main()
