# Roteiro do vídeo — FarmTech Solutions, Fase 1

**Duração alvo:** até 5 minutos. **Formato:** gravação de tela com narração.
**Deixe pronto antes de gravar:** terminal já aberto na raiz do projeto (`cd .../FarmTech-Fase1`),
o VS Code com `src/farmtech.py` aberto e a página do repositório no GitHub numa aba do navegador.
Restaure os dados de exemplo antes de começar: `cp dados/farmtech-exemplo.csv dados/farmtech.csv`.

> As frases abaixo são sugestões — fale do seu jeito, mas mantenha a ordem.

---

## 0:00–0:25 · Abertura

**Na tela:** o README no GitHub, com o nome do projeto e o grupo.

> "Oi, eu sou o `<preencher: seu nome>`, do grupo `<preencher>`. Esse é o projeto da Fase 1 da
> FarmTech Solutions. A ideia é digitalizar uma fazenda que planta soja e milho: calcular a área
> de plantio, calcular quanto insumo cada talhão precisa e analisar tudo isso em estatística."

---

## 0:25–1:00 · O código, por cima

**Na tela:** `src/farmtech.py` aberto, rolando do topo até os vetores.

> "O programa é em Python puro, sem biblioteca nenhuma. No topo eu deixo as duas culturas num
> vetor, `CULTURAS = ["Soja", "Milho"]` — se a fazenda trocar de cultura, muda só aqui.
> Logo abaixo estão os vetores de dados: `cultura`, `figura`, `area_m2`, `area_ha`, `insumo_nome`,
> `insumo_total` e `unidade`. São listas paralelas: cada talhão que eu cadastro ocupa a mesma
> posição em todas elas — o talhão zero é `cultura[0]`, `area_m2[0]`, `insumo_total[0]`."

**Role até `cadastrar()`** e mostre as duas fórmulas comentadas.

> "A soja usa área de retângulo, comprimento vezes largura. O milho é pivô central, então é área
> de círculo: 3.14159 vezes o raio ao quadrado. Depois eu divido por dez mil para ter hectares."

---

## 1:00–1:20 · Rodando o app

**Na tela:** terminal.

```bash
python3 src/farmtech.py
```

> "Rodo sempre da raiz do projeto, porque é de lá que ele enxerga a pasta `dados`. O menu está
> dentro de um `while`: ele fica repetindo até eu escolher a opção 5."

---

## 1:20–2:10 · Cadastrando um talhão de soja (opção 1)

**Digite:** `1` → `1` (Soja) → `250` → `120` → `20` → `240` → `120`

> "Opção 1, cultura 1, soja. Talhão de 250 por 120 metros: dá 30 mil metros quadrados, 3 hectares.
> Agora o insumo: fosfato, 20 mililitros por metro de rua, 240 ruas de 120 metros cada. O programa
> multiplica os três e divide por mil para virar litro: 576 litros de fosfato."

Aponte a linha `[CSV atualizado: dados/farmtech.csv - 1 registro(s)]`.

> "Repare: toda vez que os dados mudam, ele já regrava o CSV. É esse arquivo que o R vai ler."

---

## 2:10–2:45 · Cadastrando um talhão de milho (opção 1)

**Digite:** `1` → `2` (Milho) → `100` → `180`

> "Agora milho, que é pivô central: eu só preciso do raio, 100 metros. Área do círculo dá
> 31.415 metros quadrados, 3,14 hectares. O insumo do milho é nitrogênio em quilo por hectare:
> 180 quilos por hectare vezes 3,14 hectares dá 565 quilos e 49."

---

## 2:45–3:00 · Listando (opção 2)

**Digite:** `2`

> "Opção 2, saída de dados. Aqui eu uso um `for` percorrendo os vetores e mostro cada talhão com
> o índice dele — índice 0 e índice 1 — já formatado com duas casas decimais."

---

## 3:00–3:25 · Atualizando (opção 3)

**Digite:** `3` → `0` → `400` → `150` → `25` → `300` → `150`

> "Opção 3, atualizar. Escolho a posição 0, a soja, e digito as medidas novas: 400 por 150.
> Em vez de `append`, agora o programa grava direto naquela posição do vetor. A soja passou a
> ter 60 mil metros quadrados e 1.125 litros de fosfato."

---

## 3:25–3:50 · Deletando e validações (opção 4)

**Digite:** `4` → `99` (posição inexistente, de propósito) → depois `1`

> "Opção 4, deletar. Se eu digitar uma posição que não existe, o `while` da validação segura e
> pede de novo — o programa não quebra. Agora a posição 1, o milho: ele sai de todos os sete
> vetores ao mesmo tempo, senão as listas ficariam desalinhadas."

**Digite:** `2` para listar de novo, e `9` para mostrar a validação do menu.

> "Listando de novo, sobrou só a soja. E se eu digitar 9 no menu, ele avisa que a opção é inválida."

---

## 3:50–4:00 · Saindo (opção 5)

**Digite:** `5`

> "Opção 5 encerra o `while` e fecha o programa."

---

## 4:00–4:20 · Mostrando o CSV

**Na tela:** `cat dados/farmtech.csv` (ou abra o arquivo no VS Code).

> "Esse é o arquivo que o Python gerou: uma linha de cabeçalho e uma linha por talhão, separado
> por vírgula e com ponto decimal, que é o formato que o R entende."

Se você quiser rodar o R com os 6 talhões de exemplo, rode antes:
`cp dados/farmtech-exemplo.csv dados/farmtech.csv` (e comente que é a base de demonstração).

---

## 4:20–4:45 · Rodando o R

**Na tela:** terminal.

```bash
Rscript src/estatisticas.R
```

> "O script em R é só R base, sem pacote nenhum. Ele lê o CSV com `read.csv` e calcula média e
> desvio padrão da área e do insumo — primeiro no geral, depois separando soja e milho com
> `subset`. No fim ele ainda mostra a tabela inteira e o tamanho total da fazenda, 22,6 hectares."

> *(Se o R não estiver instalado na sua máquina, use a alternativa online descrita em
> `docs/COMO-RODAR.md` e mostre o resultado rodando no navegador.)*

---

## 4:45–5:00 · Fechamento no GitHub

**Na tela:** o repositório no GitHub, mostrando as pastas `src`, `dados`, `docs` e o README.

> "O projeto está versionado no GitHub com o README no padrão da FIAP: descrição, estrutura de
> pastas, como executar e histórico de versões. É isso, obrigado!"

---

## Checklist antes de enviar

- [ ] O vídeo tem no máximo 5 minutos.
- [ ] Apareceram as opções 1, 2, 3, 4 e 5 do menu.
- [ ] Apareceu pelo menos uma validação segurando entrada errada.
- [ ] Apareceram as duas culturas, com as duas figuras geométricas diferentes.
- [ ] Apareceu o CSV gerado e o resultado do R.
- [ ] O vídeo foi publicado como **não listado** no YouTube e o link está no README ou no portal.
- [ ] O repositório do GitHub está **público** e o link foi entregue no portal.
