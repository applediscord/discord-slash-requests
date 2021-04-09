import requests
import discord
from discord.ext import commands
from discord_slash import SlashCommand, utils

def get(header, appID, guildID):
		url = f"https://discord.com/api/v8/applications/{appID}/guilds/{guildID}/commands"
    head = f"Bot {header}"
		headers = {
		    "Authorization": head
		}
		f = requests.get(url, headers=headers)
		return f
  
def post(header, appID, guildID, jsonData):
  url = f"https://discord.com/api/v8/applications/{appID}/guilds/{guildID}/commands"
  head = f"Bot {header}"
	headers = {
		"Authorization": head
	}
	e = requests.post(url, headers=headers, json=jsonData)
  return e

def delete(header, appID, guildID, slashAppID):
  url = f"https://discord.com/api/v8/applications/{appID}/guilds/{guildID}/commands"
  head = f"Bot {header}"
	headers = {
		"Authorization": head
	}
	r = requests.delete(url + f"/{slashAppID}", headers=headers)
	return r
