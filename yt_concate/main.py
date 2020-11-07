from yt_concate.pipeline.Steps.download_videos import DownloadVideos
from yt_concate.pipeline.Steps.edit_video import EditVideo
from yt_concate.pipeline.Steps.search import Search
from yt_concate.pipeline.Steps.get_video_list import GetVideoList
from yt_concate.pipeline.Steps.download_captions import DownloadCaption
from yt_concate.pipeline.Steps.initialize_yt import InitializeYT
from yt_concate.pipeline.Steps.preflight import Preflight
from yt_concate.pipeline.Steps.postflight import Postflight
from yt_concate.pipeline.Steps.read_caption import ReadCaption
from yt_concate.pipeline.Steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils

CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaption(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()
