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


