# Unofficial HackForums API v2 Integration in Python 3


## Purpose
Other public Python implementations of the HackForums API have shown to be immature or varying levels of incomplete. The goal of this project is to provide a fully usable Python API for Hackforums available through `pip`. **hfapi** features include:
- Read/Write profile user profile information
- Easy and intuitive integration with Python network applications
- Synchronous (requests) and Asynchronous (aiohttp) implementations
- All API objects are defined with Pydantic

## How-To: Install

Installation is easy!

    python3 -m pip install -U hfapi
    
## How-To Use

The synchronous and asynchronous API implementations are identical in functionality and usage with the addition of `await` syntax in the asynchronous version.

    from hfapi import HFAppAsync, HFClientAsync       # use "HFApp" and "HFClient" for synchronous
    
    
    app = """ EXAMPLE WEB SERVER HERE """
    hf = HFAppAsync(
        client_id="[CLIENT_ID]",
        secret_key="[SECRET_KEY]",
        redirect_uri="https://example.com/authorize",
    )
   
    # Hackforums will submit a GET request with "code" as a parameter
    @app.get("/authorize")
    async def authorize(code: str):
        # use the `hf.authorize` method to create a client session
        client = await hf.authorize(code)
        me = await client.me(all=True)  # collect all (possible) data from current user
        return me.dict()


## Documentation: Modules




#### hfapi.hf_base**

Provides the base class interface for the HF App API and HF Client.

Classes:
 - HFAppBase
 - HFClientBase
