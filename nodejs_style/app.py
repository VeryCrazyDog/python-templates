# # Import our packages
# import configuration
# from util.logger import Logger

# # Main implementation
# Logger.init_logger(Logger.DEBUG)
# logger = Logger.get_logger()
# config = configuration.get_configuration(logger)
# message = config.get('default', 'message')
# logger.info('Info is not shown on console, include logging.basicConfig() if needed')
# logger.warn(message)

# # Clean up
# configuration.unload_configuration()

from util import logger
import definitions

logger.info('Hello World!')
logger.debug('Debug')
logger.info('Info')
logger.warn('Warning')
logger.error('Error')
logger.info(f'Root directory: {definitions.ROOT_DIR}')
logger.info(f'Config directory: {definitions.CONFIG_DIR}')
# logger.info(f'Host config directory: {definitions.HOST_CONFIG_DIR}')
