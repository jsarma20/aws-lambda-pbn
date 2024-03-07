import base64
from pathlib import Path
def encodeFileToPost(filename:str) -> str:
    serialized = ''
    with open(filename, "rb") as in_file:
        data = in_file.read()
        serialized = base64.b64encode(data).decode("utf-8")
    return serialized

def decodePostToImageFile(encodedImage, inputFile:Path):
    image = base64.b64decode(encodedImage)
   
    with open(inputFile, "wb") as f:
        f.write(image)