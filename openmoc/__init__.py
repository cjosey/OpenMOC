import sys, os
import random
import datetime
import signal

# For Python 2.X.X
if (sys.version_info[0] == 2):
  from openmoc import *
# For Python 3.X.X
else:
  from openmoc.openmoc import *

# Tell Python to recognize CTRL+C and stop the C++ extension module
# when this is passed in from the keyboard
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Build a log file name using the date and time
g = lambda x: x.zfill(2)
now = datetime.datetime.now()
time = (now.month, now.day, now.year, now.hour, now.minute, now.second)
year_string = '-'.join(map(g, map(str, (now.month, now.day, now.year))))
today_string = ':'.join(map(g, map(str, (now.hour, now.minute, now.second))))
time_string = year_string + '--' + today_string
initialize_logger()
set_log_filename('openmoc-' + time_string + '.log');
