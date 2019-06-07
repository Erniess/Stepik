# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
#
#
# Sample Input:
#
# cat
# catapult and cat
# catcat
# concat
# Cat
# "cat"
# !cat?
#
# Sample Output:
#
# cat
# catapult and cat
# "cat"
# !cat?
#

import re
import sys
pattern = r'\bcat\b'

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(pattern, line): print(line)