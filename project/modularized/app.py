# Import our packages
from util import logger
from configuration import config_reader
import definitions

# Implementation
logger.info('Hello World!')
logger.debug('Debug')
logger.info('Info')
logger.warn('Warning')
logger.error('Error')
logger.info(f'Root directory: {definitions.ROOT_DIR}')
logger.info(config_reader.get('default', 'message'))
