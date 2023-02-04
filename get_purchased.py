from operator import itemgetter

[[9, 4, 'afsd'], [0, 1, 'f'], [4, 2, 't']]
# Python3 code to demonstrate working
def getValue(string, type):
   # getting index of substrings
   str1 = '<' + type + '>'
   str2 = '</' + type + '>'

   idx1 = string.index(str1)
   idx2 = string.index(str2)

   result = ''

   if idx1 > 0:
      # getting elements in between
      for idx in range(idx1 + len(str1), idx2):
         result = result + string[idx]
   
   # return result
   return result


# Define a filename.
filename = "data/iTunes_2023-01-03_v2.xml"
#filename = "data/iTunes_test.xml"
fw = open("data/iTunes_purchased.txt", "w")

song = ["","","",False]
purchased = []

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as fr:
    content = fr.readlines()

for line in content:
   if line[0:6] == '<dict>':
      song = ["","","",False]
   elif line[0:7] == '</dict>':
      if song[3]:
         purchased.append(song)
         # print('{0: <50} | {1} ({2})'.format(song[0][0:49], song[1], song[2]))
   else:
      if getValue(line,'key') == 'Name':
         song[0] = getValue(line,'string')
      elif getValue(line,'key') == 'Artist':
         song[1] = getValue(line,'string')
      if getValue(line,'key') == 'Album':
         song[2] = getValue(line,'string')
      elif line.find("<key>Purchased</key><true/>") > 0:
         song[3] = True

# sort by artist
purchased = sorted(purchased, key=itemgetter(1))

for item in purchased:
   print('{0: <50} | {1: <30} ({2})'.format(item[0][0:49], item[1][0:30], item[2]))
   fw.write('{0: <50} | {1: <30} ({2})\n'.format(item[0][0:49], item[1][0:30], item[2]))

fr.close()
fw.close()
