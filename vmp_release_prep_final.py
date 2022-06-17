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
		
		
    zf=zipfile.ZipFile(file,'r')
    zf.extractall(prep_dir)
    zf.close()
#    print (zf.namelist())
#    print('\n')
		


    # Make sure there are no compressed subdirectories. If so decompress and move them up
'''		
    for root, dirs, files in os.walk(prep_dir):
	    for filenames in files:
		    if fn.fnmatch(filenames,'*.zip'):
			    #subdir_path = os.path.join(prep_dir, filenames)
			    #print(dirs)
			    #su.move(filenames, prep_dir)
'''				
		

		
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
            #print(find_script.split())
            dir_num=find_script.split()#new lines added 06/27/2016
            numberOnly = dir_num[0].rstrip('.')
            scriptName = dir_num[1]
            if numberOnly.isdigit() ==1: # new lines added 06/27/2016
                #for scripts in dir_num: #new lines added 06/27/2016
                

                for scripts in scriptName:
                    #dir_name=dir_num #new lines added 06/27/2016
                    dir_name=scriptName
                    
                    
                os.mkdir(numberOnly + '_' + dir_name) #new lines added 06/27/2016
                print(dir_name + 'added to release directory')
'''
 this code will create directories based on release notes order: example 01_vm-20682
if dir_num.isdigit() ==1:
    for word in words:
	    dir_name=words[1]

		
>>> os.mkdir(dir_num + '_' + dir_name)
'''


fileName = input('Enter file: ')
releaseNotes = input('Enter Release notes filename: ')
verifyZip(fileName)
scrapeRelease(releaseNotes)


print('VMP goblin has successfuly completed release prep....')
