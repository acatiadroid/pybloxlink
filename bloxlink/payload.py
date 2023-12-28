import aiohttp

from .objects import *
from .exceptions import _raise_error_code, _raise_error_message

RESOLVED_ROBLOX_USER_URL        = "https://api.blox.link/v4/public/guilds/{}/discord-to-roblox/{}"
RESOLVED_DISCORD_IDS_URL        = "https://api.blox.link/v4/public/guilds/{}/roblox-to-discord/{}"
UPDATE_DISCORD_USER_URL         = "https://api.blox.link/v4/public/guilds/{}/update-user/{}"
GLOBAL_RESOLVED_ROBLOX_USER_URL = "https://api.blox.link/v4/public/discord-to-roblox/{}"
GLOBAL_RESOLVED_DISCORD_IDS_URL = "https://api.blox.link/v4/public/roblox-to-discord/{}" 

def _check_exceptions(resp: dict, payload: dict, method: str):
    if resp.status != 200:
        return _raise_error_code(resp.status, payload.get("error", payload))
    
    if payload.get("error"):
        return _raise_error_message(f"{method} request failed: {payload.get("error")}")

async def _make_post_request(headers: str, url: str, client: aiohttp.ClientSession):
    async with client:
        async with client.post(url, headers=headers, json={}) as resp:
            resp.raise_for_status()
            payload = await resp.json()

            _check_exceptions(resp, payload, "POST")

    return payload

async def _make_get_request(headers: str, url: str, client: aiohttp.ClientSession):
    async with client:
        async with client.get(url, headers=headers) as resp:
            payload = await resp.json()

            _check_exceptions(resp, payload, "GET")

    return payload

class Request:
    def __init__(self, api_key):
        self.client = aiohttp.ClientSession()
        self.headers = {"Authorization": api_key}

    async def _get_roblox_user(self, discord_id: int, server_id: int = None):
        if server_id:
            resp = await _make_get_request(self.headers, RESOLVED_ROBLOX_USER_URL.format(server_id, discord_id), self.client)
        else:
            resp = await _make_get_request(self.headers, GLOBAL_RESOLVED_ROBLOX_USER_URL.format(discord_id), self.client)

        return RobloxUserResponse(resp)
    
    async def _get_discord_user(self, roblox_id: int, server_id: int = None):
        if server_id:
            resp = await _make_get_request(self.headers, RESOLVED_DISCORD_IDS_URL.format(server_id, roblox_id), self.client)
        else:
            resp = await _make_get_request(self.headers, GLOBAL_RESOLVED_DISCORD_IDS_URL.format(roblox_id), self.client)

        return DiscordUserReponse(resp)
    
    async def _update_discord_user(self, discord_id: int, server_id: int):
        resp = await _make_post_request(self.headers, UPDATE_DISCORD_USER_URL.format(server_id, discord_id), self.client)

        return resp
    