import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "'"

# The bot token. Keep this secret!
BOT_TOKEN = os.getenv('BOT_TOKEN')

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = "Stalker | 'commands"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

#Silencer
BLACKLIST=["JoboX#8949","Krzysztof#9451"]
QUOTES=["Utkaj łeb Jobczyk!","Mówiłem żebyś skleił pizde Jobo.","Dobra wez pal wroty Jobo..."]