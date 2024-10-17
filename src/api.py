from client import Client
from db import DB
from worker import Worker

class API:
    def __init__(self, acc_loc: str=None):
        # Accounts database - all account data, immutable
        self.accounts_db = DB(db_loc=acc_loc, autoload=True)

        # Sessions database - stores temporary account data (aiohttp client, mutable site data)
        self.sessions_db = DB()

        # AIOHttp client - single client can process requests for all workers
        self.client = Client()

        # Workers array - uninitialized array of workers
        self.workers = []
    
    def init(self, num_workers:int=5):
        for i in range(num_workers):
            self.workers.append(Worker(client=self.client))
    
    def close(self):
        self.client.close()
    
