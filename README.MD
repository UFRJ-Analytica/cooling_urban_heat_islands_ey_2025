# EY Open Science AI & Data Challenge 2025 - UFRJ Analytica

Bem-vindo(a) ao repositório oficial da UFRJ Analytica para o **EY Open Science AI & Data Challenge 2025**. Este documento tem como objetivo apresentar uma visão geral do desafio, explicar a estrutura do nosso repositório e fornecer instruções para instalação, dependências e uso, além de dicas para que você e sua equipe possam maximizar suas chances de sucesso na competição.

---

## Sobre a Competição

O **EY Open Science AI & Data Challenge 2025** é uma competição cujo foco é desenvolver modelos de Machine Learning capazes de prever pontos críticos de Ilhas de Calor Urbanas (UHI - Urban Heat Island) em regiões urbanas.

### Desafio

- **Construir um modelo de regressão** para prever o Índice de Ilha de Calor (UHI Index) em locais específicos.  
- **Não usar Latitude/Longitude diretamente** ou quaisquer transformações derivadas para a predição (restrição da competição).  
- **Integrar dados satelitais** (Sentinel-2 e, opcionalmente, Landsat), dados de pegadas de edifícios e dados meteorológicos para melhorar a robustez do modelo.

### Objetivo

- Identificar variáveis ambientais e urbanas que impactam o UHI.  
- Fornecer **previsões de UHI Index** para pontos de validação.  
- **Mitigar** ou **prevenir** hotspots de calor em áreas urbanas densas.

---

## Cronograma e Planejamento de Submissões

Abaixo está o cronograma oficial do desafio. Recomendamos que as equipes organizem suas tarefas e façam **múltiplas submissões** ao longo do período de competição, maximizando assim a oportunidade de ajustar e refinar o modelo para alcançar a melhor posição no ranking.

| Data (2025)      | Evento                          | Recomendações / Submissões Ideais                                 |
|------------------|----------------------------------|--------------------------------------------------------------------|
| **Jan 20**       | **Início da Competição**         | Realizar configuração do ambiente, primeira exploração dos dados   |
| **Mar 20**       | **Término da Competição**        | Data limite para enviar modelos; recomenda-se enviar várias versões|
| **Apr 11**       | **Anúncio dos Finalistas**       | Acompanhar resultados e manter documentação e melhorias prontas    |
| **May 4**        | **Conteúdo dos Finalistas**      | Preparar e enviar material detalhado (se finalista)                |
| **May 15**       | **Anúncio dos Vencedores**       | Conferir classificação final e apresentação dos resultados          |

**Dica:** Quanto mais cedo e mais vezes forem feitas as submissões, mais feedback sobre o desempenho do modelo vocês terão. Utilize o ranking para iterar na melhoria do pipeline e busque sempre superar as pontuações anteriores.

---

## Estrutura do Repositório

Abaixo está a arquitetura do projeto em formato ASCII:

    EY
    ├── assets
    ├── dataset
    ├── notebooks
    │   ├── __init__.py
    │   ├── ey-jupyter.ipynb
    │   ├── Landsat_LST (1).ipynb
    │   ├── sentinel-2-l2a-example.ipynb
    │   ├── Sentinel2_GeoTIFF.ipynb
    │   └── UHI Experiment Sample Benchmark Notebook V6.ipynb
    ├── output
    ├── submissions
    ├── time_I
    │   ├── __init__.py
    │   ├── explorer.py
    │   └── main.ipynb
    ├── time_II
    ├── utils
    │   └── __init__.py
    ├── .gitignore
    ├── README.MD
    ├── requirements.txt
    └── Training_data_uhi_index_UHI2025-v2.csv

### Descrição das Pastas Principais

