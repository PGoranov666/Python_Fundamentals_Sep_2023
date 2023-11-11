strings = input().split()
# result = ""
#
# for word in strings:
#     length = len(word)
#     result += word * length
# print(result)
result = [txt * len(txt) for txt in strings]
print("".join(result))
