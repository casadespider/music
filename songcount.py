# Define a filename.
filename = "data/iTunes_2023-01-03_v2.xml"

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as fr:
    content = fr.readlines()

songsRead = 0
recsWritten = 0
keyIn = 0

for line in content:
   if line[0:6] == '<dict>':
      songsRead += 1
      
   elif line[0:7] == '</dict>':
      print('KeyIn = ',str(keyIn))
      keyIn = 0
   else:   
      keyIn += 1

print('* - - - - - - - - - - - - - - - - - - - - - - - - *')
print('Songs = ' + str(songsRead))
print('* - - - - - - - - - - - - - - - - - - - - - - - - *')

fr.close()
