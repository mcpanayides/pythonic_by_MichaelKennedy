def main():
    printHeader()
    run_event_loop()


def printHeader():
    print('=============================================')
    print('                 Journal App')
    print('=============================================')
    print()


def run_event_loop():
    print('What do you want to do with your Journal?')

    cmd = None

    while cmd != 'x':

        cmd = input('[L]ist entries, [A]dd an entry, E[x]it:')

        if cmd == 'L':
            print('L')
        elif cmd == 'A':
            print('A')

    print('Done, Goodbye!')

main()


