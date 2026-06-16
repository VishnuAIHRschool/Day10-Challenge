# loops
# for loop
for i in range(0,90):
    print("Iteration:", i)  


# Two lists
names = ["Asvika", "Karthika", "Vishnu"]
ages = [20, 22, 25]

# Empty dictionary
students = {}

# Using for loop to create dictionary
for i in range(len(names)):
    students[names[i]] = ages[i]

# Display dictionary
print(students)


# Two lists
names = ["Asvika", "Karthika", "Vishnu"]
ages = [20, 22, 25]

# Empty dictionary
students = {}

# Using for loop with zip()
for name, age in zip(names, ages):
    students[name] = age

# Display dictionary
print(students)