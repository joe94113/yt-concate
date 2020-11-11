import time


import pytube

from .step import Step
from pytube import YouTube
from multiprocessing import Process


from yt_concate.settings import VIDEOS_DIR
from threading import Thread


class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        start = time.time()

        Threads = []

        for i in range(4):
            Threads.append(Thread(target=self.downloadvideos(data, utils)))

        for thread in Threads:
            thread.start()

        for thread in Threads:
            thread.join()

        # yt_set = set([found.yt for found in data])
        # print('videos to download=', len(yt_set))
        #
        # for yt in yt_set:
        #     url = yt.url
        #
        #     if utils.video_file_exists(yt):
        #         print(f'found existing video file for {url}, skipping')
        #         continue
        #     try:
        #         print('downloading', url)
        #         YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
        #     except pytube.exceptions.RegexMatchError:
        #         print('downloading error', url)

        end = time.time()
        print('總共費時', end-start)

        return data

    @staticmethod
    def downloadvideos(data, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download=', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue
            try:
                print('downloading', url)
                YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
            except pytube.exceptions.RegexMatchError:
                print('downloading error', url)
