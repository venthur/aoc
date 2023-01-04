from dataclasses import dataclass, asdict
from itertools import combinations


@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int


@dataclass
class Stats:
    hp: int
    damage: int
    armor: int
    cost: int


weapons = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
]

armor = [
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5),
]

rings = [
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3),
]


def wins(stats, enemy_stats):
    turn = 0
    while True:
        if stats.hp <= 0:
            return False
        if enemy_stats.hp <= 0:
            return True
        if turn % 2 == 0:
            enemy_stats.hp -= max(stats.damage - enemy_stats.armor, 1)
        else:
            stats.hp -= max(enemy_stats.damage - stats.armor, 1)
        turn += 1


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    enemy_stats = Stats(
        int(lines[0].split()[-1]),
        int(lines[1].split()[-1]),
        int(lines[2].split()[-1]),
        0,
    )
    stats = Stats(100, 0, 0, 0)

    mincost = None
    for weapon in weapons:
        # exactly one weapon
        sw = Stats(**asdict(stats))
        sw.damage += weapon.damage
        sw.cost += weapon.cost
        for arm in armor:
            # 0 or 1 armor
            swa = Stats(**asdict(sw))
            swa.armor += arm.armor
            swa.cost += arm.cost
            for r1, r2 in combinations(rings, 2):
                # 0, 1 or 2 rings
                swr1 = Stats(**asdict(sw))
                swr1.damage += r1.damage
                swr1.armor += r1.armor
                swr1.cost += r1.cost

                swr2 = Stats(**asdict(sw))
                swr2.damage += r2.damage
                swr2.armor += r2.armor
                swr2.cost += r2.cost

                swr12 = Stats(**asdict(sw))
                swr12.damage += r1.damage
                swr12.armor += r1.armor
                swr12.cost += r1.cost
                swr12.damage += r2.damage
                swr12.armor += r2.armor
                swr12.cost += r2.cost

                swar1 = Stats(**asdict(swa))
                swar1.damage += r1.damage
                swar1.armor += r1.armor
                swar1.cost += r1.cost

                swar2 = Stats(**asdict(swa))
                swar2.damage += r2.damage
                swar2.armor += r2.armor
                swar2.cost += r2.cost

                swar12 = Stats(**asdict(swa))
                swar12.damage += r1.damage
                swar12.armor += r1.armor
                swar12.cost += r1.cost
                swar12.damage += r2.damage
                swar12.armor += r2.armor
                swar12.cost += r2.cost

                for s in sw, swa, swr1, swr2, swr12, swar1, swar2, swar12:
                    s_ = Stats(**asdict(s))
                    e = Stats(**asdict(enemy_stats))
                    if wins(s_, e) and (mincost is None or s.cost < mincost):
                        mincost = s.cost

    return mincost


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    enemy_stats = Stats(
        int(lines[0].split()[-1]),
        int(lines[1].split()[-1]),
        int(lines[2].split()[-1]),
        0,
    )
    stats = Stats(100, 0, 0, 0)

    maxcost = None
    for weapon in weapons:
        # exactly one weapon
        sw = Stats(**asdict(stats))
        sw.damage += weapon.damage
        sw.cost += weapon.cost
        for arm in armor:
            # 0 or 1 armor
            swa = Stats(**asdict(sw))
            swa.armor += arm.armor
            swa.cost += arm.cost
            for r1, r2 in combinations(rings, 2):
                # 0, 1 or 2 rings
                swr1 = Stats(**asdict(sw))
                swr1.damage += r1.damage
                swr1.armor += r1.armor
                swr1.cost += r1.cost

                swr2 = Stats(**asdict(sw))
                swr2.damage += r2.damage
                swr2.armor += r2.armor
                swr2.cost += r2.cost

                swr12 = Stats(**asdict(sw))
                swr12.damage += r1.damage
                swr12.armor += r1.armor
                swr12.cost += r1.cost
                swr12.damage += r2.damage
                swr12.armor += r2.armor
                swr12.cost += r2.cost

                swar1 = Stats(**asdict(swa))
                swar1.damage += r1.damage
                swar1.armor += r1.armor
                swar1.cost += r1.cost

                swar2 = Stats(**asdict(swa))
                swar2.damage += r2.damage
                swar2.armor += r2.armor
                swar2.cost += r2.cost

                swar12 = Stats(**asdict(swa))
                swar12.damage += r1.damage
                swar12.armor += r1.armor
                swar12.cost += r1.cost
                swar12.damage += r2.damage
                swar12.armor += r2.armor
                swar12.cost += r2.cost

                for s in sw, swa, swr1, swr2, swr12, swar1, swar2, swar12:
                    s_ = Stats(**asdict(s))
                    e = Stats(**asdict(enemy_stats))
                    if not wins(s_, e) and (maxcost is None or s.cost > maxcost):
                        maxcost = s.cost

    return maxcost


assert wins(Stats(8, 5, 5, 0), Stats(12, 7, 2, 0))
print(task1('input.txt'))

print(task2('input.txt'))
