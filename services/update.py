# -*- coding: utf-8 -*-

from googleapiclient.http import MediaFileUpload

class UpdateService(object):

    def __init__(self, service, search_service, io_service):
        self.service = service
        self.search_service = search_service
        self.io_service = io_service
    
    def update(self, filename, filepath, path_on_drive=None, onProgress=None):
        files = self.search_service.find(name_equals=filename)
        if len(files) > 1:
            print("Multiple files found! Select only one: {}".format([f['name'] for f in files]))
            return
        
        if len(files) == 0:
            print("No files found to update with name: {}".format(filename))
            return
        
        google_file = files[0]
        print("Updating file: {}".format(google_file['name']))
        
        file_id = google_file['id']
        
        media_body = MediaFileUpload(filepath,resumable=True)
        
        request = self.service.files().update(
            fileId=file_id,
            media_body=media_body)
            
        response = None
        while response is None:
            status, response = request.next_chunk()
            if onProgress:
                onProgress(int((status.progress() if status else 1) * 100))
        print("Update Complete!")
        return response
