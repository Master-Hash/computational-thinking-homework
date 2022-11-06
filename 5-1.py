height, weight = eval(input())


def bmi(h: float, w: float):
    return w / h**2


b = bmi(height, weight)

c = "偏瘦" if b < 18.5 else "正常" if b < 24 else "偏胖" if b < 28 else "肥胖"

print(f"您的BMI为：{b:.2f}，{c}")
