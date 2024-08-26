
import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Bot Information
API_ID = int(environ.get("API_ID", "27996421"))
API_HASH = environ.get("API_HASH", "5f5cb6a13ecff3d90e1ec73dc366e26d")
BOT_TOKEN = environ.get("BOT_TOKEN", "7160637539:AAFd_HvXfinHvQixUeP8Qc6cq050o6vlGNY")

PICS = (environ.get('PICS', 'https://telegra.ph/file/dc34bdb48442246cc82e6.jpg')).split() # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6887525311').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "CinehutsfilesharingBot") # without @
PORT = environ.get("PORT", "8080")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', True)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://fileshare:aeGoQ59wqboXl8Eq@cluster0.dq89n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "clonedata")

#force sub 

AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002056340901').split()]

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://filesharing:filesharing123@cluster0.afn46h0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "Fileslink")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', False)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002118860679"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', False)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "api.shareus.io") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "hRPS5vvZc0OGOEUQJMJzPiojoVK2") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/How_To_Open_Linkl") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', False)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")



