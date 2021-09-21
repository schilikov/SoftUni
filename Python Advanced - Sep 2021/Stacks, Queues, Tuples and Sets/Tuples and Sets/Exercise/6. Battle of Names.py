# we are using ord() with sets in this program
n = int(input())
names_even = set()
names_odd = set()

for row in range(1, n + 1):
    name = input()
    sum_of_name = sum([ord(letter) for letter in name]) // row
    if sum_of_name % 2 == 0:
        names_even.add(sum_of_name)
    else:
        names_odd.add(sum_of_name)

even_sum = sum(names_even)
odd_sum = sum(names_odd)

result = set()
if even_sum == odd_sum:
    result = names_odd.union(names_even)
elif odd_sum > even_sum:
    result = names_odd.difference(names_even)
elif even_sum > odd_sum:
    result = names_odd.symmetric_difference(names_even)

print(', '.join([str(x) for x in result]))