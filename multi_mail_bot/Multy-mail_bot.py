                                            
#                                                        ┓ ┏   ┏┓   ┳┓   ┏┳┓   ┏┓   ┳┓
#                                                        ┃┃┃   ┣┫   ┃┃    ┃    ┣    ┃┃
#                                                        ┗┻┛   ┛┗   ┛┗    ┻    ┗┛   ┻┛
#               
#                                         A         ****   S T A T E  S H E R I F F   ****         A 

  ########################################################    ########################################################    ########################################### 
    #                                     ✦        *        *        *         #          ✦        *        *        *        *  #          ✦                         $#
    # ooo        ooooo             oooo      .                                                    o8o  oooo        .o8                     .                        #$
    #  `88.       .888'             `888    .o8                                                    `"'  `888       "888                   .o8                   czd
    #   888b     d'888  oooo  oooo   888  .o888oo oooo    ooo         ooo. .oo.  .oo.    .oooo.   oooo   888        888oooo.   .ooooo.  .o888oo 
    #   8 Y88. .P  888  `888  `888   888    888    `88.  .8'          `888P"Y88bP"Y88b  `P  )88b  `888   888        d88' `88b d88' `88b   888                   nn
    #   8  `888'   888   888   888   888    888     `88..8'   8888888  888   888   888   .oP"888   888   888        888   888 888   888   888               sdfds
    #   8    Y     888   888   888   888    888 .    `888'             888   888   888  d8(  888   888   888        888   888 888   888   888 . 
    #  o8o        o888o  `V88V"V8P' o888o   "888"     .8'             o888o o888o o888o `Y888""8o o888o o888o       `Y8bod8P' `Y8bod8P'   "888"         dfsdf
    #                                            .o..P'                                                                                        
    #                                           `Y8P'                                       ✦        *        *        ✦        *        *        *   d3%#
    #          *        ✦       *        *        *                                                                                                                                      
    ########################################################  ########################################################  ########################### 

    ###################################################
    #   #########  #########  #########  #########    #    ?***********
    #                                                 # ?***********
""""#  .......................                 """    #           ?***********"""
""""#  .......................                 """    #       ?***********
""""#  .......................                 """    # * **********
    ##                                                #        
    ##                                                #                                                           
    ##                                                #?***********?***********
    ##                                                #     ?***********
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
    ###################################################

        #______________________________________
        
                # F U T U R E S:
        #______________________________________

            # - Make a new letter:

        #/newletter (type /newletter to send a new letter) Example: #(line1) '/newletter'
        # Type the recipient's email on line number two Example: #(line2) 'email@email'
        # Type the subject on the third line Example: #(line3) 'Subject'
        # Type the message text on line number 4 and other lines of the message Example: #(line4) 'Mail body text'

        # So you need to set up 4 lines to send your new mail:

        #/newletter
        #email@email
        #my letter subject
        #my letter text

        # That is all.
        # ``````````````````````

            # - Check mail:

        #/mail - Check mail...
        # ``````````````````````
        
            # - Sending a reply:

        # Send a reply to a message on mail in a Discord channel - the email will be sent to the sender's mailbox @
        # ``````````````````````

            # - Software multi-mail bot description:

        # Add multiple accounts as you need, one per 1 text channel. Each text channel works like a mailbox for one account. Use another text channel for a second mail account, and set
        # channel IDs to configure it. Don't forget emojis to design your message folder style (Discord channel name setup, just copy and paste your favorite emoji into the text field)

        # Set up folders to receive letters from them

        # All new reader letters are marked as READ on your mail server and are not uploaded again to your channel

        # Send links or files as attachments

        # Set Interval in seconds to fetch your mailbox

        # You can set up music files from the archive to set notifications on new letters, just uncommit lines with sound definition to play them on terminal window or translate this sound to your other devices

        # /helpme - get help on chat

        # Important: if you read a letter in your mailbox and it is marked as read, it will be ignored by the bot and will not be delivered to the chat if this has not already happened

        # If you see an authentication problem, then you need to create access to other software and make a technical password on your mail provider in your account to allow access to this bot.
        # ``````````````````````

            # - Bot setup:

        # Add a new program to the Discord developer's account, authorize it on your Discord server

        # Set your new token to the script

        # Set up your mailboxes, folders to receive from them

        # Add a mail category to your server

        # Set up channels on your server and set IDs to the script; you can also set up your contacts' personal channels in the mail category

        # Run the Python script; as a result, you will see "Bot online," and you will see new mail on your channels

        # ``````````````````````


                                                                                          # MADE BY GENABOX 29/11/2023 --
                 
