import random, math
ip = ".".join(map(str, (random.randint(0, 255) for x in range(4))))
# networksNeeded = random.randint(1,16)
networksNeeded = 10
n = ip.split('.')

def findClass(x):
    print x
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
    subnetSize = int(math.log(subNetCount,2))
    hostSize = 8-subnetSize
    NAHost = '0' * hostSize
    BAHost = '1' * hostSize

    for i in range(subNetCount):
        s = i
        sub = "{0:b}".format(s)
        ndec = int(sub + NAHost,2)
        bdec = int(sub + BAHost,2)
        r = '.' + str(ndec + 1) + ' - .' + str(bdec + 1)
        table[i] = [s, sub.zfill(subnetSize),NAHost,ndec,sub.zfill(subnetSize),BAHost,bdec,r]
    table.insert(0,['Subnet',"N subnet", "N host", "=", "B subnet", "B host", "=", "Range"])
    #print 'Subnet',"NA subnet", "NA host", " = ", "BA subnet", "BA host", " = ", "Range"

    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print "| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |"
    # for i in range(len(table)):
    #     for j in table[i]:
    #         print repr(j).rjust(4),
    #     print
        # repr(i[7]).rjust(11)


print 'The IP address is ' + ip + "\nYou need " + str(networksNeeded) + " subnetworks"

ipClass = findClass(int(n[0]))

# classGuess = raw_input('\nWhat is the class of the IP?  ')
# classGuess.lower()
# if classGuess == ipClass:
#     print 'Correct'
# else:
#     print 'Incorrect, the class is ' + ipClass

subNetCount = 2 ** len("{0:b}".format(networksNeeded))
# subnetGuess = raw_input('\nHow many subnetworks do you need?  ')
#
# if int(subnetGuess) == subNetCount:
#     print 'Correct'
# else:
#     print 'Incorrect, ' + subNetCount + ' subnetworks are needed'

usableHosts = math.log(subNetCount,2) - 2
# hostGuess = raw_input('\nHow many usable hosts can are there?  ')
# if int(hostGuess) == usableHosts:
#     print 'Correct'
# else:
#     print 'Incorrect, there are ' + usableHosts + " usable hosts"

printTable()
