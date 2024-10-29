from random import choice, randint
import discord




def get_response(user_input: str) -> str:
    lowered : str = user_input.lower()
    greetings = ['hi', 'hello', 'greetings', 'bonjour', 'hola']

    if lowered == '':
        return "Ⱳħɏ ⱥɍēꞥ'ⱦ ɏꝋᵾ ꞩꝑēⱥҟīꞥꞡ ⱦꝋ ᵯē?"
    elif user_input == 'boo hello' or user_input == 'boo hi' or user_input == 'boo bonjour' in lowered:
        return "ḩ̘̝̥̯̱̪͉̒̅_i̭̘͇͈̯̮͐͋̽̑̑, fr̗͓̞_͔͕́͊̈́̈́̽̏͆͌̊ͧ̕į̯̮̲̠͕̟̼̻̞̣͎̤̙̤̈́͐͆̅ͤ́̃ͫ͐̈́̏̓ͯͥ̌̐ͤ͆̓̅̚͝ḛͯ̋̑̑ͮ͘̕nd̷̨̢̨͎̫̱͉̫̤͖̞̬̖͒̉ͣ̋̉͑ͯ͗̉́ͪ̒̓͗́̋ͮ̎́͠."
    elif 'boo how are you' in lowered:
        return 'ɏꝋᵾ ɍēᵯīꞥđ ᵯē ꝋӻ ꞩꝋᵯēꝋꞥē ī ꝋꞥȼē ҟꞥēⱳ.'
    elif '<boo bye' in lowered: 
        return f'ꞥ-ꞥꝋ, ȼꝋᵯē ƀⱥȼҟ ħēɍē, ӻɍīēꞥđ. łēⱥꝟīꞥꞡ ⱦħīꞩ ēⱥɍłɏ?'
    elif 'boo roll dice' in lowered: 
        return f"ħēħ-ĦɄħēħĦȺȺ ꞩꝋ ɏꝋᵾ ⱳⱥꞥⱦ ⱦꝋ ꝑłⱥɏ ⱥ ꞡⱥᵯē, ɉᵾꞩⱦ ᵯē ⱥꞥđ ɏꝋᵾ? ⱦħīꞩ īꞩ ⱦħē ꞥᵾᵯƀēɍ ⱦħⱥⱦ łⱥꞥđēđ: {randint(1,6)}"
    elif '<@1292049993737175151> help' in lowered:
        return "Here are the possible list of commands you can chat with his loving and friendly spirit about: [boo hello], [boo how are you], [boo bye], [boo roll dice]. You can also type ? before the command (eg. ?boo hello) to take your conversation with Jeff into the DMs."
    #elif "let's video call":
        #send_image()
    else:
        return
   
"""async def send_image():
    image_path = "spookyjeff.png"
    with open(image_path, "rb") as image_file:
        await discord.send(file= discord.File(image_file)) """