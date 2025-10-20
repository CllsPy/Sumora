# Log de Desenvolvimento - Sistema de Sumarização de Blog

**Data:** 19/10/2025

## Estratégias de Desenvolvimento

### Metodologia Aplicada

- Consulta a modelos de linguagem para esclarecimento conceitual
- Revisão de cursos na plataforma Udemy
- Pesquisa web direcionada
- Abordagem incremental: resolução de problemas individuais

## Entregas do Período

Desenvolvimento de dois módulos principais:

- `prompt_template.py`
- `summarizer.py`

## Desafios Técnicos Identificados

### Questões de Importação

Incerteza sobre práticas ótimas para importação de classes entre módulos e estruturação eficiente de dependências.

### Gestão de Ambiente

Falha operacional: esquecimento de ativação do ambiente virtual antes do início da sessão de desenvolvimento.

## Próximas Etapas

### Imediato

Construção e execução do pipeline de integração.

### Considerações Futuras

Implementação de testes unitários para cada componente desenvolvido, garantindo cobertura adequada desde as fases iniciais.

## Detalhamento do Processo de Desenvolvimento

### Fase 1: Inicialização do Projeto

### Arquitetura

Criação de novo repositório com elaboração de diagrama C1 (Context Level) para primeiro nível de abstração. Objetivo central: extração de conteúdo de posts do blog e geração automatizada de resumos via API de modelo de linguagem.

### Configuração de Ambiente Virtual

Criação do ambiente isolado:

```python
python -m venv meu_ambiente_virtual

```

Ativação do ambiente (Windows):

```python
meu_ambiente_virtual\Scripts\activate

```

### Fase 2: Configuração de Dependências

### Arquivo de Configuração

Adaptação de `setup.py` baseado em repositório de referência: https://github.com/CllsPy/similar.me/blob/main/setup.py

O `setup.py` possibilita instalação automatizada de dependências através do arquivo `requirements.txt`.

### Dependências Identificadas

- streamlit (interface gráfica)
- python-dotenv (gestão de variáveis de ambiente)
- beautifulsoup4 (extração de conteúdo web)

### Segurança

Criação de arquivo `.env` para armazenamento seguro da chave API da OpenAI.

Instalação de dependências:

```python
pip install -e .

```

### Fase 3: Estrutura de Diretórios

```
project/
├── app/              # Interface Streamlit
├── config/           # Gestão de APIs
├── data/             # HTML extraído
├── src/              # Pacotes principais (e.g., data_loader)
└── utils/            # Utilitários (logs, exceptions)

```

### Módulo Utils

- `logger.py`: Sistema de logging (código adaptado de repositório de referência)
- `custom_exception.py`: Tratamento customizado de exceções para debugging aprimorado

### Módulo Config

`config.py`: Centralização de configurações de API (atualmente apenas OpenAI)

### Fase 4: Desenvolvimento do Extrator de Conteúdo

### Evolução Arquitetural

Desenvolvimento inicial de `src/data_loader.py` com função `fetch_website(url)` para recepção de URLs.

Identificação de necessidade de módulo adicional para extração, resultando em criação de `scraper.py`.

Instalação de dependência adicional: BeautifulSoup4.

### Refatoração

Unificação de `data_loader.py` e `scraper.py` em classe única para coesão funcional.

Execução de testes revelou ambiente virtual inativo, evidenciando necessidade de checklist pré-desenvolvimento.

### Fase 5: Sistema de Prompts

Após validação do extrator, iniciou-se desenvolvimento de `prompt.py` para gerenciamento de templates de prompt.

### Fase 6: Desafios Arquiteturais

### Questão de Design

Dúvida sobre remoção de parâmetro URL de `summarizer.py`:

- Justificativa técnica
- Metodologia de implementação

**Decisão:** Manutenção do estado atual para priorizar desenvolvimento do pipeline.

### Fase 7: Integração via Pipeline

Objetivo: Orquestração de todos os módulos em `src/`.

### Lacuna de Conhecimento Identificada

Compreensão insuficiente do princípio Single Responsibility, impactando qualidade arquitetural.

### Desafios de Implementação

Dificuldade significativa na aplicação de princípios SOLID durante desenvolvimento de `pipeline.py` e `pipeline_builder.py`.

**Resultado:** Integração bem-sucedida com validação via sistema de logs.

## Análise Técnica

### Sucessos

- Metodologia incremental de desenvolvimento
- Utilização de múltiplas fontes de conhecimento técnico
- Unificação de módulos para maior coesão

### Áreas de Melhoria

- Aprofundamento em princípios SOLID
- Estabelecimento de checklist pré-desenvolvimento (ativação de ambiente)
- Implementação de testes desde fase inicial

### Conhecimento Técnico a Desenvolver

- Padrões de importação em Python
- Princípios de design orientado a objetos
- Test-driven development (TDD)



# llmwhisper
one, this will be something

![llm-wshiper-Page-2](https://github.com/user-attachments/assets/2498facb-5759-41dc-a761-01c0ab2be78c)

## Doing
 - [ x ] Configuration
 - [  ] create data_loader (unifciate sraper + data_loader)
