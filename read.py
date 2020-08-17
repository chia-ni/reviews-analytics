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

#篩選資料
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於一百字')


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')

#快寫法
good = [d for d in data if 'good' in d]

bad = ['bad' in d for d in data]

#bad = []
#for d in data:
#	bad.append('bad' in d)


#文字記數
wc = {} #word_count dictionary
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本查詢功能!')