# Import build-in packages
import logging

# Import our packages
from configuration import config_reader

# Initialization
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger()
config_reader.set_logger(logger)

# Run demo
config = config_reader.get_configuration()
logger.info(config.get('default', 'message'))
config = config_reader.get_configuration('myconfig.ini')
logger.info(config.get('default', 'message'))
