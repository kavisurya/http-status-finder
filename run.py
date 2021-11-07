import argparse
import os
import fragment

def Help():
    print("Hello Everyone!!\n This is kavisurya,\n In this tool you can give n number of inputs and parallelly you will get a output by separetely.")
    print(" Here you can give time delay to every each requests. So you will escape from some firewall securities. \n T"
          "hank you\n follow me on https://instagram.com/kavisuryaofficial\nExample : python3 run.py -f /home/rao/file.txt -d 0 -p 'Test_project' -r 0\n\n")



parser = argparse.ArgumentParser(description=Help())
parser.add_argument("-f", "--file")
parser.add_argument("-d", "--delay")
parser.add_argument("-p", "--project_Name")
parser.add_argument("-r", "--resume", help="Resume your files.\n Example : python3 run.py -f /home/rao/file.txt -d 0 -p 'Test_project' -r 3 \n\n  [3 means starts from 3rd file.] ")
args = parser.parse_args()

path = ""
delay = 0
name = ""
resume = 1

if args.file:
    path = args.file

if args.delay:
    delay = args.delay

if args.resume:
    resume = args.resume

if args.project_Name:
    name = args.project_Name

def MakeProjectDir(dirname):
    os.system("mkdir ./"+dirname)

MakeProjectDir(name)

fragment.main(path, name)

filePath = path
fileRead = open(filePath, "r")
fileLines = fileRead.readlines()
length = round(len(fileLines)/100)

print("Starting from "+ str(resume) )

try:
    for i in range(int(resume), length+1):
        os.system("python3 httpstatus.py -f ./"+name+"/Fragment/file"+str(i)+".txt -d "+delay+" -p "+name)
        print("Process "+str(i)+" completed !!")
except KeyboardInterrupt:
    print("User Exited !!")
    exit()
except Exception as f:
    print(f)