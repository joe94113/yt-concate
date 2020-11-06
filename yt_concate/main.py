from yt_concate.pipeline.Steps.get_video_list import GetVideoList
from yt_concate.pipeline.Steps.download_captions import DownloadCaption
from yt_concate.pipeline.Steps.preflight import Preflight
from yt_concate.pipeline.Steps.postflight import Postflight
from yt_concate.pipeline.Steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils

CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaption(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, Utils())


if __name__ == "__main__":
    main()
