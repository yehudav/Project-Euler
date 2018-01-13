"""     problem 21        """


nums = []
diagnols_sum = 0
jump = 2

for i in range(1, 1002002):
    nums.append(i)

j = 0
jump_index = 0

while j < 1002001:
    if jump_index == 4:
        jump += 2
        jump_index = 0

    diagnols_sum += nums[j]
    jump_index += 1
    j += jump

print(diagnols_sum)



