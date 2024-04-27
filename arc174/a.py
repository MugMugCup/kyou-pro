# 入力
N, C = map(int, input().split())
A = list(map(int, input().split()))

A_sum = [0]
for i in range(N):
    A_sum.append(A[i])
print(A_sum)

# 最大区間和を求める
ans = 0
s = 0
s_min = 0
for i in range(N):
    s += A[i]
    if s < s_min:
        s_min = s
    if ans < s - s_min:
        ans = s - s_min
    print("s: " + str(s), "s_min: " + str(s_min), "ans: " + str(ans))
    
# 出力
print(sum(A) + ans * (C - 1))