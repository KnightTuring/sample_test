import wikipedia as wiki
import os
CONTENT_FILE="tempContentFile.txt"

'''
I needed a display like the man page. less serves that purpose.
TODO:
Please move to a better alternative; less is just temporary
'''
TERM_COMMAND_TEXT_DISP="less"




'''
TODO for inputFromUser()
-> take input as command line arguments
-> add flag; (Eg <COMMAND> -f <USER_SPECIFIED_FILE_NAME> for writing output to file)
'''
def inputFromUser():
	print "Search string?"
	userRqstString=raw_input()
	return userRqstString



'''
TODO for getContentFromWikipedia()
-> Display progress bar [=========>] since it takes time to pull from Wiki
-> Add warning after 6 seconds("This seems to be taking
more time than usual."); timeout after 10 seconds ("Connection timed out")
-> Handler for "No such page exists!"
-> Cleaner content (maybe a summary)
'''
def getContentFromWikipedia(reqString):
	reqPage=wiki.page(reqString)
	return reqPage.content





'''
TODO for writeContentToFile()
-> This is a temp file for displaying using less; please delete when user 
quits
-> Change encoding to UTF-8
'''
def writeContentToFile(reqFileContent):
	contentFile=open(CONTENT_FILE,"w+") #w+ serves all my need
	
	reqFileContent=reqFileContent.encode('utf-8') #ASCII is quite a pain; UTF-8 is the hero
	
	contentFile.write(reqFileContent)


'''
As of now, when less is called; the file can be deleted and it will
still be visible because it moves to the main memory.

TODO:
Call a seperate file that will handle the "less" implementation
It will return when user exits "less";that will be the signal to delete the file.

'''
def displayFileInTerminal(fileName):
	command=TERM_COMMAND_TEXT_DISP+" "+fileName
	os.system(command)




'''
main method
'''
if __name__=="__main__":
	userString=inputFromUser()
	wikiContent=getContentFromWikipedia(userString)
	writeContentToFile(wikiContent)
	displayFileInTerminal(CONTENT_FILE)
	#deleteFile(CONTENT_FILE)
	#exit()

'''
print "Search string?"
userRqstString=raw_input()

reqPage=wiki.page(userRqstString)


contentFile=open("tempContentFile.txt","w+")
contentFile.write(reqPage)



print (reqPage.content)
'''