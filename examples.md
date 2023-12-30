# Examples
Here are some examples to aid you with using PyBloxlink.

## Looking up a Roblox user
```py
# Looks up a Roblox user using a Discord user ID.

import asyncio
from bloxlink import Bloxlink

bloxlink = Bloxlink("your api key")

async def lookup_stuff():
    user_id   = 445622915271098378 # Discord user ID to lookup
    server_id = 789141507709730816 # Server ID to look in

    roblox_user = await bloxlink.lookup_roblox_user(user_id, server_id)

    # Prints the Roblox account ID:
    print(roblox_user) # Outputs: 218061238

    # Prints the Roblox users' name:
    print(roblox_user.roblox.name) # Outputs: acatia

    # Prints whether the Discord user is voice muted.
    print(roblox_user.discord.mute) # Outputs: False

    # Prints the Discord users' nickname in the server
    print(roblox_user.discord.nick) # Outputs: asvvbdsdfadf

asyncio.run(lookup_stuff())
```

## Looking up a Discord user
```py
# Looks up a Discord user using a Roblox user ID.
#
# When looking up a Discord user, it is possible for 1 Roblox account to
# be linked to many Discord accounts.

import asyncio
from bloxlink import Bloxlink

bloxlink = Bloxlink("your api key")

async def lookup_stuff():
    user_id   = 218061238          # Roblox user ID to lookup
    server_id = 789141507709730816 # Server ID to look in

    user = await bloxlink.lookup_discord_user(user_id, server_id)

    # Prints the account(s) linked to the Roblox users
    print(user) # Outputs: 445622915271098378

    # Prints the 1st Discord users' nickname.
    print(user.discord_users[0].nick) # Outputs: asvvbdsdfadf

    # Prints the 1st Discord users' avatar.
    print(user.discord_users[0].avatar) # Outputs: None

asyncio.run(lookup_stuff())
```

## Using with `discord.py`
```py
# a minimal demonstration of using PyBloxlink with discord.py

import discord
from discord.ext import commands
from bloxlink import Bloxlink

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) # intents, etc not relevant for demo
bloxlink = Bloxlink("your api key")

@bot.command() # usage example: !update_member @acatia
async def update_member(ctx: commands.Context, member: discord.Member):
    """Updates a member with Bloxlink using the API."""
    updated = await bloxlink.update_user(member.id, ctx.guild.id)

    added_roles = updated["addedRoles"]
    removed_roles = updated["removedRoles"]
    nickname = updated["nickname"]
    roblox_id = updated["robloxID"]

    await ctx.send(f"added roles **{', '.join(added_roles)}** and removed **{', '.join(removed_roles)}**")
    await ctx.send(f"nickname set to {nickname}")
    await ctx.send(f"users roblox ID is {roblox_id}")


bot.run("token")
```

### Bot in use:

![](https://i.imgur.com/5wK9CMP.png)