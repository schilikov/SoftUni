# Compare sums of both positive and negative numbers
nums = [int(x) for x in input().split()]
positive_sum = sum(filter(lambda x: x > 0, nums))
negative_sum = sum(filter(lambda x: x < 0, nums))

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

# Test Inputs
# 1 2 -3 -4 65 -98 12 57 -84
# 1 2 3