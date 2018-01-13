"""     problem 21        """


import itertools
permutation_list = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

per = ""

for i in permutation_list[999999]:
    per += str(i)

print(per)