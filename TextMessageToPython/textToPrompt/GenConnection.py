import imaplib
from . import GetAssets


def GenerateConnection(asset: GetAssets) -> imaplib.IMAP4_SSL:
    if asset is None: raise Exception('No asset found')
    try:
        imap = imaplib.IMAP4_SSL(asset.IMAP_SERVER, asset.IMAP_PORT)
        imap.login(asset.EMAIL, asset.PASSWORD)
    except:
        raise Exception('Connection Issue')
    else: return imap
