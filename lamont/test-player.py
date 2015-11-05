# This script implements the three main methods of the Log object.
# This will eventually need to be unit tests, but...one thing at a time
from log import Log
from player import Player

logfile = Log('../logs/test-player.log')
output = Log('../output/test-player.txt')

print('First player test')
output.message('First player test')
# First player test
p1 = Player()
output.message(str(p1.data))
p1.loadID(1565)
p1.dumpToTerminal()
output.message(str(p1))

output.message("")

print('Second player test')
output.message('Second player test')
# Second player test
p2 = Player()
p2.lookupName('Brian')
output.message(str(p2))

output.message(str(type(p2)))
output.message(str(type(p2.data)))

for index, item in enumerate(p2.data):
    output.message(p2.data.index)
    output.message(p2.data.item[index])

logfile.end()
output.end()

print('Finished!')
