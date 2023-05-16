class CanNotDetectFaceErr(Exception):
    def __init__(self, text="Не удалось обнаружить лицо на изображении"):
        self.txt = text