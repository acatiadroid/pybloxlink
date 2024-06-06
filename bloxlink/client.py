from .payload import Request
from .objects import DiscordUserReponse, RobloxUserResponse

class Bloxlink:
    """The base class for all Bloxlink API interactions."""
    def __init__(self, api_key: str):
        self.request = Request(api_key)

    async def lookup_roblox_user(self, discord_id: int, server_id: int = None) -> RobloxUserResponse:
        """Looks up a Roblox user from the given Discord ID (and optional server ID).
        Returns the Roblox user ID.
        
        Attributes
        ----------
        roblox_id - the Roblox ID of the user you want to find the Discord ID of.
        
        server_id* - the ID of the server you want to search in.
        
        *if you intend on doing a global search (which required approval), do not include this argument.
        Otherwise, you must provide this argument."""
        return await self.request._get_roblox_user(discord_id, server_id)

    
    async def lookup_discord_user(self, roblox_id: int, server_id: int = None) -> DiscordUserReponse:
        """Looks up a Discord user from the given Roblox ID (and optional server ID).
        Returns the Discord user ID.
        
        Attributes
        ----------
        roblox_id - the ID of the Discord user you want to find the Roblox ID of.
        
        server_id* - the ID of the server you want to search in.
        
        *if you intend on doing a global search (which required approval), do not include this argument.
        Otherwise, you must provide this argument."""
        return await self.request._get_discord_user(roblox_id, server_id)
    
    async def update_user(self, discord_id: int, server_id: int) -> dict:
        """Updates a Discord user in the specified server. This is equivalent to running /verify in a server.
        Returns the roles which have been added/removed and the new nickname as a dict.
        
        Attributes
        ----------
        discord_id - the ID of the Discord user you want to update.
        
        server_id - the ID of the server you want to update the user in."""
        return await self.request._update_discord_user(discord_id, server_id)
