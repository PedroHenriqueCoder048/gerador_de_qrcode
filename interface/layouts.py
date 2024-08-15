import PySimpleGUI as sg

path_image = '/home/phenrique/Documentos/qrcoder/interface/qrcode.png'

layout = [
    [sg.Text('nome do qrcode')],
    [sg.Input(key='inp-name')],
    [sg.Text('link')],
    [sg.Input(key='inp-url')],
    [sg.Button('QRcode',key='btn-qr'),sg.Button('fechar')],
    [sg.Text('',key='text-res')]
]