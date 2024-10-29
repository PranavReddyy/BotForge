from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responsesdis import get_response
from discord import app_commands
from discord.ext import commands
import discord
from random import choice

#loding the token from env file 

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#setting up the bot using intents

intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
#message functionality

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empy because intents were not enabled')
        return
    
     #try [0:2] == 'boo'/""

    """this can also be written without the walrus operator (:=) which was introduced in a recent patch of python like this:
    is_private = user_message[0] == '?'
    if is_private: 
        user...."""
    
    if is_private := user_message[0] == '?': 
        user_message = user_message[1:]

    try: 
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

#handling the startup
@bot.event

async def on_ready() -> None: 
    print(f"{bot.user} is now running!")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e: 
        print(e)

@bot.tree.command(name="hello", description= "Say Hi to your new bestfriend!")

async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"ḩ̘̝̥̯̱̪͉̒̅_i̭̘͇͈̯̮͐͋̽̑̑, {interaction.user.mention}", ephemeral = True)

@bot.tree.command(name = "anon", description= "Send anonymous messages through jumping realities and timelines with Jeff.")

@app_commands.describe(anon_message = "What should I say?")

async def anon(interaction: discord.Interaction, anon_message: str):
    await interaction.response.send_message(f"Spooky Jeff is thinking...", ephemeral= True) 
    await interaction.followup.send(f"†hê vðï¢ê§ £rðm †hê å Ðï££êrêñ† rêålï†¥ ê¢hð †hï§ mê§§ågê, '{anon_message}'")

@bot.tree.command(name= "russianroulette", description= "łēⱦ'ꞩ ꝑłⱥɏ ⱥ ꞡⱥᵯē, ɉᵾꞩⱦ ᵯē ⱥꞥđ ɏꝋᵾ.")

async def roulette(interaction: discord.Interaction):
    luck = ["¥ðµ ÐïêÐ.","¥ðµ ÐïêÐ.","¥ðµ ÐïêÐ.","¥ðµ ÐïêÐ.","¥ðµ ÐïêÐ.","You Survived. H̯̐ͩO̸̴̶̝̻̹͇̖̖̪ͯ̇̌͌ͦͬ̓ͯ͑͝W̢̺̮̞͉̠̩͒͂͆̑͛̐͘̚͢ D̛͍͔̗̖̄ͥ́ͣ͆I̢̘͎͠_͍̈́D̜̬ͪ̅͟ YǪ̛̛̣̙͈͓̜̗̫͈̻͕̣͈͖͙͕̍̑̋ͮ͋ͩ̆͌͊̉̍̒̅̊̇̔̌̚͝͠Ư̛̰͑͂̊̈́ͧ͊́ͩ S̵̫̫̦͉͈̤̤͑ͯͨ͒ͦ̅Ư̡͕̏ͦͤR̸̶̨̢̥̲͍̘͇̲̘̞̯͙͈̥̉̒̾ͥ̌̃ͨͭ́̏͌̑ͦ̀͒ͣͮ̏̕V̶̯̰̺͎̪̰͖̞͉̞̤̰̗̘̳̓̌̐ͣ̿̓̅̌̓͆̓̀ͪͮͬͥ́ͮ͂̔̓ͫ͟͡I͍͋ͫͤ̃͟V̑̿́ͬE̶̡̢̢̨̛̮̲͚̙͚̝̩̲̫̼͍̦͙̊̆́̔̾͗͐̎̀̀ͧ̏̏͌̇ͬ͗̔̓̔͘͘̕̚͢͜͢ͅE̛̳͕̜̜̝͈̟̖͆̿̊ͯ̽̔̓̚E̢̹͚͍̮͚̘̺̤̯̟̖͓̻͎̙̙̾́̈́̏̀́̉̽ͪͤ̀͒ͩͯ͐͊̔̉͘͡͝È̴̠̫̗̳̜̰̥̦̣̺͙̣̣̫͊̔͗̑̐̉̌ͩ̃̏̃̄́̏͟͠͞?̸̵̶̨̡̥̖̼̜̮͔͍͕̫̮͖̤͍̦̗̭ͮ́̏̄ͩ̉̑͂͒ͥ̊ͬ͆́ͮͩ̂́ͩ͗̈́ͫ͘͟͝͞?͇̠̔͝?͚?̧̡̧̛̛͙̼̙͚͎͓̙̖̭̲͈̯͎͈͎̞͗̉ͦ́ͮ͗̓́ͯ̃̈̎̎̉̓͂͘͡͡͞ͅ!̨̻̟͔͎͖̹̖̦̮̲̞̗́͐̂͑̄̆̾̄͐̑ͣ̎̿̈́̐ͦ̐̒̽!̷̶̺͍̟̠̤̗̙͕̦͙͖͍̳̹̘̼̿͗ͭ̒ͧ͂͛̇͌̈̆̒̄́̒̆̆̇́̉̑ͣ͂́ͬ͢͜!̘̯̜̏͋͆ͮͫ͆́̑ͬͭ́ͬ̇̔ͅ"]
    await interaction.response.send_message(f"Ɏꝋᵾ łꝋⱥđ ⱦħē ꞡᵾꞥ ⱥꞥđ ꝑꝋīꞥⱦ īⱦ ⱦꝋ ɏꝋᵾɍ ħēⱥđ, *ɍⱥⱦⱦłīꞥꞡ ꞥꝋīꞩē*...{choice(luck)}")

@bot.tree.command(name = "help", description = "Get to know what all your new friend Jeff can do!")

async def help(interaction: discord.Interaction):
    await interaction.response.send_message(f"Jeff, an ambitious man from the 19th century, passed away mysteriously in 1883. Locals still whisper about his presence. On cold nights, some claim to hear faint footsteps or feel a chilling breeze, as if Jeff never truly left. Here are the possible list of commands you can chat with his loving and friendly spirit about: [boo hello], [boo how are you], [boo bye], [boo roll dice]. You can also type ? before the command (eg. ?boo hello) to take your conversation with Jeff into the DMs. Ofcourse, also feel free to use his application commands!", ephemeral= True)



#handling incoming messages 

@bot.event

async def on_message(message: Message) -> None: 
    if message.author == bot.user:
        return 
    
    username: str = str(message.author)
    user_message: str = message.content 
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#main entry point

def main() -> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()
