# This script implements the three main methods of the Log object.
# This will eventually need to be unit tests, but...one thing at a time
from log import Log

logfile = Log('test-log.log')
output = Log('test-output.log')

print(logfile.name)
print(output.name)

logfile.message("First line of log file")
output.message("First line of output file")

logfile.end()
output.end()

print('Finished!')