import datetime

def print_registries(registries, title=None):
    # calculates table anchor
    anchor = [[len(str(field)) for field in reg] for reg in registries]
    anchor = [max(col) for col in zip(*anchor)]

    print('\n')
    if title is not None: print(title)
    print('-' * len(title))
    for reg in registries:
        reg = tuple(r if r is not None else '' for r in reg)
        reg = tuple(str(r) if type(r) == datetime.date else r for r in reg)
        reg = zip(reg, anchor)
        reg = ['{:{}}'.format(*campo) for campo in reg]
        print('  |  '.join(reg))
    print('-' * len(title))
    print('\n')