# API Reference

## Client
### Client

`class bloxlink.Bloxlink(api_key)`

The base class for all Bloxlink API interactions.

**Parameters:**
* **api_key (str)**: The API key from the Bloxlink developer page.

**Methods:**
* **await lookup_roblox_user(discord_id, server_id = None)**
    
    Looks up a Roblox user from the given Discord ID (and optional server ID).
    Returns the Roblox user ID.

    **Parameters:**
    * **discord_id (int)**: the Roblox ID of the user you want to find the Discord ID of.
    * **server_id (int)**: the ID of the server you want to search in.

    \**if you intend on doing a global search (which required approval), do not include this argument.
    Otherwise, you must provide this argument.*

* **await lookup_discord_user(roblox_id, server_id = None)**

    Looks up a Discord user from the given Roblox ID (and optional server ID).
    Returns the Discord user ID.
    
    **Parameters:**   
    * **roblox_id (int)**: the ID of the Discord user you want to find the Roblox ID of.
    * **server_id (int)***: the ID of the server you want to search in.
    
    \**if you intend on doing a global search (which required approval), do not include this argument.
    Otherwise, you must provide this argument.*

* **await update_user(discord_id, server_id)**
    Updates a Discord user in the specified server. This is equivalent to running /verify in a server.
    Returns the roles which have been added/removed and the new nickname as a dict.
    
    **Parameters:**
    * **discord_id (int)** - the ID of the Discord user you want to update.
    * **server_id (int)** - the ID of the server you want to update the user in.

## Objects
### Discord User
`class bloxlink.DiscordUser`

Represents a Discord user.

This information is only retrieved if you have Bloxlink Premium.

**Attributes:**
* **avatar (Optional[str])**: The Discord users' avatar.
* **communication_disabled_until (Optional[str])**: The date whereby the Discord user has had communication disabled (timed out).
* **flags (Optional[int])**: The Discord users' permission flags.
* **nick (Optional[str])**:  The Discord Users' flags.
* **pending (Optional[bool])**: The Discord users' pending status.
* **premium_since (Optional[str])**: The date that the DIscord user has been premium since.
* **roles (Optional[list])**: A list of the Discord users' role IDs.
* **user (Optional[dict])**: The Discord users' account information.
* **mute (Optional[bool])**: Whether the user is voice muted.
* **deaf (Optional[bool])**: Whether the user is voice deafened.

## Roblox User
`class bloxlink.RobloxUser`

Represents a Roblox user.
    
This information is only retrieved if you have Bloxlink Premium.

**Attributes:**
* **name (Optional[str])**: The Roblox users' username.
* **id (Optional[str])**: The Roblox users' ID.
* **description (Optional[str])**: The Roblox users' description.
* **badges (Optional[str])**: The Roblox users' badges.
* **is_banned (Optional[str])**: Returns True if the Roblox user is banned.
* **groups (Optional[str])**: The Roblox users' groups.
* **avatar (Optional[str])**: The Roblox users' avatar.
* **rap (Optional[str])**: The Roblox users' RAP.
* **value (Optional[str])**: The Roblox users' value.
* **place_visits (Optional[str])**: The Roblox users' place visit count.
* **has_display_name (Optional[str])**: The Roblox users' Whether the user has a display name.
* **external_app_display_name (Optional[str])**: THe Roblox users' external app display name.
* **has_verified_badge (Optional[str])**: Whether the user has a verified badge.
* **groups2 (Optional[str])**: The Roblox users' groups. (this lists the groups in a dictionary using the group ID as the key as opposed to a list)

**Methods:**
* **await get_avatar_headshot_url()**

    Makes a request to Roblox's API for the avatar headshot image URL.
        Returns None if avatar can't be retrieved.

* **await get_avatar_bust_url()**

    Makes a request to Roblox's API for the avatar bust image URL.
        Returns None if avatar can't be retrieved.

* **await get_avatar_fullbody_url()**

    Makes a request to Roblox's API for the avatar full body image URL.
        Returns None if avatar can't be retrieved.

## Responses
`class bloxlink.RobloxUserResponse`

Represents a response from retrieving (looking up) a Roblox user.

**Attributes:**
* **user_id (Optional[int])**: The Roblox account ID.
* **roblox ([RobloxUser](#roblox-user))**: The linked Roblox user info.
* **discord ([DiscordUser](#discord-user))**: The linked Discord user info.

`class bloxlink.DiscordUserResponse`

Represents a response from retrieving (looking up) a Discord user.

**Attributes:**
* **discord_users (list[[DiscordUser](#discord-user)])**: A list of linked Discord users.