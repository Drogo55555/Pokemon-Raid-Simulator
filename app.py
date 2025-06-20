
import streamlit as st
from PIL import Image
import os
import requests
import io

st.set_page_config(page_title="Pokémon GO Raid Simulator", layout="wide")

# Load Icons
def load_icon(name):
    if os.path.exists(name):
        return Image.open(name).convert("RGBA")
    return None

shiny_icon = load_icon("shiny_icon.png")
dynamax_icon = load_icon("dynamax_icon.png")

def overlay_icons(sprite, shiny=False, dynamax=False):
    if sprite.mode != "RGBA":
        sprite = sprite.convert("RGBA")
    if shiny and shiny_icon:
        icon = shiny_icon.resize((32, 32))
        sprite.paste(icon, (sprite.width - 36, 4), icon)
    if dynamax and dynamax_icon:
        icon = dynamax_icon.resize((32, 32))
        sprite.paste(icon, (sprite.width - 36, sprite.height - 36), icon)
    return sprite

# Sample Pokémon sprite loader (static fallback)
def get_pokemon_sprite(name):
    try:
        url = f"https://img.pokemondb.net/sprites/home/normal/{name.lower()}.png"
        response = requests.get(url)
        return Image.open(io.BytesIO(response.content))
    except:
        return Image.new("RGBA", (96, 96), (255, 0, 0, 50))

# UI Inputs
st.title("Pokémon GO Raid Team Simulator")

pokemon_name = st.text_input("Pokémon Name", "")
shiny = st.checkbox("Shiny")
dynamax = st.checkbox("Dynamax or Gigantamax")

if pokemon_name:
    sprite = get_pokemon_sprite(pokemon_name)
    final_img = overlay_icons(sprite, shiny=shiny, dynamax=dynamax)
    st.image(final_img, caption=pokemon_name.title())

st.markdown("---")
st.subheader("Your Move Set")
fast_move = st.selectbox("Fast Move", ["Tackle", "Dragon Breath", "Shadow Claw"])
charged_move_1 = st.selectbox("Charged Move 1", ["Crunch", "Outrage", "Shadow Ball"])
charged_move_2 = st.selectbox("Charged Move 2 (Optional)", ["None", "Hyper Beam", "Dark Pulse"])

# Placeholder for future features
st.markdown("🔧 More advanced simulation features coming soon.")
