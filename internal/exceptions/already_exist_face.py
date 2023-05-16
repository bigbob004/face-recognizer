class AlreadyExistFaceErr(Exception):
    def __init__(self, text="Данное лицо уже загружен в систему. Попробуйте загрузить другое лицо"):
        self.txt = text