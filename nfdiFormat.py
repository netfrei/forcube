import re
regex = r"(label\{.*)\}\}"
subst = "\\1}"
file1=open("./nfdi4sd.tex","r")
file2=open("./nfdi4sdout.tex","w")
count=0
flagout=True
hyper=False
while True:
    count += 1
    line = file1.readline()
    if not line:
        break
    if "!!! error" in line:
        flagout=False 
    if "\hypertarget{" in line:
        flagout=False
        hyper=True
    if "\{:" in line:
        flagout=False
    if flagout:
        result=re.sub(regex, subst, line, 0, re.MULTILINE)
        file2.write(result)
    if flagout==False and hyper==True:
        flagout=True 
        hyper=False
    if flagout == False and "dbc35699789" in line:
        flagout = True
    if flagout == False and ".page-title\}" in line:
        flagout = True

print(f"Geschrieben: {count} Zeilen")
file2.close()


