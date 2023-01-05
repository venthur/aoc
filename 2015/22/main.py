from copy import deepcopy


magic_missile = dict(cost=53, damage=4, heal=0, armor=0, mana=0, duration=0)
drain = dict(cost=73, damage=2, heal=2, armor=0, mana=0, duration=0)
shield = dict(cost=113, damage=0, heal=0, armor=7, mana=0, duration=6)
poison = dict(cost=173, damage=3, heal=0, armor=0, mana=0, duration=6)
recharge = dict(cost=229, damage=0, heal=0, armor=0, mana=101, duration=5)

spells = [drain, shield, poison, recharge] # woot? correct solution but one spell missing
spells = [magic_missile, drain, shield, poison, recharge]


def apply_effects(human, boss, effects):
    human = human.copy()
    boss = boss.copy()
    effects = deepcopy(effects)

    # reset armor on each effect round, increasing it only if we have a valid
    # one again
    human['armor'] = 0
    for spell in effects:
        human['hp'] += spell['heal']
        human['mana'] += spell['mana']
        boss['hp'] -= spell['damage']
        human['armor'] += spell['armor']
        spell['duration'] -= 1

    effects = [e for e in effects if e['duration'] > 0]
    return human, boss, effects


def generate_next_states(human, boss, effects, mana_spent):
    # human:
    human, boss, effects = apply_effects(human, boss, effects)
    if boss['hp'] <= 0:
        return [[human, boss, effects, mana_spent]]

    states = []
    for spell in spells:
        # check if spell is already active
        if spell['cost'] > human['mana'] or spell['cost'] in [e['cost'] for e in effects]:
            continue

        human2 = human.copy()
        boss2 = boss.copy()
        effects2 = deepcopy(effects)

        human2['mana'] -= spell['cost']
        effects2.append(spell.copy())

        states.append([human2, boss2, effects2, mana_spent+spell['cost']])

    if len(states) == 0:
        human['hp'] = 0
        return [[human, boss, effects, mana_spent]]

    # boss
    states2 = []
    for human, boss, effects, mana_spent in states:

        human, boss, effects = apply_effects(human, boss, effects)
        if boss['hp'] <= 0:
            states2.append([human, boss, effects, mana_spent])
            continue

        human['hp'] -= min(boss['damage'] - human['armor'], 1)
        states2.append([human, boss, effects, mana_spent])

    return states2


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    hp = int(lines[0].split()[-1])
    damage = int(lines[1].split()[-1])

    boss = dict(hp=hp, armor=0, damage=damage, mana=0)
    human = dict(hp=50, armor=0, damage=0, mana=500)

    min_mana = None
    states = [[human, boss, [], 0]]
    while states:
        human, boss, effects, mana_spent = states.pop()
        print(f'{human=}\n{boss=}\n{effects=}\n{mana_spent=} {min_mana=} {len(states)=}\n')
        if human['hp'] <= 0:
            continue
        if boss['hp'] <= 0:
            if min_mana is None or mana_spent < min_mana:
                min_mana = mana_spent
            continue
        for s in generate_next_states(human, boss, effects, mana_spent):
            states.append(s)
        # prune states that are worse than our current best ones
        if min_mana is not None:
            states = [s for s in states if s[-1] < min_mana]

    return min_mana


print(task1('input.txt'))

1269
