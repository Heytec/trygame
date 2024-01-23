import streamlit as st
import random
import time

def get_random_difficulty():
    difficulty_levels = ["easy", "medium", "hard"]
    return random.choice(difficulty_levels)

def get_prize_lists(difficulty):
    easy_prizes = ["KSh.0"] * 18 + ["KSh.10", "Kenwood Blender", "Slippers", "KSh.30", "KSh.70", "Smartphone", "Coffee Maker", "Fitness Tracker"]
    medium_prizes = ["KSh.0"] * 25 + ["KSh.10", "Kenwood Blender", "Slippers", "KSh.30", "KSh.70", "Smartphone", "Coffee Maker", "Fitness Tracker", "Movie Tickets", "Headphones", "KSh.80", "Gift Voucher", "KSh.10", "Digital Watch"]
    hard_prizes = ["KSh.0"] * 50 + ["KSh.10", "Kenwood Blender", "Slippers", "KSh.30", "KSh.70", "Smartphone", "Coffee Maker", "Fitness Tracker", "Movie Tickets", "Headphones", "KSh.80", "Gift Voucher", "KSh.10", "Digital Watch", "KSh.100", "Bluetooth Earbuds", "KSh.50", "Portable Charger", "KSh.200", "Smartwatch"]

    if difficulty == "easy":
        return easy_prizes
    elif difficulty == "medium":
        return medium_prizes
    elif difficulty == "hard":
        return hard_prizes
    else:
        return medium_prizes

def play_lucky_box(bet_amount, user_box):
    difficulty = get_random_difficulty()
    all_prizes = get_prize_lists(difficulty)

    random.shuffle(all_prizes)

    result = all_prizes[user_box - 1]

    st.write("Opening the box...")
    time.sleep(1)

    st.subheader("LUCKYBOX TICKET")
    st.write(f"Bet Amount: {bet_amount} KSh")
    st.write(f"Your Box: {user_box}")
    st.write("Available Choices:")

    for i in range(7):
        st.write(f"[BOX{i + 1}] - {all_prizes[i]}")

    if result != "KSh.0":
        st.success(f"Congratulations! You won {result}.")
    else:
        st.error(f"Unfortunately, you didn't win this time. Better luck next time! You lost {bet_amount} KSh.")

# Streamlit UI
st.title("Lucky Box Game")
st.write("Try your luck and win exciting prizes!")

# Get user input
bet_amount = st.number_input("Enter your bet amount (KSh):", min_value=1, value=20, step=1)

# Display radio buttons for selecting the lucky box
user_box = st.radio("Choose your lucky box:", [f"Box {i+1}" for i in range(7)], index=0)

# Extract the box number from the label
user_box = int(user_box.split(" ")[1])

# Play button
if st.button("Play"):
    play_lucky_box(bet_amount, user_box)

