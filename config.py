import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "29346781"))
API_HASH = os.environ.get("API_HASH", "75fb004873db1864a09c71cd1307bfa8")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "5860332990"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1001959367903")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002386658352"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://manojmanojs0014:amitsihag@cluster0.r2q9d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "CodeXBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")