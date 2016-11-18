from services.search import SearchService as SearchServiceV1

class SearchService(SearchServiceV1):
    
    def get(self, file_id):
        print("Finding item by Id")
        file = self.service.files().get(fileId=file_id).execute()
        return file
        
    def find(self, name_equals=None, mimeType=None, begin_with=None, folder_name=None, Id=None):
        if Id:
            return [self.get(Id)]
        
        return SearchServiceV1.find(self,name_equals=name_equals, mimeType=mimeType, begin_with=begin_with, folder_name=folder_name)