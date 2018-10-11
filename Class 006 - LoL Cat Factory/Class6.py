import os
import subprocess
import platform
import cat_service

def main():
    folder = get_or_create_output_folder()
    header()
    print('Found or created folder: '+ folder)
    downloadCats(folder)
    displayCats(folder)


def header():
    print('=========================')
    print('=  LolCatZ Application  =')
    print('=========================')
    print()


def get_or_create_output_folder():
    baseFolder = os.path.dirname(__file__)
    folder = 'cat_pics'
    full_path = os.path.join(baseFolder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('mkdir at {}'.format(full_path))
        os.mkdir(full_path)
    return full_path


def downloadCats(folder):
    print('Contacting server to recieve LoLs and Cats')
    cat_count = 8
    for i in range (1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)
    print('Complete')


def displayCats(folder):
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    else:
        print('We dont support your OS, Sorry')


if __name__ == '__main__':
    main() 