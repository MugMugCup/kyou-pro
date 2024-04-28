from collections import defaultdict

# 入力
S = list(input())
alph_cnt = defaultdict(int)
for i in range(len(S)):
    alph_cnt[S[i]] += 1
# print(alph_cnt)

# 実装
ans = 0
use_yet = len(S)
same_alph = False
for key in alph_cnt.keys():
    use_yet -= alph_cnt[key]
    ans += use_yet * alph_cnt[key]
    # 2 つ以上ある時、
    if 2 <= alph_cnt[key] and same_alph == False:
        ans += 1
        same_alph = True
    
# 出力
print(ans)

# 4/28 一発 AC !!