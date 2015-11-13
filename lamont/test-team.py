# This script implements the three main methods of the Log object.
# This will eventually need to be unit tests, but...one thing at a time
from log import Log
from team import Team

logfile = Log('../logs/test-team.log')
output = Log('../output/test-team.txt')

t = Team()

logfile.message(str(t.data))

t.load(11)

output.message(str(t))

logfile.end()
output.end()

print('Finished!')