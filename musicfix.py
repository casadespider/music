# Define a filename.
filename = "data/iTunes_2023-01-03.xml"

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as fr:
    content = fr.readlines()

fw = open("data/iTunes_2023-01-03_v2.xml", "w")

recsRead = 0
recsWritten = 0

for line in content:
   recsRead += 1

   if line[0:5] != '<key>':
      fw.write(line)

      recsWritten += 1

print('* - - - - - - - - - - - - - - - - - - - - - - - - *')
print('Records Read = ' + str(recsRead))
print('Records Written = ' + str(recsWritten))
print('* - - - - - - - - - - - - - - - - - - - - - - - - *')

fr.close()
fw.close()