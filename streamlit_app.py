import streamlit as st

# Helper to create page entries
def make_page(filename, folder):
    return {
        "page": f"{folder}/{filename}",
        "title": filename.replace("_", " ").replace(".py", ""),
    }

graph_files = [
    "Fly_Straight_Dammit.py",
    "Forestfire_Animation.py",
    "Forest_Fire.py",
    "Hofstadters_Chaotic_Cousin.py",
    "Hofstadters_Q_Sequence.py",
    "Random_Fibonacci.py",
    "Remy_Sigrets.py",
    "Reversed_Base.py",
    "Reversed_Primes.py",
    "Square_Root_Rounded.py",
    "Star_Wars.py",
    "Stern_Sequence.py",
    "Triangles.py",
    "Wisteria.py",
]

math_files = [
    "Binary_Calculator.py",
    "Golden_Ratio.py",
    "Mandelbrot.py",
    "Pi_Over_4.py",
    "Pi.py",
    "Prime_Checker.py",
    # "Sudoku_Solver.py",
]

mastermind_files = [
    "Mastermind_Play.py",
    "Mastermind_Computer.py",
]

graphs_pages = [st.Page(**make_page(f, "backend/graphs")) for f in graph_files]
math_pages = [st.Page(**make_page(f, "backend/math")) for f in math_files]
mastermind_pages = [st.Page(**make_page(f, "backend/mastermind")) for f in mastermind_files]

pg = st.navigation(
    {
        "Graphs": graphs_pages,
        "Math": math_pages,
        "Mastermind": mastermind_pages,
    }
)

pg.run()
