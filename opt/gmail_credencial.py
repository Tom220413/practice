import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/gmail.modify",
]

def get_credential():
    """
    アクセストークンの作成
    """
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret_908733436128-lt55ufg1nrvldc6sdsgqdcib450r8b3s.apps.googleusercontent.com.json", SCOPES)
            # creds = flow.run_local_server()
            creds = flow.run_console()
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return creds