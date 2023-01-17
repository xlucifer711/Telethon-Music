import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN"," ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu7xoXyuRKNczObWv8TDqf5n1CL8jk71hAewDUPYRADHB3j_rgzd5E0OGVNW65yrH3yCTIhU06baXfC4bPkpzk4UlKBVP36cpM4VJwMU6zraNVQ9YkAEPJAhgqaH1pE6yjtPHGYq4UD6kyXGeFEs54sFGc3vsaL7nKMJ_i10NTmwqZX3uwQrY7adEAQTNQMLTedyudq6YnMe_Wli9N4mV1LPPQB4c5L537O0z2IqLNwWYcgTNJ6KUrm0aLZ814UzbxuTc_8XQgtl99ckxaiLpq8rYAcjuyuN7dLpQpj2cV0ib965Fa-oX4Qp4StPC389sgPOAApOxjYH2uW31Pi5nHAU=") 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "SORS0Coo") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "c_r_source") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/54699e9f531dfac087926.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9fd0a28073d92e3052fe3.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5636767152")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
