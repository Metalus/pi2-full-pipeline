import teste as brl
import sys
import os

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

result = []
content = [x.strip() for x in lines]
#print(content)
for i, line in enumerate(content):
    if len(line) > 27:
        content.insert(i+1, line[27:])
        content[i] = line[:27]

content = [x.ljust(27) for x in content]

ss = [' ', '.', ',']
for k,cont in enumerate(content):
    if k != len(content) - 1:
        if cont[-1] not in ss and content[k+1] not in ss:
            lstring = cont[cont.rfind(' '):]
            rstring = content[k+1][:content[k+1].find(' ')]
            res = lstring.strip()
            content[k] = cont[:cont.rfind(' ')]
            content[k] = content[k].ljust(27)
            content[k+1] = res + content[k+1]
            print(cont, content[k+1])

content = ''.join(content).strip()

content = [content[i:27+i] for i in range(0, len(content), 27)]
content[-1] = content[-1].ljust(27)
print(content)
#print(content)

for line in content:
    #print(line)
    os.system('python3 main.py \'{}\' -t'.format(line))
    file = open('out', 'r')
    bra_line = file.read()
    #print(bra_line)
    bra = brl.matrix(bra_line)
    #print(bra)
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


macumba = []

for jota in range(0, 3):
    kk = [geral2[jota][i:54+i] for i in range(0,len(geral2[jota]), 54)]
    kk[-1] = kk[-1].ljust(54, '0')
    macumba.append(kk)
#print(macumba)
resultado = []
for j in range(0, len(macumba[0])):
    for k in range(0, 3):
        resultado.append(macumba[k][j])


for line in resultado:
    numbers = []
    for num in (lambda s: map(lambda x: int(x, 2), (lambda ss: [ss[x:x+8] for x in range(0, len(ss)//8 + (len(ss) - len(ss)//8), 8)])(s)))(line):
        #os.system("./{0} {1}".format(sys.argv[2], num))
        numbers.append(num)

    #print(numbers)
