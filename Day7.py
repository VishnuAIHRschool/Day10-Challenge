# HR Employee Skills Data

# Employees having Python skill
python_team = {"Vishnu", "Asvika", "Karthika", "Ravi"}

# Employees having SQL skill
sql_team = {"Karthika", "Ravi", "Arun", "Priya"}

# Union - Employees having either Python or SQL
all_employees = python_team.union(sql_team)
print("All Skilled Employees:")
print(all_employees)

# Intersection - Employees having both skills
common_employees = python_team.intersection(sql_team)
print("\nEmployees having both Python and SQL:")
print(common_employees)

# Difference - Python only employees
python_only = python_team.difference(sql_team)
print("\nPython Only Employees:")
print(python_only)

# Add a new employee
python_team.add("Rahul")
print("\nAfter Adding Rahul:")
print(python_team)

# Remove an employee
python_team.remove("Ravi")
print("\nAfter Removing Ravi:")
print(python_team)

# Frozen Set (cannot be modified)
permanent_employees = frozenset({"Vishnu", "Asvika", "Karthika"})
print("\nPermanent Employees:")
print(permanent_employees)

# Function to display employees
def display_employees(employee_set):
    print("\nEmployee List:")
    for employee in employee_set:
        print(employee)

# Calling function
display_employees(all_employees)
