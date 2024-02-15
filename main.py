import discord
import random
import time
import requests
from mojang import MojangAPI

TOKEN = ''

client = discord.Client()

buzy = False

@client.event
async def on_ready():
    print("Bot is ingelogd als {0.user}".format(client))

@client.event
async def on_message(message):
    if buzy == False:
    #if message.channel.id == 1097934219004608633:
        #print("Omggggg we hebben een message!")
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        #print("Nieuw bericht:", user_message)
        #channel = str(message.channel.name)
        
        if message.author == client.user:
            return
        
        #if user_message.lower() == 'Test':
            #message.send("Test")
        
        #if user_message == "/help":
            #await message.reply("Hello! at the moment i'm just a useless bot :(")
        
        currentmessage = str(message.content)
        buzy = True
        try:
            await message.reply("Getting stats from " + user_message + ". please wait a second.")
            api_key = ""

            #userinput = str(input("Enter your minecraft username >>> "))
            
            userinput = currentmessage
            #print(currentmessage)

            uuid = MojangAPI.get_uuid(userinput)
            requestlink = f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}"

            hydata = requests.get(requestlink).json()

            player = hydata["player"]["displayname"]
            #print(player)
            karma = hydata["player"]["karma"]
            karma = "{:,}".format(karma)

            #print(f"{player} has {karma} karma")

            #logouttime = hydata['player']['lastLogout']
            #logintime = hydata['player']['lastLogin']

            rank = hydata['player']['newPackageRank']
            
            #logintimetest = str(logintime)
            #if logouttime < logintime:
                #online = False
            #else:
                #online = True
            #print(f'{player} has the rank {rank}')
            #print(logintime)
            #currentplayer = str(player)
            #currentrank = str(rank)
            #await message.reply("Player " + player "has " + karma + "karma, the" + rank + "rank, " + "and last logged in on " + logintime)
            await message.reply("Player " + player + " has te following stats:")
            await message.reply("Player stats:")
            await message.reply(rank + " rank")
            await message.reply(karma + " karma")
            
            await message.reply("Bedwars stats:")
            #4v4v4v4 bw stats
            await message.reply("4vs4vs4vs4:")
            try:
                bwplayed2 = str(hydata['player']['stats']['Bedwars']['four_four_games_played_bedwars'])
                await message.reply(bwplayed2 + " games played")
            except Exception as error:
                await message.reply("Cant get this players games played")
            try:
                bwWins2 = str(hydata['player']['stats']['Bedwars']['four_four_wins_bedwars'])
                await message.reply(bwWins2 + " wins")
            except Exception as error:
                await message.reply("Cant get this players wins for this gamemode")
            try:
                bwWinstreak2 = str(hydata['player']['stats']['Bedwars']['four_four_winstreak'])
                await message.reply(bwWinstreak2 + " winstreak")
            except Exception as error:
                await message.reply("Cant get this players winstreak for this gamemode")
            try:
                bwlosses2 = str(hydata['player']['stats']['Bedwars']['four_four_losses_bedwars'])
            except Exception as error:
                await message.reply("cant get this players losses for this gamemode")
                await message.reply(bwlosses2 + " losses")
            #3v3v3v3 bw stats
            try:
                await message.reply("3vs3vs3vs3 stats:")
                try:
                    bwplayed3 = str(hydata['player']['stats']['Bedwars']['four_three_games_played_bedwars'])
                    await message.reply(bwplayed3 + " games played")
                except Exception as error:
                    await message.reply("cant get this players games played for this gamemode")
                
                try:
                    bwWins3 = str(hydata['player']['stats']['Bedwars']['four_three_wins_bedwars'])
                    await message.reply(bwWins3 + " wins")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this players wins for this gamemode.")
                try:
                    bwWinstreak3 = str(hydata['player']['stats']['Bedwars']['four_three_winstreak'])
                    await message.reply(bwWinstreak3 + " winstreak")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this persons winstreak for this gamemode.")
                try:
                    bwlosses3 = str(hydata['player']['stats']['Bedwars']['four_three_losses_bedwars'])
                    await message.reply(bwlosses3 + " losses")
                except Exception as e:
                    print(e)
                
            except Exception as error:
                if error == "eight_two_wins_bedwars":
                    await message.reply("This player has no 3vs3vs3vs3 wins. L! Imagine being trash...")
                else:
                    print(error)
                    await message.reply("Something went wrong.")
            #4vs4 bw stats
            try:
                await message.reply("4vs4 stats:")
                try:
                    bwplayed4 = str(hydata['player']['stats']['Bedwars']['two_four_games_played_bedwars'])
                    await message.reply(bwplayed4 + " games played")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this players games played for this gamemode.")
                try:
                    bwWins4 = str(hydata['player']['stats']['Bedwars']['two_four_wins_bedwars'])
                    await message.reply(bwWins4 + " wins")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this players wins for this gamemode.")
                try:
                    bwWinstreak4 = str(hydata['player']['stats']['Bedwars']['two_four_winstreak'])
                    await message.reply(bwWinstreak4 + " winstreak")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this players winstreak for this gamemode")
                try:
                    bwlosses4 = str(hydata['player']['stats']['Bedwars']['two_four_losses_bedwars'])
                    await message.reply(bwlosses4 + " losses")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this players losses for this gamemode.")
            except Exception as error:
                if error == "eight_two_wins_bedwars":
                    await message.reply("This player has no 4vs4 wins. L! Imagine being trash...")
                else:
                    print(error)
                    await message.reply("Something went wrong.")
            #doubles
            try:
                await message.reply("Doubles stats:")
                try:
                    bwplayed5 = str(hydata['player']['stats']['Bedwars']['eight_two_games_played_bedwars'])
                    await message.reply(bwplayed5 + " games played")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this players games played for this gamemode.")
                try:
                    bwWins5 = str(hydata['player']['stats']['Bedwars']['eight_two_wins_bedwars'])
                    await message.reply(bwWins5 + " wins")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this players wins for this gamemode.")
                try:
                    bwWinstreak5 = str(hydata['player']['stats']['Bedwars']['eight_two_winstreak'])
                    await message.reply(bwWinstreak5 + " winstreak")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this players winstreak for this gamemode.")
                try:
                    bwlosses5 = str(hydata['player']['stats']['Bedwars']['eight_two_losses_bedwars'])
                    await message.reply(bwlosses5 + " losses")
                except Exception as e:
                    print(e)
                    await message.reply("Could not get this players losses for this gamemode.")
            except Exception as error:
                if error == "eight_two_wins_bedwars":
                    await message.reply("This player has no doubles wins. L! Imagine being trash...")
                else:
                    print(error)
                    await message.reply("Something went wrong.")
            #solo stats
            try:
                await message.reply("solo stats:")
                try:
                    bwplayed1 = str(hydata['player']['stats']['Bedwars']['eight_one_games_played_bedwars'])
                    await message.reply(bwplayed1 + " games played")
                except Exception as error:
                    await message.reply("cant get this players games played for this gamemode")
                try:
                    bwWins1 = str(hydata['player']['stats']['Bedwars']['eight_one_wins_bedwars'])
                    await message.reply(bwWins1 + " wins")
                except Exception as error:
                    await message.reply("This player has no solo wins. L! Imagine being trash...")
                try:
                    bwWinstreak1 = str(hydata['player']['stats']['Bedwars']['eight_one_winstreak'])
                    await message.reply(bwWinstreak1 + " winstreak")
                except Exception as error:
                    await message.reply("cant get this players winstreak for this gamemode")
                try:
                    bwlosses1 = str(hydata['player']['stats']['Bedwars']['eight_one_losses_bedwars'])
                    await message.reply(bwlosses1 + " losses")
                except Exception as error:
                    await message.reply("This player has not lost a single game... WHAT AN GOD!!!!!!!")
                try:
                    bwxp = str(hydata['player']['stats']['Bedwars']['Experience'])
                    await message.reply(bwxp + "Total bedwars xp")
                except Exception as error:
                    await message.reply("cant get this players bedwars xp.")

            except Exception as error:
                if error == "eight_one_wins_bedwars":
                    await message.reply("This player has no solo wins. L! Imagine being trash...")
                else:
                    print(error)
                    await message.reply("Something went wrong.")
                
            #if online == True:
                #await message.reply("And is currently online.")
            #if online == False:
                #await message.reply("And is currently offline.")
        except KeyError as E:
            if currentmessage == "/help":
                await message.reply("Type a username to get that person's stats or /BedwarsStats to get that person's bedwars stats.")
            
            else:        
                if currentmessage == "/BedwarsStats":
                    await message.reply("That is currently not possible yet. :(")
            
                else:
                    await message.reply("Je bericht is geen juiste naam.")
                    print(E)
                    buzy = False
        #if user_message == "/getstats":
    else:
        print("Message received but not in the right channel (hypixel-bot).")
client.run(TOKEN)