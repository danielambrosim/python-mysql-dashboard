#!/bin/bash

echo "=================================================="
echo "🚀 Iniciando Setup do Projeto de Gestão Comercial!"
echo "=================================================="

# 1. Clone o repositório
echo "📦 Clonando repositório do GitHub..."
git clone https://github.com/seuusuario/projeto_gestao.git
cd projeto_gestao || exit

echo "✅ Repositório clonado."

# 2. Crie e ative o ambiente virtual
echo "🐍 Criando ambiente virtual Python..."
python -m venv .venv

echo "👉 Ative o ambiente virtual:"
echo "   Windows: .venv\\Scripts\\activate"
echo "   Linux/Mac: source .venv/bin/activate"
echo "⚠️  ATIVE o ambiente e pressione [ENTER] para continuar."
read -r

# 3. Instale as dependências
echo "📚 Instalando dependências..."
pip install -r requirements.txt

# 4. Crie o banco de dados MySQL
echo "💾 Criando banco de dados MySQL (ajuste usuário/senha se necessário)..."
echo "Digite seu usuário MySQL (ex: root):"
read USUARIO
echo "Digite sua senha MySQL (vai aparecer em branco, digite e pressione ENTER):"
read -s SENHA

mysql -u"$USUARIO" -p"$SENHA" -e "CREATE DATABASE IF NOT EXISTS gestao_vendas;"

echo "✅ Banco de dados criado (gestao_vendas)."

# 5. Configure suas credenciais no arquivo db.py
echo "✏️  Lembre-se de editar o arquivo 'db.py' e inserir suas credenciais de conexão MySQL!"
echo "Pressione [ENTER] quando já tiver editado."
read -r

# 6. Crie as tabelas no banco
echo "🔨 Criando tabelas no banco de dados..."
python scripts/criar_tabelas.py

# 7. (Opcional) Popule com dados de exemplo
echo "Deseja popular o banco com dados de exemplo? [s/n]"
read POPULAR
if [ "$POPULAR" = "s" ]; then
  python scripts/seed.py
fi

# 8. Execute o dashboard
echo "🎯 Iniciando dashboard financeiro no navegador..."
streamlit run dashboard.py

echo "=========================================="
echo "🎉 Projeto rodando! Bom proveito!"
echo "=========================================="
