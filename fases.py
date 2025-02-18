from base import Fase
from util import JogoUtil
from colorama import Fore, Style, init

# Inicializa o colorama com autoreset=True
init(autoreset=True)

class FaseInicial(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.YELLOW}⭐ A AVENTURA COMEÇA! ⭐{Style.RESET_ALL}

Você, {Fore.CYAN}{self.nome_jogador}{Style.RESET_ALL}, é um estudante apaixonado por geologia do IFRN.
Durante uma visita técnica à histórica Mina Brejuí, em Currais Novos, 
sua curiosidade o leva a se separar do grupo enquanto observava um 
mineral particularmente fascinante.

{Fore.RED}😰 Agora você está sozinho nos túneis escuros da mina...{Style.RESET_ALL}
Precisa tomar uma decisão:"""

        self.opcoes = [
            "🧘‍♂️ Esperar no lugar",
            "🏃‍♂️ Explorar os túneis",
            "🔍 Procurar outro caminho",
            "↩️ Voltar tentando refazer seus passos"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}══════════════════════════════════════════{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🏔️  MINA BREJUÍ - O INÍCIO  🏔️{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}══════════════════════════════════════════{Style.RESET_ALL}\n")
        
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        
        if escolha == 0:
            return FaseEspera(self.nome_jogador)
        elif escolha == 1:
            return FaseExplorar(self.nome_jogador)
        elif escolha == 2:
            return FaseProcurar(self.nome_jogador)
        else:
            return FaseVoltar(self.nome_jogador)

class FaseEspera(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Você decide esperar, seguindo as instruções de segurança.
Enquanto aguarda, ouve sons estranhos...{Style.RESET_ALL}

{Fore.YELLOW}O que fazer?{Style.RESET_ALL}"""
        
        self.opcoes = [
            "🧘‍♂️ Manter a calma e meditar",
            "👂 Tentar identificar os sons",
            "📢 Gritar por ajuda"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 1 DE 7 - A ESPERA  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseEspera2(self.nome_jogador)

class FaseEspera2(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}O tempo passa lentamente na escuridão.
Seu celular ainda tem um pouco de bateria.{Style.RESET_ALL}

{Fore.YELLOW}Como usar o celular?{Style.RESET_ALL}"""
        
        self.opcoes = [
            "🔦 Usar como lanterna",
            "📱 Tentar ligação",
            "🎮 Economizar bateria"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 2 DE 7 - O CELULAR  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseEspera3(self.nome_jogador)

class FaseEspera3(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Você começa a sentir fome e sede.
Na sua mochila tem alguns itens.{Style.RESET_ALL}

{Fore.YELLOW}O que pegar?{Style.RESET_ALL}"""
        
        self.opcoes = [
            "🍫 Barra de chocolate",
            "💧 Garrafa d'água",
            "🔋 Bateria reserva"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 3 DE 7 - OS RECURSOS  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseEspera4(self.nome_jogador)

class FaseEspera4(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Passos ecoam pela caverna.
Parecem se aproximar...{Style.RESET_ALL}

{Fore.YELLOW}Como reagir?{Style.RESET_ALL}"""
        
        self.opcoes = [
            "🤫 Ficar em silêncio",
            "📢 Chamar por ajuda",
            "🏃 Mudar de lugar"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 4 DE 7 - OS PASSOS  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseEspera5(self.nome_jogador)

class FaseEspera5(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Uma luz fraca aparece ao longe.
Parece se mover lentamente.{Style.RESET_ALL}

{Fore.YELLOW}O que fazer?{Style.RESET_ALL}"""
        
        self.opcoes = [
            "💡 Acenar para a luz",
            "📝 Anotar a direção",
            "👀 Observar sem movimento"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 5 DE 7 - A LUZ DISTANTE  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseEspera6(self.nome_jogador)

class FaseEspera6(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Vozes começam a ficar mais claras.
Parecem ser do grupo de resgate.{Style.RESET_ALL}

{Fore.YELLOW}Como proceder?{Style.RESET_ALL}"""
        
        self.opcoes = [
            "🗣️ Gritar mais alto",
            "🚶 Ir em direção às vozes",
            "📱 Usar lanterna do celular"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 6 DE 7 - AS VOZES  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseEspera7(self.nome_jogador)

class FaseEspera7(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}O resgate está próximo, mas você ouve um pedido de socorro.
Alguém mais parece estar perdido.{Style.RESET_ALL}

{Fore.YELLOW}Decisão final:{Style.RESET_ALL}"""
        
        self.opcoes = [
            "🦸 Tentar ajudar sozinho",
            "🚨 Avisar ao resgate",
            "⏳ Esperar mais um pouco"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 7 DE 7 - A DECISÃO FINAL  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        
        if escolha == 0:
            return FinalDerrota(self.nome_jogador, "Sua coragem foi maior que sua prudência...")
        elif escolha == 1:
            return FinalVitorioso(self.nome_jogador)
        else:
            return FinalNeutro(self.nome_jogador)

class FaseExplorar(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Você decide explorar os túneis.
Logo encontra uma bifurcação:{Style.RESET_ALL}

{Fore.YELLOW}🌊 Um túnel com som de água corrente
🗿 Outro com antigas marcações nas paredes{Style.RESET_ALL}"""
        
        self.opcoes = [
            "💧 Seguir o som da água",
            "📝 Seguir as marcações antigas"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 1 DE 7 - A BIFURCAÇÃO  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseExplorar2(self.nome_jogador)

class FaseExplorar2(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Avançando pelo túnel, você encontra equipamentos antigos.
O que examinar primeiro?{Style.RESET_ALL}

{Fore.YELLOW}⛏️ Uma picareta enferrujada
🪜 Uma escada de corda
🔦 Uma lanterna antiga{Style.RESET_ALL}"""
        
        self.opcoes = [
            "Examinar a picareta",
            "Verificar a escada",
            "Testar a lanterna"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 2 DE 7 - OS EQUIPAMENTOS  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseExplorar3(self.nome_jogador)

class FaseExplorar3(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Um desabamento bloqueia parte do caminho.
Como prosseguir?{Style.RESET_ALL}

{Fore.YELLOW}🕳️ Uma pequena passagem entre as rochas
↗️ Tentar escalar por cima
↩️ Procurar outro caminho{Style.RESET_ALL}"""
        
        self.opcoes = [
            "Passar entre as rochas",
            "Escalar o bloqueio",
            "Buscar rota alternativa"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 3 DE 7 - O OBSTÁCULO  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseExplorar4(self.nome_jogador)

class FaseExplorar4(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Você encontra marcações estranhas na parede.
O que fazer?{Style.RESET_ALL}

{Fore.YELLOW}📝 Tentar decifrar os símbolos
📸 Fotografar com o celular
➡️ Seguir a direção indicada{Style.RESET_ALL}"""
        
        self.opcoes = [
            "Estudar os símbolos",
            "Registrar com foto",
            "Seguir as indicações"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 4 DE 7 - AS MARCAÇÕES  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseExplorar5(self.nome_jogador)

class FaseExplorar5(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}O túnel se divide em três caminhos.
Qual escolher?{Style.RESET_ALL}

{Fore.YELLOW}💨 Um com corrente de ar
🌊 Um com som de água
💡 Um com reflexo de luz{Style.RESET_ALL}"""
        
        self.opcoes = [
            "Seguir a corrente de ar",
            "Ir em direção à água",
            "Investigar a luz"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 5 DE 7 - A ESCOLHA  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseExplorar6(self.nome_jogador)

class FaseExplorar6(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Você ouve vozes distantes.
Como proceder?{Style.RESET_ALL}

{Fore.YELLOW}🗣️ Gritar por ajuda
👂 Tentar ouvir melhor
🏃 Correr na direção{Style.RESET_ALL}"""
        
        self.opcoes = [
            "Chamar por socorro",
            "Escutar atentamente",
            "Correr até as vozes"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 6 DE 7 - AS VOZES  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseExplorar7(self.nome_jogador)

class FaseExplorar7(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Você encontra uma saída, mas também vê equipamentos valiosos.
O que fazer?{Style.RESET_ALL}

{Fore.YELLOW}🚪 Sair imediatamente
💎 Coletar amostras importantes
📱 Chamar ajuda e esperar{Style.RESET_ALL}"""
        
        self.opcoes = [
            "Sair da mina",
            "Coletar amostras",
            "Esperar resgate"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 7 DE 7 - DECISÃO FINAL  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        
        if escolha == 0:
            return FinalVitorioso(self.nome_jogador)
        elif escolha == 1:
            return FinalDerrota(self.nome_jogador, "A ganância por descobertas causou sua perdição...")
        else:
            return FinalNeutro(self.nome_jogador)

class FaseAgua(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Você encontra um riacho subterrâneo.
Como prosseguir?{Style.RESET_ALL}

{Fore.YELLOW}🌊 Seguir o curso d'água
🏊 Atravessar nadando
🔍 Procurar uma ponte{Style.RESET_ALL}"""
        
        self.opcoes = [
            "Seguir a corrente",
            "Atravessar nadando",
            "Procurar uma forma de atravessar"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 5 DE 7 - O RIACHO  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseLuz(self.nome_jogador)

class FaseLuz(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Você vê uma luz fraca ao longe.
Como proceder?{Style.RESET_ALL}

{Fore.YELLOW}🚶 Aproximar-se devagar
🏃 Correr até a luz
📢 Chamar por ajuda{Style.RESET_ALL}"""
        
        self.opcoes = [
            "Aproximar com cautela",
            "Correr até a luz",
            "Gritar por ajuda"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 6 DE 7 - A LUZ  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        return FaseDecisaoFinal(self.nome_jogador)

class FaseDecisaoFinal(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.descricao = f"""
{Fore.CYAN}Você encontra uma saída, mas ouve pedidos de socorro.
O que fazer?{Style.RESET_ALL}

{Fore.YELLOW}🚪 Sair e buscar ajuda
🦸 Tentar ajudar sozinho
⏳ Esperar mais pessoas chegarem{Style.RESET_ALL}"""
        
        self.opcoes = [
            "Sair e buscar ajuda",
            "Tentar ajudar agora",
            "Aguardar reforços"
        ]

    def executar(self):
        print(f"\n{Fore.YELLOW}🔍  ETAPA 7 DE 7 - A DECISÃO FINAL  🔍{Style.RESET_ALL}")
        JogoUtil.print_slow(self.descricao)
        escolha = JogoUtil.exibir_opcoes(self.opcoes)
        
        if escolha == 0:
            return FinalVitorioso(self.nome_jogador)
        elif escolha == 1:
            return FinalDerrota(self.nome_jogador, "Sua coragem foi maior que sua prudência...")
        else:
            return FinalNeutro(self.nome_jogador)

class FinalVitorioso(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
    
    def executar(self):
        mensagem = f"""
{Fore.GREEN}🌟 VITÓRIA! 🌟{Style.RESET_ALL}

Parabéns, {Fore.CYAN}{self.nome_jogador}{Style.RESET_ALL}! 
Você conseguiu encontrar o caminho de volta em segurança!

{Fore.YELLOW}🏆 Sua aventura termina com sucesso!{Style.RESET_ALL}"""
        
        JogoUtil.print_slow(mensagem)
        return None

class FinalDerrota(Fase):
    def __init__(self, nome_jogador, mensagem):
        self.nome_jogador = nome_jogador
        self.mensagem = mensagem
    
    def executar(self):
        mensagem = f"""
{Fore.RED}💀 FIM DE JOGO 💀{Style.RESET_ALL}

Infelizmente, {Fore.CYAN}{self.nome_jogador}{Style.RESET_ALL}, 
você se perdeu nas profundezas da mina...

{Fore.RED}☠️ Sua aventura termina aqui...{Style.RESET_ALL}

{Fore.RED}{self.mensagem}{Style.RESET_ALL}"""
        
        JogoUtil.print_slow(mensagem)
        return None

class FinalNeutro(Fase):
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
    
    def executar(self):
        mensagem = f"""
{Fore.YELLOW}⚠️ FINAL ALTERNATIVO ⚠️{Style.RESET_ALL}

{Fore.CYAN}{self.nome_jogador}{Style.RESET_ALL}, você sobreviveu, 
mas sua aventura teve consequências inesperadas...

{Fore.YELLOW}🤔 Nem toda escolha leva ao melhor caminho...{Style.RESET_ALL}"""
        
        JogoUtil.print_slow(mensagem)
        return None