import qrcode


def get_url_and_name(url:str,name:str):
    
    my_qrcode = qrcode.make(url)

    my_qrcode.save(f'{name}.png')