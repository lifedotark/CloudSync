# -*- coding: utf-8 -*-

import oauth2client, os
from oauth2client import client, tools

class CredentialsService(object):
    
    def __init__(self, config_filepath, ioService):
        
        
        self.ioService = ioService
        
        configs = self.ioService.load_config_file(config_filepath)

        self.app_name = configs["app_name"]
        self.scopes = configs['scopes']
        self.client_secret_file = configs["client_secret_file"]
        self.credential_file = configs["credential_file"]
    
    def get_credentials(self):
        store = oauth2client.file.Storage(self.credential_file)
        
        credentials = store.get()
        if not credentials or credentials.invalid:
            
            flow = client.flow_from_clientsecrets(self.client_secret_file, self.scopes)
            flow.user_agent = self.app_name
            credentials = tools.run_flow(flow, store)
                
        return credentials