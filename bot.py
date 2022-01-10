import discord,requests,json
from flask import endless_ping


client = discord.Client() #Discord Client ID
 
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

def get_balance(): #etherscan API to get amount of eth in wallet
	loadethjson = requests.get("https://api.etherscan.io/api?module=account&action=balance&address=" + str(command_value[1]) + "&tag=latest&apikey= (#Your etherscan API key) ")
	json_data = json.loads(loadethjson.text)
	purest_value = json_data['result']
	pure_value = int(purest_value)
	eth_value = pure_value * (10**-18)
	final_value = "{:.2f}".format(eth_value)
	return(final_value + " " + "<:poop:923780779404836894>") #emoji won't load unless it's something that your disc account can use so feel free to change

@client.event
async def on_message(message):
	global command_value
	if message.content.startswith("%balance"):
		retrieveaddy = message.content
		command_value = retrieveaddy.split(" ")
		embedVar = discord.Embed(title="Balance: " + get_balance(), color=0x00ff00)
		await message.channel.send(embed=embedVar)


endless_ping()
client.run('#Your Discord Client ID')