#                *        *        *        *       

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#


#                                        ``````````                   ``````````
    #                                        ``````````                   ``````````

                                        #   S Y S T E M   I M P O R T   S E T U P   

# Import the necessary module, assuming you have already imported the required libraries.
# You may need to add "import nextcord" and "from nextcord.ext import commands" if not already done.

#-----------system import-----------#
import re
import nextcord
from nextcord.ext import commands
import imaplib
from email import message_from_bytes
import asyncio
from email.header import decode_header
from colorama import init, Fore, Style
from bs4 import BeautifulSoup
from email.mime.text import MIMEText 
import smtplib
from email.mime.text import MIMEText

#                                        ``````````                   ``````````
    #                                        ``````````                   ``````````

                                        #   S O U N D   S E T U P
# ----- sound part --------------------------------------------------@
# Import necessary modules for playing sounds.
from pydub import AudioSegment
from pydub.playback import play
import os
import threading

# Get the current directory of the script.
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# Define a function to play a sound from a given file path.
def play_sound(file_path):
    try:
        sound = AudioSegment.from_file(file_path)
        play(sound)
    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to play a sound for a new letter.
def pley_new_letter():
    mp3_path = current_directory+'/sound/bot_new_letter.mp3'  # Replace with your own sound file path
    sound_thread = threading.Thread(target=play_sound, args=(mp3_path,))
    sound_thread.start()

# Define a function to play a sound for manual email checking.
def pley_manual_check():
    mp3_path = current_directory+'/sound/bot_manual_check.mp3'  # Replace with your own sound file path
    sound_thread = threading.Thread(target=play_sound, args=(mp3_path,))
    sound_thread.start()

# Define a function to play a sound for bot errors.
def pley_bot_error():
    mp3_path = current_directory+'/sound/bot_error.mp3'  # Replace with your own sound file path
    sound_thread = threading.Thread(target=play_sound, args=(mp3_path,))
    sound_thread.start()

# ----- sound part --------------------------------------------------@

 #                                        ``````````                   ``````````
    #                                        ``````````                   ``````````

                                        #   B O T   S E T U P
########## PREVILEGIES $$$$$$$$$$$
# Define the command prefix for your bot.
command_prefix = '/'

# Create an instance of the Bot class with specified intents.
intents = nextcord.Intents.default()
intents.message_content = True

# Initialize the bot with the defined command prefix and intents.
bot = commands.Bot(command_prefix, intents=intents)

########## BOT LOGIN $$$$$$$$$$$
TOKEN = 'test'

######################## THIS FUNCTION MAKE TIME STAMP ON SIGNATURE AND TERMINAL ######################## 
import datetime  # Make sure to import the datetime module if not already done.

def get_current_time():
    # Return the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# You can use this function like this to insert timestamps in other places of your code:
# timestamp = get_current_time()
# print(f'This is a log entry with a timestamp: {timestamp}')



#                                        ``````````                   ``````````
    #                                        ``````````                   ``````````

                                        #   E M A I L   A C C O U N T S   S E T U P

######################## THIS SETUP DATA DOR YOUR EMAIL BOXES ######################## 

#Mail featching interval
FETCH_INTERVAL_SECONDS = 365  # Interval in seconds (5 minutes)

# Your sender name
mysendername = 'First name Last name'

# Signature for replyes and new lerres
signature = '----------------------------------------------------------------------------------- \n My best, First name Last name. Contacts:\n+ 123, + 123\ne-mail: email@email, email@email\nDiscord: discord nikname \nGithub: https://github.com/ \nThis message send by free-source mail software https://github.com/Genabox/Discord/tree/main/multi_mail_bot'

#****************************************  Email Accounts *************************************************

