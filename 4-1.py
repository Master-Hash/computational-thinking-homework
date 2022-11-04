import string

lower_letter, upper_letter, digit, punctuation, other = 0, 0, 0, 0, 0
password = input()

if set(password) - set(string.ascii_letters + string.digits + string.punctuation):
    print("密码只能包含数字、字母、标点符号")
    exit()
if not 8 <= len(password) <= 16:
    print("密码长度应为8-16个字符")
    exit()

for c in password:
    if c in string.ascii_lowercase:
        lower_letter = 1
    elif c in string.ascii_uppercase:
        upper_letter = 1
    elif c in string.digits:
        digit = 1
    elif c in string.punctuation:
        punctuation = 1
    else:
        other = 1

total = sum([lower_letter, upper_letter, digit, punctuation])
if total < 2:
    print("弱")
elif total == 2:
    print("中")
elif total == 3:
    print("强")
else:
    print("极强")
