def test(lst):
    result={}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1,"Jean castro","V"],[2,"lula Powell","V"],[3,"Brain Howell","VI"],
            [4,"Lynne Foster","VI"],[5,"Zachary Seamon","VII"]]

print("Original list of students is:-")
print(students)
print("Converted list to a dictionary:-")
print(test(students))