email_accounts = [
    {
        #                                        ``````````     MAIL PROVIDER LOGO              ``````````
        #                                        ``````````                                     ``````````
        #+================= email account 1 ==================+
        'email_address': 'email@email', #EMAIL ADDRESS
        'email_password': 'password', #EMAIL PASSWORD
        'imap_server': 'address', #EMAIL IMAP SERVER
        'discord_channel_id': 123, #CHANNEL ID OF YOUR DISCORD MAIL CHANNEL
        'folders': ['INBOX', 'archive'] ,  # Replace "INBOX" with the name of the folder from which you want to select letters.

        'smtp_server': 'address',  #EMAIL SMTP
        'smtp_port': 587,  #EMAIL SMTP PORT
        'smtp_username': 'email@email',  #EMAIL SMTP USERNAME
        'smtp_password': 'password'  #EMAIL SMTP MASSWORD
    },

    {
        #                                        ``````````     MAIL PROVIDER LOGO              ``````````
        #                                        ``````````                                     ``````````
        #+================= email account 2 ==================+
        'email_address': 'email@email', #EMAIL ADDRESS
        'email_password': 'password', #EMAIL PASSWORD
        'imap_server': 'address', #EMAIL IMAP SERVER
        'discord_channel_id': 123, #CHANNEL ID OF YOUR DISCORD MAIL CHANNEL
        'folders': ['INBOX', 'archive'] ,  # Replace "INBOX" with the name of the folder from which you want to select letters.

        'smtp_server': 'address',  #EMAIL SMTP
        'smtp_port': 587,  #EMAIL SMTP PORT
        'smtp_username': 'email@email',  #EMAIL SMTP USERNAME
        'smtp_password': 'password'  #EMAIL SMTP MASSWORD
    }

# -------- Add more accounts as needed !! --------
]

 
#                                        ``````````                   ``````````
    #                                        ``````````                   ``````````

                                        #   P R O C E S S I N G    M A I L    L E T T E R    T E X T    F O R   C H A T

######################## THIS FUNCTION CLEANING UP TEXT IN RECEIVED LETTERS TO POST IT IN CHAT THREAD ######################## 
def clean_text(text):
    # Replace multiple consecutive line breaks with just two line breaks.
    cleaned_text = text.replace('\n\n', '\n')

    # Replace any remaining consecutive whitespace characters with a single space.
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    # Remove leading and trailing whitespace from the text.
    cleaned_text = cleaned_text.strip()
 
    # Trim the text to a maximum of 1700 characters.
    cleaned_text = cleaned_text[:1700]

    return cleaned_text
  
######################## THIS FUNCTION NOTIFIES YOU THE BOT IS READY ######################## 
@bot.event  # Define an event handler for when the bot is ready.
async def on_ready():
    # Print a message when the bot is successfully logged in.
    print(f"{Fore.YELLOW}[MULTY-MAIL BOT] @ === -- Bot successfully logged in as: {bot.user.name} -- === @ Discord")
    
    # Iterate through a list of email accounts and create a coroutine task for each.
    for account in email_accounts:
        # Create a coroutine task to fetch mail for each email account.
        bot.loop.create_task(fetch_mail(account))

       


#                                        ``````````                   ``````````
    #                                        ``````````                   ``````````

                                        #   P R O C E S S I N G    A L L    C H A T    M E S S A G E S    I N C L U D E   C O M A N D S  

######################## THIS FUNCTION PROCESSING MESSAGES ######################## 

@bot.event  # Define an event handler for when a message is received.
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages sent by the bot itself.

    # Check if the current channel is in the list of allowed channels for the bot.
    allowed_channels = [acc['discord_channel_id'] for acc in email_accounts]

    if message.channel.id not in allowed_channels:
        return  # Ignore messages in channels not configured for the bot.

    # Get the ID of the current Discord channel.
    current_channel_id = message.channel.id

    # Search for a dictionary in email_accounts based on discord_channel_id.
    account = next((acc for acc in email_accounts if acc['discord_channel_id'] == current_channel_id), None)

    if account:
        email_address = account['email_address']
        # You now have the value of email_address for the current channel.
        # print(f'Email Address for Current Channel: {email_address}')
        receiver = email_address
    else:
        # If the channel is not found in email_accounts, you can handle it accordingly.
        print('There is no configured account for sending emails in this channel.')

    if message.type == nextcord.MessageType.default:
        await handle_newletter(account, message)
    else:
        if message.type == nextcord.MessageType.reply:
            await handle_reply(account, message)

    if '/mail' in message.content:
        await fetch_mail_manual(account, message.channel)
    # else:
    #     await message.channel.send('Mail has been successfully checked and updated.')

    if '/helpme' in message.content:
        await message.channel.send('Hi, I am a Mail Discord bot. How can I assist you?')


        
 
                                        #   R E C E I V E    M A I L    F U N T I O N   
         #                                        ``````````                ``````````                ``````````
          #                                         ``````````                ``````````                ``````````
