# Import build-in packages
import os

# Initialization
os.environ['LOG_LEVEL'] = 'DEBUG'

# Run demo
from util import logger
logger.debug('Debug')
logger.info('Info')
logger.warn('Warning')
logger.error('Error')
logger.fatal('Fatal')
