import discord


from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)

TOKEN = 'ODAxMjc4NzIzNDg2Nzc3MzY0.YAeW9g.KFYavJ95561dwOrOyHBGf49zjLw'

track = 'Spielberg'
flag = '\U0001F1E6\U0001F1F9'


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('!f2standings'):
        await message.channel.send('\U0001F947- Connor Pelkmans \U0001F948- Toby Sanford  \U0001F949- Dave Southword')

    if message.content.startswith('!pelkmans'):
        await message.channel.send('Connor Pelkmans \U0001F1E8\U0001F1E6 is the ARL rFactor 2 Formula 3 Summer Series Champion and is a 5 time ARL race winner.')

    if message.content.startswith('!prins'):
        await message.channel.send('Stijn Prins \U0001F1F3\U0001F1F1 is the ARL Formula 3 Season 3 Champion and has 10 wins in ARL to his name.')

    if message.content.startswith('!mocilenko'):
        await message.channel.send('Vladislav Močilenko \U0001F1F8\U0001F1F0 is the ARL Formula 3 Season 1 Champion and has 8 ARL race victories.')

    if message.content.startswith('!simapex'):
        await message.channel.send('SimApex <:SimApex:786993131152867358> is the most successful team in ARL history with 27 race wins, 3 drivers titles, and 2 constructors titles.')

    if message.content.startswith('!champions'):
        await message.channel.send('Season 1 - Vladislav Močilenko, Season 2 - Mixa Mortiferum, Season 3 - Stijn Prins, Summer Series - Connor Pelkmans')

    if message.content.startswith('!incident'):
        await message.channel.send('Your report should include: Driver To Report, Offense Committed, Lap, Corner, Explanation, and Further Comments.')

    
    if message.content.startswith('!bookings'):
        await message.channel.send('<@&682329471105237038><@&785998204683812884> Welcome back again everyone! This week round three takes place at Spielberg \U0001F1E6\U0001F1F9. We hope to see you on track!  Bookings are now open and they close on 20:00 CET this friday. Reacting bellow by saying "book in", confirms your attendance for the race, if you are not able to show up for the race when booked in, please book out by saying "book out," when failed to book out if booked in before the bookings close, will cause in further penalisation according to the rule book.')
    
    if message.content.startswith('book in'):
        await message.channel.send('You have booked in \U0001F4DD')

    if message.content.startswith('book out'):
        await message.channel.send('You have booked out \U0001F44B')

    if message.content.startswith('!commands'):
        await message.channel.send('!f2standings, !incident, !champions, !pelkmans, !prins, !mocilenko, !simapex')

    if message.content.startswith('!admin'):
        await message.channel.send('!bookings')

    if message.content.startswith('!gobills'):
        await message.channel.send('GO BILLS! <:bills:801275979464310834>')

    if message.content.startswith('Stijn'):
        await message.channel.send('<:stijnsbananaphone:702254506553114645>')
client.run(TOKEN)