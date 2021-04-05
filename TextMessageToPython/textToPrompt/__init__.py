from .GetAssets import Assets
from .GenConnection import GenerateConnection
from .GetMessage import *

def TextToPrompt(emailBoxName: str) -> list:
    asset = Assets()
    imap = GenerateConnection(asset)
    return GetMessageContent(GetMessage(imap, emailBoxName))
