# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions — Fase 1

## <preencher: Standalone>

## 👨‍🎓 Integrantes:
- <a href="https://www.linkedin.com/company/inova-fusca">&lt;Francis Mika Matos 1&gt;</a>


## 👩‍🏫 Professores:
### Tutor(a)
- <a href="https://www.linkedin.com/company/inova-fusca">&lt;Sabrina Otoni&gt;</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">&lt;preencher: nome do coordenador(a)&gt;</a>


## 📜 Descrição

A **FarmTech Solutions** é uma empresa de consultoria em Agricultura Digital. Nesta Fase 1 o
objetivo é dar o primeiro passo da digitalização de uma fazenda: sair da conta no papel e passar
a calcular, guardar e analisar os dados de plantio em software.

O projeto atende **duas culturas de grande importância no Brasil**:

| Cultura | Figura geométrica da área | Fórmula da área | Insumo | Cálculo do insumo | Unidade |
|---|---|---|---|---|---|
| **Soja** | Retângulo (talhão comum) | `comprimento × largura` | Fosfato | `mL por metro de rua × nº de ruas × comprimento da rua ÷ 1000` | litros (L) |
| **Milho** | Círculo (pivô central) | `3.14159 × raio × raio` | Nitrogênio | `kg por hectare × hectares` | quilos (kg) |

A entrega tem duas partes que conversam entre si:

**1. Aplicativo em Python (`src/farmtech.py`)** — um programa de terminal, com menu em loop, que:

- guarda as culturas num vetor `CULTURAS = ["Soja", "Milho"]`, fácil de trocar;
- calcula a **área de plantio** de cada talhão a partir da figura geométrica da cultura, em m² e
  em hectares (1 ha = 10.000 m²);
- calcula o **manejo de insumos** a partir das quantidades digitadas pelo usuário;
- guarda tudo em **vetores (listas) paralelos** — `cultura[]`, `figura[]`, `area_m2[]`,
  `area_ha[]`, `insumo_nome[]`, `insumo_total[]`, `unidade[]` — em que cada cadastro é
  uma posição `i` repetida em todas as listas;
- oferece um **menu** com entrada, saída, atualização, remoção de dados e saída do programa;
- usa **laços** (`while` no menu e nas validações, `for` para listar) e **decisões**
  (`if / elif / else`) para escolher o caminho de cada opção;
- **valida a entrada do usuário**: opção de menu inválida, texto onde deveria ter número,
  número negativo ou zero, e posição que não existe nos vetores;
- **exporta os dados para `dados/farmtech.csv`** a cada alteração, para o R conseguir ler.

**2. Análise estatística em R (`src/estatisticas.R`)** — um script em R base (sem pacotes
externos) que lê `dados/farmtech.csv` e calcula **média** (`mean`) e **desvio padrão** (`sd`)
da área e do total de insumo, no geral e separado por cultura, além do tamanho total da fazenda
e do maior e menor talhão.

O ciclo da entrega é: o usuário cadastra no Python → o Python grava o CSV → o R lê o CSV e
devolve as estatísticas da fazenda.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: arquivos não-estruturados do repositório, como a imagem do logo da FIAP usada neste README.

- <b>dados</b>: a base de dados do projeto em CSV. `farmtech.csv` é o arquivo que o programa em
  Python grava e o programa em R lê; `farmtech-exemplo.csv` é uma cópia com 6 talhões de exemplo
  (3 de soja e 3 de milho), para que o script em R funcione mesmo antes do primeiro cadastro.

- <b>docs</b>: documentação de apoio. `COMO-RODAR.md` traz o passo a passo de execução e
  `ROTEIRO-VIDEO.md` traz o roteiro do vídeo de demonstração.

- <b>src</b>: todo o código-fonte do projeto. `farmtech.py` é o aplicativo em Python e
  `estatisticas.R` é a análise estatística em R.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

```bash
FarmTech-Fase1
│
├── assets
│   └── logo-fiap.png
├── dados
│   ├── farmtech.csv            # base gerada pelo app e lida pelo R
│   └── farmtech-exemplo.csv    # 6 talhões de exemplo (3 soja, 3 milho)
├── docs
│   ├── COMO-RODAR.md
│   └── ROTEIRO-VIDEO.md
├── src
│   ├── farmtech.py             # aplicativo Python (menu, cálculos, CSV)
│   └── estatisticas.R          # estatísticas em R base
├── .gitignore
└── README.md
```

## 🔧 Como executar o código

**Pré-requisitos**

- **Python 3** (testado na versão 3.14). Nenhuma biblioteca externa é usada — só o Python puro.
- **R** (testado com R base, sem pacotes) — opcional, só para a parte estatística.
  Se o R não estiver instalado, veja a alternativa online em `docs/COMO-RODAR.md`.

**Passo a passo**

1. Baixe o repositório:

   ```bash
   git clone <preencher: URL do repositório no GitHub>
   cd FarmTech-Fase1
   ```

2. Rode o aplicativo em Python **a partir da raiz do projeto** (é daí que ele enxerga a pasta `dados/`):

   ```bash
   python3 src/farmtech.py
   ```

   No menu: `1` cadastra um talhão, `2` lista tudo, `3` atualiza uma posição, `4` apaga uma
   posição e `5` encerra. A cada alteração o arquivo `dados/farmtech.csv` é regravado.

3. Rode a análise estatística em R, também a partir da raiz do projeto:

   ```bash
   Rscript src/estatisticas.R
   ```

O detalhamento, com exemplos de valores para digitar e o que fazer quando o R não está
instalado, está em [`docs/COMO-RODAR.md`](docs/COMO-RODAR.md).

## 🗃 Histórico de lançamentos

* 0.1.0 - <preencher: XX/XX/2025>
    * Versão inicial da Fase 1: aplicativo em Python (menu com entrada, saída, atualização e
      remoção de dados; cálculo de área de soja e milho; cálculo de insumos; exportação para CSV)
      e análise estatística em R (média e desvio padrão, no geral e por cultura).

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
