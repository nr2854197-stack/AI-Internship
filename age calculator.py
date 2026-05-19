name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
age = current_year - birth_year

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print("Name:", name)
print("Age:", age)
print("Status:", status)