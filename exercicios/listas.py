nums = [2,5,8,11,7,9,13]

soma = sum(nums)
maior = max(nums)
menor = min(nums)
media = sum / len(nums)

# # Imprimir a lista
# print(nums) # [2,5,8,11,7,9,13]

# # Imprimir um elemento da lista
# print(nums[2]) # 8

# # Inserir um novo elemento no final da lista
# nums.append(17) # [2,5,8,11,7,9,13,17]

# # Inserir vários elementos no final da lista
# nums.extend([12,16]) # [2,5,8,11,7,9,13,17,12,16]

# # Inserir em posição específica
# nums.insert(3,29) # [2,5,8,29,11,7,9,13,17,12,16]



# # Remover o elemento do final da lista
# nums.pop() # [2,5,8,29,11,7,9,13,17,12]

# #Remover um elemento de uma posição específica da lista pelo índice
# nums.pop(2) # [2,5,29,11,7,9,13,17,12]

# #Remover um elemento de uma posição específica da lista pelo valor
# nums.remove(17) # [2,5,8,29,11,7,9,13,12]

# # Número de ekementos da lista
# total = len(nums)


# for n in nums: # Para cada elemento da minha lista faça qualquer coisa
#     if n <= 10:
#         print(n, end = " ")


# for indice in range(len(nums)):
#     if nums[indice] <= 10:
#         print(nums[indice], end = " ")