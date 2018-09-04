import threading
import discord

client = discord.Client()
client.ready = threading.Event()
CHANNELID = ""

class DiscordRelay(object):
    def __init__(self, protocol, config):
        self.token = config.get('token')
        CHANNELID = config.get('channelid')
        client_thread = threading.Thread(target=client.run, args=[self.token])
        client_thread.start()

    async def send(self, *arg, **kw):
        channel = discord.Object(id=CHANNELID)
        await client.send_message(channel, *arg)

    @client.event
    async def on_ready():
        print('Piqueserver Discord module successfully initialized.')
        channel = discord.Object(id=CHANNELID)
        await client.send_message(channel, "Piqueserver Discord module initialized.")

