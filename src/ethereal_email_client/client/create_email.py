import json
import os
import requests


class CreateEmail:
    
    def __init__(self) -> None:
        self.__account = self.__load_account()

    def create_email(self):
        payload = {
            "requestor": "YourNameOrAppName",
            "version": "1.0",
        }

        response = requests.post('https://api.nodemailer.com/user', json=payload)
        if response.status_code == 200:
            account = response.json()
            self.__account = account # See account infos to login on ethereal.email
            self.__save_account(account)
        else:
            raise Exception(f"Could not create Ethereal account: {response.text}")
    
    def get_account(self):
        return self.__account

    def __save_account(self, account):
       with open('src/ethereal_email_client/session/ethereal_account_session.json', 'w') as file:
           json.dump(account, file)
    
    def __load_account(self):
        if os.path.exists('src/ethereal_email_client/session/ethereal_account_session.json'):
            with open('src/ethereal_email_client/session/ethereal_account_session.json', 'r') as file:
                return json.load(file)
        return None
            
account_instance = CreateEmail()