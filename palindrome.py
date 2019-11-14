num = int(input("Enter a number: "))
rnum = 0
temp = num
while temp > 0:
    rnum = rnum*10 + (temp%10)
    temp = temp//10
if num == rnum:
    print(num,"is a palindrome.")
else:
    print(num,"is not a palindrome.")
