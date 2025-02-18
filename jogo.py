from fases import FaseInicial
from colorama import init, Fore, Style
import os
import time

init(autoreset=True)

class Jogo:
    def __init__(self):
        self.limpar_tela()
        self.apresentar_jogo()
        self.nome_jogador = self.obter_nome()
        self.fase_atual = FaseInicial(self.nome_jogador)

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def apresentar_jogo(self):
        print(f"{Fore.YELLOW}══════════════════════════════════════════{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}        AVENTURA NA MINA BREJUÍ{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}══════════════════════════════════════════{Style.RESET_ALL}")
        print()
        print(f"{Fore.CYAN}Uma emocionante aventura nas profundezas{Style.RESET_ALL}")
        print(f"{Fore.CYAN}da histórica mina de scheelita!{Style.RESET_ALL}")
        print()
        time.sleep(1)

    def obter_nome(self):
        while True:
            nome = input(f"{Fore.YELLOW}Digite seu nome para começar: {Style.RESET_ALL}").strip()
            if nome:
                print(f"\n{Fore.GREEN}Bem-vindo(a), {nome}!{Style.RESET_ALL}")
                time.sleep(1)
                self.limpar_tela()
                return nome
            print(f"{Fore.RED}Por favor, digite um nome válido!{Style.RESET_ALL}")

    def jogar(self):
        while self.fase_atual:
            self.fase_atual = self.fase_atual.executar()
            if not self.fase_atual:
                self.perguntar_jogar_novamente()

    def perguntar_jogar_novamente(self):
        while True:
            escolha = input(f"\n{Fore.YELLOW}Quer jogar novamente? (sim/nao): {Style.RESET_ALL}").strip().lower()
            if escolha == 'sim':
                self.limpar_tela()
                self.nome_jogador = self.obter_nome()
                self.fase_atual = FaseInicial(self.nome_jogador)
                break
            elif escolha == 'nao':
                print(f"\n{Fore.CYAN}Obrigado por jogar! Até a próxima aventura!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Por favor, responda com 'sim' ou 'nao'{Style.RESET_ALL}")

if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()