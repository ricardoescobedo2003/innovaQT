#!/bin/bash

# Actualizar el sistema e instalar herramientas necesarias
sudo apt update
sudo apt install -y build-essential
sudo apt install -y qt5-default qtcreator qt5-doc qt5-doc-html qtbase5-doc-html qtbase5-examples qtbase5-doc qttools5-dev-tools
sudo apt install python3-pip
# Instalar Qt Designer
sudo apt install -y qttools5-dev-tools

echo "Instalación completa."
