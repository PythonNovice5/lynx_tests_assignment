import logging

def configure_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Set the desired logging level

    # Create a console handler and set the level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger
