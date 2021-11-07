import argparse
import requests
import os
import time
import progressbar

print(
"""
███╗   ███╗██████╗ ██████╗ ██╗  ██╗ ██████╗
████╗ ████║██╔══██╗██╔══██╗██║  ██║██╔═████╗
██╔████╔██║██████╔╝██████╔╝███████║██║██╔██║
██║╚██╔╝██║██╔══██╗██╔══██╗╚════██║████╔╝██║
██║ ╚═╝ ██║██║  ██║██║  ██║     ██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝ ╚═════╝

""")


def Help():
    print("Hello Everyone!!\n This is kavisurya,\n In this tool you can give n number of inputs and parallelly you will get a output by separetely.")
    print(" Here you can give time delay to every each requests. So you will escape from some firewall securities. \n T"
          "hank you\n follow me on https://instagram.com/kavisuryaofficial\n\n\n\n")


parser = argparse.ArgumentParser(description=Help())
parser.add_argument("-f", "--file")
parser.add_argument("-d", "--delay")
parser.add_argument("-p", "--project_Name")
args = parser.parse_args()

path = ""
delay = 0
name = ""

if args.file:
    # print("Help Menu ", Help(), args.file)
    path = args.file

if args.delay:
    # print("Displaying O output", args.delay)
    delay = args.delay

if args.project_Name:
    # print("Displaying O output", args.project_Name)
    name = args.project_Name

file1 = open(path, "r")

# storing datas in array
k = file1.readlines()
# print(k)

"""CREATING A FILE DIRECTORY AND FILES"""


def create_file():
    a = 200
    os.system("mkdir " + name)
    os.system("cd "+name)
    for l in range(4):
        os.system("touch "+"./"+name+"/output_"+str(a)+".txt")
        a = a + 100
    print("Successfully "+name+" project created")


widgets = [' [',
		progressbar.Timer(format='elapsed time: %(elapsed)s'),
		'] ',
		progressbar.Bar('*'), ' (',
		progressbar.ETA(), ') ',
		]


create_file()
"""SAVING OUTPUT FILES"""
output_200 = open("./"+name+"/output_200.txt", "a")
output_300 = open("./"+name+"/output_300.txt", "a")
output_400 = open("./"+name+"/output_400.txt", "a")
output_500 = open("./"+name+"/output_500.txt", "a")


print("Please wait...")

bar = progressbar.ProgressBar(max_value=len(k), widgets=widgets).start()

lap = 0


def pusVals(req,x1):
    print(req, "\t",x1)
    if str(req)[0:1] == "2":
        output_200.write(str(req)+"\t"+x1)
            # print("200 OK " + k[i])
    elif str(req)[0:1] == "3":
            # print("300 OK " + k[i])
        output_300.write(str(req)+"\t"+x1)
    elif str(req)[0:1] == "4":
        output_400.write(str(req)+"\t"+x1)
    elif str(req)[0:1] == "5":
        output_500.write(str(req)+"\t"+x1)
    else:
        print("Something Happen " + x1)


for x1 in k:

    time.sleep(0.001)
    bar.update(lap)
    lap = lap + 1
    # print(x1)
    try:
        time.sleep(int(delay))
        reqq = os.popen('curl '+str(x1).replace("\n","")+' -Is | grep "HTTP/" | cut -d " " -f2').read()
        req = reqq.replace("\n","")
        # print(req, len(req))
        

        if len(str(req)) == 0:
            req = requests.get(x1)
            pusVals(req.status_code, x1)
        elif len(str(req)) > 3:
            req = requests.get(x1)
            pusVals(req.status_code, x1)
        else:
            pusVals(req,x1)

        
    except requests.exceptions.RequestException:
        pass
    except FileNotFoundError:
        print("File Olunga kudra panni payale fila kanom da !!!")
    except KeyboardInterrupt:
        print("\nExiting\nPlease Check Your Results file ./Your Project/OUTPUT_FILES.TXT")
        exit()
    except Exception as e:
        print(e)

if len(k) == lap:
    print("\nCompleted the task !!")