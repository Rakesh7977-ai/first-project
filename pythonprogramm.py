info = {
    "name" : "Rakesh",
    "age" : 16,
    "learning" : "coding",
    "is_adult" : True,
    "height_cm" : 170,
    "subjects" : ["maths", "science", "english"],
    "topics" : ("variables", "loops", "functions"),
    "address" : {
        "street" : "123 Main St",
        "city" : "New York",
        "zip" : "10001",
    }

}

print(info['name'])
print(info["height_cm"])
print(info['subjects'][1])


info["name"] = 'Rakesh chavan'
print(info["name"])

