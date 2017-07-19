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
        cmd = cmd.lower().strip()

        if cmd == 'l':
            listEntries()
        elif cmd == 'a':
            addEntries()
        elif cmd != 'x':
            print("Sorry, I don't understand {}".format(cmd))
    print('Done, Goodbye!')

def listEntries():
    print('Listing...')


def addEntries():
    print('Adding...')


main()


