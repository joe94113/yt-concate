import shutil

from .log import config_logger
from .step import Step
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class DeleteFile(Step):
    def process(self, data, inputs, utils):
        logging = config_logger()
        if inputs['cleanup']:

            CaptionPath = r"C:\Users\joe\Desktop\yt-concate\yt_concate\downloads\captions"
            Videospath = r'C:\Users\joe\Desktop\yt-concate\yt_concate\downloads\videos'
            try:
                shutil.rmtree(CaptionPath)
                shutil.rmtree(Videospath)
            except OSError as e:
                logging.warning(e)
            else:
                logging.info("The directory is deleted successfully")
