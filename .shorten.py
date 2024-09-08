import sys
import os


def shorten(path):
    parts = path.split('/')
    if len(parts) >= 3:
        if parts[1]+parts[2] == "home"+os.getlogin():
            if len(parts) == 7:
                return f'~/{parts[3]}/{parts[4]}/{parts[5]}/{parts[6]}'
            if len(parts) == 6:
                return f'~/{parts[3]}/{parts[4]}/{parts[5]}'
            if len(parts) == 5:
                return f'~/{parts[3]}/{parts[-1]}'
            if len(parts) == 4:
                return f'~/{parts[3]}'
            if len(parts) == 3:
                return f'~'
            if len(parts) > 6:
                return f'~/{parts[3]}/{parts[4]}/.../{parts[-2]}/{parts[-1]}'
    if parts[1] == '':
        if len(parts) == 5:
            return f'/{parts[1]}/{parts[2]}/{parts[3]}/{parts[4]}'
        if len(parts) == 4:
            return f'/{parts[1]}/{parts[2]}/{parts[3]}'
        if len(parts) == 3:
            return f'/{parts[1]}/{parts[2]}'
        if len(parts) == 2:
            return f'/'
        if len(parts) > 4:
            return f'/{parts[1]}/{parts[2]}/.../{parts[-2]}/{parts[-1]}'
    return path
    
if __name__ == "__main__":
    print(shorten(os.getcwd()))
