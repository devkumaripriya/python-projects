import tkinter as tk
from tkinter import messagebox
import time
import winsound  # For sound (Windows only)

current_player = "X"
winner = False

def play_click_sound():
    winsound.Beep(800, 100)  # frequency, duration

def play_win_sound():
    winsound.Beep(1000, 300)
    winsound.Beep(1200, 300)

def play_draw_sound():
    winsound.Beep(600, 400)

def check_winner():
    global winner
    combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for combo in combos:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="green")
            
            play_win_sound()
            
            if messagebox.askyesno("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!\nPlay again?"):
                restart_game()
            else:
                root.quit()
            
            winner = True
            return

    # Draw condition
    if all(button["text"] != "" for button in buttons):
        play_draw_sound()
        
        if messagebox.askyesno("Tic-Tac-Toe", "It's a draw!\nPlay again?"):
            restart_game()
        else:
            root.quit()
        
        winner = True

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        play_click_sound()
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

def restart_game():
    global current_player, winner
    current_player = "X"
    winner = False
    
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    
    label.config(text=f"Player {current_player}'s turn")

# UI setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [
    tk.Button(root, text="", font=("normal", 25), width=6, height=2,
              command=lambda i=i: button_click(i))
    for i in range(9)
]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

restart_btn = tk.Button(root, text="Restart", font=("normal", 14), command=restart_game)
restart_btn.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()