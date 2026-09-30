def digit_root(num):
    num_str = str(num)
    total = 0
    for digit in num_str:
        total += int(digit)
    if total > 9:
        return digit_root(total)
    else:
        return total

print(digit_root(4563246))