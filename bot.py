import discord
from discord.ext import commands
import asyncio
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus.dll')
f = open('token.txt','r')
voice = None
client = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='Cowbell bot under construction')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(client)

    
def end_cowbell():
    coro = voice.disconnect()
    fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
    try:
        fut.result()
    except:
        # an error happened sending the message
        pass

@client.command(pass_context=True, no_pm=True)
async def cowbell(ctx):
    """Summons the bot to join your voice channel."""
    summoned_channel = ctx.message.author.voice_channel
    if summoned_channel is None:
        await self.bot.say('You are not in a voice channel.')
        return False
    global voice
    voice = await client.join_voice_channel(summoned_channel)
    player = voice.create_ffmpeg_player('cowbell.mp3',after=end_cowbell)
    player.start()
    return True
client.run(f.read())
