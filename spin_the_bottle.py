# spin_the_bottle.py

import streamlit as st
import random

# App title
st.title("🎉 Spin the Bottle – Truth or Dare")

# Session state to store player names
if "players" not in st.session_state:
    st.session_state.players = []

# Input to add a player
new_player = st.text_input("Add Player Name:")

if st.button("Add Player"):
    if new_player.strip() != "":
        st.session_state.players.append(new_player.strip())
        st.success(f"Added {new_player}!")

# Show current players
if st.session_state.players:
    st.subheader("Players:")
    st.write(", ".join(st.session_state.players))
else:
    st.info("Add at least one player to start!")

# Truth or Dare lists
truths = [
    "What is your biggest fear?",
    "What is your most embarrassing moment?",
    "Who do you have a crush on?",
    "What is your secret talent?",
    "Have you ever lied to your best friend?"
]

dares = [
    "Sing a song loudly!",
    "Dance for 30 seconds.",
    "Do 10 push-ups.",
    "Speak in an accent for 2 minutes.",
    "Do a funny impression of someone here!"
]

# Spin the bottle button
if st.button("🎲 Spin the Bottle"):
    if st.session_state.players:
        chosen_player = random.choice(st.session_state.players)
        st.success(f"The bottle points to: **{chosen_player}**!")

        action = st.radio("Choose:", ["Truth", "Dare"])
        if action == "Truth":
            st.write(f"👉 **Truth:** {random.choice(truths)}")
        else:
            st.write(f"👉 **Dare:** {random.choice(dares)}")
    else:
        st.warning("Add players first!")

# Option to reset players
if st.button("🔄 Reset Players"):
    st.session_state.players = []
    st.info("Player list cleared!")
