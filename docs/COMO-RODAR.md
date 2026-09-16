# Como rodar o projeto

> **Regra de ouro:** rode os dois programas **a partir da pasta raiz do projeto**
> (`FarmTech-Fase1`), e não de dentro de `src/`. Os dois procuram o arquivo em
> `dados/farmtech.csv`, um caminho relativo à raiz.

```bash
cd caminho/ate/FarmTech-Fase1
```

---

## 1. Rodar o aplicativo em Python

```bash
python3 src/farmtech.py
```

Não é preciso instalar nada: o programa usa só o Python puro, sem bibliotecas externas.
Qualquer Python 3 serve (foi testado no 3.14).

### Menu

| Opção | O que faz |
|---|---|
| 1 | Entrada de dados — cadastra um talhão novo (soja ou milho) |
| 2 | Saída de dados — lista tudo que está cadastrado, com o índice de cada registro |
| 3 | Atualizar — troca as medidas de uma posição que já existe |
| 4 | Deletar — apaga o registro de uma posição |
| 5 | Sair |

A cada cadastro, atualização ou remoção, o arquivo `dados/farmtech.csv` é regravado do zero.

### Valores sugeridos para testar (e para usar na gravação do vídeo)

**Soja (retângulo):**

```
Comprimento do talhão (metros): 250
Largura do talhão (metros): 120
Fosfato por metro de rua (mL): 20
Número de ruas: 240
Comprimento de cada rua (metros): 120
```

Resultado esperado: `30000.00 m2 (3.00 ha)` e `576.00 L` de fosfato.

**Milho (círculo / pivô central):**

```
Raio do pivô central (metros): 100
Nitrogênio por hectare (kg): 180
```

Resultado esperado: `31415.90 m2 (3.14 ha)` e `565.49 kg` de nitrogênio.

### Testar as validações (ótimo para mostrar no vídeo)

- digite `9` no menu → `>> Opcao invalida! Digite um numero de 1 a 5.`
- digite `abc` ou `-5` num campo de número → `>> Digite apenas numeros positivos.`
- peça para deletar a posição `99` quando só existe a `0` → `>> Essa posicao nao existe.`

### Atenção: o app sobrescreve o CSV de exemplo

O projeto já vem com `dados/farmtech.csv` preenchido com 6 talhões de exemplo, para que o script
em R funcione antes mesmo de você rodar o Python. **Assim que você faz o primeiro cadastro, o
programa regrava esse arquivo com os seus dados** — isso é o comportamento pedido no enunciado.

Se quiser os 6 exemplos de volta (para a análise em R ficar mais interessante), é só copiar a
cópia de segurança:

```bash
cp dados/farmtech-exemplo.csv dados/farmtech.csv
```

---

## 2. Rodar a análise estatística em R

```bash
Rscript src/estatisticas.R
```

O script usa **só o R base** — `read.csv`, `mean`, `sd`, `subset`, `cat` e `print`.
Nenhum pacote precisa ser instalado.

Com os 6 talhões de exemplo em `dados/farmtech.csv`, os números que devem aparecer são:

| Recorte | Área média (m²) | Desvio padrão (m²) | Insumo médio | Desvio padrão |
|---|---|---|---|---|
| Geral (6 talhões) | 37662.19 | 22572.18 | 709.09 | 461.28 |
| Soja (3 talhões) | 35400.00 | 22393.75 | 664.20 L | 423.64 |
| Milho (3 talhões) | 39924.37 | 27512.28 | 753.98 kg | 588.58 |

E no fim: área total da fazenda `22.6 hectares`, maior talhão `7.07 ha`, menor `1.62 ha`.

> Observação que vale citar no vídeo: a média de insumo "no geral" mistura litros de fosfato com
> quilos de nitrogênio, então ela serve só de curiosidade. O número que faz sentido de verdade é
> o de cada cultura separada. O próprio script avisa isso na tela.

### Se o R não estiver instalado

`Rscript: command not found` significa que o R ainda não está na máquina. Duas saídas:

**Opção A — instalar o R (macOS, com Homebrew):**

```bash
brew install r
Rscript --version
```

Sem Homebrew, dá para baixar o instalador oficial em <https://cran.r-project.org/bin/macosx/>.

**Opção B — rodar online, sem instalar nada (funciona para a gravação do vídeo):**

1. Abra <https://rdrr.io/snippets/>.
2. Apague o conteúdo da caixa de código.
3. Cole o CSV **direto dentro do código**, trocando a primeira linha do script
   (`dados <- read.csv("dados/farmtech.csv")`) por este bloco:

   ```r
   texto <- "cultura,figura,area_m2,area_ha,insumo,total_insumo,unidade
   Soja,Retangulo,30000.00,3.00,Fosfato,576.00,L
   Soja,Retangulo,60000.00,6.00,Fosfato,1125.00,L
   Soja,Retangulo,16200.00,1.62,Fosfato,291.60,L
   Milho,Circulo,31415.90,3.14,Nitrogenio,565.49,kg
   Milho,Circulo,70685.78,7.07,Nitrogenio,1413.72,kg
   Milho,Circulo,17671.44,1.77,Nitrogenio,282.74,kg"

   dados <- read.csv(text = texto)
   ```

4. Cole **o resto do script** (da linha da função `mostrar` até o fim) logo abaixo.
5. Clique em **Run**.

Outros sites que fazem a mesma coisa: <https://www.mycompiler.io/online-r-compiler> e
<https://replit.com> (template R).
