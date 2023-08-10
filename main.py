import discord as dis
from asyncio import sleep
from frogtips import api

prefix = "!"
client = dis.Client(intents=dis.Intents.all())


def get_token(line):
    return open("bot token.txt").readlines()[line - 1]#file made seperately as bot token is private


token = get_token(17)


@client.event
async def on_message(msg: dis.Message):
    async def send(text):
        await sleep(0.25)
        await msg.channel.send(text)

    if msg.content.split()[0] == f"{prefix}frogtip":
        try:
            await send(api.Tip(int(msg.content.split()[1])).get_formatted_tip())
        except:
            await send(api.Tips().get_next_tip().get_formatted_tip())


client.run(token)
