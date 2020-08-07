data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data)) #看讀取檔案的進度
print('檔案讀取完畢，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於一百字')