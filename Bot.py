import discord
from discord.ext import commands, tasks
import codeforcesAPI as cf
import time

TOKEN = open('TOKEN.txt', 'r').readline()

bot = commands.Bot(command_prefix='!')

codeforcesList = {} # handle : time

@bot.event
async def on_ready():
    stalk.start()
    print('Bot is ready')

@bot.command()
async def add(ctx, handle):
    if handle in codeforcesList:
        await ctx.send(f'{handle} is already added')
    else:
        codeforcesList[handle] = -1
        await ctx.send(f'codeforces user **{handle}** is added')

@tasks.loop(seconds=1)
async def stalk():
    channel = bot.get_channel(754253458630246493)
    for handle, currentTime in codeforcesList.items():
        time.sleep(0.5)

        newTime, res = cf.recentSubmission(handle, currentTime)
        # print(handle, newTime, currentTime)
        if res == None:
            print('Not Found')
            continue

        if newTime > currentTime:
            if currentTime != -1:
                for problem in res:
                    name = problem['name']
                    await channel.send(f'**{handle}** just solved question **{name}**')
            codeforcesList[handle] = newTime

bot.run(TOKEN)