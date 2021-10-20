from collections import deque

jobs = deque([int(x) for x in input().split(", ")])
job_idx = int(input())

cycles = 0
for idx in range(len(jobs)):
    if jobs[job_idx] >= jobs[idx]:
        cycles += jobs[idx]

print(cycles)

# Test Inputs

# 3, 1, 10, 1, 2
# 0

# 4, 10, 10, 6, 2, 99
# 2