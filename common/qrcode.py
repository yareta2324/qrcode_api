import qrcode
import random
from io import BytesIO
from flask import send_file


def qrcode_module(source_url):
    """ Generation of TWO-DIMENSIONAL code """
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M, version=2, box_size=8, border=2
    )

    # Set qr code color list
    color_list = [
        'black', 'gray', 'green', 'maroon', 'navy', 'purple'
    ]

    # For the loop color list
    for i in range(1):
        qr_color = random.sample(color_list, 1)

    qr.add_data(source_url)
    img = qr.make_image(fill_color=qr_color[0], back_color="white", fit=True)

    byte_io = BytesIO()
    img.save(byte_io, 'png')
    byte_io.seek(0)

    return byte_io


def qrcode_stream(url):
    """ Returns as stream data """
    stream = send_file(qrcode_module(url), mimetype='image/png', cache_timeout=0, add_etags=True)
    return stream
