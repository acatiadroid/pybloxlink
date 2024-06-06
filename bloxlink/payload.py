import aiohttp

from .objects import *
from .exception import _raise_error_code, _raise_error_message

RESOLVED_ROBLOX_USER_URL        = "https://api.blox.link/v4/public/guilds/{}/discord-to-roblox/{}"
RESOLVED_DISCORD_IDS_URL        = "https://api.blox.link/v4/public/guilds/{}/roblox-to-discord/{}"
UPDATE_DISCORD_USER_URL         = "https://api.blox.link/v4/public/guilds/{}/update-user/{}"
GLOBAL_RESOLVED_ROBLOX_USER_URL = "https://api.blox.link/v4/public/discord-to-roblox/{}"
GLOBAL_RESOLVED_DISCORD_IDS_URL = "https://api.blox.link/v4/public/roblox-to-discord/{}" 

def _check_exceptions(resp: dict, payload: dict, method: str):
    if resp.status != 200:
        return _raise_error_code(resp.status, payload.get("error", payload))
    
    if payload.get("error"):
        return _raise_error_message(f"{method} request failed: {payload.get('error')}")

class Request:
    def __init__(self, api_key):
        self.headers = {"Authorization": api_key}

    async def _make_post_request(self, url: str):
        async with aiohttp.ClientSession() as client:
            async with client.post(url, headers=self.headers, json={}) as resp:  # for some reason it needs to recieve an empty payload
                payload = await resp.json()

                _check_exceptions(resp, payload, "POST")

                return payload
        
    async def _make_get_request(self, url: str):
        async with aiohttp.ClientSession() as client:
            async with client.get(url, headers=self.headers) as resp:
                payload = await resp.json()

                _check_exceptions(resp, payload, "GET")

                return payload

    async def _get_roblox_user(self, discord_id: int, server_id: int = None):
        if server_id:
            resp = await self._make_get_request(RESOLVED_ROBLOX_USER_URL.format(server_id, discord_id))
        else:
            resp = await self._make_get_request(GLOBAL_RESOLVED_ROBLOX_USER_URL.format(discord_id))

        return RobloxUserResponse(resp)
    
    async def _get_discord_user(self, roblox_id: int, server_id: int = None):
        if server_id:
            resp = await self._make_get_request(RESOLVED_DISCORD_IDS_URL.format(server_id, roblox_id))
        else:
            resp = await self._make_get_request(GLOBAL_RESOLVED_DISCORD_IDS_URL.format(roblox_id))

        return DiscordUserReponse(resp)
    
    async def _update_discord_user(self, discord_id: int, server_id: int):
        resp = await self._make_post_request(UPDATE_DISCORD_USER_URL.format(server_id, discord_id))

        return resp
    