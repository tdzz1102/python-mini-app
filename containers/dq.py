from collections import deque

dq = deque()

dq.append('luzao')

dq += ['carol', 'bella'] 
dq.extend(['eoe, asoul'])

dq += set(['yumo', 'youen']) 
dq += 'bbxg341' # 文字列は文字のlistに変換される
dq += '341', '340' # タプルとして扱う

# dq = ['eoe'] + dq
dq.extendleft(['taffy', 'bingtang']) # 逆順で

print(dq)

print(dq.pop())
print(dq.popleft())
