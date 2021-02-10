n, l = map(int, input().split())
sinks = list(map(int, input().split()))
sinks.sort()

cnt = 0
tape = 0
for sink in sinks:
    if tape < sink:
        tape = sink + l - 1
        cnt += 1
    else:
        continue

print(cnt)
