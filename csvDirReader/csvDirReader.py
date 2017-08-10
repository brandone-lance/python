import pandas as pd
import os

csvDir = input('Diretory containing CSV files: ')

##  The directory should end in a backslash.
##  This will append a backslash if not.
if '\\' not in csvDir[-1]:
    csvDir = csvDir + '\\'

csvFiles = os.listdir(csvDir)
os.chdir(csvDir)

fileCounter = 0

for currentFile in csvFiles:
    varName = currentFile[0:-4]
    commandEval = varName + '= pd.read_csv(\'' + currentFile + '\')'
    exec(commandEval)
    fileCounter = fileCounter + 1

print(str(fileCounter) + ' CSV files converted into dataframes')
