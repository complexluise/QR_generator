#!/bin/bash

# Script para crear Issue y Pull Request en GitHub
# Requiere: gh (GitHub CLI) autenticado

set -e

echo "🚀 Creando Issue y Pull Request para la app Streamlit"
echo ""

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Verificar que gh está instalado y autenticado
if ! command -v gh &> /dev/null; then
    echo "❌ Error: GitHub CLI (gh) no está instalado"
    echo "Instala desde: https://cli.github.com"
    exit 1
fi

if ! gh auth status &> /dev/null; then
    echo "❌ Error: No estás autenticado en GitHub"
    echo "Ejecuta: gh auth login"
    exit 1
fi

echo "${BLUE}📝 Paso 1: Creando Issue${NC}"
echo ""

# Crear el issue
ISSUE_URL=$(gh issue create \
    --title "Crear aplicación web Streamlit para generación de códigos QR" \
    --label "enhancement" \
    --body-file .github/ISSUE_TEMPLATE.md)

# Extraer número del issue
ISSUE_NUMBER=$(echo "$ISSUE_URL" | grep -oE '[0-9]+$')

echo "${GREEN}✅ Issue creado: #${ISSUE_NUMBER}${NC}"
echo "   URL: ${ISSUE_URL}"
echo ""

echo "${BLUE}🔀 Paso 2: Creando Pull Request${NC}"
echo ""

# Crear el PR
PR_URL=$(gh pr create \
    --title "feat: add streamlit web application for QR generation" \
    --body "$(sed "s/\[ISSUE_NUMBER\]/${ISSUE_NUMBER}/g" .github/PR_TEMPLATE.md)" \
    --base main \
    --head claude/streamlit-qr-generator-VJxPM)

echo "${GREEN}✅ Pull Request creado${NC}"
echo "   URL: ${PR_URL}"
echo "   Closes: #${ISSUE_NUMBER}"
echo ""

echo "🎉 ${GREEN}¡Listo!${NC}"
echo ""
echo "📋 Resumen:"
echo "   - Issue: ${ISSUE_URL}"
echo "   - PR: ${PR_URL}"
echo ""
echo "🚀 Próximos pasos:"
echo "   1. Revisa el PR en GitHub"
echo "   2. Merge cuando estés listo"
echo "   3. Deploy en Streamlit Cloud"
echo ""
