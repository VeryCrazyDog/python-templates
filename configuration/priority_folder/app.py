# Import build-in packages
import logging

# Initialization
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger()

# Run demo
from configuration import config_reader

config_reader.set_logger(logger)
config = config_reader.get_configuration()
logger.info(config.get('default', 'message'))
config = config_reader.get_configuration('myconfig.ini')
logger.info(config.get('default', 'message'))
