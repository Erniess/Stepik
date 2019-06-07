# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

import re
import sys
pattern = r'cat.*cat'

for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line): print(line)