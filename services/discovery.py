# -*- coding: utf-8 -*-
from apiclient import discovery, http
import httplib2

class DiscoveryService(object):
    
    def __init__(self, credentialsService):
        credentials = credentialsService.get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=http)
        
    def files(self):
        return self.service.files()