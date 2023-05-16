import numpy as np
import io
import PIL.Image as Image


def convert_bytes_to_nparray(data: bytes, mode: str = 'RGB') -> np.ndarray:
    im = Image.open(io.BytesIO(data))
    if mode:
        im = im.convert(mode)
    return np.array(im)
