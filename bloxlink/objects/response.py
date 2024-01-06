from typing import Optional

from .robloxuser import RobloxUser
from .discorduser import DiscordUser

class RobloxUserResponse:
    """Represents a response from retrieving a Roblox user."""
    def __init__(self, data: dict, request_instance):
        self.data = data
        self._request_instance = request_instance

    def __str__(self):
        return str(self.user_id)
    
    @property
    def user_id(self) -> Optional[int]:
        """The Roblox account ID."""
        return int(self.data.get("robloxID"))
    
    @property
    def roblox(self) -> RobloxUser:
        """The Discord user info. Returns a RobloxUser object."""
        return RobloxUser(self.data.get("resolved", {}).get("roblox", {}), self._request_instance)
    
    @property
    def discord(self) -> DiscordUser:
        """The Discord user info. Returns a DiscordUser object."""
        return DiscordUser(self.data.get("resolved", {}).get("discord", {}))
    
class DiscordUserReponse:
    """Represents a response from retrieving a Discord user."""
    def __init__(self, data: dict):
        self.data = data

    def __str__(self):
        return ",".join(self.data.get("resolved", {}).get("discord", {}))

    def __iter__(self):
        return iter(self.discord_users)

    @property
    def discord_users(self) -> list[DiscordUser]:
        """A list of users associated with the given ID."""
        users = []
        for discord_id in self.data.get("resolved", {}).get("discord", {}):
            users.append(DiscordUser(self.data.get("resolved", {}).get("discord", {}).get(str(discord_id))))

        return users
