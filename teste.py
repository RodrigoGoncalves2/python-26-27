nums = [1,2,3,4,1,2,3,4]

primeira = nums.index(2)
print(primeira)
ocurrencia = primeira
segunda = nums.index(2, primeira + 1)
print(segunda)
terceira = nums.index(2, segunda + 1)
print(terceira)

if terceira == '':
    ocurrencia = 2


print(ocurrencia)