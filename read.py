#寫程式碼來讀取留言檔
data = []
count = 0
with open('reviews.txt', 'r') as f:
	    for line in f:
	    	data.append(line) #把line 加入data清單裡
	    	count += 1 #count = count +1
	    	if count% 1000 == 0: #如果是一千的倍數才印一次
	    	    print(len(data))
print(len(data))
print(data)
