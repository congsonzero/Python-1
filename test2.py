ple = [input().split() for i in range(int(input()))]
print(*map(str, sorted(ple, key=lambda x: x[2])))