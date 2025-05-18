#!/bin/bash

# Remover o remote atual (caso exista)
git remote remove origin

# Adicionar o remote correto
git remote add origin https://github.com/logicadosabor/app.git

# Mudar o nome da branch para main
git branch -M main

# Push para o repositório
git push -u origin main

# Verificar status
git remote -v
