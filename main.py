import json
import csv

def common(ln):
    n_l = {}
    for word in ln:
        if word in n_l:
            n_l[word] += 1
        else:
            n_l[word] = 1
    max_word = max(n_l, key=n_l.get)
    return f"Word '{max_word}' is repeated '{n_l[max_word]}' times \n"


# Task 1
with open("text.txt", "r") as t:
    text = t.readline()
    lines = list(map(lambda x: x.lower().split(), text))
    red = []
    for i in lines:
        red.append(list(map(lambda x: x.replace(".", "").replace(",", ""), i)))
    s_dict = {}
    for line in red:
        with open('output.txt', 'a') as f:
             f.write(common(line))

# Task 2
with open("under_red.txt", "r") as t:
    comp_txt = text = t.readline()
with open("stop_words.txt", "r") as t:
    s_words = t.readline().split()
text1 = []
for i in s_words:
    text = text.lower().replace(i.lower(), '*' * len(i))
for i in range(len(text) - 1):
    if text[i] == "*":
        text1.append(text[i])
    else:
        text1.append(comp_txt[i])
final = "".join(map(str, text1))
print(final)

# Task 3
with open('students.txt', 'r') as f:
    text = f.readlines()
    print(text)
    for line in text:
        student_info = line.strip().split()
        if int(student_info[2]) < 3:
            print(f"Next student is stupid: {student_info[0]} {student_info[1]}! Mark is {student_info[2]}")

# Task 4
with open("some_str.txt", "r") as f:
    st = f.read()
res = ""
for char in st:
    if not char.isdigit():
        res += " "
    else:
        res += char
data = res.split()
print(data)
sum_l = sum(map(int, data))
print(sum_l)

# Task 5
with open("some_str.txt", "r") as f:
    text = f.readlines()
alph = "abcdefghijklmnopqrstuvwxyzabc"
alph_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZABC"
result = ""
print(text)
for i in range(len(text)):
    for j in text[i]:
        if j == " ":
            result += " "
        if j.isupper():
            letter = alph_b.find(j)
            code = letter + (i + 1)
            if letter == -1:
                result += " "
            else:
                result += alph_b[code]
        else:
            letter = alph.find(j)
            code = letter + (i + 1)
            if letter == -1:
                result += " "
            else:
                result += alph[code]
    result += "\n"

print(result)

# Task 5

def add_employee_js():
    name = input("Enter employee name: ")
    birthday = input("Enter employee birthday: ")
    height = input("Enter employee height: ")
    weight = input("Enter employee weight: ")
    car = input("Has he got a car - true or false: ")
    language = input("Enter employee language: ")
    language = language.split(" ")
    new_emp =     {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": language
    }
    with open('employees.json', 'r') as jf:
        data = json.load(jf)
    with open('employees.json', 'w') as jf:
        data.append(new_emp)
        json.dump(data, jf, indent=4)
    print("Done")
    print()


def add_employee_csv():
    name = input("Enter employee name: ")
    birthday = input("Enter employee birthday: ")
    height = input("Enter employee height: ")
    weight = input("Enter employee weight: ")
    car = input("Has he got a car - true or false: ")
    language = input("Enter employee language: ")
    language = language.split(" ")
    with open('employees.csv', 'a') as csvf:
        writer = csv.writer(csvf, delimiter=",", lineterminator="\r")
        writer.writerow([name,birthday, height, weight, car, language])
    print("Done")
    print()


def tran_fj_tc():
    with open('employees.json', 'r') as jf, open('employees.csv', 'w') as csvf:
        data = json.load(jf)
        writer = csv.writer(csvf, delimiter=",", lineterminator="\r")
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow([item['name'], item['birthday'], item['height'], item['weight'], item['car'], item['languages']])
        print("Done")
        print()



def find_info():
    with open('employees.json', 'r') as jf:
        data = json.load(jf)
    find = input("Whom you'd like to find? ")
    for i in data:
        if i['name'] == find:
            print(f"Name: {i['name']}")
            print(f"birthday: {i['birthday']}")
            print(f"height: {i['height']}")
            print(f"weight: {i['weight']}")
            print(f"car: {i['car']}")
            print(f"languages: {i['languages']}")
        print(f"Employee with name '{find}' not found")
    print()

def find_lang():
    with open('employees.json', 'r') as jf:
        data = json.load(jf)
    find = input("What language do you need? ")
    for i in data:
        for j in i['languages']:
            if j == find:
                print(f"Next employee can code in this lancuage: {i['name']}")
    print()


def menu():
    print("If you want to SAVE information from the JSON file to the CSV file - press 1")
    print("If you want to ADD an employee to the JSON - press 2")
    print("If you want to ADD an employee to the CSV - press 3")
    print("If you want to FIND an employee - press 4")
    print("If you want to FIND an employee with specific LANGUAGE - press 5")
    print("To exit press 10")
    request = int(input("What do you want to do? "))
    while request != 10:
        if request == 1:
            tran_fj_tc()
            return menu()
        elif request == 2:
            add_employee_js()
            return menu()
        elif request == 3:
            add_employee_csv()
            return menu()
        elif request == 4:
            find_info()
            return menu()
        elif request == 5:
            find_lang()
            return menu()
    else:
        print("Bye")


print("Hi, this is simple program to use for")
menu()




