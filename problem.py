import random, math
ip = str(random.randint(0,223)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' + str(random.randint(0,255))
#ip = ".".join(map(str, (random.randint(0, 255) for x in range(4))))
networksNeeded = random.randint(1,16)

n = ip.split('.')

def findClass(x):
    if 1 <= x <= 127:
        return 'a'
    if 128 <= x <= 191:
        return 'b'
    if 192 <= x <= 223:
        return 'c'
    if 224 <= x <= 239:
        return 'd'
    if 240 <= x <= 255:
        return 'e'
    else:
        print 'The IP has no class'

def printTable():
    table = [[] for i in range(subNetCount)]

    for i in range(subNetCount):
        s = i
        sub = "{0:b}".format(s)
        ndec = int(sub + NAHost,2)
        bdec = int(sub + BAHost,2)
        r = '.' + str(ndec + 1) + ' - .' + str(bdec + 1)
        table[i] = [s, sub.zfill(subnetSize),NAHost,ndec,sub.zfill(subnetSize),BAHost,bdec,r]
    table.insert(0,['Subnet',"N subnet", "N host", "=", "B subnet", "B host", "=", "Range"])

    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print "| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |"

print 'The IP address is ' + ip + "\nYou need " + str(networksNeeded) + " subnetworks"

ipClass = findClass(int(n[0]))

classGuess = raw_input('\nWhat is the class of the IP?  ')
classGuess.lower()
if classGuess == ipClass:
    print 'Correct'
else:
    print 'Incorrect, the class is ' + ipClass

subNetCount = 2 ** len("{0:b}".format(networksNeeded))
subnetGuess = raw_input('\nHow many subnetworks will be created?  ')

if int(subnetGuess) == subNetCount:
    print 'Correct'
else:
    print 'Incorrect, ' + subNetCount + ' subnetworks are needed'

subnetSize = int(math.log(subNetCount,2))
hostSize = 8-subnetSize
NAHost = '0' * hostSize
BAHost = '1' * hostSize
hostCount = 2 ** hostSize - 2
hostGuess = raw_input('\nHow many usable hosts are there?  ')
if int(hostGuess) == hostCount:
    print 'Correct'
else:
    print 'Incorrect, there are ' + str(hostCount) + ' usable hosts'
raw_input('Press Enter to view table')
printTable()
maskGuess = raw_input('What will the subnet mask be (whole IP)? ')
mask = ''
if ipClass == 'a':
    mask = '255.255.255.'+ str(2 ** subnetSize - 1)
elif ipClass == 'b':
    mask = '255.255.'+ str(2 ** subnetSize - 1) + '.0'
elif ipClass == 'c':
    mask = '255.'+ str(2 ** subnetSize - 1) + '0.0'
else:
    print 'Something went wrong'
if maskGuess == mask:
    print 'Correct'
else:
    print 'Incorrect, the mask is ' + mask
