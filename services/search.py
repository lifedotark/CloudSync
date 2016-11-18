# -*- coding: utf-8 -*-

class SearchService(object):
    
    def __init__(self,service):
        self.service = service
    
    
    def find(self, name_equals=None, mimeType=None, begin_with=None, folder_name=None):
            
        query = "{} and trashed=False"
        
        if begin_with:
            query = query.format("name contains '{}'".format(begin_with))
            
        if name_equals:
            query = query.format("name='{}'".format(name_equals))
        
        if folder_name:
            folder = self.find(name_equals=folder_name)
            if not folder:
                return []
                
            query = "{} and '{}' in parents".format(query, folder[0]['id'])
        
        if mimeType:
            query = "%s and mimeType='%s'" % (query, mimeType)
        
        print("The query: \"{}\"".format(query))
        response = self.service.files().list(q=query,fields="files(id, name, mimeType, trashed, parents)").execute()
        
        files = response.get('files', [])
        
        if len(files) == 0:
            print("Not found: {}".format(name_equals))
        
        return files

    def get_folder(self, name, parent_id=None):
        folder_mimeType = 'application/vnd.google-apps.folder'
        folders = self.find(name, folder_mimeType) or None
    
        if not folders or folders[0].get('mimeType') != folder_mimeType:
            print("{} not found! creating one...".format(name))
            folder_metadata = {
                'name' : name,
                'mimeType' : folder_mimeType
            }
    
            if parent_id:
                folder_metadata['parents'] = [parent_id]
    
            return self.service.files().create(body=folder_metadata, fields="id").execute()
    
        return folders[0]
        