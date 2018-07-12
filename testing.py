import requests, os
import requests.auth
from fake_useragent import UserAgent
from pprint import pprint

# enable useragent
ua = UserAgent()

# change working directory to where program is currently running.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Conf file used to keep password sand username secret.
# First line contains apikey, second line appID, third line username, fourth line password
confFile = open('conf.txt', 'r')
lines = confFile.readlines()

# get rid of descriptions and newline characters for data in conf file.
key = lines[0][5:-1]
appID = lines[1][4:-1]
un = lines[2][4:-1]
pw = lines[3][4:]

# Get Access token for reddit api
client_auth = requests.auth.HTTPBasicAuth(appID, key)
post_data = {"grant_type": "password", "username":un, "password":pw}
headers = {"User-Agent" : ua.ie}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data = post_data, headers = headers)
json = response.json()
print(json['access_token'])

headers = {"Authorization" : "bearer " + json['access_token'],"User-Agent": ua.ie }
response = requests.get("https://oauth.reddit.com/api/v1/me", headers = headers)

pprint(response.json())




