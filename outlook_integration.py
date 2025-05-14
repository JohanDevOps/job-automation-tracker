from exchangelib import Credentials, Account, DELEGATE

def get_outlook_account(email, password):
    creds = Credentials(email, password)
    return Account(primary_smtp_address=email, credentials=creds, autodiscover=True, access_type=DELEGATE)
