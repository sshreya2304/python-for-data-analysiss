students = {
    "name" : "shreya",
    "age" : 21,
    "marks" : {
        "phy" : 100,
        "chem" : 100,
        "maths" : 100
    }
}

print(students.keys())
print(list(students.keys()))
print(len(students))
print(students.values())
print(students.items())
print(students.get("name"))
students.update({"city" : "vadodara"})
print(students)
