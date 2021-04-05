from textToPrompt import TextToPrompt
from textToPrompt.ContentToPython import ConvertMessageToPython

contentList = TextToPrompt(emailBoxName='Inbox')
ConvertMessageToPython(contentList)
