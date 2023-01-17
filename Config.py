import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN"," ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBuzGK9tIh5yJhZdJm6_SQt7SgEjurymCGubx5fovYGW8eh7KEiRmF3mhrloLR40HL735Ga2Uiu-S5hLqRK3Vn1G9sVHDZXTW14Qz_br_Njjcyv0r_dmk05F8g-bulgNjgZLRtR2Pjngb3jyZy3QoLbHbJeNhYV5e3V1ejI1v2pC-aMIYZt9duQ1AwhkZAmpeK4eS2MBx--MmyGACe2WYEpaX0DIEJjkB8sD-hu8zB0ZX74yHsA19UQvtYtXr9tk0hcqXZGyZOu_O2oK8SIUPTSpk-XpVJ3NG9xL_Zg3QvLH9wUExXei9s-O2Gm-OnmImJS2nQO83mZ56WPj59LgViTGE=")
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
