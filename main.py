import random

import discord as dis
from asyncio import sleep
from frogtips import api

prefix = "!"
client = dis.Client(intents=dis.Intents.all())
sopdict = {}
sopallids = []
sopalldict = {}
sopalltime = {}
sopids = []


def get_token(line):
    return open("bot token owo.txt").readlines()[line - 1]


token = get_token(17)


@client.event
async def on_message(msg: dis.Message):
    async def send(text):
        await sleep(0.25)
        await msg.channel.send(text)
    global sopids, sopfile, sopallids, sopallchoice, cooldown, lvl, xp
    if msg.content.split()[0] == f"{prefix}frogtip":
        try:
            await send(api.Tip(int(msg.content.split()[1])).get_formatted_tip())
        except:
            await send(api.Tips().get_next_tip().get_formatted_tip())
    try:
        if (msg.content.removeprefix(prefix) == "smashorpass" and msg.author.id not in sopids):
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            sopdict[msg.author.id] = random.randint(0, len(open("sop.ca").readlines()) - 1)
            await send(f"""<@{msg.author.id}>
    Smash -- or -- Pass
        {sopsplit[sopdict[msg.author.id]][2]}""")
            await send(sopsplit[sopdict[msg.author.id]][3])
            await send(f"{prefix}smash - {prefix}pass")
            sopids += [msg.author.id]
        elif msg.content.removeprefix(prefix) == "smashorpass" and msg.author.id in sopids:
            await send(
                "You already have an ongoing game, if this is false, please contact an admin to restart the bot to fix the issue")
        if msg.content.removeprefix(prefix).lower() == "smash" and msg.author.id in sopids:
            sopids.remove(msg.author.id)
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line].split(","))
            (sopsplit[sopdict[msg.author.id] - 1][0]) = int(sopsplit[sopdict[msg.author.id] - 1][0]) + 1
            sopsplitfinal = []
            for line in range(len(sopsplit)):
                sopsplitfinal.append(f"{sopsplit[line][0]},{sopsplit[line][1]},{sopsplit[line][2]},{sopsplit[line][3]}")
            open("sop.ca", "w").writelines(sopsplitfinal)
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(sopsplit[sopdict[msg.author.id]][2])
            await send(sopsplit[sopdict[msg.author.id]][3])
            await send(f"""You(<@{msg.author.id}>) Said: **smash**
            You agree with {round(((float(sopsplit[sopdict[msg.author.id]][0]) - 1) / ((float(sopsplit[sopdict[msg.author.id]][0]) - 1) + (float(sopsplit[sopdict[msg.author.id]][1])))) * 100)}% of people ({int(sopsplit[sopdict[msg.author.id]][0]) - 1} people)
            {prefix}smash - {round(((float(sopsplit[sopdict[msg.author.id]][0]) - 1) / ((float(sopsplit[sopdict[msg.author.id]][0]) - 1) + (float(sopsplit[sopdict[msg.author.id]][1])))) * 100)}% ({int(sopsplit[sopdict[msg.author.id]][0]) - 1} people)  {prefix}pass - {round(((float(sopsplit[sopdict[msg.author.id]][1])) / ((float(sopsplit[sopdict[msg.author.id]][0]) - 1) + (float(sopsplit[sopdict[msg.author.id]][1])))) * 100)}% ({int(sopsplit[sopdict[msg.author.id]][1])} people)""")
        if msg.content.removeprefix(prefix).lower() == "pass" and msg.author.id in sopids:
            sopids.remove(msg.author.id)
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line].split(","))
            (sopsplit[sopdict[msg.author.id] - 1][1]) = int(sopsplit[sopdict[msg.author.id] - 1][1]) + 1
            sopsplitfinal = []
            for line in range(len(sopsplit)):
                sopsplitfinal.append(f"{sopsplit[line][0]},{sopsplit[line][1]},{sopsplit[line][2]},{sopsplit[line][3]}")
            open("sop.ca", "w").writelines(sopsplitfinal)
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(sopsplit[sopdict[msg.author.id]][2])
            await send(sopsplit[sopdict[msg.author.id]][3])
            await send(f"""You(<@{msg.author.id}>) Said: **pass**
            You agree with {round(((float(sopsplit[sopdict[msg.author.id]][1]) - 1) / ((float(sopsplit[sopdict[msg.author.id]][0])) + (float(sopsplit[sopdict[msg.author.id]][1]) - 1))) * 100)}% of people ({int(sopsplit[sopdict[msg.author.id]][1]) - 1} people)
            {prefix}smash - {round((float(sopsplit[sopdict[msg.author.id]][0]) / ((float(sopsplit[sopdict[msg.author.id]][0])) + (float(sopsplit[sopdict[msg.author.id]][1]) - 1))) * 100)}% ({int(sopsplit[sopdict[msg.author.id]][0])} people)  {prefix}pass - {round(((float(sopsplit[sopdict[msg.author.id]][1]) - 1) / ((float(sopsplit[sopdict[msg.author.id]][0])) + (float(sopsplit[sopdict[msg.author.id]][1]) - 1))) * 100)}% ({int(sopsplit[sopdict[msg.author.id]][1]) - 1} people)""")
        if msg.content.split()[0] == f"{prefix}smashorpass" and msg.content.split()[1] == "all":
            sopalldict[msg.author.id] = -1
            sopalltime[msg.author.id] = -1
    
        if msg.content.removeprefix(prefix).lower() == "smash" and msg.author.id in sopallids:
            sopallids.remove(msg.author.id)
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line].split(","))
            (sopsplit[sopalldict[msg.author.id] - 1][0]) = int(sopsplit[sopalldict[msg.author.id] - 1][0]) + 1
            sopsplitfinal = []
            for line in range(len(sopsplit)):
                sopsplitfinal.append(f"{sopsplit[line][0]},{sopsplit[line][1]},{sopsplit[line][2]},{sopsplit[line][3]}")
            open("sop.ca", "w").writelines(sopsplitfinal)
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(sopsplit[sopalldict[msg.author.id]][2])
            await send(sopsplit[sopalldict[msg.author.id]][3])
            await send(f"""You(<@{msg.author.id}>) Said: **smash**
            You agree with {round(((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) / ((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) + (float(sopsplit[sopalldict[msg.author.id]][1])))) * 100)}% of people ({int(sopsplit[sopalldict[msg.author.id]][0]) - 1} people)
            {prefix}smash - {round(((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) / ((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) + (float(sopsplit[sopalldict[msg.author.id]][1])))) * 100)}% ({int(sopsplit[sopalldict[msg.author.id]][0]) - 1} people)  {prefix}pass - {round(((float(sopsplit[sopalldict[msg.author.id]][1])) / ((float(sopsplit[sopalldict[msg.author.id]][0]) - 1) + (float(sopsplit[sopalldict[msg.author.id]][1])))) * 100)}% ({int(sopsplit[sopalldict[msg.author.id]][1])} people)""")
            await send("‎")
        if msg.content.removeprefix(prefix).lower() == "pass" and msg.author.id in sopallids:
            sopallids.remove(msg.author.id)
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line].split(","))
            (sopsplit[sopalldict[msg.author.id] - 1][1]) = int(sopsplit[sopalldict[msg.author.id] - 1][1]) + 1
            sopsplitfinal = []
            for line in range(len(sopsplit)):
                sopsplitfinal.append(f"{sopsplit[line][0]},{sopsplit[line][1]},{sopsplit[line][2]},{sopsplit[line][3]}")
            open("sop.ca", "w").writelines(sopsplitfinal)
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(sopsplit[sopalldict[msg.author.id]][2])
            await send(sopsplit[sopalldict[msg.author.id]][3])
            await send(f"""You(<@{msg.author.id}>) Said: **pass**
            You agree with {round(((float(sopsplit[sopalldict[msg.author.id]][1]) - 1) / ((float(sopsplit[sopalldict[msg.author.id]][0])) + (float(sopsplit[sopalldict[msg.author.id]][1]) - 1))) * 100)}% of people ({int(sopsplit[sopalldict[msg.author.id]][1]) - 1} people)
            {prefix}smash - {round((float(sopsplit[sopalldict[msg.author.id]][0]) / ((float(sopsplit[sopalldict[msg.author.id]][0])) + (float(sopsplit[sopalldict[msg.author.id]][1]) - 1))) * 100)}% ({int(sopsplit[sopalldict[msg.author.id]][0])} people)  {prefix}pass - {round(((float(sopsplit[sopalldict[msg.author.id]][1]) - 1) / ((float(sopsplit[sopalldict[msg.author.id]][0])) + (float(sopsplit[sopalldict[msg.author.id]][1]) - 1))) * 100)}% ({int(sopsplit[sopalldict[msg.author.id]][1]) - 1} people)""")
            await send("‎")
        if msg.content.removeprefix(prefix).lower() == "stop" and msg.author.id in sopallids:
            await send("Stopped!")
            sopallids.remove(msg.author.id)
            sopalltime[msg.author.id] = len(open("sop.ca").readlines()) - 1
            msg.content = 0
        if (sopalltime[msg.author.id] != len(
                open("sop.ca").readlines()) - 1) and msg.author.id not in sopallids:
            sopallids += [msg.author.id]
            if sopalltime[msg.author.id] == -1:
                sopallchoice = []
                sopallchoice = random.sample(range(0, len(open("sop.ca").readlines())),
                                             len(open("sop.ca").readlines()))
            sopalltime[msg.author.id] += 1
            sopalldict[msg.author.id] = sopallchoice[sopalltime[msg.author.id]]
            sopfile = open("sop.ca").readlines()
            sopsplit = []
            for line in range(len(open("sop.ca").readlines())):
                sopsplit.append(sopfile[line - 1].split(","))
            await send(f"""<@{msg.author.id}>
            Smash -- or -- Pass [{sopalltime[msg.author.id] + 1}/{len(open("sop.ca").readlines())}]
                {sopsplit[sopalldict[msg.author.id]][2]}""")
            await send(sopsplit[sopalldict[msg.author.id]][3])
            await send(f"{prefix}smash - {prefix}pass - {prefix}stop")
        elif msg.content.removeprefix(prefix) == "smashorpassall" and (sopalltime[msg.author.id] > -1):
            await send(
                "You already have an ongoing game, if this is false, please contact an admin to restart the bot to fix the issue")
    except:
        pass

client.run(token)
