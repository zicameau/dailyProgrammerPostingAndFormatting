import requests, os
import requests.auth

# change working directory to where program is currently running.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Conf file used to keep password sand username secret.
# First line contains pw and second line appID
confFile = open('conf.txt', 'r')
lines = confFile.readlines()

# get rid of descriptions for key and id
lines[0] = lines[0][5:]
lines[1] = lines[1][4:]

client_auth = requests.auth.HTTPBasicAuth(lines[1], lines[0])
post_data = {}


