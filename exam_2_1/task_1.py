#1 Написать программу для получения списка словарей из списков.

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# d =[]
# n = 0
# while n < len(color_name):
#     d.append({'Color_name':color_name[n], 'Color_code':color_code[n]})
#     n +=1
# print(d)

b = zip(color_name,color_code)
# print(dict(b))
print(list(b))
print(dict(b))