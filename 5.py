a = ["user1","user2","user3","user4","user5"]
b = []
print("Пользователи зарегистрировались на сайте")
for i in a[:]:
    print(f"{i} не проверен")
    b.append(a.pop(0))
print("Пользователи прошли проверку")
for i in b:
    print(f"{i} проверен")
