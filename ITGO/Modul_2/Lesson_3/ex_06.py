#sum = 0

#for _el in range(1, 26):  
    #if sum >= 100: #ми хочемо припинити програму, коли сумма досягне сотні
     #   break
    #sum += 5
#print(sum)

# Два цикла

sum = 0

for i in range (1, 2):
    print('----')
    for _el in range(1, 26):
        if sum >= 100:  # ми хочемо припинити програму, коли сумма досягне сотні
            break
        sum += 5
    print(i)

print(sum)
