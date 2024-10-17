import uuid

class Account:
    def __init__(self,
                 uuid:str=None,
                 username:str=None,
                 password:str=None,
                 email:str=None,
                 dob:str=None):
        """Account Data
        
        uuid:int     - Account uuid
        username:str - Account username
        password:str - Account password
        email:str    - Account email
        dob:str      - Account date of birth
        """
        self.uuid = uuid
        self.username = username
        self.password = password
        self.email = email
        self.dob = dob
    
    @staticmethod
    def create_account(username:str=None,
                       password:str=None,
                       email:str=None,
                       dob:str=None):
        return Account(uuid=uuid.uuid4(),
                       username=username,
                       password=password,
                       email=email,
                       dob=dob)