# tic_tac_toe.py
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw

# Initialize game variables
if "board" not in st.session_state:
    st.session_state.board = np.array([''] * 9)

if "player" not in st.session_state:
    st.session_state.player = 0

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "game_over" not in st.session_state:
    st.session_state.game_over = False

def draw_board():
    img_size = 100
    cell_padding = 5

    img = Image.new("RGB", (img_size, img_size), color="white")
    draw = ImageDraw.Draw(img)

    cell_size = img_size // 3
    for i in range(1, 3):
        line_position = i * cell_size
        draw.line([(line_position, 0), (line_position, img_size)], fill="black", width=2)
        draw.line([(0, line_position), (img_size, line_position)], fill="black", width=2)

    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            cell_center_x = j * cell_size + cell_size // 2
            cell_center_y = i * cell_size + cell_size // 2

            if st.session_state.board[index] == 'X':
                draw.text((cell_center_x - cell_padding, cell_center_y - cell_padding), "X", fill="black")
            elif st.session_state.board[index] == 'O':
                draw.text((cell_center_x - cell_padding, cell_center_y - cell_padding), "O", fill="black")

    st.image(img, caption=f"Player {st.session_state.player + 1}'s turn", use_column_width=True)

def check_game_over():
    for i in range(3):
        if np.all(st.session_state.board[i * 3 : (i + 1) * 3] == 'X') or np.all(st.session_state.board[i * 3 : (i + 1) * 3] == 'O'):
            return True, f"Player {st.session_state.player + 1} Wins!"

        if np.all(st.session_state.board[i : 9 : 3] == 'X') or np.all(st.session_state.board[i : 9 : 3] == 'O'):
            return True, f"Player {st.session_state.player + 1} Wins!"

    if np.all(st.session_state.board[::4] == 'X') or np.all(st.session_state.board[::4] == 'O') or np.all(
        st.session_state.board[2:8:2] == 'X'
    ) or np.all(st.session_state.board[2:8:2] == 'O'):
        return True, f"Player {st.session_state.player + 1} Wins!"

    return False, None

def on_button_click(row, col):
    if st.session_state.game_started and not st.session_state.game_over:
        index = row * 3 + col
        if st.session_state.board[index] == '':
            st.session_state.board[index] = 'X' if st.session_state.player == 0 else 'O'
            st.session_state.player ^= 1
            game_over, winner = check_game_over()
            if game_over:
                st.success(winner)
                st.session_state.game_over = True

def reset_game():
    st.session_state.board = np.array([''] * 9)
    st.session_state.player = 0
    st.session_state.game_over = False

def play_tic_tac_toe():

    if not st.session_state.game_started:
        play_start = st.button("Play Game")
        if play_start:
            st.session_state.game_started = True
            draw_board()
    else:
        for i in range(3):
            col1, col2, col3 = st.columns([1, 1, 1])
            for j in range(3):
                button_label = st.session_state.board[i * 3 + j]
                col = col1 if j == 0 else col2 if j == 1 else col3
                col.button(str(button_label), key=(i, j), on_click=on_button_click, args=(i, j))

        draw_board()

        col4 = st.columns([1, 1])
        col4[0].button("Restart", on_click=reset_game)
        col4[1].button("Exit", on_click=st.stop)

if __name__ == "__main__":
    play_tic_tac_toe()
