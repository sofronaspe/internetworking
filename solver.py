import random, math
ip = raw_input("What is the ip? ")
networksNeeded = int(raw_input("How many networks do you want to make? "))
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
print 'The class IP is ' + ipClass

subNetCount = 2 ** len("{0:b}".format(networksNeeded))
print 'The subnet count is ' + str(subNetCount)

subnetSize = int(math.log(subNetCount,2))
hostSize = 8-subnetSize
NAHost = '0' * hostSize
BAHost = '1' * hostSize
hostCount = 2 ** hostSize - 2
print 'There are ' + str(hostCount) + ' usable hosts'
raw_input('Press Enter to view table')
printTable()
mask = ''
if ipClass == 'a':
    mask = '255.255.255.'+ str(2 ** subnetSize - 1)
elif ipClass == 'b':
    mask = '255.255.'+ str(2 ** subnetSize - 1) + '.0'
elif ipClass == 'c':
    mask = '255.'+ str(2 ** subnetSize - 1) + '.0.0'
else:
    print 'Something went wrong'
print 'The subnet mask is ' + mask
