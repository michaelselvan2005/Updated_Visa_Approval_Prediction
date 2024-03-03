from us_visa.components.data_ingestion import main
#from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
try:
    a = 1/ 10
    print(a)
except Exception as e:
    raise USvisaException(e, sys) from e

