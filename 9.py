a = [1,5,4,7,2,4]
b = ["key1","key2","key3","key4","key5","key6"]
n = int(input("Введие степень:"))
dict = zip(a,b)
for i,c in dict:
    key = i**n
    print(f"Я знаю твой ключ - {key}, его значение - {c}")
    
