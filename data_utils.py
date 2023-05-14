import yaml 

class DatabaseConnector:

    def __init__(self, data):
        self.data = data
    
    def read_db_creds(self, creds_file):
        with open(creds_file, 'r') as f:
            creds = yaml.safe_load(f)
        return creds