from recognize_faces import recognize_faces
from train import get_persons_data

def main():
    persons_data = get_persons_data('persons_data/data.json')
    recognize_faces('01_kinopoisk.ru-Justice-League-3048080.jpg', persons_data)


if __name__ == "__main__":
    main()