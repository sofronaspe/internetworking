import random, math
ip = ".".join(map(str, (random.randint(0, 255) for x in range(4))))
networksNeeded = random.randint(1,16)
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

print 'The IP address is ' + ip + "\nYou need " + str(networksNeeded) + " subnetworks"

ipClass = findClass(int(n[0]))

classGuess = raw_input('\n\hat is the class of the IP?  ')
classGuess.lower()
if classGuess == ipClass:
    print 'Correct'
else:
    print 'Incorrect, the class is ' + ipClass

subnetCount = 2 ** len("{0:b}".format(networksNeeded))
subnetGuess = raw_input('\nHow many subnetworks do you need?  ')

if int(subnetGuess) == subnetCount:
    print 'Correct'
else:
    print 'Incorrect, ' + subnetCount + ' subnetworks are needed'

usableHosts = math.log(subnetCount,2) - 2
hostGuess = raw_input('\nHow many usable hosts can are there?  ')
if int(hostGuess) == usableHosts:
    print 'Correct'
else:
    print 'Incorrect, there are ' + usableHosts + " usable hosts"
