import discord
from discord.ext import commands
import aiohttp



bot = commands.Bot(command_prefix="!", help_command=None)
token = "YOUR_TOKEN"

# DISCORD FUNCTIONS
@bot.command()
async def anime(ctx, *, arg):
    try:
        acces_token = open('token.txt', 'r')
        acces_token = acces_token.read()
        header = {'Authorization': 'Bearer {}'.format(acces_token)}
        params = {'q': arg, 'limit': 4, 'fields': 'id,title,synopsis,status,rank,status,num_episodes'}
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.myanimelist.net/v2/anime', headers=header, params=params) as req:
                response = await req.json()
                
                anime_name = []
                for i in range(1, 4):
                    anime_name.append(response['data'][i]['node']['title'])
                    
                anime_list_embed = create_embed(response['data'][0]['node']['title'], f"{response['data'][0]['node']['synopsis']}\nStatus : {response['data'][0]['node']['status']}\nRank : {response['data'][0]['node']['rank']}\nNombre d'épisodes : {response['data'][0]['node']['num_episodes']}", response['data'][0]['node']['main_picture']['large'], response['data'][0]['node']['main_picture']['large'], f"You can see for :\n{anime_name[0]}\n{anime_name[1]}\n{anime_name[2]}")
                await ctx.send(embed=anime_list_embed)
                
    except KeyError:
        await ctx.send("No anime found")


def create_embed(title, description, image, auth, foot_text):
    embed = discord.Embed() #instance de la classe Embed()
    embed.title = title
    embed.description = description
    embed.set_image(url=image)
    embed.set_author(name="NewbieContest", icon_url=auth)
    embed.set_footer(text=foot_text)
    return embed


bot.run(token)
