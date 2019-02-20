import json
import requests
import time
import os

apiKey = "6f03a8a3-e3ed-4be4-afe6-4d6b3a7ec686"
platform = "5"
playerName = input("Origin name: ")
url = "https://public-api.tracker.gg/apex/v1/standard/profile/" + platform + "/" + playerName
headers = {"TRN-Api-Key": apiKey}

def main(url, headers):
	r = requests.get(url, headers = headers)
	if r.status_code == 200:
		print("User Info Loaded:")
		return r.text
	else:
		return "Oh no, " + r.status_code

while True: # 1 == 1 is redundant. Use `while True:` fair enough
	os.system('cls')
	data = json.loads(main(url, headers))

	lvl = data['data']['stats'][0]['displayValue']
	name = data['data']['metadata']['platformUserHandle']
	kills = data['data']['stats'][1]['displayValue']
	damage = data['data']['stats'][2]['displayValue']
	hS = data['data']['stats'][3]['displayValue']
	gamesPlayed = data['data']['stats'][4]['displayValue']
	champion = data['data']['children'][0]['metadata']['legend_name']

	print("Player Name: " + name)
	print("Champion: " + champion)
	print("Level: " + lvl)
	print("Kills: " + kills)
	print("Damage Done: " + damage)
	print("Headshots: " + hS)

	time.sleep(120)
