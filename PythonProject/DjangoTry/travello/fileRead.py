import os

class fileOperation:

    def fileReading(self,pathUrl):
        rowData1 = []

        with open(pathUrl, "r+") as locationFile:
            print('|*******File Read*******|')
            print(locationFile)
            print("File Readable ", locationFile.readable())
            if locationFile.readable():
                print('|*******File data*******|')
                rowData1 = locationFile.read()
                print(rowData1)
                print("count ", len(rowData1))
            else:
                print("file not readable")
                print("||*************||")
            return rowData1

