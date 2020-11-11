from .log import config_logger
from .step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        logging = config_logger()
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue

            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)

        logging.info("{} of videos found for this searchword".format(len(found)))
        return found
