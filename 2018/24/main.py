from itertools import count


def parse_input(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    team = None
    groups = []
    group = 0
    for line in lines:
        if not line:
            continue
        if line.startswith('Immune System'):
            team = 0
            group = 1
            continue
        elif line.startswith('Infection'):
            team = 1
            group = 1
            continue

        ls = line.split()
        units = int(ls[0])
        hp = int(ls[4])
        initiative = int(ls[-1])
        ap = int(ls[-6])
        a = ls[-5]

        w = []
        if 'weak to' in line:
            ls = line.split('weak to ')[-1]
            ls = ls.split(')')[0]
            ls = ls.split(';')[0]
            w = ls.split(', ')

        i = []
        if 'immune to' in line:
            ls = line.split('immune to ')[-1]
            ls = ls.split(')')[0]
            ls = ls.split(';')[0]
            i = ls.split(', ')

        groups.append([team, group, units, hp, initiative, ap, a, tuple(w), tuple(i)])
        group += 1

    return groups


def damage(attacker, defender):
    if attacker[-3] in defender[-1]:
        return 0
    power = attacker[2] * attacker[-4]
    if attacker[-3] in defender[-2]:
        return power * 2
    return power


def task1(fn):
    groups = parse_input(fn)

    while len({team for team, *_ in groups}) > 1:

        # target selection

        # secondary: initiative
        groups.sort(key=lambda x: x[4], reverse=True)
        # primary: effective power
        groups.sort(key=lambda x: x[2] * x[-4], reverse=True)

        attacked = set()
        attack_defend_map = dict()
        for team, group, units, hp, initiative, ap, a, wk, im in groups:
            potential_targets = list(filter(lambda x: x[0] != team and tuple(x) not in attacked, groups))

            # damage, effective power, initiative
            potential_targets.sort(key=lambda x: x[4], reverse=True)
            potential_targets.sort(key=lambda x: x[2] * x[-4], reverse=True)
            potential_targets.sort(key=lambda x: damage([team, group, units, hp, initiative, ap, a, wk, im], x), reverse=True)

            if potential_targets:
                attacked.add(tuple(potential_targets[0]))
                attack_defend_map[team, group] = potential_targets[0][:2]

        # attacking
        # by decreasing initiative
        groups.sort(key=lambda x: x[4], reverse=True)
        for attacker in groups:
            # attacking?
            if tuple(attacker[:2]) not in attack_defend_map:
                continue
            # dead?
            if attacker[2] <= 0:
                continue
            # who?
            defender_id = attack_defend_map[tuple(attacker[:2])]
            defender = [d for d in groups if d[:2] == defender_id][0]
            defender_idx = groups.index(defender)
            # attack
            dmg = damage(attacker, defender)
            kills = dmg // defender[3]
            #print(f'{attacker[:2]} attacks {defender[:2]} dealing {dmg}, killing {kills}')
            defender[2] -= kills
            groups[defender_idx] = defender[:]

        groups = [g for g in groups if g[2] > 0]
        #print()
        #for g in groups:
        #    print(g)

    return sum(map(lambda x: x[2], groups))


def task2(fn):

    for boost in count():
        print(f'Boosting: {boost}')

        groups = parse_input(fn)
        for g in groups:
            if g[0] == 0:
                g[5] += boost

        while len({team for team, *_ in groups}) > 1:

            # stalemate detection:
            groups_old = [g[:] for g in groups]

            # target selection

            # secondary: initiative
            groups.sort(key=lambda x: x[4], reverse=True)
            # primary: effective power
            groups.sort(key=lambda x: x[2] * x[-4], reverse=True)

            attacked = set()
            attack_defend_map = dict()
            for team, group, units, hp, initiative, ap, a, wk, im in groups:
                potential_targets = list(filter(lambda x: x[0] != team and tuple(x) not in attacked, groups))

                # damage, effective power, initiative
                potential_targets.sort(key=lambda x: x[4], reverse=True)
                potential_targets.sort(key=lambda x: x[2] * x[-4], reverse=True)
                potential_targets.sort(key=lambda x: damage([team, group, units, hp, initiative, ap, a, wk, im], x), reverse=True)

                if potential_targets and damage([team, group, units, hp, initiative, ap, a, wk, im], potential_targets[0]) > 0:
                    attacked.add(tuple(potential_targets[0]))
                    attack_defend_map[team, group] = potential_targets[0][:2]

            # attacking
            # by decreasing initiative
            groups.sort(key=lambda x: x[4], reverse=True)
            for attacker in groups:
                # attacking?
                if tuple(attacker[:2]) not in attack_defend_map:
                    continue
                # dead?
                if attacker[2] <= 0:
                    continue
                # who?
                defender_id = attack_defend_map[tuple(attacker[:2])]
                defender = [d for d in groups if d[:2] == defender_id][0]
                defender_idx = groups.index(defender)
                # attack
                dmg = damage(attacker, defender)
                kills = dmg // defender[3]
                #print(f'{attacker[:2]} attacks {defender[:2]} dealing {dmg}, killing {kills}')
                defender[2] -= kills
                groups[defender_idx] = defender[:]

            groups = [g for g in groups if g[2] > 0]
            #print()
            #for g in groups:
            #    print(g)

            groups.sort()
            groups_old.sort()
            if groups == groups_old:
                print('Stalemate!')
                break

        immune_groups = list(filter(lambda x: x[0] == 0, groups))
        infection_groups = list(filter(lambda x: x[0] == 1, groups))

        immune_units = sum(x[2] for x in immune_groups)
        infection_units = sum(x[2] for x in infection_groups)

        print(f'{immune_units=} {infection_units=}')

        if immune_units > 0 and infection_units == 0:
            return immune_units



assert task1('test_input.txt') == 5216
print(task1('input.txt'))

assert task2('test_input.txt') == 51
print(task2('input.txt'))
