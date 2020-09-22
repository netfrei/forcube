import re
file1=open("./nfdi4sd.pd","r")
file2=open("./nfdi4sdout.pd","w")
count=0
flag=True
hyper=False

r1 = r"(#\s.*)\s\{.*"
s1 = "\\1"
r2 = r"(## .*)\s\{.*"


def sublin(line):
    result=line
    if re.match(r1,line):
        result = re.sub(r1, s1, line, 0, re.MULTILINE)
    elif re.match(r2,line):
        result = re.sub(r2, s1, line, 0, re.MULTILINE)
        # result=""
    return(result)

def switchflag(line,flag):
    if "!!! error" in line:
        flag=not flag 
    return(flag)
def switchflagout(line,flag):
    if "dbc35699789" in line:
        flag=not flag
    return(flag)


r3 = r"\*\*(.*)\*\*"
r4 = r"\*\*.*\*\*[:]*(.*)"

def begnote(line):
    label = re.findall(r3, line)[0]
    be = r"\begin{awesomeblock}[magenta]{1pt}{"+label+"}{magenta}"
    bf = re.findall(r4, line)[0]
    file2.write(be)
    file2.write(bf)
  
def finnote(l,s):
    flag=False
    if s=="error":
        if "dbc35699789" in l:
            flag=True 
    if s=="note": 
        if len(l)<4:
            flag=True
    return(flag)

def noteenv(line):
    if "!!! " in line:
        innote=True
        if "error" in line:
            while innote:
                line=file1.readline()
                if finnote(line,"error"):
                    innote=False
            line=file1.readline()
        else:
            line=file1.readline()
            begnote(line)
            while innote:
                line=file1.readline()
                if finnote(line,"note"):
                    innote=False
                    bo = r"\end{awesomeblock}"
                    file2.write(bo)
                line=file1.readline()
    return(line) 


while True:
    count += 1
    line = file1.readline()
    if not line:
        break
    line=sublin(line)
    line=noteenv(line)
    file2.write(line)
    
print(f"Geschrieben: {count} Zeilen ")
file2.close()


