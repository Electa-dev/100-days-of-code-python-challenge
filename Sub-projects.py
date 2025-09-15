# long version
def calculate_love_score(name1, name2):
    this_true = "true"
    this_love = "love"
    for_true = []
    for_love = []

    for letter in name1:
        if letter in this_true:
            for_true.append(letter)

        if letter in this_love:
            for_love.append(letter)

    for letter in name2:
        if letter in this_true:
            for_true.append(letter)

        if letter in this_love:
            for_love.append(letter)

    count_t = 0
    count_r = 0
    count_u = 0
    count_e = 0
    for letter in for_true:
        if letter == "t":
            count_t += 1

    for letter in for_true:
        if letter == "r":
            count_r += 1


    for letter in for_true:
        if letter == "u":
            count_u += 1


    for letter in for_true:
        if letter == "e":
            count_e += 1

    print(f"T occurs {count_t} times")
    print(f"R occurs {count_r} times")
    print(f"U occurs {count_u} times")
    print(f"E occurs {count_e} times")
    total = count_t + count_r + count_u + count_e
    print(f"Total = {total}")

    count_l = 0
    count_o = 0
    count_v = 0
    count_e1 = 0
    for letter in for_love:
        if letter == "l":
            count_l += 1

    for letter in for_love:
        if letter == "o":
            count_o += 1

    for letter in for_love:
        if letter == "v":
            count_v += 1

    for letter in for_love:
        if letter == "e":
            count_e1 += 1

    print(f"L occurs {count_l} times")
    print(f"O occurs {count_o} times")
    print(f"V occurs {count_v} times")
    print(f"E occurs {count_e1} times")
    total1 = count_l + count_o + count_v + count_e1
    print(f"Total = {total1}")

    love_score = str(total) + str(total1)
    print(f"Love Score = {love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")



# Short version
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")







