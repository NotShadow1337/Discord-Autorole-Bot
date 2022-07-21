#libraries
import discord
from utils import *
from discord.ext import commands

#intents (used to detect member joins)
intents = discord.Intents.default()
intents.members = True

#client object
client = commands.Bot(command_prefix = 'z', case_insensitive = True, intents = intents)

#when the bot is ready to be used
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

#when a member joins the server
@client.event
async def on_member_join(member):
    if not int(guild_id) == member.guild.id:  return
    roles = get_autorole()
    for role in roles:
        try:
            role = client.get_guild(int(guild_id)).get_role(role)
            await member.add_roles(role)
        except Exception as e:
            print(e)

#a simple command which sends the bots latency
@client.slash_command(name = 'ping', description = 'returns the client latency', usage = 'ping')
async def ping(ctx):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    await ctx.respond(f'Pong! **{round(client.latency * 1000)}*ms 🏓')

#the autorole commands start from here
#command to add a role to the autorole list
@client.slash_command(name = 'autorole_add', description = 'adds a role to the autorole list', usage = 'autorole <role>')
async def autorole_add(ctx, role: discord.Role):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        return await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    if is_autorole(role.id) == False:
        add_autorole(role.id)
        await ctx.respond(f'{success_emoji} Added {role.name} to the autorole list')
    else:
        await ctx.respond(f'{error_emoji} {role.name} is already in the autorole list')

#command to remove a role from the autorole list
@client.slash_command(name = 'autorole_remove', description = 'removes a role from the autorole list', usage = 'autorole <role>')
async def autorole_remove(ctx, role: discord.Role):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        return await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    if is_autorole(role.id) == True:
        remove_autorole(role.id)
        await ctx.respond(f'{success_emoji} Removed {role.name} from the autorole list')
    else:
        await ctx.respond(f'{error_emoji} {role.name} is not in the autorole list')

#command to get the autorole list
@client.slash_command(name = 'autorole_list', description = 'returns the autorole list', usage = 'autorole_list')
async def autorole_list(ctx):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        return await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    roles = get_autorole()
    if len(roles) == 0:
        await ctx.respond(f'{error_emoji} The autorole list is empty')
    else:
        roles = [client.get_guild(int(guild_id)).get_role(role).name for role in roles]
        await ctx.respond(f'{success_emoji} The autorole list is: `{roles}`')

#logging in to the bot
client.run(token)