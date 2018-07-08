import requests, os
import requests.auth
from fake_useragent import UserAgent

# enable useragent
ua = UserAgent()

# change working directory to where program is currently running.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Conf file used to keep password sand username secret.
# First line contains apikey, second line appID, third line username, fourth line password
confFile = open('conf.txt', 'r')
lines = confFile.readlines()

# get rid of descriptions and newline characters for data in conf file.
lines[0] = lines[0][5:-1]
lines[1] = lines[1][4:-1]
lines[2] = lines[2][4:-1]
lines[3] = lines[3][4:0]

# Get Access token for reddit api
client_auth = requests.auth.HTTPBasicAuth(lines[1], lines[0])
post_data = {"grant_type": "password", "username":lines[3], "password":lines[2]}
headers = {"User-Agent" : ua.ie}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data = post_data, headers = headers)
print(response.json())


