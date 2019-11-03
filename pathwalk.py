#import section
import os,sys

#function section
def printtree(path):
    detailssubfolder = {}
    detailsfile = {}
    detailsfilecount = {}
    detailsfoldercount = {}
    for foldername,subfoldername,filename in os.walk(path):
        print ("\n\nFolder : \n" + foldername +  "\nSubfolder: \n" +  str(subfoldername))
        print ("\nfile: \n" +  str(filename))
        print ("\nSubfolder count: \n" + str(len(subfoldername)) + "\nfilecount: \n" +  str(len(filename)))
        detailssubfolder[foldername] = subfoldername
        detailsfile[foldername] = filename
        detailsfilecount[foldername] = len(filename)
        detailsfoldercount[foldername] = len(subfoldername)
    return detailssubfolder,detailsfile,detailsfilecount,detailsfoldercount
#input section
if len(sys.argv) > 1:
	path = ' '.join(sys.argv[1:])
# I used system module to accept arguments and arguments is stored in list by sys.argv where the zero index represent the python file name thereby 
# joining from index 1 using join of string formating 
else:
	path = input("enter the path with escape sequence you want files and folder tree : ")

# required variable in empty
gdetailssubfolder = {}
gdetailsfile = {}
gdetailsfilecount = {}
gdetailsfoldercount = {}
#code
gdetailssubfolder,gdetailsfile,gdetailsfilecount,gdetailsfoldercount = printtree(path)

print("\n#######################SUMMARY#################################\n\n#######################count dict:#######################\n")
print("#######################FILE Count####################### : \n")
print(gdetailsfilecount)
print ("\n#######################Folder count #######################: \n")
print(gdetailsfoldercount)

print("\n#######################Subfolder dict#######################\n")
print (gdetailssubfolder)
print("\n\n#######################file dict#######################\n")
print (gdetailsfile)
input("Press enter to exit...")

# NOTE you can use it from cmd run using     -->  pathwalk.py c:\folder1\folder2
