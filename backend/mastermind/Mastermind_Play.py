import streamlit as st
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


def main():
    st.title("🎯 Mastermind Game")
    st.markdown("""
    Welcome to **Mastermind**!  
    Try to guess the computer's secret code of 4 colors (numbers 1-6).  
    - After each guess, you'll see feedback:
        - **⚪**: Correct color in the correct position.
        - **⚫**: Correct color, wrong position.
    - You have **10 attempts** to crack the code!
    - Enter your guess as a 4-digit number (e.g., 1234).
    """)

    # Initialize game variables
    if 'solution' not in st.session_state:
        st.session_state.solution = [random.randint(1, 6) for _ in range(4)]
        st.session_state.all_guesses = []
        st.session_state.all_pins = []
        st.session_state.count = 0
        st.session_state.all_pos = all_possibilities()
        st.session_state.game_over = False

    # User input for guess
    guess_input = st.text_input("Enter your guess (e.g., 1234):", "")

    # Show Submit Guess button only if game is not over
    if not st.session_state.game_over:
        if st.button("Submit Guess"):
            if len(guess_input) == 4 and guess_input.isdigit() and all(1 <= int(i) <= 6 for i in guess_input):
                guess = [int(i) for i in guess_input]
                st.session_state.all_guesses.append(guess)
                feedback_result = feedback(guess, st.session_state.solution)
                st.session_state.all_pins.append(feedback_result)
                st.session_state.count += 1

                # Remove impossible combinations
                st.session_state.all_pos = remover(st.session_state.all_pos, st.session_state.solution, guess)

                # Check for win condition
                if guess == st.session_state.solution:
                    st.success(f"Congratulations! You've cracked the code in {st.session_state.count} attempts.")
                    st.session_state.game_over = True
                elif st.session_state.count >= 10:
                    st.error(f"Sorry, you've used all 10 attempts! The code was: {''.join(map(str, st.session_state.solution))}")
                    st.session_state.game_over = True
            else:
                st.error("Please enter a valid 4-digit guess using numbers 1-6.")
    else:
        # Show Play Again button only if game is over
        if st.button("Play Again"):
            for key in ["solution", "all_guesses", "all_pins", "count", "all_pos", "game_over"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    # Display current board
    if st.session_state.all_guesses:
        st.write("### Your Guesses")
        import pandas as pd

        board = []
        for guess, pins in zip(st.session_state.all_guesses, st.session_state.all_pins):
            guess_str = " ".join(str(n) for n in guess)
            feedback_str = "⚪" * pins[0] + "⚫" * pins[1]
            board.append({"Guess": guess_str, "Feedback": feedback_str})

        df = pd.DataFrame(board)
        df.index = df.index + 1
        st.table(df)
        st.caption("Guess: numbers, Feedback: ⚪ = white (correct color & position), ⚫ = black (correct color, wrong position).")

main()
