# http-status-finder

Hello Everyone!!
 This is kavisurya,
 In this tool you can give n number of inputs and parallelly you will get a output by separetely.
 Here you can give time delay to every each requests. So you will escape from some firewall securities. 
 Thank you
 follow me on https://instagram.com/kavisuryaofficial

## Installation
```
git clone https://github.com/kavisurya/http-status-finder.git
cd http-status-finder/
pip install -r requirements.txt
python3 httpstatusless.py -h
```


### Output

```
███╗   ███╗██████╗ ██████╗ ██╗  ██╗ ██████╗
████╗ ████║██╔══██╗██╔══██╗██║  ██║██╔═████╗
██╔████╔██║██████╔╝██████╔╝███████║██║██╔██║
██║╚██╔╝██║██╔══██╗██╔══██╗╚════██║████╔╝██║
██║ ╚═╝ ██║██║  ██║██║  ██║     ██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝ ╚═════╝


Hello Everyone!!
 This is kavisurya,
 In this tool you can give n number of inputs and parallelly you will get a output by separetely.
 Here you can give time delay to every each requests. So you will escape from some firewall securities. 
 Thank you
 follow me on https://instagram.com/kavisuryaofficial




usage: httpstatusless.py [-h] [-f FILE] [-d DELAY] [-p PROJECT_NAME]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE
  -d DELAY, --delay DELAY
  -p PROJECT_NAME, --project_Name PROJECT_NAME

```

# If your URL list lesser than 300, Use below commands !!
### Usage
```
-f -> input file example : /home/rao/urls.txt 
-d -> delay for each requests 
-p -> Your project name


python3 httpstatusless.py -f /home/rao/urls.txt -d 0 -p 'projectname'

```

### Time based checking

```
python3 httpstatusless.py -f /home/rao/urls.txt -d 5 -p 'projectname'

```


# If your URL list greter than 300, Use below commands !!
### Usage

```
cd http-status-finder/
python3 run.py -h

```
## Output
```
Hello Everyone!!
 This is kavisurya,
 In this tool you can give n number of inputs and parallelly you will get a output by separetely.
 Here you can give time delay to every each requests. So you will escape from some firewall securities. 
 Thank you
 follow me on https://instagram.com/kavisuryaofficial
Example : python3 run.py -f /home/rao/file.txt -d 0 -p 'Test_project' -r 0


usage: run.py [-h] [-f FILE] [-d DELAY] [-p PROJECT_NAME] [-r RESUME]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE
  -d DELAY, --delay DELAY
  -p PROJECT_NAME, --project_Name PROJECT_NAME
  -r RESUME, --resume RESUME
                        Resume your files. Example : python3 run.py -f /home/rao/file.txt -d 0 -p 'Test_project' -r 3 [3 means starts
                        from 3rd file.]

```


## Description
In this Mode for a complete large number of checking processes. If your URL's 30000 or lakhs,  The first work is in this tool, split your URL's by 100. Ex: your URL's like 30000, [ 30000/100 = 300 ] Here your URL's splitting 300, and giving input to the tool. You can see the split URLs path /yourprojectname/Fragnement/file1.txt....file300.txt. In this process, you're suddenly come out from this tool, you can again resume that process. 
Ex. During 3'rd file process, you're come out of this tool, you can resume with the 3rd file using the -r parameter.  

```
python3 run.py -f /home/rao/file.txt -d 0 -p 'Test_project' -r 3 [3 means starts from 3rd file.]

```


### usage

```
python3 run.py -f /home/rao/file.txt -d 0 -p 'Test_project' -r 0

-f -> input file example : /home/rao/urls.txt 
-d -> delay for each requests 
-p -> Your project name
-r -> Resume your files.
```

