#!/bin/bash
# =============================================================
# Setup del repositorio GitHub para computer_vision_2_tp
# Ejecutar desde la carpeta raíz del proyecto:
#   chmod +x setup_github.sh && ./setup_github.sh
# =============================================================

set -e  # detener si hay errores

REPO_NAME="computer_vision_2_tp"
GITHUB_USER="spardo83"   # <--- tu usuario de GitHub

echo "=========================================="
echo "  Setup GitHub: $GITHUB_USER/$REPO_NAME"
echo "=========================================="

# 1. Inicializar git (si no está ya inicializado)
if [ ! -d ".git" ]; then
    git init
    echo "✅ Repositorio git inicializado"
else
    echo "ℹ️  Repositorio git ya existe"
fi

# 2. Configurar usuario git (si no está configurado)
if [ -z "$(git config user.name)" ]; then
    git config user.name "Sebastian Pardo"
    git config user.email "spardo83@gmail.com"
    echo "✅ Usuario git configurado"
fi

# 3. Agregar todos los archivos iniciales
git add pyproject.toml .gitignore README.md
git add notebooks/
git add src/
git add data/.gitkeep models/.gitkeep runs/.gitkeep videos/.gitkeep 2>/dev/null || true

# 4. Primer commit
git commit -m "feat: initial project structure

- 4 Jupyter notebooks (setup, training, comparison, tracking demo)
- pyproject.toml con uv (ultralytics, roboflow, jupyter)
- PPEComplianceTracker con ByteTrack integration
- README con instrucciones completas"

echo "✅ Commit inicial creado"

# 5. Crear rama main
git branch -M main

# 6. Crear el repositorio en GitHub con gh CLI
echo ""
echo "Creando repositorio público en GitHub..."
echo "(Se necesita gh CLI instalado y autenticado)"
echo ""

if command -v gh &> /dev/null; then
    gh repo create "$REPO_NAME" \
        --public \
        --description "Sistema de Monitoreo Automático de EPP en Obras de Construcción | YOLO + ByteTrack" \
        --source=. \
        --remote=origin \
        --push
    echo ""
    echo "✅ Repositorio creado y código publicado!"
    echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
else
    echo "⚠️  gh CLI no encontrado. Pasos manuales:"
    echo ""
    echo "1. Ir a https://github.com/new"
    echo "   - Nombre: $REPO_NAME"
    echo "   - Visibilidad: Public"
    echo "   - NO inicializar con README"
    echo ""
    echo "2. Ejecutar estos comandos:"
    echo "   git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git"
    echo "   git push -u origin main"
    echo ""
fi
