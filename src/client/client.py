import aiohttp

class Client:
    def __init__(self):
        """AIOHttp client interface"""
        self._client = aiohttp.ClientSession()
    
    async def request(self,
                       method:str,
                       url:str,
                       session:any,
                       headers:dict=None,
                       params:dict=None) -> any:
        """Defines default request behavior"""
        cookies = session.cookies
        headers = headers.update(session.headers)

        return self._client.request(method=method,
                                    url=url,
                                    cookies=cookies,
                                    headers=headers,
                                    params=params)
    
    # async def get(self,
    #               url:str,
    #               session:any) -> any:
    #     """Sends GET request"""
    #     return self._request('GET',
    #                          url=url,
    #                          session=session)
    
    # async def post(self,
    #               url:str,
    #               session:any) -> any:
    #     """Sends POST request"""
    #     return self._request('POST',
    #                          url=url,
    #                          session=session)
    
    def close(self):
        self._client.close()