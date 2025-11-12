import os
import shutil

# CAMINHO RELATIVO (FUNCIONA EM QUALQUER PC)
pasta_origem = "fotos"  # Pasta "fotos" ao lado do script
pasta_destino = "fotos_organizadas"
os.makedirs(pasta_destino, exist_ok=True)

print(f"\nOrganizando fotos de:\n   {os.path.abspath(pasta_origem)}")
print(f"Para:\n   {os.path.abspath(pasta_destino)}\n")

contador = 0
for arquivo in os.listdir(pasta_origem):
    caminho_antigo = os.path.join(pasta_origem, arquivo)
    if os.path.isfile(caminho_antigo) and arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
        contador += 1
        extensao = os.path.splitext(arquivo)[1].lower()
        novo_nome = f"foto_{contador:03d}{extensao}"
        caminho_novo = os.path.join(pasta_destino, novo_nome)
        shutil.copy(caminho_antigo, caminho_novo)
        print(f"OK: {arquivo} → {novo_nome}")

print(f"\n{contador} FOTOS ORGANIZADAS COM SUCESSO!")
print(f"Abra a pasta: {os.path.abspath(pasta_destino)}")
input("\nPressione Enter para fechar...")
