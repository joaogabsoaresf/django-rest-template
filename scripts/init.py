import subprocess
import sys

def main():
    # O shell irá encerrar a execução do script quando um comando falhar
    try:
        print("Iniciando criação do ambiente python virtual.")
        subprocess.run(["python3", "-m", "venv", "venv"], check=True)
        print("Ambiente criado com sucesso.")
        subprocess.run(["venv/bin/pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run(["venv/bin/pip", "install", "-r", "core/requirements.txt"], check=True)
        
        subprocess.run(["git", "init"], check=True)
        print("Git inicilizado com sucesso.")
        
        print("Ative o ambiente com o comando: source venv/bin/activate")
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}", file=sys.stderr)
        sys.exit(1)
