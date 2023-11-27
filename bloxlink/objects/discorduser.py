from typing import Optional

class DiscordUser:
    """Represents a Discord user.

    This information is only retrieved if you have Bloxlink Premium."""
    def __init__(self, data: dict):
        self.data = data

    @property
    def avatar(self) -> Optional[str]:
        """The Discord users' avatar."""
        return self.data.get("avatar")
    
    @property
    def communication_disabled_until(self) -> Optional[str]:
        """The date whereby the Discord user has had communication disabled (timed out)."""
        return self.data.get("communication_disabled_until")
    
    @property
    def flags(self) -> Optional[int]:
        """The Discord users' permission flags."""
        return self.data.get("flags")
    
    @property
    def nick(self) -> Optional[str]:
        """The Discord users' nickname."""
        return self.data.get("nick")
    
    @property
    def pending(self) -> Optional[bool]:
        """The Discord users' pending status."""
        return self.data.get("pending")
    
    @property
    def premium_since(self) -> Optional[str]:
        """The date that the Discord user has been premium since."""
        return self.data.get("premium_since")
    
    @property
    def roles(self) -> Optional[list]:
        """A list of the Discord users' roles IDs."""
        return self.data.get("roles")
    
    @property
    def user(self) -> Optional[dict]:
        """The Discord users' account information."""
        return self.data.get("roles")
    
    @property
    def mute(self) -> Optional[bool]:
        """Whether the user is voice muted."""
        return self.data.get("mute")
    
    @property
    def deaf(self) -> Optional[bool]:
        """Whether the user is voice deafened."""
        return self.data.get("deaf")