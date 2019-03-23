# Run demo
import logging
from configuration import config_reader

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s [%(levelname)s] %(message)s'
)
config = config_reader.get_configuration()
logging.info(config.get('default', 'message'))
