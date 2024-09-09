import random

search_results = ['kim kardashian', 'neymar', 'australia', 'harry kane']
dic = {
    search_results[0]: 100000,
    search_results[1]: 2000000,
    search_results[2]: 3000000,
    search_results[3]: 4000000,
}
game_over = False
score = 0


while not game_over:

    compare1 = random.choice(search_results)
    compare2 = random.choice(search_results)
    if compare1 == compare2:
        compare2 = random.choice(search_results)

    ask = str(input(f'Higher or Lower? {compare1} or {compare2}: ')).lower()

    if ask in dic.keys():
        if dic[ask] > dic[compare1] or dic[ask] > dic[compare2]:
            print('Correct, Higher!')
            score += 1
        else:
            print('Incorrect, Lower!')
            game_over = True

    while game_over:

        print(f' you\'re score ended at: {score}')
        break






