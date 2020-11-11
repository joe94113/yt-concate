from .log import config_logger
from .step import Step
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR


class Postflight(Step):
    def process(self, data, inputs, utils):
        logging = config_logger()
        logging.info('in Postflight')


