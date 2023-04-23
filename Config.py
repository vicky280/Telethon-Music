import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6216246377"))
    API_HASH = os.environ.get("API_HASH", "15a6e87d2e3e0f45f92fb1a0c667a9ee")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", AAHeli_Jw07bPhpMhZ9BXIOJZFXmSDI0MAY)
    STRING_SESSION = os.environ.get("STRING_SESSION",1BVtsOL4Buwloa8Q0IMAnxp4puewtJdYKeVLMN0T5_pDqEWtQ7rjkTHHn4ELzv4d77qn4sEVTE0xl3qc3H_7cr8AvjoQXarXPamykzdhlo77RHy03MsIkOo4vc6yCGA9VVawllKgoqXCPGvJ8jQpt2Y9R5EnkKn-_GcUF14yHuc8cQXEGO057A2-07BWYNJFF6j_8iMDYtG6jbb6d8K91NFonqj2geGKqA0YzN0nFyj-aYyxb7p2OYh8GBSEgQYCeNW27QV56_N818Mt35eU7OTe2oQ7W3gEH-F5pTjjIhQiTOk9d0rsjsTAKKXGIKKLU2QeLVAl3KcGx8bOQLpKC0M42Livo7MU=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("Madueibot", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://github.com/Yash450/Telethon-Music")
    CMD_IMG = os.environ.get("CMD_IMG", "")
    ASSISTANT_ID = int(os.environ.get("6216246377", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
