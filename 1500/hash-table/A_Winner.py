
t = int(input())
history_names = []
history_scores = []
final_scores = {}
 
for i in range(t):
    n, m = input().split()
    m = int(m)
    history_names.append(n)
    history_scores.append(m)
    
    if n in final_scores:
        final_scores[n] += m
    else:
        final_scores[n] = m
 
max_score = -10**9
for name in final_scores:
    if final_scores[name] > max_score:
        max_score = final_scores[name]
 
current_scores = {}
for i in range(t):
    n = history_names[i]
    m = history_scores[i]
    
    if n in current_scores:
        current_scores[n] += m
    else:
        current_scores[n] = m
        
    if final_scores[n] == max_score and current_scores[n] >= max_score:
        print(n)
        break