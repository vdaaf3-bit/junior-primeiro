import os
import shutil

# CAMINHO FIXO PARA ONEDRIVE
pasta_origem = r"C:\Users\Valeria\OneDrive - Instituição Adventista de Ensino\Área de Trabalho\fotos"
pasta_destino = os.path.join(os.path.dirname(pasta_origem), "fotos_organizadas")
os.makedirs(pasta_destino, exist_ok=True)

print(f"\nOrganizando fotos de:\n   {pasta_origem}")
print(f"Para:\n   {pasta_destino}\n")

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
print(f"Abra a pasta: {pasta_destino}")
input("\nPressione Enter para fechar...")