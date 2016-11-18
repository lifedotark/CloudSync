# -*- coding: utf-8 -*-

import os
from json import loads

class IOService(object):

    def get_all_folders(self, filepath):
    
        print("Listing all folders in path: {}".format(filepath))
        
        folders = []
            
        while True:
            filepath, last_folder = os.path.split(filepath)
            
            if not last_folder:
                break
            
            folders.insert(0, last_folder)
        
        print("Found: {} folders".format(len(folders)))
        return folders
    
    def load_config_file(self, config_filepath):
        configs = loads(self.read_file(config_filepath))
        
        # configs["credentials_dir"] = os.path.expanduser(configs["credentials_dir"])
        configs["client_secret_file"] = os.path.expanduser(configs["client_secret_file"])
        configs["credential_file"] = os.path.expanduser(configs["credential_file"])
        
        return configs
    
    def read_file(self, filepath):
        with open(filepath,"r") as file:
            return "".join([line.strip() for line in file.readlines()])
            
    def create_if_not_exists(self, filepath):
        if not os.path.exists(filepath):
            os.makedirs(filepath)

    def get_path(self, folderpath, filename):
        return os.path.join(folderpath, filename)