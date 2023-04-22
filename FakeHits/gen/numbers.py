import requests
import string
import random
from random import randint

class Network:
    
    def __init__(self) -> None:
        self.network 
     
    def network(self):
        ip = ".".join(str(randint(0, 255)) for _ in range(4))
        while True:
            try:
                r = requests.get('http://ip-api.com/json/' + ip).json()
                c = r['regionName']
                timez = r['timezone']
                return ip, c, timez
            except:
                ip = ".".join(str(randint(0, 255)) for _ in range(4))

    def roblox(self):
        rcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"+random.choice(string.digits)+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(744))
        robux = random.randint(1,69000)
        probux = random.randint(1,3000)
        pin = random.randint(0000,9999)
        nrobux = "{:,}".format(robux)
        nprobux = "{:,}".format(probux)
        return rcookie,pin,nrobux,nprobux