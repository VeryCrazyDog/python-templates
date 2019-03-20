# Import build-in packages
import os
import shutil
import time

# Import our packages
from definitions import ROOT_DIR

# Initialization
log_dir = os.path.join(ROOT_DIR, 'log')
if os.path.isdir(log_dir):
    shutil.rmtree(log_dir)
while os.path.isdir(log_dir):
    time.sleep(1)

# Run demo
from util import logger

logger.debug('Debug')
logger.info('Info')
logger.warn('Warning')
logger.error('Error')
logger.fatal('Fatal')
