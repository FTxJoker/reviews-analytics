data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完畢，共有 {0} 筆資料'.format(len(data)))

sum_len = 0
for d in data:
    sum_len += len(d)
print('每筆留言平均長度為 {0} 個字元'.format(sum_len / len(data)))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有 {0} 筆留言長度小於100個字元'.format(len(new)))
print(new[0])
print(new[1])
