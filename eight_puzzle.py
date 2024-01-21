# eight_puzzle.py
import streamlit as st
import numpy as np

class EightPuzzleGame:
    def __init__(self):
        # Initialize game variables
        if "board" not in st.session_state:
            st.session_state.board = np.array([[1, 2, 3], [4, 5, 6], [7, 8, None]])

        # Define the goal state
        self.goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, None]])

    def shuffle_board(self):
        flat_board = st.session_state.board.flatten()
        np.random.shuffle(flat_board)
        st.session_state.board = flat_board.reshape((3, 3))

    def is_solved(self):
        return np.array_equal(st.session_state.board, self.goal_state)

    def perform_move(self, row, col):
        empty_position = np.argwhere(st.session_state.board == None)
        tile_position = np.argwhere(st.session_state.board == st.session_state.board[row, col])

        if np.abs(empty_position[0][0] - tile_position[0][0]) + np.abs(empty_position[0][1] - tile_position[0][1]) == 1:
            st.session_state.board[empty_position[0][0], empty_position[0][1]] = st.session_state.board[row, col]
            st.session_state.board[row, col] = None

def play_eight_puzzle():
    game = EightPuzzleGame()

    st.title("8-Puzzle Game")

    if not game.is_solved():
        st.subheader("Arrange the numbers in order to solve the puzzle:")
        for i in range(3):
            col1, col2, col3 = st.columns([1, 1, 1])
            for j in range(3):
                tile_label = str(st.session_state.board[i][j]) if st.session_state.board[i][j] is not None else ""
                col = col1 if j == 0 else col2 if j == 1 else col3
                col.button(tile_label, key=(i, j), on_click=game.perform_move, args=(i, j))
    else:
        st.success("Congratulations! You solved the puzzle.")

    st.button("Shuffle Board", on_click=game.shuffle_board)

if __name__ == "__main__":
    play_eight_puzzle()
