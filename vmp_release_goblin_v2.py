import os, zipfile, shutil as su, fnmatch as fn, re

# Global Variables

prep_dir = r'C:\Users\mdevall\Downloads\release_temp'

# Test for valid file and Decompress downloaded zip file

def verifyZip(file):
    pathToZip = os.chdir(r'C:\Users\mdevall\Downloads')
    currentDir = os.getcwd()

    # Using isfile here not only verifies if the file is zip but also if it exists
    if not os.path.isfile(file):
        raise OSError('Error:', fileName, ' is not a valid zip file or does not exist.')
		
    # Create file object, extract release files from zip and close the file object		
    zf=zipfile.ZipFile(file,'r') 
    zf.extractall(prep_dir) 
    zf.close()




# Function scrapes the release notes for script order of execution				
def scrapeRelease(release):
    try:
        fhand = open(release)
    except:
        print('File cannot be opened:'), release
    else:
        count = 0
        releaseDirectory = releaseNotes.rsplit('.',1)[0] #Name the release directory by removing file type from release notes string
        os.chdir(prep_dir)
        os.mkdir(releaseDirectory)
        os.chdir(releaseDirectory) #Change directory to prepared release directory
        
        for line in fhand:
            line = line.rstrip()
            sql = line.find('.sql')
            if line.find('.sql') ==-1:
                continue
            find_script = line[:]
            count += 1
            dir_num=find_script.split()
            numberOnly = dir_num[0].rstrip('.')
            scriptName = dir_num[1]
            
            if numberOnly.isdigit() ==1: # Test to see if line begins with digit if so it will be used as directory name
                for scripts in scriptName:
                    dir_name=scriptName
                    
                    
                os.mkdir(numberOnly + '_' + dir_name)
                print(dir_name + ' added to release directory')
                
        return(releaseDirectory) # Added this to return the newley created release directory for use in stageRelease function

# Function builds directory structure for each case
def stageRelease():
    os.chdir(prep_dir)
    releaseDirectory = releaseNotes.rsplit('.',1)[0] #Name the release directory by removing file type from release notes string
    os.chdir(releaseDirectory) #Change directory to prepared release directory
        
    for root, dirs, files in os.walk(prep_dir):
            for subDirectories in dirs:
                print(subDirectories)
                if dirs != releaseDirectory:
                    os.chdir(dirs)
                    zf = zipfile.ZipFile(filenames)
                if subDirectories == dirs:
                    for zips in files:
                        print(zips)
                
                filePath = os.path.join(dirs,zips)
                zf = zipfile.ZipFile(filePath)
                zf.extractall(dirs)
                #if fn.fnmatch(filenames,'*.zip'):
                #subfile = os.path.join(prep_dir, filenames)
                        #subfile = os.path.abspath(filenames)
                
                        #print(filenames)
'''
                 zf = zipfile.ZipFile(subfile)
                    ticket_name=subfile.rsplit('.',1)[0]
                    ticket_name=ticket_name.split('_')
                    ticket_name=ticket_name[-1]
                    print(ticket_name)
                    print(subDirectories)
                    if ticket_name in subDirectories:
                        su.move(filenames,subDirectories)
                        zf = zipfile.ZipFile(filenames)
                        zf.extractall(subDirectories)
                #if
                #zf.extractall
                    #for subfile in f.namelist():
                        #if fn.fnmatch(subfile,'*.sql') and fn.fnmatch(dir_na
                #print(filenames)
                        #zf.close()

'''

fileName = input('Enter file: ')
releaseNotes = input('Enter Release notes filename: ')
verifyZip(fileName)
scrapeRelease(releaseNotes)
stageRelease()

print('VMP goblin has successfuly completed release prep....')
