import json
import discord

from discord.ext import commands

with open('config.json') as config:
    config = json.load(config)

token = config['token']

# Enable the intents that your bot will use
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def greet(ctx):
    await ctx.send(f'Hello {ctx.message.author.mention}!')

@client.command()
async def add(ctx, a: int, b: int):
    try:
        result = a + b
    except:
        await ctx.send('Error: One or both of the provided arguments are not integers.')
    else:
        await ctx.send(f'The sum of {a} and {b} is {result}')

@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(f'The product of {a} and {b} is {a*b}')

client.run(token)
