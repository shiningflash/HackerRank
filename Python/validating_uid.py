import re

if __name__ == '__main__':
    for _ in range(int(input())):
        uid = input()
        try:
            assert re.fullmatch(r'^[a-zA-Z0-9]{10}', uid)
            assert re.fullmatch(r'([a-z0-9]*[A-Z]+[a-z0-9]*){2,}', uid)
            assert re.fullmatch(r'([a-zA-Z]*[0-9]+[a-zA-Z]*){3,}', uid)
            assert len(uid) == len(set(uid))
        except AssertionError:
            print('Invalid')    
        else:
            print('Valid')
        