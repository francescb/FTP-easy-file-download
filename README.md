# Easy file downloader via FTP
Download multiple files from a server via FTP.

What Is This?
-------------

Easy file downloader via FTP is a simple script to make, as its name indicates, downloading files from servers via FTP easy and intuitive. This script allows you to download multiple files from a specified directory on the server, allowing to filter by file type.

How To Use This
---------------

1. Download the script and make sure that Python is installed in your computer.
2. Open a terminal console and execute the script by using the command:
 ``` python FilesDownloaderFTP.py -H "hostname" -u "username" -p "password" -d "server Directory" -f "file Type" -t "local Directory" ``` 

  
   - -H HOSTNAME           Specify hostname
   - -u USERNAME           Specify username
   - -p PASSWORD           Specify password
   - -d DIRECTORY          Specify FTP directory from which to download the files
   - -f FILETYPE           Specify Filetype to Retrieve (do not specify it if no specific filetype is needed to be retrieved)
   - -t TARGETDESTINATION  Specify Local Destination in which to store the files retrieved
