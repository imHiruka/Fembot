import discord

client = discord.Client(activity=discord.Game(name='Femboy Greeting Robot biep boop'), intents=discord.Intents.all())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has appeared on guild {member.guild}!')
    channel = client.get_channel(1337132829817049150)
    await channel.send(f"{member.mention} Just joined, give them a nice warm welcome!")


client.run('Token')
