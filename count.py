from collections import Counter

phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11", "iPhone 12", "iPhone 12", "Xiaomi Mi11", "Xiaomi"]

count = Counter(phones)

print(count)
print(count['iPhone 12'])

text = "Ехал Грека через реку видит Грека в реке рак".lower().replace(' ','')
count = Counter(text)

print(count)
print(count['Грека'])