######################## THIS FUNCTION PROCESSING MESSAGES FROM MAILBOX TO CHAT ######################## 

async def fetch_mail(account):
    # Extract email account information from the provided 'account' dictionary.
    email_address = account['email_address']
    email_password = account['email_password']
    imap_server = account['imap_server']
    discord_channel_id = account['discord_channel_id']

    # Check if the 'folders' key exists, and if not, use 'folder' instead.
    if 'folders' in account:
        folders = account['folders']
    else:
        folders = [account['folder']]

    # Continuously fetch and process emails as long as the bot is not closed.
    while not bot.is_closed():
        try:
            for folder in folders:
                # Connect to the IMAP server.
                mail_server = imaplib.IMAP4_SSL(imap_server)
                mail_server.login(email_address, email_password)
                mail_server.select(folder)

                # Search for unread emails.
                _, message_ids = mail_server.search(None, 'UNSEEN')
                message_ids = message_ids[0].split()

                for message_id in message_ids:
                    _, message_data = mail_server.fetch(message_id, '(RFC822)')
                    raw_message = message_data[0][1]
                    parsed_message = message_from_bytes(raw_message)

                    # Extract information from the email.
                    subject = parsed_message['subject']
                    decoded_subject = decode_header(subject)[0][0]
                    if isinstance(decoded_subject, bytes):
                        decoded_subject = decoded_subject.decode('utf-8')
                    sender = parsed_message['from']
                    decoded_sender = decode_header(sender)[0][0]
                    if isinstance(decoded_sender, bytes):
                        decoded_sender = decoded_sender.decode('utf-8')

                    # Check for text/plain or text/html parts in the email.
                    body_text = ""
                    for part in parsed_message.walk():
                        content_type = part.get_content_type()
                        if "text/plain" in content_type:
                            payload = part.get_payload(decode=True).decode()
                            body_text = payload
                        elif "text/html" in content_type:
                            payload = part.get_payload(decode=True).decode()
                            soup = BeautifulSoup(payload, 'html.parser')
                            body_text = soup.get_text()

                    # Clean up unnecessary line breaks and spaces in the email body.
                    cleaned_body_text = clean_text(body_text)

                    # Print email details for debugging.
                    print(f'Sender: {decoded_sender}')
                    print(f'Subject: {decoded_subject}')
                    print(f'Folder: {folder}')
                    print(f'Body of the email:\n{cleaned_body_text}')
                    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')

                    # Send a message to the Discord channel.
                    channel = bot.get_channel(discord_channel_id)
                    await channel.send(f'**New letter from**: {decoded_sender}\n'
                                       f'**Subject**: {decoded_subject}\n'
                                       f'**Mailbox**: {email_address}\n'
                                       f'**Folder**: {folder}\n'
                                       f'**Body**: {cleaned_body_text}\n'
                                       f'============================\n')

                    # Mark the email as read.
                    mail_server.store(message_id, '+FLAGS', '\\Seen')

                    # Print a message to indicate successful email processing.
                    print(f'{Fore.GREEN}[{get_current_time()}] [MAILBOT] {email_address} New letters received.{Style.RESET_ALL}')

                mail_server.logout()

            # Print a message to indicate successful completion of email processing.
            print(f'{Fore.LIGHTRED_EX}[{get_current_time()}] [MAILBOT] {email_address} Letters successfully received and processed.{Style.RESET_ALL}')

        except Exception as e:
            # Print an error message in case of any exceptions.
            print(f'{Fore.RED}[{get_current_time()}] [MAILBOT] {email_address} Error while receiving or processing emails: {e}{Style.RESET_ALL}')
            
        # Add a delay before fetching emails again.
        await asyncio.sleep(FETCH_INTERVAL_SECONDS)



        #        ``````````     ``````````            ``````````                ``````````                   ``````````
        #        ``````````     ``````````            ``````````                ``````````                   ``````````


