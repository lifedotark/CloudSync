# -*- coding: utf-8 -*-

import os
from apiclient import http

class DownloadService(object):
    
    def __init__(self, service, search_service):
        self.service = service
        self.search_service = search_service
    

    def download_file(self, where_to_download,query,onProgress=None):
        files = self.search_service.find(**query)
        
        if len(files) == 0:
            print("File not found! '{}'".format(query))
            return 
        
        if len(files) > 1:
            print("There are multiple files! Select only one: {}".format([x['name'] for x in files]))
            return 
        
        file = files[0]
        print("File found! '{}'".format(file['name']))
        
        print("Downloading File...")
        
        fullpath = os.path.join(where_to_download, file['name'])
        print("Saving in {}".format(fullpath))
        
        file_stream = open(fullpath,"wb")
        
        request = self.service.files().get_media(fileId=file['id'])
        media_request = http.MediaIoBaseDownload(file_stream,request)
        
        done = False
        while done is False:
            status, done = media_request.next_chunk()
            if onProgress:
                onProgress(int((status.progress() if status else 1) * 100))
            
        print("Download Complete!")