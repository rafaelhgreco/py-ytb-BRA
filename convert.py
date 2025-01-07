import subprocess
import os
from pathlib import Path
import sys

# Configurar a codificação para UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# IMPORTANTE: Ajuste este caminho para onde você extraiu o ffmpeg
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

def converter_para_mp3(pasta_origem):
    # Verificar se o ffmpeg existe
    if not os.path.exists(FFMPEG_PATH):
        print(f"ERRO: ffmpeg não encontrado em {FFMPEG_PATH}")
        return
    
    # Lista de extensões de áudio/vídeo suportadas
    extensoes_suportadas = ['.wav', '.m4a', '.wma', '.aac', '.ogg', '.flac', '.mp4', '.webm']
    
    # Verificar se a pasta existe
    if not os.path.exists(pasta_origem):
        print(f"A pasta {pasta_origem} não foi encontrada!")
        return
    
    # Listar arquivos na pasta
    arquivos = os.listdir(pasta_origem)
    if not arquivos:
        print("A pasta está vazia!")
        return
    
    print(f"Encontrados {len(arquivos)} arquivos na pasta.")
    
    # Criar pasta para arquivos convertidos
    pasta_destino = os.path.join(pasta_origem, 'convertidos_mp3')
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Pasta de destino criada: {pasta_destino}")
    
    # Converter arquivos
    for arquivo in arquivos:
        try:
            caminho_arquivo = os.path.join(pasta_origem, arquivo)
            
            if not os.path.isfile(caminho_arquivo):
                continue
                
            extensao = Path(arquivo).suffix.lower()
            if extensao not in extensoes_suportadas:
                continue
            
            print(f"\nProcessando: {arquivo}")
            
            # Preparar nome do arquivo de saída
            nome_sem_extensao = os.path.splitext(arquivo)[0]
            nome_seguro = ''.join(c for c in nome_sem_extensao if c.isalnum() or c in (' ', '-', '_'))
            arquivo_mp3 = os.path.join(pasta_destino, f"{nome_seguro}.mp3")
            
            # Comando do ffmpeg
            comando = [
                FFMPEG_PATH,
                '-i', caminho_arquivo,
                '-codec:a', 'libmp3lame',
                '-q:a', '2',
                arquivo_mp3
            ]
            
            # Executar conversão
            print("Iniciando conversão...")
            processo = subprocess.run(
                comando,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore'
            )
            
            if processo.returncode == 0:
                print(f"Sucesso: {arquivo} convertido para MP3")
            else:
                print(f"Erro ao converter {arquivo}:")
                print(processo.stderr)
            
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {str(e)}")

if __name__ == "__main__":
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    pasta_origem = os.path.join(pasta_script, "musicas_youtube")
    
    print(f"Pasta de origem: {pasta_origem}")
    print("Iniciando processo de conversão...")
    converter_para_mp3(pasta_origem)
    print("\nProcesso finalizado!")