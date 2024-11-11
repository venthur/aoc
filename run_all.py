from pathlib import Path
import subprocess
from multiprocessing import Pool
from time import time

TIMEOUT = 15


def run_program(program):
    t0 = time()
    try:
        subprocess.run(
            ['python3', 'main.py'],
            cwd=program.parent,
            timeout=TIMEOUT,
            capture_output=True,
        )
    except subprocess.TimeoutExpired:
        print('x', end='', flush=True)
        return TIMEOUT
    print('.', end='', flush=True)
    return time() - t0


def main():
    p = Path('.')
    programs = sorted(list(p.glob('**/main.py')))

    times = {}
    with Pool() as p:
        results = p.map(run_program, programs)
        for program, result in zip(programs, results):
            times[program] = result

    # sort times by value
    times = sorted(times.items(), key=lambda x: x[1], reverse=True)

    for program, time in times:
        print(f'{program}: {time:.2f} s')

if __name__ == '__main__':
    main()