######################## THIS FUNCTION PROCESSING MESSAGES FROM MAILBOX TO CHAT MANUALITY######################## 
async def fetch_mail_manual(account, discord_channel):
    # Extract email account information from the provided 'account' dictionary.
    email_address = account['email_address']
    email_password = account['email_password']
    imap_server = account['imap_server']

    # Check if the 'folders' key exists, and if not, use 'folder' instead.
    if 'folders' in account:
        folders = account['folders']
    else:
        folders = [account['folder']]

    try:
        for folder in folders:
            # Connect to the IMAP server.
            mail_server = imaplib.IMAP4_SSL(imap_server)
            mail_server.login(email_address, email_password)
            mail_server.select(folder)

            # Search for unread emails.
            _, message_ids = mail_server.search(None, 'UNSEEN')
            message_ids = message_ids[0].split()

            for message_id in message_ids:
                _, message_data = mail_server.fetch(message_id, '(RFC822)')
                raw_message = message_data[0][1]
                parsed_message = message_from_bytes(raw_message)

                # Extract information from the email.
                subject = parsed_message['subject']
                decoded_subject = decode_header(subject)[0][0]
                if isinstance(decoded_subject, bytes):
                    decoded_subject = decoded_subject.decode('utf-8')
                sender = parsed_message['from']
                decoded_sender = decode_header(sender)[0][0]
                if isinstance(decoded_sender, bytes):
                    decoded_sender = decoded_sender.decode('utf-8')

                # Check for text/plain or text/html parts in the email.
                body_text = ""
                for part in parsed_message.walk():
                    content_type = part.get_content_type()
                    if "text/plain" in content_type:
                        payload = part.get_payload(decode=True).decode()
                        body_text = payload
                    elif "text/html" in content_type:
                        payload = part.get_payload(decode=True).decode()
                        soup = BeautifulSoup(payload, 'html.parser')
                        body_text = soup.get_text()

                # Clean up unnecessary line breaks and spaces in the email body.
                cleaned_body_text = clean_text(body_text)

                # Print email details for debugging.
                print(f'Sender: {decoded_sender}')
                print(f'Subject: {decoded_subject}')
                print(f'Folder: {folder}')
                print(f'Body of the email:\n{cleaned_body_text}')
                print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')

                # Send a message to the Discord channel.
                await discord_channel.send(f'**New letter from**: {decoded_sender}\n'
                                           f'**Subject**: {decoded_subject}\n'
                                           f'**Mailbox**: {email_address}\n'
                                           f'**Folder**: {folder}\n'
                                           f'**Body**: {cleaned_body_text}\n'
                                           f'============================\n')

                # Mark the email as read.
                mail_server.store(message_id, '+FLAGS', '\\Seen')

            mail_server.logout()

        # Print a message to indicate successful completion of email processing.
        print(f'{Fore.BLUE}[{get_current_time()}] [MAILBOT] Letters successfully received and processed manually.{Style.RESET_ALL}')

        #``````````````````````````````````````

        # Play a sound to indicate successful email verification in the terminal.
        # pley_manual_check()
        # Uncommit this line to play sound on receiving new letters

        #``````````````````````````````````````

        # Send a notification of successful email verification to the chat.
        await discord_channel.send('Mail was successfully verified and updated')

    except Exception as e:
        # Print an error message in case of any exceptions.
        print(f'{Fore.RED}[{get_current_time()}] [MAILBOT] Error while receiving or processing emails: {e}{Style.RESET_ALL}')
        # Play a sound to indicate an error in email verification in the terminal.
        pley_bot_error()






        #                                        ``````````                   ``````````
    #                                        ``````````                   ``````````

                                        #   S E N D     M A I L    F U N T I O N S  


######################## THIS FUNCTION SEND MAIL AND PRINT RESULT IN TERMINAL WITH SENDING PROGRESS ######################## 

