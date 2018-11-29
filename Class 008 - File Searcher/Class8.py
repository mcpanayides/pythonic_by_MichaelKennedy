def main():
    print_header()

    folder = get_folder_from_user()
    
    if not folder:
        print('Sorry that is invalid!')
        return

    text = get_search_from_user()
    if not text:
        print('We cannot search for nothing!')
        return

    search_folders



def print_header():
    print('=================================')
    print('|       File Searcher App       |')
    print('=================================')
    print()


def get_folder_from_user():
    folder = input('What folder do you want to search in: ')
    if not folder or folder.strip():
        return None

    if not os.path.isdir(folder):
        return None
    
    return os.path.abspath(folder)


def get_search_from_user():
    text = input('What are you searching for: ')
    return text


def search_folders():
    print('Would search {} for {}: '.format(folder, text)


if __name__ == '__main__':
    main()