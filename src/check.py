def fetchHeading(filename):
    file=open(filename)
    line=file.readline()
    heading=[]
    headings=line.split(",")
    for i in range(len(headings)):
        heading.append((headings[i]))
    file.close()
    return heading

def fetchHeadingWithIndex(filename):
    file=open(filename)
    line=file.readline()
    heading=[]
    headings=line.split(",")
    for i in range(len(headings)):
        heading.append((i,headings[i]))
    file.close()
    return heading

def getMissing(filename):
    heading=fetchHeadingWithIndex(filename)
    file=open(filename)
    line=file.readline()
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
    file.close()
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
    file.close()
    return isMissing

def isMissingByHeading(filename,x,headIn):
    heading=fetchHeading(filename)
    file=open(filename)
    line=file.readline()
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
    file.close()
    return  isMissing

def getMissingListbyLine(filename,lineNumber):
    heading=fetchHeading(filename)
    file = open(filename)
    line = file.readline()
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
    file.close()
    return missing,attributeCount


def getMissingListbyHeadingNumber(filename,headingnumber):
   heading=fetchHeading(filename)
   return getMissingListbyHeadingName(filename,heading[headingnumber])

def getMissingListbyHeadingName(filename,headingname):
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
            if ((linewords[i] == "" or linewords[i] == "?") and heading[i]== headingname) :
                missing.append((heading[i],linecount))
                missinglinecount=missinglinecount+1
        line = file.readline()
        linecount = linecount + 1
    file.close()
    return missing,missinglinecount



# print "Checking iq/sj dataset"
# filename="../dataset/dengue_train_iq.csv"
# # filename="../dataset/dengue_train_sj.csv"
# missing,missingcount = getMissing(filename)
# print missing
# print missingcount
# print "Checking isMissing"
# print isMissing(filename,45,11)
# print "Checking isMissingByHeading"
# print isMissingByHeading(filename,21,'station_precip_mm')
# print "Checking getMissingByLine"
# missing,attributecount = getMissingListbyLine(filename,234)
# print missing
# print attributecount
# print "Checking getMissingListbyHeadingNumber"
# missing,missingcount = getMissingListbyHeadingNumber(filename,19)
# print missing
# print missingcount
# print "Checking getMissingListbyHeadingName"
# missing,missingcount = getMissingListbyHeadingName(filename,'station_precip_mm')
# print missing
# print missingcount
