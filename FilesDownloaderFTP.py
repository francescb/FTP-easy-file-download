# Download files from server using FTP

import ftplib
import optparse
from os import listdir, getcwd, chdir, mkdir
from os.path import isfile, join, isdir

def serverLogin(hostname, username, password):
    """Connect to a server via FTP.
    * hostname: server's hostname.
    * username: username to access the server via FTP.
    * password: password to access the server via FTP.
    """

    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(user = username, passwd = password)
        print("\n[*] " + str(hostname) + " FTP Logon Succeded.")
        return ftp
    except Exception as e:
        print("\n[-] " + str(hostname) + " FTP Logon Failed.")
        return False

def listFiles(ftp, directory, fileType = "*", resetDirectoryToRoot = False):
    """List all the files from a server's directory.
    * ftp: instance of FTP class
    * directory: Server directory from which to list files.
    * fileType: Optional argument used to filter files by file type.
    * resetDirectoryToRoot: Optional argument used to set the FTP current directory back to the root directory after using the function. Otherwise, current directory is set to the same as the directory argument.
    """

    ftp.cwd(directory)
    files = ftp.nlst()
    files = [file for file in files if file.endswith(fileType)]
    print(str(len(files)) + " " + fileType +" files found in " + directory)
    if resetDirectoryToRoot:
        ftp.cwd("/")
    return files

def downloadFiles(ftp, fileList, destination, fileType = ""):
    """Download multiple files from a server via FTP.
    * ftp: instance of FTP class
    * fileList: list of files to be downloaded from the specified directory.
    * destination Local directory in which to save files.
    """

    if not isdir(destination):
        mkdir(destination)
    localFileList = [file for file in listdir(destination) if isfile(join(destination, file)) and file.endswith(fileType)]
    filesNotLocal = [file for file in fileList if file not in localFileList]
    chdir(destination)
    errors = 0
    nFiles = 0
    if len(fileList) == 0:
        print("\n[*] All files are already locally stored. No files downloaded.")
    elif len(fileList) > len(filesNotLocal):
        print("\n[*] Updating files in " + destination + ": " + str(len(filesNotLocal)) + " are not locally stored.")
    else:
        print("\n[*] Downloading all " + str(fileType) + " files to " + str(destination) + ".")
    for file in filesNotLocal:
        try:
            ftp.retrbinary("RETR " + file ,open(file, 'wb').write)
            nFiles += 1
        except:
            print("Error downloading " + str(file))
            errors += 1
    print("\n[*] Finished downloading " + str(nFiles) + " files: " + str(errors) + " errors found.")
    return errors

def main():
    parser = optparse.OptionParser(usage="usage: %prog [options]", description="""Download multiple files from a server via FTP.
    Specify the type of file to be downloaded, the FTP directory where they are located and the local directory where the files must be saved""")
    parser.add_option("-H", dest = "hostname", type = "string", help = "Specify hostname")
    parser.add_option("-u", dest = "username", type = "string", help = "Specify username")
    parser.add_option("-p", dest = "password", type = "string", help = "Specify password")
    parser.add_option("-d", dest = "directory", type = "string", help = "Specify FTP directory")
    parser.add_option("-f", dest = "fileType", type = "string", help = "Specify Filetype to Retrieve")
    parser.add_option("-t", dest = "targetDestination", type = "string", help = "Specify Local Destination")
    options, args = parser.parse_args()
    hostname = options.hostname
    username = options.username
    password = options.password
    directory = options.directory
    fileType = options.fileType
    destination = options.targetDestination
    ftp = serverLogin(hostname, username, password)
    fileList = listFiles(ftp, directory, fileType)
    downloadFiles(ftp, fileList, destination, fileType)
    ftp.quit()

if __name__ == "__main__":
    main()
