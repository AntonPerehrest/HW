# #3 Строка состоит из русских букв разных регистров. Очистить строку от прописных букв.
#
# # str3 = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# # for i in str3:
# #     for j in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
# #         if i == j:
# #             str3 = str3.replace(i, '')
# # print(str3)
#
#
# # n = a.index(20)
# # a.remove(20)
# # a.insert(n, 200)
# # print(a)
#
# #Поменять местами  1 и 3
# lis = [3,2,1]
# lis.pop(0)
# lis.insert(0,1)
# lis.pop(2)
# lis.append(3)
# print(lis)
#
# # # lis.reverse()
# # # print(lis)
# # # lis[0] = 1
# # # lis[2] = 3
# # # print(lis)
# #
# lis[0], lis[2] = lis[2], lis[0]
# # print(lis)
#
#
# # a = lis.index(1)
# # b = lis.index(3)
# # lis.remove(1)
# # lis.remove(3)
# # lis.insert(a,3)
# # lis.insert(b,1)
# # print(lis)
#
#
# lis = [5,20,15,20,25,50,20]
# for i in lis:
#     if i == 20:
#         lis.remove(20)
# print(lis)
# a = [1,2,3,4,5,6,7,8,8,88]
# print(max(a))

# lis = ['крот', 'белка', 'выхухоль', 'волк']
# a = max(lis, key=len)
# lis1 = []
# for i in lis:
#     n = len(i)
#     if n < len(a):
#         i+='_'*(len(a)-n)
#         lis1.append(i)
#     elif n == len(a):
#         lis1.append(i)
# print(lis1)

# max(   , key)
# .ljust
# .rjust

# lis = ['крот', 'белка', 'выхухоль', 'волк']
# lis1 = []
# for i in lis:
#         lis1.append(i.ljust(len(max(lis, key=len)),'_'))
# print(lis1)



s = 32423423
print(f'ecfsfsf {s}')
print(f'ecfsfsf {s}')