async def send_email_new(account, sender, sender_email, sender_name, subject, body, message, receiver, sendfunction, email_address):
    global signature, mysendername

    try:
        # Find the email account based on the receiver's email address.
        account = next((acc for acc in email_accounts if acc['email_address'] == email_address), None)

        if account is None:
            print(f'No account found for receiver: {receiver}')
            return

        # Extract email account configuration information.
        email_password = account.get('email_password', '')
        smtp_server = account.get('smtp_server', '')
        smtp_port = account.get('smtp_port', 0)
        smtp_username = account.get('smtp_username', '')
        smtp_password = account.get('smtp_password', '')
        channel_id = account.get('discord_channel_id')
        channel = bot.get_channel(channel_id)

        # Check if the account configuration is valid.
        if not email_password or not smtp_server or not smtp_port or not smtp_username or not smtp_password:
            print('Invalid account configuration')
            pley_bot_error()
            return

        # Connect to the SMTP server.
        print(f'SENDMAIL: Starting sending new letter message...')
        print(f'Connecting to SMTP server: {smtp_server}:{smtp_port}')
        smtp_server_obj = smtplib.SMTP(smtp_server, smtp_port)
        smtp_server_obj.starttls()
        smtp_server_obj.login(smtp_username, smtp_password)
        print('SMTP server connection successful')

        nettime = get_current_time()

        # Create the email message.
        full_message = f"From {mysendername}\n{body}\n"
        msg = MIMEText(full_message, 'plain', 'utf-8')
        msg['To'] = receiver
        msg['From'] = f'{sender_name} <{sender_email}>'
        msg['Subject'] = subject

        # Attempt to send the email.
        try:
            print('Sending email...')
            smtp_server_obj.send_message(msg)
            print(f'{Fore.GREEN}Email sent successfully to: {receiver}, Subject: {subject} {nettime}')
            await channel.send(f'Email sent successfully to: <{receiver}>\nSubject: {subject}\n{body}')
        except Exception as send_error:
            print(f'Error while sending email: {send_error}')
            print(f'Sender Email: {sender_email}')
            print(f'Sender Name: {sender_name}')
            print(f'Subject: {subject}')
            print(f'Body: {body}')
        finally:
            # Close the connection to the SMTP server.
            smtp_server_obj.quit()

    except Exception as e:
        print(f'{Fore.RED}Error while sending email: {e}')

 


        #        ``````````     ``````````            ``````````                ``````````                   ``````````
 
######################## THIS FUNCTION SEND MAIL AND PRINT RESULT IN TERMINAL WITH SENDING PROGRESS ######################## 

async def send_email_reply(account, sender, sender_email, sender_name, subject, body, message, receiver, sendfunction, email_address):
    global signature, mysendername

    try:
        # Find the email account based on the receiver's email address.
        account = next((acc for acc in email_accounts if acc['email_address'] == receiver), None)

        if account is None:
            print(f'No account found for receiver: {email_address}')
            pley_bot_error()
            return

        # Extract email account configuration information.
        email_password = account.get('email_password', '')
        smtp_server = account.get('smtp_server', '')
        smtp_port = account.get('smtp_port', 0)
        smtp_username = account.get('smtp_username', '')
        smtp_password = account.get('smtp_password', '')
        channel_id = account.get('discord_channel_id')
        channel = bot.get_channel(channel_id)

        # Check if the account configuration is valid.
        if not email_password or not smtp_server or not smtp_port or not smtp_username or not smtp_password:
            print('Invalid account configuration')
            return
        
        # Connect to the SMTP server.
        print(f'SENDMAIL: Starting sending reply on message...')
        print(f'Connecting to SMTP server: {smtp_server}:{smtp_port}')
        smtp_server_obj = smtplib.SMTP(smtp_server, smtp_port)
        smtp_server_obj.starttls()
        smtp_server_obj.login(smtp_username, smtp_password)
        print('SMTP server connection successful')

        nettime = get_current_time()

        # Create the email message.
        full_message = f"From {mysendername} {receiver}\nSubject RE: {subject}\n{message.content}\n{'=' * 50}\n{nettime}\n{signature}\n\n{'*' * 20}{' Your message '}{'*' * 40}\n{body}"
        msg = MIMEText(full_message, 'plain', 'utf-8')
        msg['From'] = receiver
        msg['To'] = f'{sender_name} <{sender_email}>'
        msg['Subject'] = subject

        # Attempt to send the email.
        try:
            print('Sending email...')
            smtp_server_obj.send_message(msg)
            print(f'{Fore.GREEN}Reply on mail sent successfully to: {sender_email}, Subject: {subject} {nettime}')
            await channel.send(f'Reply on mail sent successfully to: <{sender_email}>\nSubject: {subject}\n{body}')
        except Exception as send_error:
            print(f'Error while sending email: {send_error}')
            print(f'Sender Email: {sender_email}')
            print(f'Sender Name: {sender_name}')
            print(f'Subject: {subject}')
            print(f'Body: {body}')
        finally:
            # Close the connection to the SMTP server.
            smtp_server_obj.quit()

    except Exception as e:
        print(f'{Fore.RED}Error while sending email: {e}')
        pley_bot_error()

 

         #                                        ``````````                ``````````                ``````````
          #                                         ``````````                ``````````                ``````````

                                        #  F U N T I O N    P R O C E S S I N G   C H A T   D E F I N I T I O N S  
 
