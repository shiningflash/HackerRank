IPv4 = r'^(([01]?\d{1,2}|2[0-4]\d|25[0-5])\.){3}([01]?\d{1,2}|2[0-4]\d|25[0-5])$'
IPv6 = r'^([0-9a-f]{1,4}:){7}[0-9a-f]{1,4}$'

import re

if __name__ == '__main__':
    for _ in range(int(input())):
        ip = input().lower()
        result = "IPv4" if re.search(IPv4, ip) else ("IPv6" if re.search(IPv6, ip) else "Neither")
        print(result)
