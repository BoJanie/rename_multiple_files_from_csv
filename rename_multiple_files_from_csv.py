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

#This section makes sure all files in .csv are in folder. If not, it informs the user.
for key in IDs:
    if not os.path.isfile(str(path+key)):
        print key + ' is listed in .csv file but is not in folder.'
                
for filename in os.listdir(path):
    oldname = filename

failed = []
for oldname in os.listdir(path):
    try:
        old = os.path.join(path, oldname)
        new = os.path.join(path, IDs[oldname])
        os.rename(old, new)
    #this error section will inform the user if a file in the directory was not in csv
    #could also be error in other cases? The lack of .csv was the only one I experienced.
    except KeyError, OSError:
        failed.append(oldname)
        print oldname + ' was not in the .csv file and so was not renamed.'
