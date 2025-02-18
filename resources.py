import os
from base import Item  # Adicionando importação da classe Item

# Diretório dos recursos
RESOURCES_DIR = os.path.join(os.path.dirname(__file__), 'resources')

# Criar diretório se não existir
if not os.path.exists(RESOURCES_DIR):
    os.makedirs(RESOURCES_DIR)

# Caminhos para os arquivos de som
TYPE_SOUND = os.path.join(RESOURCES_DIR, 'teclado.wav')
VICTORY_SOUND = os.path.join(RESOURCES_DIR, 'victory.wav')
GAMEOVER_SOUND = os.path.join(RESOURCES_DIR, 'gameover.wav')
ITEM_FOUND_SOUND = os.path.join(RESOURCES_DIR, 'item.wav')
ACHIEVEMENT_SOUND = os.path.join(RESOURCES_DIR, 'achievement.wav')
DANGER_SOUND = os.path.join(RESOURCES_DIR, 'danger.wav')
WATER_SOUND = os.path.join(RESOURCES_DIR, 'water.wav')
FOOTSTEPS_SOUND = os.path.join(RESOURCES_DIR, 'footsteps.wav')
CAVE_AMBIENT_SOUND = os.path.join(RESOURCES_DIR, 'cave.wav')

# Itens iniciais
ITENS_INICIAIS = {
    "Lanterna": Item("Lanterna", "Uma lanterna com bateria limitada", "🔦"),
    "Celular": Item("Celular", "Celular com sinal fraco e pouca bateria", "📱"),
    "Água": Item("Água", "Garrafa com água potável", "💧"),
    "Caderno": Item("Caderno", "Caderno para anotações", "📝")
}

# Conquistas
CONQUISTAS = {
    "explorador_nato": "🎯 Explorador Nato - Descobriu 3 áreas diferentes",
    "sobrevivente": "🛡️ Sobrevivente Cauteloso - Manteve todos os status acima de 50%",
    "cientista": "🔬 Cientista Curioso - Coletou 5 amostras diferentes",
    "cartografo": "🗺️ Cartógrafo Amador - Mapeou uma área inexplorada",
    "mestre_mina": "👑 Mestre da Mina - Completou todas as conquistas"
}

# Eventos aleatórios
EVENTOS = [
    {
        "nome": "Encontro com Morcegos",
        "descricao": "Um grupo de morcegos voa agitado pela caverna!",
        "emoji": "🦇",
        "efeitos": {"sanidade": -10, "energia": -5}
    },
    {
        "nome": "Goteira Misteriosa",
        "descricao": "Gotas de água mineral caem do teto...",
        "emoji": "💧",
        "efeitos": {"hidratacao": +10}
    },
    {
        "nome": "Pegadas Antigas",
        "descricao": "Você encontra pegadas misteriosas no chão...",
        "emoji": "👣",
        "efeitos": {"conhecimento": +5}
    }
] 