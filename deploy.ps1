# Deploy Script
$ErrorActionPreference = "Stop"

Write-Host "Iniciando configuração do Git..."

# .gitignore
if (-not (Test-Path ".gitignore")) {
    ".venv/" | Out-File ".gitignore" -Encoding utf8
    "__pycache__/" | Out-File ".gitignore" -Append -Encoding utf8
    ".gemini/" | Out-File ".gitignore" -Append -Encoding utf8
    Write-Host ".gitignore criado."
}

# Init
if (-not (Test-Path ".git")) {
    git init
    Write-Host "Repositório git iniciado."
}

# Add & Commit
git add .
try {
    git commit -m "App de Treino - Versão Final"
    Write-Host "Arquivos commitados."
} catch {
    Write-Host "Nada para commitar ou erro no commit (pode ser ignorado se já estiver tudo limpo)."
}

# Branch
git branch -M main

# Remote
try {
    git remote add origin https://github.com/idarlandias/Treino_App.git
    Write-Host "Remote adicionado."
} catch {
    Write-Host "Remote 'origin' já existe. Atualizando URL..."
    git remote set-url origin https://github.com/idarlandias/Treino_App.git
}

# Push
Write-Host "Tentando fazer push (pPode pedir senha na janela de popup)..."
try {
    git push -u origin main
    Write-Host "SUCESSO! Código enviado para o GitHub."
} catch {
    Write-Host "ERRO NO PUSH: Provavelmente precisa de autenticação."
    Write-Host "Por favor, rode 'git push -u origin main' no terminal e insira suas credenciais."
    exit 1
}
