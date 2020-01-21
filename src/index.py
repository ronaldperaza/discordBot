import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re


miBot = commands.Bot(command_prefix='>', description='Esto es un bot de ayuda')

@miBot.command()
async def ping(ctx):
    await ctx.send('pong')

@miBot.command()
async def suma(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@miBot.command()
async def info(ctx):
    myEmbed = discord.Embed(title=f"{ctx.guild.name}", description="Comprobando informancion lo que sea aqui", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    myEmbed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    myEmbed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    myEmbed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    myEmbed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    myEmbed.set_thumbnail(url="https://www.google.com/search?q=python+logo+png&sxsrf=ACYBGNSMv14dKxO3vOiM-W-hNaWohiXJNA:1579563372018&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj5x8GNrJPnAhVSU98KHYdDDxwQ_AUoAXoECA0QAw&biw=1280&bih=566#imgrc=LZX-8IrGzQmVqM:")
    await ctx.send(embed=myEmbed)

@miBot.command()
async def youtube(ctx, *, search):
    busqueda = parse.urlencode({'search_query': search})
    respuesta_html = request.urlopen('http://www.youtube.com/results?' + busqueda)
    resultado_busqueda = re.findall('href=\"\\/watch\\?v=(.{11})', respuesta_html.read().decode())
    #print(resultado_busqueda)
    await ctx.send('https://www.youtube.com/watch?v=' + resultado_busqueda[0])


#enventos
@miBot.event   #sin parentesis
async def on_ready():
    await miBot.change_presence(activity=discord.Streaming(name="tutorials", url="http://www.twitch.tv/accountname"))
    print("my Bot is ready")


miBot.run('NjY4OTQ2OTU1NjQwMjQyMTc3.XiYrmQ.tC-lrCJer8rVttbqOfnbGumk8uM')