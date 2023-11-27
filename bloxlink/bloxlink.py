from .http import Request

class Bloxlink:
    """The base class for all Bloxlink API interactions."""
    def __init__(self, api_key: str):
        self.api_key = api_key

    def lookup_roblox_id(discord_id: int, server_id: int = None):
        """Looks up a Roblox user from the given Discord ID (and optional server ID).
        Returns the Roblox user ID.
        
        Attributes
        ----------
        roblox_id - the Roblox ID of the user you want to find the Discord ID of.
        
        server_id* - the ID of the server you want to search in.
        
        *if you intend on doing a global search (which required approval), do not include this argument.
        Otherwise, you must provide this argument."""

    
    def lookup_discord_id(discord_id: int, server_id: int = None):
        """Looks up a Discord user from the given Roblox ID (and optional server ID).
        Returns the Discord user ID.
        
        Attributes
        ----------
        discord_id - the ID of the Discord user you want to find the Roblox ID of.
        
        server_id* - the ID of the server you want to search in.
        
        *if you intend on doing a global search (which required approval), do not include this argument.
        Otherwise, you must provide this argument."""