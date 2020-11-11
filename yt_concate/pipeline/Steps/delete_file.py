import shutil

from .step import Step
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class DeleteFile(Step):
    def process(self, data, inputs, utils):

        if inputs['cleanup']:

            CaptionPath = r"C:\Users\joe\Desktop\yt-concate\yt_concate\downloads\captions"
            Videospath = r'C:\Users\joe\Desktop\yt-concate\yt_concate\downloads\videos'
            try:
                shutil.rmtree(CaptionPath)
                shutil.rmtree(Videospath)
            except OSError as e:
                print(e)
            else:
                print("The directory is deleted successfully")
