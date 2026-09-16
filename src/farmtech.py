# ==========================================================
# FarmTech Solutions - Fase 1
# Programa que calcula a area de plantio e a quantidade de
# insumos de duas culturas: soja e milho.
#
# IMPORTANTE: rode sempre a partir da raiz do projeto:
#     python3 src/farmtech.py
# (o programa grava o CSV em dados/farmtech.csv)
# ==========================================================

# Vetor (lista) com as culturas do projeto.
# Para trocar de cultura no futuro, basta mudar os nomes aqui.
CULTURAS = ["Soja", "Milho"]

# Valor de PI usado na conta da area do circulo (pivo central do milho).
PI = 3.14159

# Caminho do arquivo CSV que o programa em R vai ler depois.
ARQUIVO_CSV = "dados/farmtech.csv"

# ---------- VETORES DE DADOS (listas paralelas) ----------
# Cada cadastro ocupa a MESMA posicao i em todas as listas.
# Exemplo: cultura[0], area_m2[0] e insumo_total[0] falam do mesmo talhao.
cultura = []       # "Soja" ou "Milho"
figura = []        # "Retangulo" ou "Circulo"
area_m2 = []       # area em metros quadrados
area_ha = []       # a mesma area em hectares
insumo_nome = []   # "Fosfato" ou "Nitrogenio"
insumo_total = []  # quanto de insumo a lavoura precisa
unidade = []       # "L" (litros) ou "kg" (quilos)


# ---------- FUNCOES DE APOIO ----------

def eh_numero(texto):
    # Diz se o texto digitado pode virar numero (aceita um ponto decimal).
    texto = texto.replace(".", "", 1)  # tira um ponto, se houver
    return texto.isdigit()             # sobrou so digito? entao e numero


def ler_numero(pergunta):
    # Pergunta um numero e so devolve quando o valor for valido e maior que zero.
    # Esse while e a validacao de entrada (nao aceita texto nem numero negativo).
    numero = 0.0
    while numero <= 0:
        texto = input(pergunta)
        texto = texto.replace(",", ".")  # aceita virgula como separador decimal
        if eh_numero(texto):
            numero = float(texto)        # casting: texto vira numero
            if numero <= 0:
                print("  >> O valor precisa ser maior que zero.")
        else:
            print("  >> Digite apenas numeros positivos. Exemplo: 120.5")
    return numero


def ler_posicao(acao):
    # Pergunta uma posicao da lista e so devolve quando ela realmente existir.
    posicao = -1
    while posicao < 0:
        texto = input(f"Posicao que deseja {acao} (0 a {len(cultura) - 1}): ")
        if texto.isdigit():
            if int(texto) < len(cultura):
                posicao = int(texto)
            else:
                print("  >> Essa posicao nao existe. Tente de novo.")
        else:
            print("  >> Digite um numero inteiro (0, 1, 2 ...).")
    return posicao


def salvar_csv():
    # Regrava o CSV inteiro: cabecalho + uma linha por cadastro.
    # Roda toda vez que os dados mudam, para o R sempre ler a versao mais nova.
    arquivo = open(ARQUIVO_CSV, "w")
    arquivo.write("cultura,figura,area_m2,area_ha,insumo,total_insumo,unidade\n")
    for i in range(len(cultura)):
        linha = cultura[i] + "," + figura[i] + ","
        linha = linha + f"{area_m2[i]:.2f}" + "," + f"{area_ha[i]:.2f}" + ","
        linha = linha + insumo_nome[i] + "," + f"{insumo_total[i]:.2f}" + "," + unidade[i]
        arquivo.write(linha + "\n")
    arquivo.close()
    print(f"[CSV atualizado: {ARQUIVO_CSV} - {len(cultura)} registro(s)]")


