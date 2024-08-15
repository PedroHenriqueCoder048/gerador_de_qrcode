import PySimpleGUI as sg
from interface.layouts import layout
from generator.generator import get_url_and_name

window = sg.Window(title='QRcode Generator',size=(255,240),layout=layout)

while True:
    event , value = window.read()

    if event == sg.WIN_CLOSED or event == 'fechar':
        break
    
    if event == 'btn-qr':
        url = window['inp-url'].get()
        name = window['inp-name'].get()
        if bool(url) == False or bool(name) == False:
            window['text-res'].update('campo nome ou link vazio ')
        
        else:
            get_url_and_name(url=url,name=name)
            window['text-res'].update('qrcode gerado com sucesso! ')
        
