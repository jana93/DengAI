import check
def missingMaxMinByLine(filename):
    max=0;
    maxline=0;
    file = open(filename)
    length = len(file.readline().split(",")) - 1
    minline = 2000;
    min = length
    file=open(filename)
    line=file.readline()
    linecount=0
    while line:
        x,count=check.getMissingListbyLine(filename,linecount)
        if(count > max):
            max = count
            maxline=linecount
        if(count < min):
            min = count
            minline=linecount
        linecount=linecount+1
        line=file.readline()
    file.close()
    return maxline,minline

def missingMaxMinByAttribute(filename):
    max=0;
    maxAttri=0
    file=open(filename)
    length= len(file.readline().split(","))-1
    minAttri=length
    min =2000
    for i in range(length):
        x,count=check.getMissingListbyHeadingNumber(filename,i)
        if(count > max):
            max = count
            maxAttri=i
        if(count < min):
            min = count
            minAttri=i
    file.close()
    return maxAttri,minAttri



def missingMaxMinByAttributeName(filename):
    max,min=missingMaxMinByAttribute(filename)
    heading=check.fetchHeading(filename)
    return heading[max],heading[min]


filename="../dataset/dengue_train_iq.csv"
# max,min = missingMaxMinByAttribute(filename)
# print max
# print min
# max,min = missingMaxMinByLine(filename)
# print max
# print min
# max,min = missingMaxMinByAttributeName(filename)
# print max
# print min