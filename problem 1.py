

def arithmetic_sequence_sum(n):
    return (n * (n+1)) / 2

multiples_of_three = 3 * arithmetic_sequence_sum(333)
multiples_of_five = 5 * arithmetic_sequence_sum(199)
multiples_of_fifteen = 15 * arithmetic_sequence_sum(66)

print(multiples_of_three + multiples_of_five - multiples_of_fifteen )