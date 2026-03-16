# GAAP Process Datasets 🏭📊

Um repositório aberto e centralizado de datasets públicos focados em **Detecção e Diagnóstico de Falhas (FDD - Fault Detection and Diagnosis)**, anomalias e monitoramento de condições para Engenharia Química e de Processos.

## 📦 Datasets Disponíveis

Atualmente, o script de download fornece acesso aos seguintes benchmarks:

1. **3W Dataset (Petrobras):** Dados reais e simulados de eventos indesejáveis em poços de petróleo offshore.
2. **Tennessee Eastman Process (TEP):** O benchmark clássico de simulação de processos químicos para testar algoritmos de controle e monitoramento.
3. **WAID Dataset (Petrobras):** Base de dados focada em incidentes e integridade de poços.
4. **CWRU Bearing Dataset:** O padrão ouro para manutenção preditiva e análise de vibração em rolamentos de equipamentos rotativos.

## 🚀 Como utilizar

Para manter o repositório leve e permitir que você baixe apenas o que precisa, utilizamos um script interativo em Python.

### Pré-requisitos
Certifique-se de ter o Python instalado e instale as dependências necessárias:
```bash
pip install requests tqdm
