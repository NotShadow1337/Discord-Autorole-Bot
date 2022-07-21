#libraries
import json

#configuration
with open('config.json') as f:
    config = json.load(f)
    token = config['token']
    guild_id = config['guild_id']
    success_emoji = config['emojis']['success']
    error_emoji = config['emojis']['failure']

#autorole functions
#add a role to the autorole list
def add_autorole(roleid:int):
    with open('database.json', 'r') as f:
        database = json.load(f)
        database['autorole'].append(roleid)
        with open('database.json', 'w') as f:
            json.dump(database, f, indent = 4)

#remove a role from the autorole list
def remove_autorole(roleid:int):
    with open('database.json', 'r') as f:
        database = json.load(f)
        database['autorole'].remove(roleid)
        with open('database.json', 'w') as f:
            json.dump(database, f, indent = 4)

#get the autorole list
def get_autorole():
    with open('database.json', 'r') as f:
        database = json.load(f)
        return database['autorole']

#check if a role is in the autorole list
def is_autorole(roleid:int):
    with open('database.json', 'r') as f:
        database = json.load(f)
        if roleid in database['autorole']:
            return True
        else:
            return False