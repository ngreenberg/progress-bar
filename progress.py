from __future__ import division

import os
import sys
import time

def progress_bar(index, length):
    progress = index / length

    screen_width = int(os.popen('stty size', 'r').read().split()[1])

    percent_width = 4
    percent_progress = ('%d%%' % (progress * 100)).rjust(percent_width)

    incomplete = 'INCOMPLETE'
    complete = 'COMPLETE!!!'
    message_width = len(max((incomplete, complete), key=len)) + 2
    message = complete if index == length else incomplete
    message = message.ljust(message_width)

    bar_width = screen_width - percent_width - message_width - 4
    bar_progress = '#' * int(progress * bar_width)
    bar_left = '-' * (bar_width - len(bar_progress))
    bar = '|%s%s|' % (bar_progress, bar_left)

    return '%s %s %s' % (percent_progress, bar, message)

if __name__ == '__main__':
    os.system('clear')

    screen_width = int(os.popen('stty size', 'r').read().split()[1])
    print
    print 'PROGRESS BAR'.center(screen_width)
    print

    length = 100
    for i in range(length):
        time.sleep(.1)

        sys.stdout.write('\r%s' % progress_bar(i, length))
        sys.stdout.flush()

    time.sleep(.1)

    print '\r%s' % progress_bar(length, length)

    screen_height = int(os.popen('stty size', 'r').read().split()[0])
    print '\n' * (screen_height - 6)
