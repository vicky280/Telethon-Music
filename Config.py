import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("15a6e87d2e3e0f45f92fb1a0c667a9ee", None)
    STRING_SESSION = os.environ.get("1BVtsOL4Buwloa8Q0IMAnxp4puewtJdYKeVLMN0T5_pDqEWtQ7rjkTHHn4ELzv4d77qn4sEVTE0xl3qc3H_7cr8AvjoQXarXPamykzdhlo77RHy03MsIkOo4vc6yCGA9VVawllKgoqXCPGvJ8jQpt2Y9R5EnkKn-_GcUF14yHuc8cQXEGO057A2-07BWYNJFF6j_8iMDYtG6jbb6d8K91NFonqj2geGKqA0YzN0nFyj-aYyxb7p2OYh8GBSEgQYCeNW27QV56_N818Mt35eU7OTe2oQ7W3gEH-F5pTjjIhQiTOk9d0rsjsTAKKXGIKKLU2QeLVAl3KcGx8bOQLpKC0M42Livo7MU=", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
