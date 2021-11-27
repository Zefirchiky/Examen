a = ['pizza', 'falafel', 'Napoleon cake']
b = a
b.append(input("Мороженое нарав. вашему другу:"))
print("Вам нравятся:")
for i in a:
    print(i)
print("Вашему другу нравятся:")
for i in b:
    print(i)
