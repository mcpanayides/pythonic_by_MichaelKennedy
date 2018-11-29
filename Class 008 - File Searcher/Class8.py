import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print('Sorry that is invalid!')
        return None

    text = get_search_from_user()
    if not text:
        print('We cannot search for nothing!')
        return None

    matches = search_folders(folder, text)
    for m in matches:
        print('|=============Match===============|')
        print('|file: ' + m.file)
        print('|line: {}' .format(m.line))
        print('|match: ' + m.text.strip())
        print('|==========end of match===========|')



def print_header():
    print('=================================')
    print('|       File Searcher App       |')
    print('=================================')
    print()


def get_folder_from_user():
    folder = input('What folder do you want to search in: ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None
    
    return os.path.abspath(folder)


def get_search_from_user():
    text = input('What are you searching for: ')
    return text.lower()


def search_folders(folder, text):
    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    matches = []
    with open(filename, 'r', encoding='utf-8') as fin:
        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                matches.append(m)
        return matches



if __name__ == '__main__':
    main()