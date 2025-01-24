# YouTube Playlist Music Downloader

Sistema para download automático de músicas de playlists do YouTube.

## Pré-requisitos

- Python 3.x
- FFmpeg instalado e configurado nas variáveis de ambiente
- Bibliotecas Python necessárias (instale via pip):
  ```
  pip install yt-dlp ffmpeg-python typing
  ```

## Estrutura do Projeto

```
.
├── extract.py
├── main.py
└── musicas_youtube/
```

## Instruções de Uso

### 1. Extração dos Links da Playlist

1. Abra o arquivo `extract.py`
2. Localize a variável `url_playlist`
3. Adicione o link da playlist do YouTube:
   ```python
   url_playlist = 'LINK-DA-PLAYLIST'
   ```
4. Execute o script para gerar o arquivo CSV com os links:
   ```bash
   python extract.py
   ```

### 2. Download das Músicas

1. Abra o arquivo `main.py`
2. Localize a seção `# Lista de URLs das músicas do YouTube`
3. Adicione os links extraídos:
   ```python
   urls_musicas = [
       'link1',
       'link2',
       ...
   ]
   ```
4. Execute o script:
   ```bash
   python main.py
   ```

### 3. Configuração do FFmpeg

1. Baixe o FFmpeg do site oficial
2. Adicione o FFmpeg nas Variáveis de Ambiente do sistema
3. Verifique a instalação:
   ```bash
   ffmpeg -version
   ```

### Estrutura de Pastas

- Certifique-se de que existe uma pasta chamada `musicas_youtube` no diretório do projeto
- Os arquivos baixados serão convertidos e salvos nesta pasta

## Notas Importantes

- Verifique se todos os links da playlist são válidos
- Mantenha o FFmpeg atualizado
- Certifique-se de ter permissão para download do conteúdo
