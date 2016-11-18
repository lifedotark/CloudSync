## Synopsis

A simple command line app that allows you to upload your files to Google Drive. It was designed to be used in environments like Raspberry Pi, so probably it will run nice enough wherever you use it ;-)

I needed a way to upload and download large files from google drive using the command line. Other Python packages that I used, when the file was too large, the script consumed all the memory available and crashed. So, this project born with the goal to not consume all your memory, and to be simple enouth to embed in your projects.

It was developed and tested using python3.

## Installation

First, you need to run:

```
pip3 install -r requirements.txt
```

After that, you need to set the correct properties in config.json

Inside that file you need to configure some properties required by the app:

Property|Meaning
--------|-------
client_secret_file | The path to your app credentials. It is provided by google, when you create your app. An simple guide can be accessed in https://developers.google.com/drive/v3/web/quickstart/python.
credential_file | The path where the authorization provided by your login should be saved.
scopes | The permissions that your application should have when accessing the cloud files your users. The complete list can be accessed in https://developers.google.com/drive/v2/web/scopes
app_name | The name of your app. It must be the same as the name that you provided when registering your application.



In the end, your config file should look like this:
```json
{
    "client_secret_file":"/home/ubuntu/.credentials/client_secrets.json",
    "credential_file":"/home/ubuntu/.credentials/credentials.json",
    "scopes":"https://www.googleapis.com/auth/drive",
    "app_name":"YourAppName"
}
```

## Code example

To run as a command line App:

To show all that was implemented, just run the following:

```
python3 sync.py -h
```

The output:

```
python3 sync.py -h

usage: sync.py [-h] [-f FIND] [-u] [-d] [-Id ID] [-bw BEGIN_WITH]
               [-fn FILE_NAME] [-cd CLOUD_DRIVE] [-si SAVE_IN] [-p FILEPATH]

optional arguments:
  -h, --help            show this help message and exit
  -f FIND, --find FIND  Find an file
  -u, --upload          Upload a file
  -d, --download        Download a file
  -Id ID                Your file Id.
  -bw BEGIN_WITH, --begin_with BEGIN_WITH
                        Find a file with the name starting with the value.
  -fn FILE_NAME, --file_name FILE_NAME
                        You file's name. Used to Download a file with the
                        exact name, or upload a file with that name.
  -cd CLOUD_DRIVE, --cloud_drive CLOUD_DRIVE
                        The cloud folder that you want to use. If you have
                        multiple files with the same name, you can use this as
                        an filter. For upload, the folder to put your file.
  -si SAVE_IN, --save_in SAVE_IN
                        Where to save your file.
  -p FILEPATH, --filepath FILEPATH
                        Path to the the file that you want to upload.

```

#### To upload:

```
python3 sync.py -p '/your/file/path.txt' -fn "FileNameInDrive.txt" -cd "/Your/Folder/In/Drive"
```
#### To download:

```
python3 sync.py -d -fn "your_file_name"
```

If you have multiple files with the same name:

```
python3 sync.py -d -fn "your_file_name" -cd "the folder name"
```

**OR**

```
python3 sync.py -d -Id "The Id of your file"
```

#### To find a file Search:

```
python3 sync.py -f "Your file name"
```

## RoadMap

- Add examples showing how to embed it inside a project;
- When runing for the first time, create a wizard like to create the config file;
- Add a delete file option;
- Add onedrive and dropbox cloud services;
