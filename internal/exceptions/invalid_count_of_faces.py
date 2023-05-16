class InvalidCountOfFaceFaceErr(Exception):
    def __init__(self, text="На изображении должно быть только одно лицо"):
        self.txt = text