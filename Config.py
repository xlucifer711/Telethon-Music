import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN"," ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu5cV_ZdrPpJWQY2WczEEAXMjgXIxEscBKD9ap1duWFCbHM8xtbFoyHfdAQ7-h2lBFC3bNmuoBuB2aIY7hIG_hvMyXlUBCbCxPnLn4tKhGqC9liKmWE7Vqu2NMasosSdeLCnqNp6BIzxpoIdvl1ORJOaAj5hrAulng4EfxS9ekKp6hCuMsbwC0rsADYlAAMvwCs7OmQyDb-9uDhAvV3yRnb3BbV44GmQImHIDpU-8zZQIi4AJvA6OBaJ2kZVh4RSoaVy7T9jwHRUPTlcRF_RBnE4XJlR2a2-QLEEeP8GpLl81kwe2l2h_pW24kFX_O57NAqRXsDJR6lslXLHXZDdaDDk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "SORS0Coo") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "c_r_source") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/54699e9f531dfac087926.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9fd0a28073d92e3052fe3.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
