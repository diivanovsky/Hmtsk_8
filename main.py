# def common(ln):
#     n_l = {}
#     for word in ln:
#         if word in n_l:
#             n_l[word] += 1
#         else:
#             n_l[word] = 1
#     max_word = max(n_l, key=n_l.get)
#     return f"Word '{max_word}' is repeated '{n_l[max_word]}' times \n"
#
#
# # Task 1
# with open("text.txt", "r") as t:
#     text = t.readline()
#     lines = list(map(lambda x: x.lower().split(), text))
#     red = []
#     for i in lines:
#         red.append(list(map(lambda x: x.replace(".", "").replace(",", ""), i)))
#     s_dict = {}
#     for line in red:
#         with open('output.txt', 'a') as f:
#              f.write(common(line))
# # Task 2
#
# with open("under_red.txt", "r") as t:
#     comp_txt = text = t.readline()
# with open("stop_words.txt", "r") as t:
#     s_words = t.readline().split()
# text1 = []
# for i in s_words:
#     text = text.lower().replace(i.lower(), '*' * len(i))
# for i in range(len(text) - 1):
#     if text[i] == "*":
#         text1.append(text[i])
#     else:
#         text1.append(comp_txt[i])
# final = "".join(map(str, text1))
# print(final)

# Task 3 hyinja

# with open('students.txt', 'r') as f:
#     for line in f:
#         student_info = line.strip().split()
#         if int(student_info[2]) < 3:
#             print(student_info[0], student_info[1])

# Task 4
# with open("some_str.txt", "r") as f:
#     st = f.read()
# res = ""
# for char in st:
#     if not char.isdigit():
#         res += " "
#     else:
#         res += char
# data = res.split()
# print(data)
# sum_l = sum(map(int, data))
# print(sum_l)

# Task 5
def encode_en(text):
    alph = "abcdefghijklmnopqrstuvwxyzabc"
    alph_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZABC"
    result = ""
    for i in range(len(text)):
        for j in text[i]:
            if j == " ":
                result += " "
            if j == "/n":
                result += j
            if j.isupper():
                letter = alph_b.find(j)
                code = letter + (i + 1)
                result += alph_b[code]
            else:
                letter = alph.find(j)
                code = letter + (i + 1)
                result += alph[code]
    return result


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