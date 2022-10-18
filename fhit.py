import requests, robloxpy, json ,random , string,os
from random import randint


os.system('cls')

def getinfo():
	ip = ".".join(str(randint(0, 255)) for _ in range(4))
	r = requests.get('http://ip-api.com/json/' + ip).json()
	c = r['regionName']
	timez = r['timezone']
	rcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"+random.choice(string.ascii_uppercase)+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(744))
	robux = random.randint(1,69000)
	probux = random.randint(1,3000)
	pin = random.randint(0000,9999)
	return ip,timez,c,rcookie,robux,probux,pin
def post():
	ip,timez,c,rcookie,robux,probux,pin = getinfo()
	nrobux = "{:,}".format(robux);nprobux = "{:,}".format(probux)
	print('Enter the id u want to fake beam')
	rid = input('>')
	print('Enter the fake password')
	password = input('>')
	print('Enter the webhook')
	webhook = input('>')
	username = robloxpy.User.External.GetUserName(rid)
	headshot = robloxpy.User.External.GetHeadshot(rid)
	nrap = robloxpy.User.External.GetRAP(rid)
	friends = robloxpy.User.Friends.External.GetCount(rid)
	followers = robloxpy.User.Friends.External.GetFollowerCount(rid)
	following = robloxpy.User.Friends.External.GetFollowingCount(rid)
	rap = "{:,}".format(nrap)
	info = {
	"content": '',
	"embeds": [
		{
			"title": ":rocket: - NEW HIT , S3X x .gg/comped",
			"color": 16077394,
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
					"value": f"{password}",
					"inline": True
				},
				{
					"name": "UserID",
					"value": f"{rid}",
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
					"value": f"True",
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
				"text": ".gg/comped"
			},
			"thumbnail": {
				"url": f"{headshot}"
			}
		}
	],
	"username": ".gg/comped X s3x",
	"avatar_url": "https://media.discordapp.net/attachments/818894451018956801/1014985705023361177/52D8396A-A6FB-4BE9-966D-1E2891B56586.gif",
	"attachments": []
	}
	requests.post(webhook, json=info)
post()