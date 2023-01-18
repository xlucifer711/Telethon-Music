import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN"," ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBuyJ19lH68e8nw-eAn5KyqRJbKjJc2RIqkCRdvYk40vK3N-flpTpNqRPnJ2UMTnV0uCDZ9C5zWeqPx1PxV3GN_NDSAfXBCHtZfxUr6dWZaue3kTnOmNUy8tiG56Omr2xY6Lm2v014pUb8lL_0BhkQFq9BmEmfBThyucR3rY1WYAihFGH89bL85bJU1o-AUz2wA1038C9k0Qiisox9Yy0zNPo2sTc_eNdpon-AlDx392lFqC_nW5eNeG7zFHL9RiUuM0HNM2bJe4mWXbU2t1iVZbGT3DOWHpRAVBJtID5liOxRLJYfJ7LZoQz3r9vjw2O7z4VhuDi510VVVeWJx7bQKb4=") 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "SORS0Coo") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "c_r_source") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/54699e9f531dfac087926.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/9fd0a28073d92e3052fe3.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5701016541")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
