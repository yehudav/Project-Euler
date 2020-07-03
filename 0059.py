let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']


def dec(path):
    file = open(path, "r")
    nums = []
    for line in file:
        nums += list(map(int, line.split(",")))
    for i in let:
        for j in let:
            for k in let:
                key = []
                for p in range(len(nums) // 3 + 1):
                    key.append(i)
                    key.append(j)# todo refactor
                    key.append(k)
                if len(nums) % 3 == 1:
                    key.append(i)
                if len(nums) % 3 == 2:
                    key.append(i)
                    key.append(j)

                msg = ""
                for e in range(len(nums)):
                    msg += chr(nums[e] ^ ord(key[e]))
                if "the " in msg:
                    print("---------------------------------------------------\n\n" + msg + "\n"
                          + i + "," + j + "," + k + "\n")
    key = []
    for p in range(len(nums) // 3 + 1):
        key.append("g")
        key.append("o")
        key.append("d")
    if len(nums) % 3 == 1:
        key.append("g")
    if len(nums) % 3 == 2:
        key.append("g")
        key.append("o")

    sum = 0
    for e in range(len(nums)):
        sum += nums[e] ^ ord(key[e])
    print(sum)


dec("C:\\Users\\YehudaVaknin\\PycharmProjects\\untitled1\\file")
