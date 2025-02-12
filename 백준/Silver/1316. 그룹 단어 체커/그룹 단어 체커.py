N = int(input())

count = 0

for _ in range(N) :
    word = input()
    unique_chars = set() # 각 문자가 중복되지 않도록 집합에 저장

    is_group_word = True

    for i, char in enumerate(word) :
        if char in unique_chars :
            if word[i - 1] != char :
                is_group_word = False
                break

        else : 
            unique_chars.add(char)

    if is_group_word :
        count += 1

print(count) 