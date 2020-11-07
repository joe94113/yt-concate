
class Found:
    def __init__(self, yt, caption, time):
        self.yt = yt
        self.cation = caption
        self.time = time

    def __str__(self):
        return '<Found(yt=' + str(self.yt) + '>'

    def __repr__(self):
        content = ' , '.join([
            'yt=' + str(self.yt),
            'caption=' + str(self.cation),
            'time=' + str(self.time),
        ])
        return '<Found(' + content + ')>'
