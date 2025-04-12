import tkinter as tk
import random

OPTIONS = ["Rock", "Paper", "Scissors"]

# Global scores
scores = {"Player 1": 0, "Player 2": 0, "User": 0, "Computer": 0}
player_choices = {}

# Determine winner
def get_winner(p1, p2):
    if p1 == p2:
        return "Tie"
    elif (p1 == "Rock" and p2 == "Scissors") or \
         (p1 == "Scissors" and p2 == "Paper") or \
         (p1 == "Paper" and p2 == "Rock"):
        return "Player 1"
    else:
        return "Player 2"

# Reset everything
def reset_game():
    for key in scores:
        scores[key] = 0
    update_score()
    result_label.config(text="Choose a mode to play!")
    mode_frame.pack()
    single_frame.pack_forget()
    player1_frame.pack_forget()
    player2_frame.pack_forget()
    next_btn.pack_forget()

# Score display
def update_score():
    score_text = f"Score - Player 1: {scores['Player 1']} | Player 2: {scores['Player 2']} | You: {scores['User']} | Computer: {scores['Computer']}"
    score_label.config(text=score_text)

# === SINGLE PLAYER MODE ===
def start_single_player():
    mode_frame.pack_forget()
    result_label.config(text="Choose Rock, Paper or Scissors:")
    single_frame.pack()

def play_single(choice):
    user = choice
    comp = random.choice(OPTIONS)
    result = get_winner(user, comp)
    result_text = f"You chose: {user}\nComputer chose: {comp}\n"
    if result == "Tie":
        result_text += "🤝 It's a Tie!"
    elif result == "Player 1":
        result_text += "🎉 You Win!"
        scores['User'] += 1
    else:
        result_text += "😞 You Lose!"
        scores['Computer'] += 1

    result_label.config(text=result_text)
    update_score()

# === TWO PLAYER MODE ===
def start_two_player():
    mode_frame.pack_forget()
    result_label.config(text="Player 1: Choose Rock, Paper or Scissors:")
    player1_frame.pack()
    next_btn.pack_forget()

def player1_select(choice):
    player_choices['Player 1'] = choice
    player1_frame.pack_forget()
    result_label.config(text="Player 2: Choose Rock, Paper or Scissors:")
    player2_frame.pack()

def player2_select(choice):
    player_choices['Player 2'] = choice
    player2_frame.pack_forget()
    show_2p_result()

def show_2p_result():
    p1 = player_choices['Player 1']
    p2 = player_choices['Player 2']
    result = get_winner(p1, p2)
    result_text = f"Player 1 chose: {p1}\nPlayer 2 chose: {p2}\n"

    if result == "Tie":
        result_text += "🤝 It's a Tie!"
    else:
        result_text += f"🎉 {result} Wins!"
        scores[result] += 1

    result_label.config(text=result_text)
    update_score()
    next_btn.pack(pady=10)

def next_round_2p():
    result_label.config(text="Player 1: Choose Rock, Paper or Scissors:")
    next_btn.pack_forget()
    player1_frame.pack()

# === UI SETUP ===
root = tk.Tk()
root.title("Rock-Paper-Scissors - Single & Two Player")
root.geometry("500x500")
root.config(bg="#f0f9ff")
root.resizable(False, False)

title = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 16, "bold"), bg="#f0f9ff", fg="#01579b")
title.pack(pady=10)

# Mode selection
mode_frame = tk.Frame(root, bg="#f0f9ff")
tk.Label(mode_frame, text="Choose Game Mode:", font=("Arial", 12, "bold"), bg="#f0f9ff").pack(pady=5)
tk.Button(mode_frame, text="Single Player", width=15, font=("Arial", 10, "bold"),
          bg="#0288d1", fg="white", command=start_single_player).pack(pady=5)
tk.Button(mode_frame, text="Two Player", width=15, font=("Arial", 10, "bold"),
          bg="#00796b", fg="white", command=start_two_player).pack(pady=5)
mode_frame.pack()

# Result
result_label = tk.Label(root, text="Choose a mode to play!", font=("Arial", 12), bg="#f0f9ff")
result_label.pack(pady=15)

# Score
score_label = tk.Label(root, text="Score - Player 1: 0 | Player 2: 0 | You: 0 | Computer: 0", font=("Arial", 10, "bold"),
                       bg="#f0f9ff", fg="#006064")
score_label.pack(pady=5)

# SINGLE PLAYER FRAME
single_frame = tk.Frame(root, bg="#f0f9ff")
for opt in OPTIONS:
    tk.Button(single_frame, text=opt, width=12, font=("Arial", 10, "bold"),
              bg="#4dd0e1", fg="white", command=lambda o=opt: play_single(o)).pack(side=tk.LEFT, padx=10)

# PLAYER 1
player1_frame = tk.Frame(root, bg="#f0f9ff")
for opt in OPTIONS:
    tk.Button(player1_frame, text=opt, width=12, font=("Arial", 10, "bold"),
              bg="#4db6ac", fg="white", command=lambda o=opt: player1_select(o)).pack(side=tk.LEFT, padx=10)

# PLAYER 2
player2_frame = tk.Frame(root, bg="#f0f9ff")
for opt in OPTIONS:
    tk.Button(player2_frame, text=opt, width=12, font=("Arial", 10, "bold"),
              bg="#26a69a", fg="white", command=lambda o=opt: player2_select(o)).pack(side=tk.LEFT, padx=10)

# Next round button for 2P
next_btn = tk.Button(root, text="Next Round", font=("Arial", 10, "bold"), bg="#0097a7", fg="white", command=next_round_2p)

# Reset game
tk.Button(root, text="Reset Game", font=("Arial", 10, "bold"), bg="#c62828", fg="white", command=reset_game).pack(pady=10)

# Start
root.mainloop()