def mostrar_menu():
    # So desenha o menu na tela.
    print("\n========== MENU FARMTECH ==========")
    print("1 - Entrada de dados (novo cadastro)")
    print("2 - Saida de dados (listar tudo)")
    print("3 - Atualizar dados de uma posicao")
    print("4 - Deletar dados de uma posicao")
    print("5 - Sair")
    print("===================================")


# ---------- OPCAO 1: ENTRADA DE DADOS ----------

def cadastrar():
    # Pergunta a cultura, calcula area e insumo, e guarda tudo no fim das listas.
    print("\n--- ENTRADA DE DADOS ---")
    print(f"1 - {CULTURAS[0]}  (area retangular)")
    print(f"2 - {CULTURAS[1]} (area circular - pivo central)")

    # Validacao: fica perguntando ate o usuario escolher 1 ou 2.
    escolha = ""
    while escolha != "1" and escolha != "2":
        escolha = input("Escolha a cultura (1 ou 2): ")
        if escolha != "1" and escolha != "2":
            print("  >> Opcao invalida. Digite 1 ou 2.")

    if escolha == "1":
        # SOJA - area do RETANGULO = comprimento x largura
        comprimento = ler_numero("Comprimento do talhao (metros): ")
        largura = ler_numero("Largura do talhao (metros): ")
        metros2 = comprimento * largura
        hectares = metros2 / 10000  # 1 hectare = 10.000 m2

        # INSUMO DA SOJA - fosfato em mL por metro de rua
        # total em mL = mL por metro x numero de ruas x comprimento da rua
        ml_por_metro = ler_numero("Fosfato por metro de rua (mL): ")
        ruas = int(ler_numero("Numero de ruas: "))  # int(): rua e contagem inteira
        comprimento_rua = ler_numero("Comprimento de cada rua (metros): ")
        total_ml = ml_por_metro * ruas * comprimento_rua
        litros = total_ml / 1000  # 1 litro = 1.000 mL

        # Guarda o cadastro no fim de CADA lista (sempre a mesma posicao).
        cultura.append(CULTURAS[0])
        figura.append("Retangulo")
        area_m2.append(metros2)
        area_ha.append(hectares)
        insumo_nome.append("Fosfato")
        insumo_total.append(litros)
        unidade.append("L")

        print(f"\nSoja cadastrada na posicao {len(cultura) - 1}.")
        print(f"Area: {metros2:.2f} m2 ({hectares:.2f} ha)")
        print(f"Fosfato necessario: {litros:.2f} L")
    else:
        # MILHO - area do CIRCULO = PI x raio x raio
        raio = ler_numero("Raio do pivo central (metros): ")
        metros2 = PI * raio * raio
        hectares = metros2 / 10000  # 1 hectare = 10.000 m2

        # INSUMO DO MILHO - nitrogenio em kg por hectare
        # total em kg = kg por hectare x quantidade de hectares
        kg_por_hectare = ler_numero("Nitrogenio por hectare (kg): ")
        total_kg = kg_por_hectare * hectares

        cultura.append(CULTURAS[1])
        figura.append("Circulo")
        area_m2.append(metros2)
        area_ha.append(hectares)
        insumo_nome.append("Nitrogenio")
        insumo_total.append(total_kg)
        unidade.append("kg")

        print(f"\nMilho cadastrado na posicao {len(cultura) - 1}.")
        print(f"Area: {metros2:.2f} m2 ({hectares:.2f} ha)")
        print(f"Nitrogenio necessario: {total_kg:.2f} kg")


# ---------- OPCAO 2: SAIDA DE DADOS ----------

def listar():
    # Percorre as listas com for e mostra todos os cadastros com o indice.
    print("\n--- SAIDA DE DADOS ---")
    if len(cultura) == 0:
        print("Nenhum dado cadastrado ainda. Use a opcao 1 do menu.")
    else:
        print("Idx | Cultura | Figura    |      Area m2 | Area ha | Insumo     |      Total")
        print("----+---------+-----------+--------------+---------+------------+-----------")
        for i in range(len(cultura)):
            print(f"{i:3} | {cultura[i]:7} | {figura[i]:9} | {area_m2[i]:12.2f} | {area_ha[i]:7.2f} | {insumo_nome[i]:10} | {insumo_total[i]:8.2f} {unidade[i]}")
        print(f"\nTotal de talhoes cadastrados: {len(cultura)}")


