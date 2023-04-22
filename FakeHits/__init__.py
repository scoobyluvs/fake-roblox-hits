import requests
from FakeHits.http import main as webhooksend
class Main:
    
    def __init__(self, webhook: str, id: int, password: str) -> None:
        
        self.webhook = webhook
        self.id = id
        self.password = password
        
        print('reached __init__')
    
    def __repr__(self) -> str:
        print('reached repr')
        try:
            r = requests.get(f"https://users.roblox.com/v1/users/{self.id}")
            if r.status_code != 200:
                return "Roblox Error"
        except:
            return "Roblox Error"
        
        try:
            r = requests.get(self.webhook)
            if r.status_code != 200:
                return "Webhook Error"
        except:
            return "Webhook Error"
        
        webhooksend(self.webhook,self.id,self.password) 
        
        return "Success"
