import discord
import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, I am a Python Discord Bot!')

    if message.content.startswith('$swchar'):
        await swchar(message)

async def swchar(message) -> None:
    try:
        id = random.randint(0, 10)
        response = requests.get(f"https://swapi.dev/api/people/{id}/")
        response.raise_for_status()
        data = response.json()
    except requests.HTTPError:
        return

    embed = discord.Embed(
        title=data.get("name"),
        description=data.get("url"),
    )
    embed.add_field(name="Height", value=data.get("height"))
    embed.add_field(name="Mass", value=data.get("mass"))
    embed.add_field(name="Hair Color", value=data.get("hair_color"))
    embed.add_field(name="Birth Year", value=data.get("birth_year"))
    embed.add_field(name="Eye Color", value=data.get("eye_color"))
    embed.add_field(name="Gender", value=data.get("gender"))
    await message.channel.send(embed=embed)

client.run(DISCORD_TOKEN)
