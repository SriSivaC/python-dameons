#!/usr/bin/env python

import logging

nw1 = datetime.now().isoformat().replace('T','_').split(':')[0]
logfile_name = 'test_log'+nw1+'.log'
#logfile_name = logfile_name
logging.basicConfig(filename=logfile_name, filemode='a', format='%(asctime)s :: %(levelname)s  - %(message)s',level=logging.DEBUG)
logging.info("Test execution")
