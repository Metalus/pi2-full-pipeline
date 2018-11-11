import pybrl as brl
import sys
import os

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

result = []
content = [x.strip() for x in lines]
for i, line in enumerate(content):
    if len(line) > 27:
        content.insert(i+1, line[27:])
        content[i] = line[:27]

content = [x.ljust(27) for x in content]
for line in content:
    os.system('python3 Tradutor/Braille-Translator/main.py {} -t'.format(line))
    file = open('out', 'r')
    bra_line = file.read()
    bra = brl.matrix(bra_line)
    char_lines = []
    for i in range(0, 3):
        temp = [item[i] for item in bra]
        temp = [inner for outer in temp for inner in outer]
        char_lines.append(temp)
    
    for char_line in char_lines:
        result.append(''.join([str(e) for e in char_line]))

print(result)

#for line in result:
#    for num in (lambda s: map(lambda x: int(x, 2), (lambda ss: [ss[x:x+8] for x in range(0, len(ss)//8 + (len(ss) - len(ss)//8), 8)])(s)))(line):
#        os.system("./{0} {1}".format(sys.argv[2], num))
