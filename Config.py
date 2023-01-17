import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN"," ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu12BqyFkGh8K5ZkkSwamONxfC5Kzg0AQxx9fHzfJ1sBBV2BPB6x7tRcOVyd02yG2kzpcJ0HLbXkQwCZdYCPk9cKWVbGIzvWHbgV87RVrvcVRUNr3nPT9j4WD7sjqiiq9or1bOur23zdM2xUBWplYV_XMonrM_q9a3UJEkafoUHTBZw_gKraEvbFdexG6BBqwzEts1-X3LeWsM6Wjh2RTcUcOgxHWxDRh7QIGt-OPHdD4xt38P4GAKVDNYQbJy-frX84NQKYe_P10YwVMn0YQ4nDcATXQXS2Uo7V7vMcDsrQ3i15FX2i8_WRBZO5y7VmHYIyFHJKrNkA4zrGqSoAOorA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "SORS0Coo") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "c_r_source") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/54699e9f531dfac087926.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9fd0a28073d92e3052fe3.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5092041118")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
