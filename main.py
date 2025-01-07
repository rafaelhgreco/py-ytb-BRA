import os
from yt_dlp import YoutubeDL
from typing import List

def baixar_musicas_youtube(urls: List[str], pasta_download: str = 'musicas_youtube'):
    """
    Baixa múltiplas músicas do YouTube em alta qualidade.
    
    Args:
        urls (List[str]): Lista de URLs das músicas do YouTube
        pasta_download (str, optional): Pasta para salvar as músicas
    """
    # Criar pasta de download se não existir
    os.makedirs(pasta_download, exist_ok=True)
    
    # Configurações do YoutubeDL para download de áudio
    configuracoes_ydl = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(pasta_download, '%(title)s.%(ext)s'),
        # Ignorar downloads de erro
        'ignoreerrors': True,
        # Contornar restrições de idade
        'age_limit': 99,
    }
    
    # Criar objeto YoutubeDL
    with YoutubeDL(configuracoes_ydl) as ydl:
        # Baixar cada música
        for url in urls:
            try:
                print(f"Baixando: {url}")
                # Executar download
                ydl.download([url])
                
            except Exception as e:
                print(f"Erro ao baixar {url}: {e}")

def main():
    # Lista de URLs das músicas do YouTube
    urls_musicas = [
        'https://www.youtube.com/exemplo1',
        'https://www.youtube.com/exemplo2'
        # Adicione mais URLs aqui
    ]
    
    # Pasta de download
    PASTA_DOWNLOAD = 'musicas_youtube'
    
    # Executar download
    baixar_musicas_youtube(urls_musicas, PASTA_DOWNLOAD)

if __name__ == '__main__':
    main()