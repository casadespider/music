import json

carDict = [
   {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
   },
   {
      "brand": "Chevy",
      "model": "Corvette",
      "year": 1967
   }
]

newCar = {
   "brand": "Honda",
   "model": "Accord",
   "year": 1998
}
carDict.append(newCar)

newCar = {
   "style": "Hatchback",
   "brand": "Honda",
   "model": "Civic",
   "cyls": 4,
   "year": 2014
}

carDict.append(newCar)

print(carDict)
# print(myDict[1]["year"])


# for x in carDict:
#    print(x["year"])   


# for x in carDict:
#    print(x["style"]) 
# 
# # Make into json string
jsonString = json.dumps(carDict, indent=4)

print(jsonString) 

text_file = open("cars.json", "w")
n = text_file.write(jsonString)
text_file.close()

