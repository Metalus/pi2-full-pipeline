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
    line = line.ljust(27)
    os.system('python3 main.py \'{}\' -t'.format(line))
    file = open('out', 'r')
    bra_line = file.read()
    bra_line = bra_line.strip()
    print("Braille: {}".format(bra_line))
    os.system('python3 main.py \'{}\' -b'.format(bra_line))
    bra = brl.matrix(bra_line)
    bri = [[[0,0], [0,0],[0,0]]] * (27 - len(bra))
    bra = bra + bri
    char_lines = []
    for i in range(0, 3):
        temp = [item[i] for item in bra]
        temp = [inner for outer in temp for inner in outer]
        char_lines.append(temp)
    
    for char_line in char_lines:
        result.append(''.join([str(e) for e in char_line]))

for i, k in enumerate(result):
    if len(k) != 54:
        print(i, k)
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
i = 0
for line in result:
    
    if not i:
        print('-------------------------------------------------------')
    print(line)
    i = (i+1) % 3

for line in result:
    numbers = []
    for num in (lambda s: map(lambda x: int(x, 2), (lambda ss: [ss[x:x+8] for x in range(0, len(ss)//8 + (len(ss) - len(ss)//8), 8)])(s)))(line):
        c = os.system("./{0} {1}".format('a.out', num))
        
        retorno = bin(c)[2:].rjust(8, '0')
        codigo = retorno[:len(retorno)-8] if len(retorno) > 8 else '00000000'
        codigoreal = int(codigo, 2)
        if codigoreal == 0:
            numbers.append(num)
        else:
            print(codigoreal)
            sys.exit()
            break
    print('impressao completa')
    print(numbers)
