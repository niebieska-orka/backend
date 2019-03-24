import csv

import pyqrcode
from PIL import Image
from boardgamegeek import BGGClient

from boardGames.rental.models import Game


def generate_qr(game_ID):
    url = pyqrcode.QRCode(game_ID, error='H')
    url.png('{}.png'.format(game_ID), scale=14)
    generated_qr_image = Image.open('{}.png'.format(game_ID))
    generated_qr_image = generated_qr_image.convert("RGBA")
    box = (135, 135, 235, 235)
    generated_qr_image.crop(box)
    logo = Image.open('pega_logo.jpg')
    imgSmall = logo.resize((256, 256), resample=Image.BILINEAR)
    logo = imgSmall.resize(logo.size, Image.NEAREST).convert('1')
    logo = logo.resize((box[2] - box[0], box[3] - box[1]))
    generated_qr_image.paste(logo, box)
    # generated_qr_image.show()
    generated_qr_image.save(game_ID + ".png")


def get_data_for_game(title):
    bgg = BGGClient()
    g = bgg.game(title)
    # return g.image, g.description, g.min_players, g.max_players, g.min_age, \
    #     g.playing_time / 60, g.rating_average, g.designers
    return g.description
    # publishers = g.publishers
    # image = g.image







