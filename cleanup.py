import os,time

cwd = os.getcwd()
print "Working directory is {}".format(cwd)
#create the date string
date = time.localtime()
delim = "_"
dateStr = str(date.tm_year) + delim + str(date.tm_mon)+ delim + str(date.tm_mday)

print dateStr
#create folder name. rename prefix if you like
prefix = "cleanup_"
folderName = cwd+os.sep+prefix+dateStr 
if not os.path.exists(folderName):
    os.mkdir(folderName)
#loop through files
filenames = os.listdir(cwd)

for i in filenames:
    if os.path.isdir(cwd+os.sep+i):
        print "{} is directory Not moving".format(i)
    else:
        print "{} is file. Moving".format(i)
        os.rename(cwd+os.sep+i,folderName+os.sep+i)

