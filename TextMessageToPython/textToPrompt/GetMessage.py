import email
from scriptText import number

phoneTypes = {
    'tmomail.net': 'T-Mobile',
    'vmobl.com': 'Virgin Mobile',
    'txt.att.net': 'AT&T',
    'messaging.sprintpcs.com': 'Sprint',
    'vtext.com': 'Verizon',
    'mmst5.tracfone.com': 'Tracfone',
    'message.ting.com': 'Ting',
    'myboostmobile.com': 'Boost Mobile',
    'email.uscc.net': 'U.S. Cellular',
    'mymetropcs.com': 'Metro PCS',
}

def GetPhoneType(domainName: str) -> str:
    try: return phoneTypes[domainName]
    except: return f'Unlisted ({domainName})'

def GetMessage(imap, boxName: str) -> email:
    imap.select(boxName)
    result, data = imap.uid('search', None, "ALL")
    inbox_item = data[0].split()
    most_recent = inbox_item[-1]
    result2, email_data = imap.uid('fetch', most_recent, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    return email.message_from_string(raw_email, policy=email.policy.default)

def GetMessageContent(message) -> list:
    messageContent = []
    mail_bytes = []
    if message['From'] == number and message.is_multipart() is True:
        senderFull = message["From"]
        senderList = senderFull.split('@')
        sender = senderList[0]
        if str(sender).startswith('+1'):
            sender = sender.replace('+1', '')
            messageContent.append(f'From: {sender}')
        else: messageContent.append(f'From: {sender}')
        messageContent.append(f'Company: {GetPhoneType(senderList[1])}')
        for p in message.get_payload():
            mail_bytes.append(p.get_payload(decode=True))
        messageContent.append(f'Content: {mail_bytes[0].decode("utf-8")}')
        return messageContent
    elif message['From'] == number:
        return message.get_payload(decode=True).decode('utf-8').strip()
    else: return "No email found yet"
