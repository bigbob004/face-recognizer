from recognize_faces import recognize_faces
from train import get_persons_data

def main():
    persons_data = get_persons_data('persons_data/data.json')
    recognize_faces('gal gadot.jpg', persons_data)


if __name__ == "__main__":
    main()