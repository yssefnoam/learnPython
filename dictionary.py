
def main():
    #student = {'name': "youssef noam", 'age': 23}
    student = dict(name="youssef noam", age = 23)
    print(student, type(student), id(student))
    print(student['name'])
    student['name'] = "YOUSSEF NOAM"
    print(student, type(student), id(student))
    print(student['name'])
    student.clear()

main()
