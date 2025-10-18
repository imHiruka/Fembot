import discord
from discord.ext import commands

client = discord.Client(activity=discord.Game(name='Femboy Greeting Robot biep boop'), intents=discord.Intents.all())

bot = commands.Bot(command_prefix='//')

welcome_channel_id = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has appeared on guild {member.guild}!')
    channel = client.get_channel(welcome_channel_id)
    await channel.send(f"{member.mention} Just joined, give them a nice warm welcome!")

@bot.command()
async def set_id(wc_id: int):
    global welcome_channel_id
    if id:
        welcome_channel_id = wc_id

bot.add_command(set_id)

client.run('Token')
