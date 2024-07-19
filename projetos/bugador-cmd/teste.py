import os

# Nome do arquivo .bat
bat_filename = "script.bat"

# Cria um arquivo .bat com os comandos desejados
with open(bat_filename, "w") as file:
    file.write("dlgfkSDLFSFOSDFOSDKFSDFKSJDFSIJFSPFSDPIFJSDIFJSDIFJSDIFOSJFSJFSIFJSFOJSDOFJSFSDSDSD\n")

# Abre o cmd e executa o arquivo .bat
while True:
    os.system(f"start cmd /k {bat_filename}")

# Opcional: remover o arquivo .bat após a execução
# os.remove(bat_filename)
