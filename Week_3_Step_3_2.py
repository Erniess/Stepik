# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.

import re
import sys
pattern = r'\bcat\b'

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(pattern, line): print(line)