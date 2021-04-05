from datetime import datetime
from . import TextToPrompt

def ConvertMessageToPython(contentList: list) -> 'Python':
    for item in contentList: print(str(item))
    output = contentList[2].replace('Content: ', '')
    with open(f'textPythonFiles/test{datetime.timestamp(datetime.now())}.py', 'w') as file:
        file.write(output)