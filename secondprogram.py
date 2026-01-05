
#         #strings and conditions

# str1 = "Rakesh"
# str2 = "Chauhan"
# final_str = str1 + " " + str2
# print(final_str)

# len1 = len(str1)
# len2 = len(str2)
# final_str2 = len1+len2
# print(len1)
# print(len2)
# print(final_str2)


#        # indexing starts with whole number in python

# str = "Rakesh chauhan"
# print(str[5])

#         #Sliceing in python for ML learning

# str = "Rakesh chavan"
# print(str[0:6])

# print(str[7:15])
# print(str[0:7])


# str2 = "apple"
# print(str2[-8:-2])

#         str function

# str = "i am a hacker"
# print(str.endswith("er"))
# str = str.capitalize()
# print(str.capitalize())
# print(str)

# print(str.find("h"))
# print(str.find("a"))
# print(str.replace("a","o"))
# print(str.count("a"))

# name = "Rakesh"
# a = input("enter your name :")
# print("my name is:", len(name))

# str = "heei$bbwhb4SS$WUSH$"
# print(str.find("$"))

#         Conditional statement

# age = 15
# if(age >= 18):
#     print("universal rights")

# else:
#     print("not having universal rights")



# light = "yellow"

# if(light == "red"):
#     print("stop")

# elif(light == "green"):
#     print("go")

# elif(light == "yellow"):
#     print("go slow")

# else:
#     print('light is broken')




# marks = int(input(" enter student marks : "))

# if(marks >= 90):
#     print("A grade")

# elif(marks >= 80 and marks < 90):
#     print("B grade")


# elif(marks >= 70 and marks < 80):
#     print("C grade")

# elif(marks >= 33 and marks < 70):
#     print("D grade")


#         #nesting

# age2 = 76

# if(age2 >= 18):
#     if(age2 >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
    
# else:
#     print("not eligable")



                        # LIST AND TRUPLE IN PYTHON


# marks = [10, 22.3, 83.3, 72.4, 93.9]
# print(marks[0])

# print(marks)

# print(type(marks))


# student = ["Rakesh", 73.4, "Grade b"]
# print(student[0])


# student[0] = "Ayush"
# print(student)

#             #List Method

# list = [1, 2, 3,]
# list.append(4)
# print(list)

# list.sort(reverse=True)
# print(list)

# list.sort()

# print(list)

# list.insert(1,10)
# print(list)


# list.remove(1)
# print(list)


# ##tuples

# tup = (12, 2, 22, 32, 23)
# print(type(tup))

# print(tup[1])

# print(tup.index(22))


# movies = []

# mov1 = input("enter 1st movie: ")
# mov2 = input('enter 2nd movie: ')
# mov3 = input("enter 3rd movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


list = [1,3, 4]
copy_list = list.copy()

copy_list.reverse()

if(copy_list == list):
    print("palindrom")
else:
    print("not palindrom")    


grade = ["A", "B", "A", "D"]    
grade.sort()
print(grade)

