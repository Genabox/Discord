#   ____ ___ ____   ____ ___  ____  ____                 
#  |  _ \_ _/ ___| / ___/ _ \|  _ \|  _ \                
#  | | | | |\___ \| |  | | | | |_) | | | |               
#  | |_| | | ___) | |__| |_| |  _ <| |_| |               
#  |____/___|____/ \____\___/|_| \_\____/  _ _____ _____ 
#  / ___/ ___|| | | |  / ___| |   |_ _| \ | | ____|_   _|
#  \___ \___ \| |_| | | |   | |    | ||  \| |  _|   | |  
#   ___) |__) |  _  | | |___| |___ | || |\  | |___  | |  
#  |____/____/|_| |_|  \____|_____|___|_| \_|_____| |_|  
                                                       
import nextcord
from nextcord.ext import commands
import paramiko
import asyncio
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom
from colorama import init, Fore, Style

# Initialize Nextcord intents
intents = nextcord.Intents.default()
intents.message_content = True

# Create a bot instance
bot = commands.Bot(command_prefix='/', intents=intents)

# Replace with your specific Discord channel ID and bot token
channelid = ''  # Discord channel ID for bot testing
token = ''  # Your bot token

# Global variables
ssh_clients = {}  # Dictionary to store SSH clients for each server
base_dir = "H:\\soft\\python\\ssh"  # Specify the path to the base directory
file_name = "serverlist.xml"
server_list_file = os.path.join(base_dir, file_name)

# Helper function to read the server list from the XML file
def read_server_list():
    server_list = []
    if os.path.exists(server_list_file):
        tree = ET.parse(server_list_file)
        root = tree.getroot()
        for server_element in root:
            server_info = {}
            server_info["name"] = server_element.find("name").text
            server_info["user"] = server_element.find("user").text
            server_info["ip"] = server_element.find("ip").text
            server_info["password"] = server_element.find("password").text
            server_list.append(server_info)
    return server_list

@bot.event
async def on_ready():
    print(f"{Fore.RED}[SSH BOT] @ === -- Bot successfully logged in as: {bot.user.name} -- === @ Discord{Style.RESET_ALL}")

# Helper function to write the server list to the XML file
def write_server_list(server_list):
    root = ET.Element("servers")
    for i, server_info in enumerate(server_list, 1):
        server_element = ET.Element(f"server{i}")
        name_element = ET.SubElement(server_element, "name")
        name_element.text = server_info["name"]
        user_element = ET.SubElement(server_element, "user")
        user_element.text = server_info["user"]
        ip_element = ET.SubElement(server_element, "ip")
        ip_element.text = server_info["ip"]
        password_element = ET.SubElement(server_element, "password")
        password_element.text = server_info["password"]
        root.append(server_element)

    tree = ET.ElementTree(root)
    tree.write(server_list_file, encoding="utf-8")

