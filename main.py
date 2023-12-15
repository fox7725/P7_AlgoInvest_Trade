def maximiser_benefices(actions, budget):
    n = len(actions)
    tableau = [[0 for x in range(budget + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        cout, profit_percent = actions[i-1]
        profit = cout * profit_percent / 100
        for j in range(1, budget + 1):
            if cout <= j:
                tableau[i][j] = max(profit + tableau[i-1][j-cout], tableau[i-1][j])
            else:
                tableau[i][j] = tableau[i-1][j]

    # Reconstitution du choix des actions
    res = tableau[n][budget]
    w = budget
    actions_choisies = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == tableau[i-1][w]:
            continue
        else:
            actions_choisies.append(i)
            res -= actions[i-1][1] * actions[i-1][0] / 100
            w -= actions[i-1][0]

    return actions_choisies

# Exemple d'utilisation
actions = [
    (20, 5), (30, 10), (50, 15), (70, 20), (60, 17),
    (80, 25), (22, 7), (26, 11), (48, 13), (34, 27),
    (42, 17), (110, 9), (38, 23), (14, 1), (18, 3),
    (8, 8), (4, 12), (10, 14), (24, 21), (114, 18)
]

budget = 500
actions_optimales = maximiser_benefices(actions, budget)
print("Actions à acheter :", actions_optimales)

