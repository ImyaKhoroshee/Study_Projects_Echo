# test = '5_1/46+3i+1/i-63-3/70:5/6+4_1/23+10i2/3i+10_1/2i*2i'

# result = ''
# list = []

# set = {'+', '-', '*', ':', 'i', '_', '/'}

# for i in range (0, len(test)):
#     if test[i] not in set:
#         result += test[i]
#     else:
#         list.append(result)
#         list.append(test[i])
#         result = ''

# list_without_spaces = [i for i in list if i]
# print(list_without_spaces)
# list2 = []

# for j in range (0, len(list_without_spaces)):
#     if list_without_spaces[j] not in set:
#         result += list_without_spaces[j]
#     else:
#         if result.isdigit():
#             list2.append(int(result))
#             list2.append(list_without_spaces[j])
#             result = ''
#         else:
#             list2.append(result)
#             list2.append(list_without_spaces[j])
#             result = ''

# list3 = []

# for i in range(len(list2)):
#     if list2[i] != '':
#         list3.append(list2[i])
# print(list3)


# list3 = [5, '_', 1, '/', 46, '+', 3, 'i', '+', 1, '/', 'i', '-', 63, '-', 3, '/', 70, ':', 5, '/', 6, '+', 4, '_', 1, '/', 23, '+', 10, 'i', 2, '/', 3, 'i', '+', 10, '_', 1, '/', 2, 'i', '*', 2, 'i']
# list4 = []
# i = 0

# while i < len(list3):

#     if list3[i].isdigit() and list3[i+1] == '_':
#         list4.append(list3[i]*list3[i+4]+list3[i+2])
#         i+=5
#     else:
#         list4.append(list[i])
#         i+=1

# print(list4)


# test = '5_1/46+3i+1/i-63-3/70:5/6+4_1/23+10i2/3i+10_1/2i*2i'
# print(f'Оригинал {test}')