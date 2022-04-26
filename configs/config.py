import sys
import logging


FILE_FORMATS_DICT = {'json': 'json_converter'}

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdout, format=LOG_FORMAT, level=logging.INFO)

logger = logging.getLogger('indentify_test')
logger.setLevel(logging.INFO)
