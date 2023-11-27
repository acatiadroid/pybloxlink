from typing import Optional

class ResolvedUser:
    """Represents a resolved user."""
    def __init__(self, data: dict):
        self.data = data
    
    def __str__(self) -> str:
        return str(self.data.get("robloxID"))

        
