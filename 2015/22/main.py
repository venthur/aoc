def generate_next_states(human, boss, effects, mana_spent):
    # human:

    # run effects
    for i, name, turns_left in enumerate(effects):
        if name == 'shield' and turns_left == 0:
            human[1] -= 7
            effects[i][1] -= 1
        elif name == 'recharge' and turns_left > 0:
            human[3] += 101
            effects[i][1] -= 1
    effects = [e for e in effects if e[1] >= 0]

    future_states = {
        spell: [human[:], boss[:], effects[:], mana_spent]
        for spell
        in ('magic missile', 'drain', 'shield', 'poison', 'recharge')
    }

    possible_states = []
    for spell, [human, boss, effects, mana_spent] in future_states.items():
        if spell == 'magic missile' and human[3] >= 53:
            boss[0] -= 4
            human[3] -= 53
            mana_spent -= 53
            possible_states.append([human, boss, effects, mana_spent])
        elif spell == 'drain' and human[3] >= 73:
            boss[0] -= 2
            human[0] += 2
            human[3] -= 73
            mana_spent -= 73
            possible_states.append([human, boss, effects, mana_spent])
        elif spell == 'shield' and human[3] >= 113:
            human[1] += 7
            human[3] -= 113
            mana_spent -= 113
            effects.append([state, ])
            possible_states.append([human, boss, effects, mana_spent])


    # boss:

    # run effects
    for i, name, turns_left in enumerate(effects):
        if name == 'poison' and turns_left > 0:
            boss[0] -= 3
            effects[i][1] -= 1
    effects = [e for e in effects if e[1] >= 0]

    return possible_states


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    hp = int(lines[0].split()[-1])
    damage = int(lines[1].split()[-1])

    # hp, armor, damage, mana
    boss = [hp, 0, damage, 0]
    human = [50, 0, 0, 500]

    # list[[str, int]]
    effects = []
    mana_spent = 0

    min_mana = None
    states = [[human, boss, effects, mana_spent]]
    while states:
        human, boss, effects, mana_spent = states.pop()
        if boss[0] <= 0:
            if min_mana is None or mana_spent < min_mana:
                min_mana = mana_spent
            continue
        for s in generate_next_states(human, boss, effects, mana_spent):
            states.append(s)
    return min_mana


print(task1('input.txt'))
