def check(filename):
    file=open(filename)
    line=file.readline()
    heading=[]
    headings=line.split(",")
    for i in range(len(headings)):
        heading.append((i,headings[i]))
    line=file.readline()
    linecount=0
    missing=[]
    missingcount=0
    while line:
        linewords=line.split(",")
        for i in range(len(linewords)):
            if (linewords[i] == "" or linewords[i] == "?"):
                missing.append((linecount,heading[i]))
                missingcount=missingcount+1
        line=file.readline()
        linecount=linecount+1
    return  missing,missingcount

def isMissing(filename,x,y):
    file=open(filename)
    line=file.readline()
    line=file.readline()
    linecount =0;
    isMissing =False
    while line:
        linewords=line.split(",")
        for i in range(len(linewords)):
            if (linewords[i] == "" or linewords[i] == "?"):
                if(linecount ==x and i==y):
                    isMissing = True
        line=file.readline()
        linecount=linecount+1
    return isMissing

def isMissingByHeading(filename,x,headIn):
    file=open(filename)
    line=file.readline()
    heading=[]
    headings=line.split(",")
    for i in range(len(headings)):
        heading.append(headings[i])
    line=file.readline()
    linecount=0
    isMissing =False
    while line:
        linewords=line.split(",")
        for i in range(len(linewords)):
            if (linewords[i] == "" or linewords[i] == "?"):
                if(heading[i] == headIn and linecount==x):
                    isMissing=True
        line=file.readline()
        linecount=linecount+1
    return  isMissing

def isMissingListbyLine(filename,lineNumber):
    file = open(filename)
    line = file.readline()
    heading = []
    headings = line.split(",")
    for i in range(len(headings)):
        heading.append((i, headings[i]))
    line = file.readline()
    linecount = 0
    missing = []
    isFound= False
    while line:
        linewords = line.split(",")
        attributeCount=0
        for i in range(len(linewords)):
            if ((linewords[i] == "" or linewords[i] == "?") and linecount == lineNumber) :
                missing.append((linecount, heading[i]))
                attributeCount=attributeCount+1
                isFound = True
        if(isFound == False):
            line = file.readline()
            linecount = linecount + 1
        else :
            break
    return missing,attributeCount


def isMissingListbyHeadingNumber(filename,headingnumber):
    file = open(filename)
    line = file.readline()
    heading = []
    headings = line.split(",")
    for i in range(len(headings)):
        heading.append((i,headings[i]))
    line = file.readline()
    linecount = 0
    missing = []
    missinglinecount=0
    while line:
        linewords = line.split(",")
        for i in range(len(linewords)):
            if ((linewords[i] == "" or linewords[i] == "?") and i == headingnumber) :
                missing.append((heading[i],linecount))
                missinglinecount=missinglinecount+1
            line = file.readline()
            linecount = linecount + 1
    return missing,missinglinecount

def isMissingListbyHeadingName(filename,headingname):
    file = open(filename)
    line = file.readline()
    heading = []
    headings = line.split(",")
    for i in range(len(headings)):
        heading.append(headings[i])
    line = file.readline()
    linecount = 0
    missing = []
    missinglinecount=0
    while line:
        linewords = line.split(",")
        for i in range(len(linewords)):
            if ((linewords[i] == "" or linewords[i] == "?") and heading[i] == headingname) :
                missing.append((heading[i],linecount))
                missinglinecount=missinglinecount+1
            line = file.readline()
            linecount = linecount + 1
    return missing,missinglinecount


# print "Checking iq/sj dataset"
filename="../dataset/dengue_train_iq.csv"
# filename="../dataset/dengue_train_sj.csv"
# missing,missingcount = check(filename)
# print missing
# print missingcount
# print "Checking isMissing"
# print isMissing(filename,45,11)
# print "Checking isMissingByHeading"
# print isMissingByHeading(filename,21,'station_precip_mm')
# print "Checking isMissingByLine"
# missing,attributecount = isMissingListbyLine(filename,45)
# print missing
# print attributecount

print "Checking isMissingListbyHeadingNumber"
missing,missingcount = isMissingListbyHeadingNumber(filename,22)
print missing
print missingcount
print "Checking isMissingListbyHeadingName"
missing,missingcount = isMissingListbyHeadingName(filename,'station_precip_mm')
print missing
print missingcount
