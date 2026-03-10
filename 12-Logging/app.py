import logging

## logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger('ArithmeticApp')

def add(a, b):
    results = a + b
    logger.debug(f'Adding {a}+{b} = {results}')  # fixed
    return results


def subtract(a, b):
    results = a - b
    logger.debug(f'subtract {a}-{b} = {results}')  # fixed
    return results


def multiply(a, b):
    results = a * b
    logger.debug(f'multiply {a}*{b} = {results}')  # fixed
    return results


def divide(a,b):
    try:
        result = a/b
        logger.debug(f'Dividing {a}/{b}={result}')
        return result
    except ZeroDivisionError:
        logger.error('Division by Zero error')
        return None



add(10,89)
subtract(89,9)
multiply(7,9)
divide(40,7)
