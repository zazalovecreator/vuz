file = open('текст.txt', 'r', encoding='utf-8').read()
k = ''
ans = []

for i in range(len(file)):
    if file[i] != '.':
        k = k + file[i]
    else:
        k = k + file[i]
        ans.append(k)
        k = ''

ans = [s for s in ans if ',' not in s]

print(ans)

