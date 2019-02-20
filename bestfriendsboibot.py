import discord
from discord.ext import commands
import discord.ext

bot = commands.Bot(command_prefix='.')
bot.remove_command("help")
print (discord.__version__)


@bot.event
async def on_ready():
    print ("Ready when you are")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_status(game=discord.Game(name='Type .help in #commands'))
    await bot.say("owo hi im aliv now :D")

@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("hi dere we now best friends *wink*")


    
bot.run("NTQ3Nzg2NjcwNTExMDk1ODIw.D071uQ.UoYdNPLttxs68KmQBPMLbBu4HNU")