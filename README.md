# GAAP Process Datasets 🏭📊

Bem-vindo ao **GAAP Process Datasets**! 

Este é um repositório aberto e centralizado de datasets públicos focados em **Detecção e Diagnóstico de Falhas (FDD - Fault Detection and Diagnosis)**, anomalias e monitoramento de condições. Ele foi criado para facilitar a vida de estudantes, pesquisadores e profissionais de Engenharia Química e de Processos que precisam de dados confiáveis para testar seus modelos.

## 📦 Datasets Disponíveis

Atualmente, nossa ferramenta permite o download automático dos seguintes benchmarks:

1. **3W Dataset (Petrobras):** Dados reais e simulados de eventos indesejáveis em poços de petróleo offshore.
2. **Tennessee Eastman Process (TEP):** O benchmark clássico de simulação de processos químicos para testar algoritmos de controle e monitoramento.
3. **WAID Dataset (Petrobras):** Base de dados focada em incidentes e integridade de poços.
4. **CWRU Bearing Dataset:** O padrão ouro para manutenção preditiva e análise de vibração em rolamentos de equipamentos rotativos.

---

## 🚀 Como baixar e utilizar os dados

Como esses arquivos de dados são muito pesados, eles não ficam armazenados diretamente aqui no GitHub. Nós criamos um **gerenciador automático em Python** para que você possa escolher e baixar apenas os datasets que realmente vai usar, direto para o seu computador.

Siga o passo a passo abaixo, mesmo que você não tenha experiência com programação!

### Passo 1: Tenha o Python instalado
Para rodar o baixador automático, você precisa ter o Python instalado no seu computador. Se não tiver, baixe e instale a versão mais recente em [python.org](https://www.python.org/downloads/). 
*(Dica para Windows: durante a instalação do Python, não esqueça de marcar a caixinha "Add Python to PATH").*

### Passo 2: Baixe este repositório para o seu computador
Você tem duas opções para fazer isso:

**Opção A (Para iniciantes):** 
1. No topo desta página, clique no botão verde escrito **"<> Code"**.
2. Clique em **"Download ZIP"**.
3. Extraia a pasta `.zip` em algum lugar do seu computador (como a Área de Trabalho).

**Opção B (Para quem usa Git):**
Abra o seu terminal e digite:
```bash
git clone [https://github.com/SEU_USUARIO/gaap-process-datasets.git](https://github.com/SEU_USUARIO/gaap-process-datasets.git)
cd gaap-process-datasets
```
*(Lembre-se de substituir `SEU_USUARIO` pelo seu usuário real do GitHub)*

### Passo 3: Prepare o ambiente
Abra o terminal (ou Prompt de Comando / CMD no Windows), navegue até a pasta onde você salvou este projeto e instale as duas bibliotecas necessárias digitando o comando abaixo e apertando Enter:
```bash
pip install requests tqdm
```

### Passo 4: Rode o gerenciador e baixe seus dados!
No mesmo terminal, digite o comando abaixo para iniciar o painel interativo:
```bash
python download_datasets.py
```
Um menu vai aparecer na sua tela! Basta digitar o número correspondente ao dataset que você quer baixar e apertar Enter. O script fará o download e a extração sozinhos. 

**Onde os dados vão parar?**
Todos os arquivos extraídos aparecerão dentro de uma pasta chamada `data/`, que será criada automaticamente na mesma pasta do projeto.
