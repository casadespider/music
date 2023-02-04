import re

pattern = '<key>\d{4,6}</key>'
test_string = '<keys>242701</key><text>junk</text>'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	

inString = '<key>1234</key>'

if inString.startswith('<key') and inString.endswith('</key'):
   print("yup") 
else:
   print("nope")    