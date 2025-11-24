#1-misol
matn = "Salom dunyo"
print(f"matn: {matn}")

soni = 0
for i in range(len(matn)):
    if matn[i] == ' ':
        soni += 1

#2-misol
text = "o'zbekiston  respublikasi"
print(f"text: {text}")

soni = 0
for i in range(len(text)):
    if text[i] == ' ':
        print(f"Probellar soni: {soni}")

#3-misol
text = "123 456 789"
print(f"text: {text}")

soni = 0
for i in range(len(text)):
    if text[i] == ' ':
        soni += 1

print(f"Probellar soni: {soni}")

#4-misol
text = ""
print(f"text: {text}")

soni = 0
for i in range(len(text)):
    if text[i] == ' ':
        soni += 1

print(f"Probellar soni; {soni}")

#5-misol
text = "      "
print(f"text: {text}")

soni = 0
for i in range(len(text)):
    if text[i] == ' ':
        soni += 1

print(f'Probellar soni: {soni}')
