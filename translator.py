import teste as brl
import sys
import os

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

result = []
content = ' '.join([x.strip() for x in lines])
curr = content
resultt = []

ss = [' ', '.', ',']
while len(curr) != 0:
    if len(curr) >= 27:
        if curr[26] not in ss and curr[27] not in ss:  
            lstring = curr[:(curr[:27].rfind(' '))]
            resultt.append(lstring.strip().ljust(27))
            curr = curr[curr[:27].rfind(' '):].strip()
        else:
            lstring = curr[:(curr[:27].rfind(' '))]
            resultt.append(curr[:27].strip())
            curr = curr[27:].strip()
    else:
        resultt.append(curr.ljust(27))
        curr = ''
#print(content)
#print(resultt)
content = resultt

for line in content:
    #print(line)
    os.system('python3 main.py \'{}\' -t'.format(line))
    file = open('out', 'r')
    bra_line = file.read()
    print("Braille: {}".format(bra_line))
    os.system('python3 main.py \'{}\' -b'.format(bra_line))
    bra = brl.matrix(bra_line)
    char_lines = []
    for i in range(0, 3):
        temp = [item[i] for item in bra]
        temp = [inner for outer in temp for inner in outer]
        char_lines.append(temp)
    
    for char_line in char_lines:
        result.append(''.join([str(e) for e in char_line]))

geral = [x for x in [r for r in result]]
geral2 = []

for i in range(0, 3):
    vec = ''
    for j in range(i, len(geral), 3):
        vec += geral[j]
    geral2.append(vec)

"""
macumba = []

for jota in range(0, 3):
    kk = [geral2[jota][i:54+i] for i in range(0,len(geral2[jota]), 54)]
    kk[-1] = kk[-1].ljust(54, '0')
    macumba.append(kk)
resultado = []
for j in range(0, len(macumba[0])):
    for k in range(0, 3):
        resultado.append(macumba[k][j])
"""
for line in result:
    print(line)

for line in result:
    numbers = []
    for num in (lambda s: map(lambda x: int(x, 2), (lambda ss: [ss[x:x+8] for x in range(0, len(ss)//8 + (len(ss) - len(ss)//8), 8)])(s)))(line):
        #os.system("./{0} {1}".format(sys.argv[2], num))
        numbers.append(num)

    print(numbers)
