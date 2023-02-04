# Define a filename.
filename = "data/iTunes_2023-01-03_v2.xml"

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as fr:
    content = fr.readlines()

songsRead = 0
track = ''
name = ''
artist = ''
album = ''
purchased = False
purchaseCnt = 0

for line in content:
   if line[0:6] == '<dict>':
      songsRead += 1
      # clear for next
      name = ''
      artist = ''
      album = ''
      purchased = False
      
   elif line[0:7] == '</dict>':
      if purchased:
         purchaseCnt += 1
         print("Song: ", name, " Artist: ", artist, " Album: ", album)

   else:   
      if line.find("<key>Name</key>") > 0:
         name = line
      elif line.find("<key>Artist</key>") > 0:
         artist = line
      elif line.find("<key>Album</key>") > 0:
         album = line
      elif line.find("<key>Purchased</key><true/>") > 0: 
         purchased = True       

print('* - - - - - - - - - - - - - - - - - - - - - - - - *')
print('Songs = ' + str(songsRead))
print('Purchased = ' + str(purchaseCnt))
print('* - - - - - - - - - - - - - - - - - - - - - - - - *')

fr.close()