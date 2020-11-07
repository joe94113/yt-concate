import time

import pytube
from pytube import YouTube
from yt_concate.pipeline.Steps.step import Step
from yt_concate.pipeline.Steps.step import StepException


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        # download the package by:  pip install pytube
        start = time.time()
        for yt in data:
            print('downloading caption for', yt.id)
            if utils.caption_file_exists(yt):
                print('find existing caption file')
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError, pytube.exceptions.RegexMatchError):
                print('Error when downloading caption for', yt.url)
                continue

            # save the caption to a file named Output.txt
            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 's')

        return data
