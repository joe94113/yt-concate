from pytube import YouTube
from yt_concate.pipeline.Steps.step import Step
from yt_concate.pipeline.Steps.step import StepException

import time


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        # download the package by:  pip install pytube
        start = time.time()
        for url in data:
            source = YouTube(url)

            en_caption = source.captions.get_by_language_code('en')

            en_caption_convert_to_srt = (en_caption.generate_srt_captions())

            print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_path(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 's')
