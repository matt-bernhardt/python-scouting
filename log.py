log = ''


def start(logFile):
    global log
    log = open(logFile, 'w')
    log.write('Log start\n')


def message(msg):
    global log
    log.write(msg)
    log.write('\n')


def end():
    global log
    log.write('Log end\n')
    log.close()
