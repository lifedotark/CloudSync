# -*- coding: utf-8 -*-

from googleapiclient.http import MediaFileUpload

class UploadService(object):

    def __init__(self, service, search_service, io_service):
        self.service = service
        self.search_service = search_service
        self.io_service = io_service

    def _upload_file(self, filename, filepath, folder_id=None, onProgress=None):
            
        print("Uploading file: {}".format(filename))
        
        file_metadata = {
            'name':filename
        }  
        
        if folder_id:
            file_metadata['parents']=[folder_id]
        
        media = MediaFileUpload(filepath,resumable=True)
        request = self.service.files().create(body=file_metadata, media_body=media,fields="id")
        
        response = None
        while response is None:
            status, response = request.next_chunk()
            if onProgress:
                onProgress(int((status.progress() if status else 1) * 100))
        print("Upload Complete!")
        return response
        
    def upload(self, filename, filepath, path_on_drive, onProgress=None):
        
        folders_path = self.io_service.get_all_folders(path_on_drive)
        
        google_folder = None
        for folder_name in folders_path:
            if google_folder:
                google_folder = self.search_service.get_folder(folder_name, google_folder.get('id'))
            else:
                google_folder = self.search_service.get_folder(folder_name)
                
        self._upload_file(filename,filepath,google_folder.get('id'), onProgress)