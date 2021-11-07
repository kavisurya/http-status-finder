import os



def MakeDir(output):
    os.system("mkdir -p "+ output)


def DynamicFileCreate(txtname,output):
    os.system("touch "+output+"/file"+str(txtname)+".txt")

def DynamicFileWrite(fname,values,output):
    fileOpenAppend = open(output+"/file"+str(fname)+".txt", "a")
    fileOpenAppend.write(values)



def MainFileWrite(fileLines,output):
    count = 1
    mfile = 1
    for x in fileLines:
        if count == 100:
            DynamicFileWrite(mfile, x,output)
            count = 1
            mfile = mfile + 1
        
        else:
            DynamicFileWrite(mfile, x,output)

        count = count + 1


def MainOne(fileLines,output):
    count = 1
    MakeDir(output)
    mkfile = 1
    for x in fileLines:
        if count == 100:
            DynamicFileCreate(mkfile,output)
            count = 1
            mkfile = mkfile + 1
        
        count = count + 1

def main(inputFilefromExt, projectName):
    try:
        # filePath = "/home/baby/Documents/My tools/recon/impactguru.com-waybackurls"
        filePath = inputFilefromExt
        fileRead = open(filePath, "r")
        fileLines = fileRead.readlines()
        output = "./"+projectName+"/Fragment"
        
        MainOne(fileLines,output)
        MainFileWrite(fileLines,output)
        print("Success from fragment")
    except Exception as e:
        print(e)