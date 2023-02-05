import re
from re import sub

def camel_case(word):
   splitWord = word.split()

   camelWord = splitWord[0].lower()

   for x in range(1, len(splitWord)): 
      camelWord = camelWord + splitWord[x]

   return camelWord   


def getKeyValue(keyString):
   startpos = keyString.find('<key>') + 5
   endpos = keyString.find('</key>')

   return camel_case(keyString[startpos:endpos])


def getInteger(intString):
   startpos = intString.find('<integer>') + 9
   endpos = intString.find('</integer>')

   return intString[startpos:endpos]


def getString(strString):
   startpos = strString.find('<string>') + 8
   endpos = strString.find('</string>')

   return strString[startpos:endpos]


def getDate(dteString):
   startpos = dteString.find('<date>') + 6
   endpos = dteString.find('</date>')

   return dteString[startpos:endpos]


def checkSongStart(inString):
   if inString.startswith('<key') and inString.endswith('</key>'):
      return True
   else:
      return False   


def processElement(inString):
   print(inString)

   # Get key data string
   # get key value
   keyval = getKeyValue(inString)

   if inString.find('<integer>') != -1:
      value = getInteger(inString)
   elif inString.find('<string>') != -1:
      value = getString(inString)    
   elif inString.find('<date>') != -1:
      value = getDate(inString)    
   elif inString.find('<true/>') != -1:
      value = "true"
   elif inString.find('<false/>') != -1:
      value = "false"
   else:
      value = "notfound"   
      

   print(keyval + ' : ' + value)


# variables
startReading = False
startSong = False
xmlcntr = 0

xmlfile = open("iTunes_short.xml", "r")

xmlline = xmlfile.readline()

while xmlline:
   #print(xmlline)
   xmlcntr += 1

   if not startReading:
      # Get to point of starting to read
      if xmlline.find('<key>Tracks</key>') != -1:
         startReading = True

         # read the next line '<dict>'
         xmlline = xmlfile.readline()

         # add curly brace start
   elif not startSong:
      if checkSongStart(xmlline):
         startSong = True

         # read the next line '<dict>'
         xmlline = xmlfile.readline()
   else:
      if xmlline == '</dict>':
         startSong = False

         # add curly brace end + ,
      else:
         # process the line
         processElement(xmlline)

         # add json line 
         # and another line to add 
         # one more for dexterity    

   # read next line
   xmlline = xmlfile.readline().strip()

xmlfile.close()
