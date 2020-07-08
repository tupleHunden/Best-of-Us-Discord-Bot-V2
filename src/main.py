"""
    This is a rewrite of the Discord Bot found at: github.com/tupleHunden/Best-of-Us-Discord-Bot/
"""

import os  # This will help us work with dotenv easier
import random  # This will help us with any random selection generation
import discord  # This is how we will interact with Discord
import requests  # This will help us work with API Requests easier
from discord.ext import commands  # Command Extension of the Discord Library
from dotenv import load_dotenv  # dotenv will make it easier to use sensitive tokens/info

# This will configure the dotenv file to read sensitive tokens for the slack bot
load_dotenv()

# These constants will enable sensitive token info to be used by the bot.
DISCORD_CLIENT_ID = os.getenv('DISCORD_CLIENT_ID')
DISCORD_CLIENT_SECRET = os.getenv('DISCORD_CLIENT_SECRET')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    """
        on_ready() will display a message when the bot is connected to Discord.
    """
    print(f'{bot.user} has successfully connected to Discord')


@bot.event
async def on_member_join(member):
    """
        on_member_join() will send a direct message to all new users welcoming them to Discord.
    """
    await member.create_dm()
    await member.dm_channel.send(f'Hello {member.name}, welcome to Best of Us!  '
                                 f'You should read our #server-info, #announcements, #suggestions, '
                                 f'and #welcome-mat channels to get familiar with things. '
                                 f'Check out #server-info first, it will guide you through some '
                                 f'information about us and how the server works. '
                                 f' When you feel comfortable with the rules, '
                                 f'check out #welcome-mat to get your roles set up.  Just ping '
                                 f'Alch or any other Admin for roles and we can get you sorted. '
                                 f'If you have any questions at all, please let one of the admins '
                                 f'know, we are at the top of the member list.'
                                 f'Thanks! ~Alchemist8')


@bot.command('chuck', help="This will provide the user with a random chuck norris joke")
async def chuck_norris(ctx):
    """
        chuck_norris() will provide the user with a random chuck norris joke.
    """
    chuck_request = requests.get('https://api.chucknorris.io/jokes/random')

    if chuck_request.status_code == 200:
        chuck_response = chuck_request.json()
        await ctx.send(chuck_response['value'])


@bot.command('github', help='This will provide a link to the repo')
async def github(ctx):
    """
        github() will provide a link to the repo.
    """
    await ctx.send('https://github.com/tupleHunden/Best-of-Us-Discord-Bot-V2')


@bot.command('bah', help='This will provide a link to the DOD BAH Calculator')
async def bah(ctx):
    """
        bah() will provide a link to the DOD BAH Calculator.
    """
    await ctx.send('https://www.defensetravel.dod.mil/site/bahCalc.cfm')


@bot.command('invite', help='This will provide an invite to the Discord Server')
async def invite(ctx):
    """
        invite() will provide a link to the Discord Server.
    """
    await ctx.send('https://discord.gg/bestofus')


@bot.command('8ball', help='This will send a random response similar to a Magic 8 Ball')
async def eight_ball(ctx):
    """
        eight_ball() will send a random response from response_list.
    """
    response_list = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes – definitely.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Don\'t count on it.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.']

    response = str(random.choices(response_list))[2:-2]

    await ctx.send(response)


@bot.command('ping', help='Pong!')
async def ping(ctx):
    """
        ping() will send pong to the user.
    """
    await ctx.send('pong')


@bot.command('tl', help='This will send a link to the TL Comic Website')
async def terminal_lance(ctx):
    """
        terminal_lance() will send a link to the terminal lance comic website.
    """
    await ctx.send('https://terminallance.com')


@bot.command('players', help='This will post the current online plays in EVE Online.')
async def eve_player_count(ctx):
    """
        eve_player_count() will send the current number of online players in EVE Online.
    """
    api_request = requests.get('https://esi.evetech.net/latest/status/?datasource=tranquility')
    if api_request.status_code == 200:
        response = api_request.json()
        await ctx.send(f"There are currently {response['players']} people playing EVE Online.")


@bot.command('who', help='This will look up a specific player in EVE Online')
async def player_lookup(ctx, args):
    """
        player_lookup() will send information on a provided player
    """
    character_id_search = requests.get(f"https://esi.evetech.net/latest/search/?categories="
                                       f"character&datasource=tranquility&language=en-us&search="
                                       f"{args}&strict=true")

    character_id = character_id_search.json()

    character_name_search = requests.get(f"https://esi.evetech.net/latest/characters/"
                                         f"{character_id['character'][0]}/?datasource=tranquility")

    specific_character_name = character_name_search.json()

    zkill = f"https://zkillboard.com/character/{character_id['character'][0]}/"

    embed = discord.Embed(title=specific_character_name['name'], description=zkill)

    await ctx.send(embed=embed)


@bot.command('lab', help='This will return the top 3 players on the Path of Exile Lab Ladder.')
async def poe_lab_ladder(ctx):
    """
        poe_lab_ladder() will return the top 3 players on the Path of Exile Lab ladder
    """
    api_request = requests.get("http://api.pathofexile.com/ladders/"
                               "League?type=labyrinth&difficulty=Merciless")

    api_json = api_request.json()

    first_place = discord.Embed(title=f"1st Place\n{api_json['entries'][0]['character']['name']}",
                                description=f"{api_json['entries'][0]['character']['class']}\n "
                                            f"Time: {api_json['entries'][0]['time']}")

    second_place = discord.Embed(title=f"2nd Place\n{api_json['entries'][1]['character']['name']}",
                                 description=f"{api_json['entries'][1]['character']['class']}\n "
                                             f"Time: {api_json['entries'][1]['time']}")

    third_place = discord.Embed(title=f"3rd Place\n{api_json['entries'][2]['character']['name']}",
                                description=f"{api_json['entries'][2]['character']['class']}\n "
                                            f"Time: {api_json['entries'][2]['time']}")

    await ctx.send(embed=first_place)
    await ctx.send(embed=second_place)
    await ctx.send(embed=third_place)


@bot.command('dog', help='This will post a random picture of a dog.')
async def dog(ctx):
    """
        dog() will post random pictures of a dog
    """
    random_dog = requests.get("https://random.dog/woof.json")
    dog_json = random_dog.json()

    await ctx.send(dog_json['url'])


@bot.command('bored', help='This will provide the user with an activity to do.')
async def bored(ctx):
    """
        bored() will provide the user with an activity to do
    """
    api_request = requests.get('https://www.boredapi.com/api/activity/')
    activity = api_request.json()

    await ctx.send(f"You should {activity['activity']}")


@bot.command('xkcd', help='This will post a random xkcd comic.')
async def xkcd(ctx):
    """
        xkcd() will provide the user with a random xkcd comic.
    """
    random_id = random.randrange(1, 2329)
    api_request = requests.get(f'https://xkcd.com/{random_id}/info.0.json')

    comic = api_request.json()

    await ctx.send(comic['img'])


# This will bring the bot online.
bot.run(DISCORD_BOT_TOKEN)
