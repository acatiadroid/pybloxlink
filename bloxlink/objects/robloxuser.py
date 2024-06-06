from typing import Optional

class RobloxUser:
    """Represents a Roblox user.
    
    This information is only retrieved if you have Bloxlink Premium."""
    def __init__(self, data: dict):
        self.data = data

    def __str__(self) -> Optional[str]:
        return str(self.data.get("name"))
    
    def __int__(self) -> Optional[int]:
        return int(self.data.get("id"))
    
    @property
    def name(self) -> Optional[str]:
        """The Roblox users' username."""
        return self.data.get("name")
    
    @property
    def id(self) -> Optional[int]:
        """The Roblox users' ID."""
        return self.data.get("id")

    @property
    def description(self) -> Optional[int]:
        """The Roblox users' description."""
        return self.data.get("description")
    
    @property
    def badges(self) -> Optional[list]:
        """The Roblox users' badges."""
        return self.data.get("badges")
    
    @property
    def is_banned(self) -> Optional[bool]:
        """Returns True if the users' Roblox account is banned."""
        return self.data.get("isBanned")
    
    @property
    def groups(self) -> Optional[list]:
        """The Roblox users' groups."""
        return self.data.get("groups")
    
    @property
    def avatar(self) -> Optional[dict]:
        """The Roblox users' avatar(s)."""
        return self.data.get("avatar")
    
    @property
    def rap(self) -> Optional[dict]:
        """The Roblox users' RAP."""
        return self.data.get("rap")
    
    @property
    def value(self) -> Optional[dict]:
        """The Roblox users' value."""
        return self.data.get("value")
    
    @property
    def place_visits(self) -> Optional[int]:
        """The Roblox users' place visits count."""
        return self.data.get("placeVisits")
    
    @property
    def has_display_name(self) -> Optional[str]:
        """Whether the user has a display name."""
        return self.data.get("hasDisplayName")
    
    @property
    def external_app_display_name(self) -> Optional[str]:
        """The Roblox users' external app display name."""
        return self.data.get("externalAppDisplayName")
    
    @property
    def has_verified_badge(self) -> Optional[bool]:
        """Whether the user has a verified badge."""
        return self.data.get("hasVerifiedBadge")
    
    @property
    def groups2(self) -> Optional[dict]:
        """The Roblox users' groups.
        
        (this lists the groups in a dictionary using the group ID as the key as opposed to a list)"""
        return self.data.get("groupsv2")