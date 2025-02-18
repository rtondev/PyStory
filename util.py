from colorama import init, Fore, Style
import time
import sys
import platform
import random
from resources import TYPE_SOUND, VICTORY_SOUND, GAMEOVER_SOUND
import os
import winsound

# Configuração do som baseada no sistema operacional
if platform.system() == "Windows":
    def play_type_sound():
        try:
            winsound.PlaySound(TYPE_SOUND, winsound.SND_ASYNC | winsound.SND_NOSTOP)
        except:
            # Som alternativo caso dê erro
            winsound.Beep(random.randint(800, 1000), 10)

    def play_victory_sound():
        try:
            winsound.PlaySound(VICTORY_SOUND, winsound.SND_FILENAME)
        except:
            # Som alternativo de vitória
            for _ in range(3):
                winsound.Beep(1000, 100)
                time.sleep(0.05)
            winsound.Beep(1500, 300)

    def play_gameover_sound():
        try:
            winsound.PlaySound(GAMEOVER_SOUND, winsound.SND_FILENAME)
        except:
            # Som alternativo de derrota
            for _ in range(3):
                winsound.Beep(400, 200)
            winsound.Beep(300, 400)
elif platform.system() == "Darwin":  # MacOS
    import os
    def play_type_sound():
        os.system("afplay /System/Library/Sounds/Tink.aiff")
else:  # Linux
    import os
    def play_type_sound():
        os.system("play -q -n synth 0.1 sine 800 2>/dev/null || true")

# Inicializa o colorama com autoreset=True e força o uso de cores no Windows
init(autoreset=True, convert=True, strip=False)

class JogoUtil:
    @staticmethod
    def print_slow(text, delay=0):
        """Imprime o texto diretamente"""
        print(text)

    @staticmethod
    def play_ending_sound(is_victory):
        """Toca o som apropriado para o final do jogo"""
        if is_victory:
            play_victory_sound()
        else:
            play_gameover_sound()

    @staticmethod
    def exibir_opcoes(opcoes):
        print(f"\n{Fore.YELLOW}Suas opções:{Style.RESET_ALL}\n")
        for i, opcao in enumerate(opcoes, 1):
            print(f"{Fore.CYAN}[{i}]{Style.RESET_ALL} {Fore.GREEN}{opcao}{Style.RESET_ALL}")
        
        while True:
            try:
                escolha = int(input(f"\n{Fore.YELLOW}Digite sua escolha (1-{len(opcoes)}): {Style.RESET_ALL}")) - 1
                if 0 <= escolha < len(opcoes):
                    return escolha
                print(f"{Fore.RED}Opção inválida! Tente novamente.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Por favor, digite um número válido!{Style.RESET_ALL}")