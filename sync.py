from cloud import CloudSync
from pprint import pprint
import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--find", help="Find an file")
parser.add_argument("-u","--upload", help="Upload a file", action="store_true")
parser.add_argument("-d","--download", help="Download a file", action="store_true")
parser.add_argument("-Id", help="Your file Id.")
parser.add_argument("-bw","--begin_with", help="Find a file with the name starting with the value.")
parser.add_argument("-fn","--file_name", help="You file's name. Used to Download a file with the exact name, or upload a file with that name.")
parser.add_argument("-cd","--cloud_drive", help="The cloud folder that you want to use. If you have multiple files with the same name, you can use this as an filter. For upload, the folder to put your file.")
parser.add_argument("-si","--save_in", help="Where to save your file.", default=os.getcwd())
parser.add_argument("-p","--filepath", help="Path to the the file that you want to upload.")
args = parser.parse_args()

sync = CloudSync()

if args.find:
    res = sync.find(args.find)
    pprint(res)
    
if args.download:
    if not (args.file_name or args.begin_with or args.Id):
        print("To download a file, you need to inform a name, an Id or a word that exists in the file name.")
        quit()
    
    query = {
        "begin_with":args.begin_with,
        "name_equals":args.file_name,
        "folder_name":args.cloud_drive,
        "Id":args.Id
    }
    sync.download(os.path.expanduser(args.save_in), query)       

if args.upload:
    if not (args.file_name and args.filepath and args.cloud_drive):
        print("To upload a file, you need to inform a name, the filepath and the cloud folder name.")
        quit()
        
    sync.upload(args.file_name, os.path.expanduser(args.filepath), args.cloud_drive)

print("Done!")

