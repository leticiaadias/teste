# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
# https:// dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
# pyautogui.click -> clicar com o mouse 
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE =0.3

# PASSO 1 
# abrir o chrome
pyautogui.press(“win”)
pyautogui.write(“chrome”)
pyautogui .press(“enter”)

# entrar no link
link = “https:// dlp.hashtagtreinamentos.com/python/intensivao/login”
pyautogui.white(link)
pyautogui.press(“enter”)

# esperar o site carregar
time.sleep(3)
