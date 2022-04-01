import os, shutil

for folderName, subFolders, fileNames in os.walk('D:\\pythonSTUFF\\SelectCopyFolder\\'):
    print('The current folder is '+ folderName)

    for subfolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in fileNames:
        if os.path.getsize(os.path.join(folderName, filename)) > 200000:
            print(filename)
            #os.unlink(filename)

    print('')

