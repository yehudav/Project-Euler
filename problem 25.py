

f11 = 89
f12 = 144
counter = 12
fn_minus_2 = f11
fn_minus_1 = f12


while len(str(fn_minus_1)) < 1000:
    temp = fn_minus_2
    fn_minus_2 = fn_minus_1
    fn_minus_1 += temp
    counter += 1

print(counter)



