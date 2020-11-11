from .log import config_logger
from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        logging = config_logger()
        logging.info('in Preflight')
        utils.create_dirs()
