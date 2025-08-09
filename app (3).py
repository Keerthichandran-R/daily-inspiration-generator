# app.py
import streamlit as st
import random
from datetime import date

# App Title
st.set_page_config(page_title="Daily Inspiration", page_icon="🌟", layout="centered")
st.title("🌟 Daily Inspiration Generator")

# Quotes List
quotes = [
    "Believe you can and you're halfway there.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Little things make big days.",
    "It always seems impossible until it’s done."
]

# Show today's date
st.write(f"📅 Today's date: {date.today().strftime('%B %d, %Y')}")

# Generate a quote
if st.button("✨ Inspire Me!"):
    quote = random.choice(quotes)
    st.success(quote)
else:
    st.info("Click the button to get your daily dose of inspiration!")

# Footer
st.write("---")
st.caption("Built with ❤️ using Streamlit")
