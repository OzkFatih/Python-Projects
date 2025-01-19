def decodeString(s):
    leet_code = {'0': 'o', '1': 'i', '3': 'e', '4': 'a', '5': 's', '7': 't', '8': 'b'}
    for key, value in leet_code.items():
        s = s.replace(key, value)
    return s

if __name__ == '__main__':
    s = 'h3ll0 w0rld'
    print(decodeString(s))