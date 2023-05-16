class FaceNotFoundErr(Exception):
    def __init__(self, text="Не удалось найти лицо в системе, попробуйте выбрать другую фотографию или добавьте изображение в систему"):
        self.txt = text