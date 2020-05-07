#!/usr/bin/env python

import sys, time
from daemon3x import Daemon
from datetime import datetime

import logging

nw1 = datetime.now().isoformat().replace('T','_').split(':')[0]
logfile_name = 'test_log'+nw1+'.log'
#logfile_name = logfile_name
logging.basicConfig(filename=logfile_name, filemode='a', format='%(asctime)s :: %(levelname)s  - %(message)s',level=logging.DEBUG)

class MyDaemon(Daemon):
    def run(self):
        while True:
            logging.info("Test execution")
            time.sleep(1)

if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