#########################################  SENDING OWN NEW LETTER ############################################  
async def handle_newletter(account, message):
    # Ваш код для обработки новых писем (newletter)
    
        if account:
                # Объявляем что мы отправляем письмо
                sendfunction = 'newletter'
                # Теперь у вас есть значение email_address для текущего канала
                email_address = account['email_address']
                

                sender_name = mysendername
                nettime = get_current_time()
                # Проверяем, начинается ли сообщение с команды "/newletter"
                if message.content.startswith('/newletter'):
                    # Разбиваем сообщение на строки
                    lines = message.content.split('\n')

                    # Проверяем, есть ли как минимум 3 строки (команда, email и текст письма)
                    if len(lines) >= 3:
                        email = lines[1]
                        receiver =  email

                        sender_email = email_address
                        subject = lines[2]
                        message_text = '\n'.join(lines[3:])  # Объединяем оставшиеся строки в теле письма
                        body = f"{message_text}\n {nettime}\n {signature}"
#
#                       full_message = f"From {mysendername}\n {body}\n   "
#                       full_message = f"From {mysendername} {receiver}\nSubject: {subject}\n{body}\n\n{'=' * 50}\n{nettime}\n{signature}\n "
                        sender = None
                        await sender_data(account, sender, sender_name, sender_email, subject, body, message, receiver, sendfunction, email_address)
                        
                    else:
                        # Выводим сообщение о нехватке информации и справку
                        await message.channel.send('Недостаточно информации для отправки письма. Введите данные в следующем формате:\n'
                                                '/newletter\n'
                                                'email@example.com\n'
                                                'Тема письма\n'
                                                'Текст письма')

 


         #                                        ``````````                ``````````                ``````````
          #                                         ``````````                ``````````                ``````````

                                          #  F U N T I O N   R E P L Y   O N   M E S S A G E S  
 
#########################################  SENDING REPLY ON OWR LETTER ############################################  

async def handle_reply(account, message):
    
    # Extract the account details
    if account:
        # Output the full message being replied to in the terminal
        email_address = account['email_address']

        # Initialize variables to store information
        quoted_message = message.reference.resolved if message.reference else None
        quoted_message_text = quoted_message.content if quoted_message else ""
        sendfunction = 'reply'

        sender = None 
        sender_name = None 
        sender_email = None

        receiver = None
        receiver_name = None
        receiver_email = None

        subject = None
        folder = None
        body = None
        receiver = None

        # Function to extract sender information
        def extract_sender_info(sender_info):
            nonlocal sender, sender_name, sender_email
            if sender_info:
                if "<" in sender_info and ">" in sender_info:
                    sender_name, sender_email = sender_info.split("<")
                    sender_email = sender_email.rstrip(">")
                else:
                    sender_email = sender_info.strip()
            else:
                sender_name = sender_email = None

        try:
            # Parse the quoted message text
            for line in quoted_message_text.split('\n'):
                if line.startswith("**New letter from**"):
                    sender_info = line.replace("**New letter from**: ", "")
                    extract_sender_info(sender_info)

                elif line.startswith("**Subject**"):
                    subject = line.replace("**Subject**: ", "")

                elif line.startswith("**Folder**"):
                    folder = line.replace("**Folder**: ", "")

                elif line.startswith("**Body**"):
                    body = line.replace("**Body**: ", "")

            receiver = sender_email

        except Exception as e:
            print(f'Error extracting data from the quoted message: {e}')

        # Call the sender_data function to send the reply email
        await sender_data(account, sender, sender_name, sender_email, subject, body, message, receiver, sendfunction, email_address)
        
        if sender and sender_email and subject and body:
            sender_name = sender
    else:
        await message.channel.send('There is no configured account for sending emails in this channel.')

 
  



         #                                        ``````````                ``````````                ``````````
         #                                         ``````````                ``````````                ``````````

                                        #  F U N T I O N    P R O C E S S I N G   L E T T E R   S E N D I N G    D A T A  

######################## THIS FUNCTION COLLECT ALL DATA TO SEND NEW MESSAGE OR REPLY ON MAIL ######################## 

