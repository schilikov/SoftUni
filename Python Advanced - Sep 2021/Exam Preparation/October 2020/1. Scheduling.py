from collections import deque

jobs = deque([int(x) for x in input().split(", ")])
job_idx = int(input())

cycles = 0

for idx in range(len(jobs)):
    if jobs[job_idx] >= jobs[idx]:
        cycles += jobs[idx]

print(cycles)