from collections import defaultdict

# words마다 자릿수만큼 가중치를 줘서 다 더해줌
words = []
score = defaultdict(int)
for _ in range(int(input())):
    word = input()
    words.append(word)

    for i in range(len(word)):
        score[word[i]] += 10 ** (len(word) - i)

mapping, value = {}, 9
for c, _ in sorted(score.items(), key=lambda x:x[1], reverse=True):
    mapping[c] = str(value)
    value -= 1

ans = 0
for word in words:
    number = ''
    for w in word:
        number += mapping[w]
    ans += int(number)
print(ans)
    
