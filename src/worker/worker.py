class Worker:
    def __init__(self, client:any=None):
        """Neopets Worker
        
        Handles requests given account data.
        """
        self._client = client
    
    async def _do_request(self,
                         method:str,
                         url:str,
                         session:str,
                         headers:dict=None,
                         params:dict=None) -> any:
        return self._client.request(method=method,
                                    url=url,
                                    session=session,
                                    headers=headers,
                                    params=params)