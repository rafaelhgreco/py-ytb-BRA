from pytube import Playlist
import csv

def extrair_links_playlist(url_playlist: str):
    """
    Extrai todos os links de vídeos de uma playlist do YouTube.
    
    Args:
        url_playlist (str): URL da playlist do YouTube
    
    Returns:
        List[str]: Lista de links dos vídeos na playlist
    """
    try:
        # Criar objeto Playlist
        playlist = Playlist(url_playlist)
        
        # Lista para armazenar os links formatados
        links_musicas = [f"'{link}'," for link in playlist.video_urls]
        
        print(f"Total de músicas encontradas: {len(links_musicas)}")
        
        return links_musicas
    
    except Exception as e:
        print(f"Erro ao extrair playlist: {e}")
        return []

def main():
    # URL da playlist do YouTube (cole aqui a URL completa)
    url_playlist = 'LINK-DA-PLAYLIST'
    
    # Extrair links
    links_musicas = extrair_links_playlist(url_playlist)
    
    # Imprimir links
    if links_musicas:
        print("\nLinks das músicas:")
        for link in links_musicas:
            print(link)

if __name__ == '__main__':
    main()