import discord
from flask import endless_ping
import requests
import json

client = discord.Client() #Discord Client ID
eth_addy = ["#input your eth address here"] #Eth Address 

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

def get_balance(): #etherscan API to get amount of eth in wallet
	loadethjson = requests.get("https://api.etherscan.io/api?module=account&action=balance&address=" + str(eth_addy[0]) + "&tag=latest&apikey= (#Your etherscan API key) ")
	json_data = json.loads(loadethjson.text)
	purest_value = json_data['result']
	pure_value = int(purest_value)
	eth_value = pure_value * (10**-18)
	final_value = "{:.2f}".format(eth_value)
	return(final_value + " " + "<:poop:923780779404836894>") #emoji won't load unless it's something that your disc account can use so feel free to change

@client.event
async def on_message(message):
	if message.content.startswith('%btc'):
		await message.channel.send("https://alternative.me/crypto/fear-and-greed-index.png")

	if message.content.startswith('%eth'):
		await message.channel.send("https://fear-and-greed-indexes.vercel.app/api/eth.png")
	if message.content.startswith("%balance"):
		embedVar = discord.Embed(title="Balance: " + get_balance(), color=0x00ff00)
		await message.channel.send(embed=embedVar)
	# if message.content.startswith("%Change Address"): #(gets this as the message content when it should be the address  you inputed)
	# 	await message.channel.send("What do you want your new address to be?:")
	# 	# new_addy = message.content
	# 	# eth_addy.append(new_addy)
	# 	# eth_addy.remove(eth_addy[0])

endless_ping()
client.run('#Your Discord Client ID')