async def sender_data(account, sender, sender_name, sender_email, subject, body, message, receiver, sendfunction, email_address):
    if sendfunction == 'reply':
        # Print information about the reply email being prepared
        print(f'{Fore.BLUE}\nCollecting new data to send a reply message:')
        print(f'{Fore.WHITE}Receiver: {sender_name} {sender_email}')
        print(f'{Fore.WHITE}Sender: {email_address}')

        if sender_name:
            print(f'{Fore.WHITE}Sender name: {sender_name}')

        if sender_email:
            print(f'{Fore.WHITE}Sender email: {sender_email}')

        if subject:
            print(f'{Fore.WHITE}Subject: {subject}')

        if account and "folders" in account and account["folders"]:
            print(f'{Fore.YELLOW}Folder: {account["folders"][0]}')  # Taken from the first folder of the account (INBOX, etc.)

        if body:
            print(f'{Fore.WHITE}Body: {body}')

        if message and message.content:
            print(f'{Fore.WHITE}Message: {message.content}')

        if sender_name and sender_email and receiver and message:
            # Call the send_email_reply function to send the reply email
            print('Start sending email...')
            print('---------------------------------------')
            await send_email_reply(account, sender, sender_email, sender_name, subject, body, message, receiver, sendfunction, email_address)

    elif sendfunction == 'newletter':
        # Print information about the new email being prepared
        print(f'{Fore.BLUE}\nCollecting new data to send a new letter:')

        if sender_name:
            print(f'{Fore.WHITE}Sender from: {sender_name} <{sender_email}>')

        if receiver:
            print(f'{Fore.WHITE}Receiver: {receiver}')

        if subject:
            print(f'{Fore.WHITE}Subject: {subject}')

        if body:
            print(f'{Fore.WHITE}Body: {body}')

        if sender_name and sender_email and receiver and message:
            # Call the send_email_new function to send the new email
            print('Start sending email...')
            print('---------------------------------------')
            await send_email_new(account, sender, sender_email, sender_name, subject, body, message, receiver, sendfunction, email_address)



######################## RUN MAIL BOT ######################## 
# use your bot token from discord developers page, of your account

bot.run(TOKEN)
 

      ### # # # ## # ######### #########  ###########  ###### ##  ## ## #### ####### ## ## ##
    #                                                                                          ##$$@------  
    #                                                                                   #@*     $$@------  
 ## ##                                #                                                               $$@------  
    #                                                                                                     #  $$@    ------             
    #   # ▄▄▄▄ ▓██   ██▓ #  ▄████ ▓█████  ███▄    █  ▄▄▄  #    ▄▄▄▄    ▒█████  ▒██   ██▒                       $$@------  ------  
    #   ▓█████▄▒██  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▒████▄    ▓█████▄ ▒██▒  ██▒▒▒ █ █ ▒░  #                         $$@------  
    #   ▒██▒ ▄██▒██ ██░   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒██  ▀█▄  ▒██▒ ▄██▒██░  ██▒░░  █   ░                                 **   $$@------  
    #   ▒██░█▀  ░ ▐██▓░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██░█▀  ▒██   ██░ ░ █ █ ▒                                         $$@     ------   
 ## #   ░▓█  ▀█▓░ ██▒▓░ # ░▒▓███▀▒░▒████▒▒██░   ▓██░ ▓█   ▓██▒░▓█  ▀█▓░ ████▓▒░▒██▒ ▒██▒ #                                            **      $$@  ------  
    #   ░▒▓███▀▒ ██▒▒▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░▒▓███▀▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░                                                             $$@  ------      ------  
    #   ▒░▒   ░▓██ ░▒░      ░   ░  ░ ░  ░░ ░░ # ░ ▒░  ▒   ▒▒ ░▒░▒   ░   ░ ▒ ▒░ ░░   ░▒ ░ #                                                      &  ^&   ------  ------       
    #    ░ #  ░▒ ▒ ░░     ░ ░   ░    ░      ░#  ░ ░   ░   ▒    ░    ░ ░ ░ ░ ▒   ░    ░                                                      $$@------  
        #    ░     ░ ░              ░    ░  ░         ░   #   ░  ░ ░          ░ ░   ░    ░  #                                       $$@------  ---   
    #         ░░ ░               #                                   ░         #         #                           $$@    ** ------              
 ## ##                                                                                               $$@       $$@------  
    ####                                                                                        $$@------  ------  
     ##### # # # ## # ######### #########  ###########  ###### ##  ## ## #### ####### ## ##------  ------  
 


 