- **assets/**  
  Reúne arquivos de logotipos, imagens e outros recursos estáticos.

- **dataset/**  
  Espaço reservado para armazenar dados brutos adicionais, caso sejam necessários.

- **notebooks/**  
  Contém notebooks Jupyter de exploração e exemplos de uso do Planetary Computer, manipulação de dados satelitais (Sentinel-2/Landsat) e um benchmark de UHI.

- **output/**  
  Saída de análises ou modelos intermediários (por exemplo, arquivos GeoTIFF ou CSVs resultantes).

- **submissions/**  
  Local para armazenar os arquivos de submissão gerados (por exemplo, `submission.csv`).

- **time_I/**  
  Equipe I da competição. Contém o `main.ipynb` com o **workflow** principal de previsão e scripts auxiliares (e.g., `explorer.py`).

- **time_II/**  
  Equipe II da competição. (Estrutura inicialmente vazia ou a definir.)

- **utils/**  
  Funções de utilidade geral ou classes auxiliares, se necessário.

- **requirements.txt**  
  Lista de bibliotecas e versões necessárias para executar o projeto.

- **Training_data_uhi_index_UHI2025-v2.csv**  
  Arquivo CSV principal com dados de UHI (contendo colunas de Latitude, Longitude e o valor do `UHI Index`, entre outras informações).

---

## Como Usar

### 1. Clonar o Repositório

    git clone https://github.com/UFRJ-Analytica/cooling_urban_heat_islands_ey_2025.git
    cd UFRJ-Analytica-EY

### 2. Criar e Ativar Ambiente Virtual (opcional, mas recomendado)

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # ou
    venv\Scripts\activate  # Windows

### 3. Instalar Dependências

Instale as bibliotecas listadas em `requirements.txt`:

    pip install -r requirements.txt

Algumas bibliotecas relevantes:  
- **numpy**, **pandas**, **scikit-learn**  
- **rasterio**, **rioxarray**, **xarray**, **geopandas**  
- **pystac-client**, **planetary-computer**, **stackstac** (para acesso aos dados satelitais)  
- **matplotlib**, **seaborn**, **tqdm**

### 4. Executar o Workflow Principal

- Navegue até a pasta do time respectivo (por exemplo, `time_I`) e abra o `main.ipynb` em um ambiente Jupyter ou similar:

        jupyter notebook time_I/main.ipynb

- **main.ipynb** exemplifica o fluxo de trabalho:  
  1. Carregamento dos dados de UHI (`Training_data_uhi_index_UHI2025-v2.csv`).  
  2. Extração de variáveis de bandas de satélite (usando `S2_sample.tiff` ou outro arquivo).  
  3. Cálculo de índices (NDVI, etc.) para cada ponto.  
  4. Treinamento e avaliação do modelo (Random Forest ou outro).  
  5. Geração de arquivo de submissão (`submission.csv`).

### 5. Ajustar Parâmetros e Explorar Abordagens

- Use notebooks em `notebooks/` para referência de como acessar dados de satélite, criar GeoTIFFs, calcular índices avançados etc.  
- Integre dados extras em `dataset/`, caso encontre fontes relevantes (metereologia, pegada de edifícios, etc.).

---

## Dicas para Vencer a Competição

1. **Não Use Latitude e Longitude como Features**  
   Respeite a regra da competição. Você pode utilizá-las para extrair dados satelitais ou características geoespaciais, mas não diretamente no modelo.

2. **Engenharia de Features Criativa**  
   - Explore índices de vegetação (NDVI, EVI, SAVI, etc.), de água (NDWI), de área construída (NDBI).  
   - Considere combinar dados meteorológicos (temperatura, umidade, vento) e de uso do solo (pegadas de edifícios, densidade populacional).

3. **Validação Robusta**  
   - Use validação cruzada (k-fold) para reduzir overfitting.  
   - Separe dados para teste realista.

4. **Modelos e Hiperparâmetros**  
   - Não se limite ao Random Forest. Experimente XGBoost, LightGBM, redes neurais, etc.  
   - Faça `hyperparameter tuning` sistematicamente.

5. **Documente e Versão**  
   - Mantenha seu repositório atualizado.  
   - Use **git** e crie *branches* se necessário.

6. **Contribuição em Equipe**  
   - Divida tarefas (coleta e limpeza de dados, engenharia de features, modelagem, visualização).  
   - Registre as decisões e insights no README interno ou no wiki do repositório.

7. **Apresentação e Explicabilidade**  
   - Use SHAP, LIME ou similar para explicar o impacto das variáveis.  
   - Visualizações claras podem ajudar a demonstrar insights.

---

## Tarefas e Deveres

- **Time I:** Responsável por ....  
- **Time II:** Responsável por ....  
- **Cooperação:** Ambos os times podem compartilhar descobertas, mas cada um terá sua própria solução final.

---

## Contribuindo

1. Faça um *fork* ou *branch* do repositório.  
2. Crie sua *branch* com as alterações: `git checkout -b feature/sua-feature`  
3. Faça commits claros e objetivos: `git commit -m "Descrição das mudanças"`  
4. Envie suas alterações: `git push origin feature/sua-feature`  
5. Abra um *pull request* descrevendo seu trabalho.

---

## Licença

Verifique termos e condições especificados pela **EY** para uso e distribuição dos dados. Siga as políticas de licenciamento de dados abertos (quando aplicável) e referências às fontes externas.

---

## Contato

Em caso de dúvidas sobre o projeto ou sugestões:  
- **Responsável**: [Gustavo Felicidade / Jefferson Rafael]  
- **Email**: [Gustavo](gustavofelicidade@ufrj.br)
- **Email**: [Jefferson](contatojefferson25@proton.me)
- **Canal interno**: Whatsapp/Meet/Discord

Boa sorte na competição!
