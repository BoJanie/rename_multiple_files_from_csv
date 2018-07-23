#original had unicodecsv as csv, but this version of python says it doesn't exist
import os, csv, sys

#open and store csv file as a 'dictionary'
IDs = {}
#   'rb' = r is for 'reading' the file and 'b' is for binary
with open('rename_key.csv','rb') as csvfile:
    timeReader = csv.reader(csvfile, delimiter = ',')
    #build dictionary with associated IDs
    for row in timeReader:
        IDs[row[0]] = row[1]

path = 'rename_these_files/'
tmpPath = 'renamed_files/'

for filename in os.listdir(path):
    oldname = filename
    newname = IDs[oldname]
    os.rename(path + oldname, tmpPath + newname)

#Below is code to allow errors
#failed = []
#for oldname in os.listdir(path):
#    try:
#        old = os.path.join(path, oldname)
#        new = os.path.join(tmpPath, IDs[oldname])
#        os.rename(old, new)
#    except KeyError, OSError:
#        failed.append(oldname)