# ---------- OPCAO 3: ATUALIZAR DADOS ----------

def atualizar():
    # Troca os dados de uma posicao que ja existe (a cultura continua a mesma).
    print("\n--- ATUALIZAR DADOS ---")
    if len(cultura) == 0:
        print("Nao ha dados para atualizar.")
    else:
        listar()
        posicao = ler_posicao("atualizar")
        print(f"\nA posicao {posicao} e da cultura {cultura[posicao]}.")
        print("Digite os dados novos:")

        if cultura[posicao] == CULTURAS[0]:
            # SOJA - refaz as mesmas contas do cadastro
            comprimento = ler_numero("Comprimento do talhao (metros): ")
            largura = ler_numero("Largura do talhao (metros): ")
            metros2 = comprimento * largura
            hectares = metros2 / 10000

            ml_por_metro = ler_numero("Fosfato por metro de rua (mL): ")
            ruas = int(ler_numero("Numero de ruas: "))
            comprimento_rua = ler_numero("Comprimento de cada rua (metros): ")
            litros = (ml_por_metro * ruas * comprimento_rua) / 1000

            # Agora GRAVA na posicao escolhida (em vez de usar append).
            area_m2[posicao] = metros2
            area_ha[posicao] = hectares
            insumo_total[posicao] = litros
            print(f"\nPosicao {posicao} atualizada: {metros2:.2f} m2 e {litros:.2f} L de fosfato.")
        else:
            # MILHO - refaz as mesmas contas do cadastro
            raio = ler_numero("Raio do pivo central (metros): ")
            metros2 = PI * raio * raio
            hectares = metros2 / 10000

            kg_por_hectare = ler_numero("Nitrogenio por hectare (kg): ")
            total_kg = kg_por_hectare * hectares

            area_m2[posicao] = metros2
            area_ha[posicao] = hectares
            insumo_total[posicao] = total_kg
            print(f"\nPosicao {posicao} atualizada: {metros2:.2f} m2 e {total_kg:.2f} kg de nitrogenio.")


# ---------- OPCAO 4: DELETAR DADOS ----------

def deletar():
    # Apaga um cadastro. Precisa tirar a posicao de TODAS as listas,
    # senao os vetores ficariam desalinhados.
    print("\n--- DELETAR DADOS ---")
    if len(cultura) == 0:
        print("Nao ha dados para deletar.")
    else:
        listar()
        posicao = ler_posicao("deletar")
        apagada = cultura[posicao]
        del cultura[posicao]
        del figura[posicao]
        del area_m2[posicao]
        del area_ha[posicao]
        del insumo_nome[posicao]
        del insumo_total[posicao]
        del unidade[posicao]
        print(f"\nCadastro de {apagada} na posicao {posicao} foi apagado.")


# ==========================================================
# PROGRAMA PRINCIPAL - menu que roda dentro de um while
# ==========================================================

print("=" * 50)
print("        FarmTech Solutions - Fase 1")
print(f"        Culturas: {CULTURAS[0]} e {CULTURAS[1]}")
print("=" * 50)

opcao = ""
while opcao != "5":
    mostrar_menu()
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar()
        salvar_csv()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
        salvar_csv()
    elif opcao == "4":
        deletar()
        salvar_csv()
    elif opcao == "5":
        print("\nEncerrando o programa. Dados salvos em " + ARQUIVO_CSV + ".")
        print("Agora e so rodar o R: Rscript src/estatisticas.R")
    else:
        # Validacao do menu: qualquer coisa fora de 1 a 5 cai aqui.
        print("\n>> Opcao invalida! Digite um numero de 1 a 5.")
