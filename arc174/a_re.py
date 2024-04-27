# 入力
N, C = map(int, input().split())
A = list(map(int, input().split()))

A_sum = [0]
for i in range(N):
    A_sum.append(A_sum[i] + A[i])

"""最大区間和 問題"""

# 最大区間和
ans = 0
# 累積和
s = 0
if 0 < C:
    # 累積和の最小値
    s_min = 0
    for i in range(N):
        s += A[i]
        # 累積和の最小値を更新
        if s < s_min:
            s_min = s
        # 区間和の最大値を更新
        if ans < s - s_min:
            ans = s - s_min
elif C <= 0:
    s_max = 0
    for i in range(N):
        s += A[i]
        # 累積和の最大値を更新
        if s_max < s:
            s_max = s
        # 区間和の最小値を更新
        if s - s_max < ans:
            ans = s - s_max

print(sum(A) + ans * (C - 1))

# 4/27 18:45
# WA でした...
# C < 0 の時が原因かもしれません

# 4/27 20:53
# C < 0 の時の処理を追加しました

# 4/27 20:58
# C = 0 の時の処理を追加しました
# AC !!