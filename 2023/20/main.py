def task1(fn):
    outputs = {}
    op = {}
    # for flipfops, it stores the state,
    # for conjunctions, it stores inputs
    data = {}

    with open(fn) as fh:
        for line in fh.read().splitlines():
            module, out = line.split(' -> ')
            out = out.split(', ')

            if module.startswith('%'):
                module = module[1:]
                op[module] = 'flipflop'
            elif module.startswith('&'):
                module = module[1:]
                op[module] = 'conjunction'
            outputs[module] = out

    # get all conjunctions and find their inputs
    conjunctions = [module for module in op if op[module] == 'conjunction']
    for input_, outs in outputs.items():
        for output in outs:
            if output in conjunctions:
                d = data.get(output, dict())
                d[input_] = 'low'
                data[output] = d


    pulses = dict(low=0, high=0)
    for i in range(1000):
        # button sends a low pulse to broadcaster
        pulses['low'] += 1
        queue = [('broadcaster', 'low', 'button')]
        while queue:

            current_module, signal, origin = queue.pop(0)

            if current_module == 'broadcaster':
                for output in outputs[current_module]:
                    queue.append((output, signal, current_module))
                    pulses[signal] += 1
                continue

            operation = op.get(current_module)
            if operation == 'flipflop':
                if signal == 'high':
                    # high pulses are ignored
                    continue
                elif signal == 'low':
                    # default state is 'off'
                    state = data.get(current_module, 'off')
                    if state == 'off':
                        data[current_module] = 'on'
                        for output in outputs[current_module]:
                            queue.append((output, 'high', current_module))
                            pulses['high'] += 1
                    elif state == 'on':
                        data[current_module] = 'off'
                        for output in outputs[current_module]:
                            queue.append((output, 'low', current_module))
                            pulses['low'] += 1
                    else:
                        raise ValueError(state)
            elif operation == 'conjunction':
                data[current_module][origin] = signal
                if all(i == 'high' for i in data[current_module].values()):
                    for output in outputs[current_module]:
                        queue.append((output, 'low', current_module))
                        pulses['low'] += 1
                else:
                    for output in outputs[current_module]:
                        queue.append((output, 'high', current_module))
                        pulses['high'] += 1
            else:
                # no operation assigned
                pass


    return pulses['low'] * pulses['high']


def task2(fn):
    outputs = {}
    op = {}
    # for flipfops, it stores the state,
    # for conjunctions, it stores inputs
    data = {}

    with open(fn) as fh:
        for line in fh.read().splitlines():
            module, out = line.split(' -> ')
            out = out.split(', ')

            if module.startswith('%'):
                module = module[1:]
                op[module] = 'flipflop'
            elif module.startswith('&'):
                module = module[1:]
                op[module] = 'conjunction'
            outputs[module] = out

    # get all conjunctions and find their inputs
    conjunctions = [module for module in op if op[module] == 'conjunction']
    for input_, outs in outputs.items():
        for output in outs:
            if output in conjunctions:
                d = data.get(output, dict())
                d[input_] = 'low'
                data[output] = d

    pulses = dict(low=0, high=0)
    button_pressed = 0
    while True:
        # button sends a low pulse to broadcaster
        button_pressed += 1
        pulses['low'] += 1
        queue = [('broadcaster', 'low', 'button')]
        while queue:

            for current_module, signal, _ in queue:
                if current_module == 'rx' and signal == 'low':
                    return button_pressed

            current_module, signal, origin = queue.pop(0)

            if current_module == 'broadcaster':
                for output in outputs[current_module]:
                    queue.append((output, signal, current_module))
                    pulses[signal] += 1
                continue

            operation = op.get(current_module)
            if operation == 'flipflop':
                if signal == 'high':
                    # high pulses are ignored
                    continue
                elif signal == 'low':
                    # default state is 'off'
                    state = data.get(current_module, 'off')
                    if state == 'off':
                        data[current_module] = 'on'
                        for output in outputs[current_module]:
                            queue.append((output, 'high', current_module))
                            pulses['high'] += 1
                    elif state == 'on':
                        data[current_module] = 'off'
                        for output in outputs[current_module]:
                            queue.append((output, 'low', current_module))
                            pulses['low'] += 1
                    else:
                        raise ValueError(state)
            elif operation == 'conjunction':
                data[current_module][origin] = signal
                if all(i == 'high' for i in data[current_module].values()):
                    for output in outputs[current_module]:
                        queue.append((output, 'low', current_module))
                        pulses['low'] += 1
                else:
                    for output in outputs[current_module]:
                        queue.append((output, 'high', current_module))
                        pulses['high'] += 1
            else:
                # no operation assigned
                pass


assert task1('test_input.txt') == 32000000
assert task1('test_input2.txt') == 11687500
print(task1('input.txt'))

print(task2('input.txt'))
