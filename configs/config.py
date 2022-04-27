import sys
import logging

from file_readers.CSVFileReader import CSVFileReader
from file_readers.JSONFileReader import JSONFileReader


FILE_READERS = {
    'csv': CSVFileReader,
    'json': JSONFileReader,
}

SEARCH_BY_PARAMETERS = (
    'Flight_ticket',
    'Passport_number',
)

SEARCH_IDENTITY = {
   'Full_name': 'Jason Bourne',
}


MATCHING_VALUE_THRESHOLD = 0.9


LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdout, format=LOG_FORMAT, level=logging.INFO)

logger = logging.getLogger('indentify_test')
logger.setLevel(logging.INFO)
