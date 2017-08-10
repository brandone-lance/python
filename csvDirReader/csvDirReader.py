import pandas as pd
import os

csvDir = input('Diretory containing CSV files: ')

##  The directory should end in a backslash.
##  This will append a backslash if not.
if '\\' not in csvDir[-1]:
    csvDir = csvDir + '\\'

##  Create a list of filenames from directory of choice and
##  Change to the directory
csvFiles = os.listdir(csvDir)
os.chdir(csvDir)

##  Set our counters to zero...
fileCounter = 0
failCounter = 0

##  If it's a proper csv, read into dataframe else iterate failcounter
for currentFile in csvFiles:
    if 'csv' in currentFile[-3:]:        
        varName = currentFile[0:-4]
        commandEval = varName + '= pd.read_csv(\'' + currentFile + '\')'
        exec(commandEval)
        fileCounter = fileCounter + 1
    else:
        failCounter = failCounter + 1

##  Print our results...
print(str(fileCounter) + ' CSV files converted into dataframes.')
if failCounter != 0:
    print(str(failCounter) + ' file(s) failed to be converted.')
