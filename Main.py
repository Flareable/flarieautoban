import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")
keep_alive()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Kata-kata yang dianggap toxic
banned_words = ["nigga", "nigg4", "n1gg4", "fuck", "stfu", "kontol", "k0nt0l", "nigga", "nigg4", "n1gga", "niqqa", "n!gga", "n1gg@", "n!gg@", "n!gg4", "nlgga",
    "fuck", "f*ck", "f@ck", "fuc*", "fucc", "fuk", "fck", "fuxk",
    "motherfucker", "m0therfucker", "motherf*cker", "moth3rfucker", "m0th3rf*cker",
    "bitch", "b!tch", "bi7ch", "b1tch", "b*tch", "biatch", "b!@tch",
    "asshole", "4sshole", "a$$hole", "ashole", "a55hole", "as$hole",
    "dick", "d1ck", "d!ck", "d*ck", "d!c*", "d1c*",
    "pussy", "dower", "p*ssy", "pu55y", "p@ssy", "p*55y",
    "suck my ass", "suck my d", "suck my d*ck", "suck my p*ssy", "lick my", "suck ur mom",
    "go to hell", "burn in hell", "die b*tch", "f you", "fuk u", "fck u",
    "stfu", "s-t-f-u", "stf*", "shut the fuck up",
    "kontol", "k0ntol", "k0ntl", "k*ntol", "kuntul", "kont*l", "k0nt*l",
    "memek", "m3m3k", "m3mek", "me***", "m3***", "m3m3*", "m*m3k",
    "ngentot", "ng3ntot", "ngent0t", "ng3nt0t", "ng*ntot", "ng*nt0t", "ngntt", "nge**",
    "anjing", "anj1ng", "4njing", "anji*ng", "anj!ng", "anji**", "anying",
    "bangsat", "b4ngsat", "bangs4t", "bangs@t", "b@ngsat", "bangs*t", "bangke", "bangkek",
    "tai", "t@i", "t4i", "ta1", "t4!",
    "bajingan", "b4jingan", "b@jingan", "baj1ngan", "b*jingan",
    "kampret", "kampr3t", "k4mpr3t", "k4mpret", "k4mpr3d", "kamp**",
    "goblok", "g0blok", "g*blok", "gob**k", "gblk", "g0bl0k", "gobl0k",
    "tolol", "t0l0l", "t*l*l", "tll", "t0l*l",
    "idiot", "idi0t", "id!ot", "idi0t", "1diot",
    "bego", "beg0", "b3g0", "b*g0", "bg0",
    "jancok", "j4ncok", "j@nco*k", "janc0k", "j4nc0k", "j4nck", "janco*k",
    "bitch ass", "fuck u", "bego lu", "lu goblok", "dasar tolol", "dasar anjing",
    "lu tai", "anjing lu", "ngentot lu", "memek lu", "kontol lu", "fuck this", "bitch please"]

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()
    username = str(message.author)  # hasilnya "username#discriminator", misalnya "aether_100#1234"
    username_only = str(message.author.name)  # cuma "aether_100"

    # List user yang dibebaskan dari auto-ban
    protected_users = ["aether_100"]

    if any(word in msg for word in banned_words):
        if username_only in protected_users:
            await message.channel.send(f"{message.author.mention} waduh tuan Flareable, kamu toxic ya, tapi karena kamu adalah pembuatku jadi tidak aku ban deh.")
            return  # stop sampai sini

        try:
            await message.author.ban(reason="Toxic language detected.")
            await message.channel.send(
                f"{message.author.mention} telah dibanned karena toxic!\n"
                f"**User has been banned** for using offensive language!"
            )
        except discord.Forbidden:
            await message.channel.send("Waduh mentang-menatng owner server berani toxic nih")
        except Exception as e:
            print(e)

    await bot.process_commands(message)

bot.run(TOKEN)