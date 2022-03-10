def sort(num):
    for i in range(5):
        minP = i
        for j in range(i, 6):
            if num[j] < num[minP]:
                minP = j

        num[i], num[minP] = num[minP], num[i]

        # def reversemkc(num):
        #     num.reverse()
        #     return num
        #print(num)


num = [5, 3, 8, 6, 7, 2]
sort(num)
print(num)