import random
import urllib.request


def download_image(url):
    name = random.randrange(1, 1000)
    image = str(name) + ".jpg"
    urllib.request.urlretrieve(url,image)


download_image("https://wallpapercave.com/wp/wp1818972.jpg")
