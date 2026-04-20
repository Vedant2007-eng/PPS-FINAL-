str = input()

cnt = 0
for i in str :
	if i in ['A','E','I','O','U','a','e','i','o','u']:
		cnt = cnt + 1
print(cnt)
