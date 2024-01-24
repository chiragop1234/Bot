import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='imagine')
async def imagine(ctx, prompt, model):
    available_models = ["v1", "v2", "v2-beta", "v3 (DALL-E)", "lexica", "prodia", "simurg", "animefy", "raava", "shonin"]
    
    if model not in available_models:
        await ctx.send(f"Invalid model. Available models: {', '.join(available_models)}")
        return
    
    api_url = f'http://ai.harmon.com.tr/imagine?token=chirag&prompt={prompt}&model={model}'
    
    try:
        response = requests.get(api_url)
        result = response.json()
        image_url = result.get('result')

        # Create an embed with the image
        embed = discord.Embed()
        embed.set_image(url=image_url)

        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {e}")

bot.run(os.getenv('TOKEN'))
