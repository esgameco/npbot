import aiohttp
from fake_useragent import UserAgent

class Session:
    def __init__(self,
                 uuid:str=None,
                 cookies:aiohttp.CookieJar=None,
                 headers:dict=None) -> None:
        """Account Session
        
        uuid:int                  - Account uuid for lookup in accounts DB
        cookies:aiohttp.CookieJar - Cookie jar for session
        headers:dict              - Session headers (user agent, etc.)
        """
        self.uuid = uuid
        self.cookies = cookies
        self.headers = headers
    
    @staticmethod
    def create_session(account:any):
        """Creates session from account data"""
        return Session(uuid=account.uuid,
                       cookies=aiohttp.CookieJar(unsafe=True),
                       headers={UserAgent().chrome()})