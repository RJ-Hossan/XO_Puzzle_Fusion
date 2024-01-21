# app.py
import streamlit as st
from tic_tac_toe import play_tic_tac_toe
from eight_puzzle import play_eight_puzzle

def main():
    st.title("Game Hub")

    selected_game = st.sidebar.radio("Select a Game", ["Tic Tac Toe", "8 Puzzle"])

    if selected_game == "Tic Tac Toe":
        st.subheader("Tic Tac Toe Game")
        play_tic_tac_toe()

    elif selected_game == "8 Puzzle":
        st.subheader("8-Puzzle Game")
        play_eight_puzzle()

if __name__ == "__main__":
    main()
