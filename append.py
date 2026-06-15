# # n=[1,2,3,4]
# # n.append(n[-1]+n[-2])
# # print(n)

# print(max("baLl"))
# print(min("bAall"))

# print(max([10,4,5]))
# print(min([10,30,4,6,7]))

# print(bool("1"))

l=[10,20,30]
ls=[10,20,30]
if l is ls:
    print("list are same")
else:
    print("List are different ")

if l[0] is ls[0]:
    print(id(l[0]),'Both came from the same location')
else:
    print(id(l[0]),id(ls[0]),'Both came from the different location')