@bot.command()
async def readsetup(ctx):
    try:
        with open(server_list_file, 'r') as file:
            xml_content = file.read()
        await ctx.send("XML file content:\n```xml\n" + xml_content + "\n```")
    except FileNotFoundError:
        await ctx.send("The XML file does not exist.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Command to list servers
@bot.command()
async def serverlist(ctx):
    server_list = read_server_list()
    if server_list:
        formatted_list = ["Server list to connect:"]
        for i, server_info in enumerate(server_list, 1):
            name = server_info["name"]
            user = server_info["user"]
            ip = server_info["ip"]
            formatted_list.append(f"{i} {name}: {user}@{ip}")
        await ctx.send('\n'.join(formatted_list))
    else:
        await ctx.send("Server list is empty.")

@bot.command()
async def addserver(ctx, server_name: str, server_info: str):
    # Parse the server_info string to extract user, ip, and password
    server_info_parts = server_info.split("@")
    if len(server_info_parts) == 2:
        user, ip = server_info_parts
        password = "qwerty"  # You can set a default password here
    else:
        await ctx.send("Invalid server_info format. Use 'user@ip'.")
        return

    # Get the current server count from the XML file
    tree = ET.parse(server_list_file)
    root = tree.getroot()
    server_count = len(root)

    # Check if the server name is already used
    for server_element in root:
        name_element = server_element.find("name")
        if name_element is not None and name_element.text == server_name:
            await ctx.send("Server name is not unique. Please choose a different name.")
            return

    # Add the new server to the XML file with the next available server number
    server_element = ET.Element(f"server{server_count + 1}")
    user_element = ET.SubElement(server_element, "user")
    user_element.text = user
    ip_element = ET.SubElement(server_element, "ip")
    ip_element.text = ip
    password_element = ET.SubElement(server_element, "password")
    password_element.text = password

    # Add server name
    name_element = ET.SubElement(server_element, "name")
    name_element.text = server_name

    root.append(server_element)

    # Save the XML back to the file
    tree.write(server_list_file, encoding="utf-8", xml_declaration=True)

    with open(server_list_file, 'a') as file:
        file.write('\n')

    await ctx.send(f"Adding new server ({server_name}): {user}@{ip}")
    await ctx.send("Server added successfully.")

@bot.command()
async def removeserver(ctx, server_identifier: str):
    server_list = read_server_list()

    if not server_list:
        await ctx.send("Server list is empty.")
        return

    # Try to find the server to remove by name or index
    server_to_remove = None
    try:
        index = int(server_identifier)
        if 1 <= index <= len(server_list):
            server_to_remove = server_list[index - 1]
    except ValueError:
        for server in server_list:
            if server["name"].lower() == server_identifier.lower():
                server_to_remove = server

    if server_to_remove:
        server_list.remove(server_to_remove)
        write_server_list(server_list)
        await ctx.send(f"Removed server: {server_to_remove['name']} ({server_to_remove['user']}@{server_to_remove['ip']})")
    else:
        await ctx.send("Server not found in the list.")

# Global variables
ssh_clients = {}  # Dictionary to store SSH clients for each server
ssh_current_directory = {}  # Dictionary to store current directories for each server

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from other bots

    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    # Check if an SSH connection is established for the server associated with the message
    if message.guild.id in ssh_clients:
        ssh_client = ssh_clients[message.guild.id]

        # Get the current directory on the server
        current_directory = ssh_current_directory.get(message.guild.id, "/")

        # Concatenate text from all messages in the chat
        command = message.content
        async for msg in message.channel.history(limit=10):  # You can customize the message history limit
            if msg != message and not msg.author.bot:
                command += "\n" + msg.content

        # If the command starts with /cd, update the current directory
        if command.startswith("/cd "):
            new_directory = command.split("/cd ", 1)[1]
            ssh_current_directory[message.guild.id] = new_directory
            await message.channel.send(f"Changed directory to: {new_directory}")
            return

        # Full command to execute on the server
        full_command = f"(cd {current_directory} && {command})"

        # Send the text as a command to the SSH server
        try:
            stdin, stdout, stderr = ssh_client.exec_command(full_command)
            response = stdout.read().decode("utf-8")
            await message.channel.send(f"Received from SSH:\n```\n{response}\n```")
        except Exception as e:
            await message.channel.send(f"Failed to send command to SSH: {str(e)}")
    else:
        await bot.process_commands(message)  # Be sure to call this function to handle other commands

@bot.command()
async def connect(ctx, server_identifier: str):
    server_list = read_server_list()

    if not server_list:
        await ctx.send("Server list is empty. Use `/addserver` to add servers.")
        return

    # Try to find the server to connect by name or index
    server_to_connect = None
    try:
        index = int(server_identifier)
        if 1 <= index <= len(server_list):
            server_to_connect = server_list[index - 1]
    except ValueError:
        for server in server_list:
            if server["name"].lower() == server_identifier.lower():
                server_to_connect = server

    if server_to_connect:
        host = server_to_connect["ip"]
        username = server_to_connect["user"]
        password = server_to_connect["password"]

        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(host, username=username, password=password)

            ssh_clients[ctx.guild.id] = ssh_client
            await ctx.send(f"Connected to {host} as {username}.")
            await ctx.send("Now mirroring messages between Discord and SSH. Type `/disconnect` to disconnect.")

            await start_mirroring(ctx, ssh_client)
        except Exception as e:
            await ctx.send(f"Failed to connect to {host}: {str(e)}")
    else:
        await ctx.send("Server not found in the list. Use `/serverlist` to see available servers.")

@bot.command()
async def disconnect(ctx):
    if ctx.guild.id in ssh_clients:
        ssh_clients[ctx.guild.id].close()
        del ssh_clients[ctx.guild.id]
        await ctx.send("Disconnected from the server.")
    else:
        await ctx.send("Not connected to any server.")

async def start_mirroring(ctx, ssh_client):
    while True:
        if ctx.guild.id not in ssh_clients:
            break

        # Read messages from Discord chat
        try:
            message = await bot.wait_for("message", timeout=180)
        except asyncio.TimeoutError:
            continue

        if message.author == bot.user:
            continue

        if message.content.startswith("/disconnect"):
            # Send exit or logout command to SSH session
            try:
                ssh_client.exec_command("exit")  # You can use "exit" or "logout" here
                await asyncio.sleep(2)  # Wait for some time to allow SSH session to finish
                ssh_client.close()

                # Remove the SSH client from the dictionary
                del ssh_clients[ctx.guild.id]

                await ctx.send("Disconnected from the server.")
                break
            except Exception as e:
                await ctx.send(f"Failed to disconnect from SSH: {str(e)}")
                continue

        # Send Discord message to SSH session
        try:
            stdin, stdout, stderr = ssh_client.exec_command(message.content)
            await ctx.send(f"Sent to SSH: {message.content}")

            response = ""
            for line in stdout:
                response += line

            await ctx.send(f"Received from SSH: {response.strip()}")
        except Exception as e:
            await ctx.send(f"Failed to send message to SSH: {str(e)}")

@bot.command()
async def helpme(ctx):
    embed = nextcord.Embed(title="SSH Bot Commands", color=0x00ff00)
    embed.add_field(name="/serverlist", value="List available servers.", inline=False)
    embed.add_field(name="/addserver [name] [user@ip] [password]", value="Add a new server to the list.", inline=False)
    embed.add_field(name="/removeserver [name or index]", value="Remove a server from the list.", inline=False)
    embed.add_field(name="/readsetup", value="Show server setup file with passwords and all information.", inline=False)
    embed.add_field(name="/connect [name or index]", value="Connect to a server from the list.", inline=False)
    embed.add_field(name="/disconnect", value="Disconnect from the connected server.", inline=False)
    embed.add_field(name="ssh commands", value="Use pwd, cd, dir, and other commands to explore folders", inline=False)
    await ctx.send(embed=embed)

# Run the bot
bot.run(token)


#
#          )                 )               )    )  
#   (   ( /(   (          ( /(  (      (  ( /( ( /(  
# ( )\  )\())  )\ )   (   )\()) )\   ( )\ )\()))\()) 
# )((_)((_)\  (()/(   )\ ((_)((((_)( )((_|(_)\((_)\  
#((_)___ ((_)  /(_))_((_) _((_)\ _ )((_)_  ((_)_((_) 
# | _ ) \ / / (_)) __| __| \| (_)_\(_) _ )/ _ \ \/ / 
# | _ \\ V /    | (_ | _|| .` |/ _ \ | _ \ (_) >  <  
# |___/ |_|      \___|___|_|\_/_/ \_\|___/\___/_/\_\ 
#                                                   
#  # if you want, say thanks ~ btc: 14CZG7Tp9vyHLxJoCi1FYKzgyjeG3BuPMe
