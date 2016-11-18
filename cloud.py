# -*- coding: utf-8 -*-
import sys
from services.credentials import CredentialsService
from services.download import DownloadService
from services.io import IOService
from services.searchv2 import SearchService
from services.upload import UploadService
from services.update import UpdateService
from services.discovery import DiscoveryService

class CloudSync(object):

    def __init__(self, config_filepath="./config.json"):
        
        ioService = IOService()
        service = DiscoveryService(CredentialsService(config_filepath, ioService))
        
        self.searchService = SearchService(service)
        self.downloadService = DownloadService(service,self.searchService)
        self.uploadService = UploadService(service,self.searchService, ioService)
        self.updateService = UpdateService(service,self.searchService, ioService)

    def download(self, where_to_download,query):
        self.downloadService.download_file(where_to_download,query,self._onProgress)
    
    def upload(self, filename, filepath, path_on_drive):
        self.uploadService.upload(filename, filepath, path_on_drive,onProgress=self._onProgress)
    
    def update(self, filename, filepath, path_on_drive):
        self.updateService.update(filename, filepath, path_on_drive, onProgress=self._onProgress)

    def find(self, filename, foldername=None):
        files = self.searchService.find(begin_with=filename,folder_name=foldername)
        return files

    def _onProgress(self, prog):
        sys.stdout.write("\r[{0}] {1}% ".format('#'*prog, prog))
        sys.stdout.flush()
        
    
