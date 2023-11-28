from typing import Optional

from .robloxuser import RobloxUser
from .discorduser import DiscordUser

class RobloxUserResponse:
    """Represents a response from retrieving a Roblox user."""
    def __init__(self, data: dict):
        self.data = data
    
    @property
    def roblox_id(self) -> Optional[int]:
        """The Roblox account ID."""
        return int(self.data.get("robloxID"))
    
    @property
    def roblox(self) -> RobloxUser:
        """The Discord user info.
        Returns a RobloxUser object."""
        return RobloxUser(self.data.get("resolved", {}).get("roblox", {}))
    
    @property
    def discord(self) -> DiscordUser:
        """The Discord user info.
        Returns a DiscordUser object."""
        return DiscordUser(self.data.get("resolved", {}).get("discord", {}))
    
class DiscordUserReponse:
    """Represents a response from retrieving a Discord user."""
    def __init__(self, data: dict):
        self.data = data

    @property
    def discord_ids(self) -> list:
        """A list of account linked to the given ID."""
        return self.data.get("discordIDs")
    
    
