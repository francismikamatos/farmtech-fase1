# ==========================================================
# FarmTech Solutions - Fase 1
# Estatisticas basicas em R (somente R base, sem pacote nenhum)
#
# IMPORTANTE: rode a partir da raiz do projeto:
#     Rscript src/estatisticas.R
# ==========================================================

# Le o arquivo CSV que o programa em Python gerou.
dados <- read.csv("dados/farmtech.csv")

# Funcao simples que mostra media e desvio padrao de uma coluna de numeros.
# O desvio padrao (sd) precisa de pelo menos 2 registros para existir.
mostrar <- function(rotulo, valores) {
  if (length(valores) == 0) {
    cat(rotulo, "-> nenhum registro\n")
  } else if (length(valores) == 1) {
    cat(rotulo, "-> media:", round(mean(valores), 2),
        "| desvio padrao: (precisa de 2 ou mais registros)\n")
  } else {
    cat(rotulo, "-> media:", round(mean(valores), 2),
        "| desvio padrao:", round(sd(valores), 2), "\n")
  }
}

cat("============================================================\n")
cat("   FarmTech Solutions - Estatisticas da Fase 1\n")
cat("============================================================\n\n")

cat("Talhoes cadastrados no CSV:", nrow(dados), "\n\n")

# ---------- 1) NUMEROS GERAIS (todas as culturas juntas) ----------
cat("--- GERAL (soja + milho) ---\n")
mostrar("Area (m2)   ", dados$area_m2)
mostrar("Area (ha)   ", dados$area_ha)
mostrar("Insumo total", dados$total_insumo)
cat("OBS: no geral o insumo mistura litros de fosfato com quilos de\n")
cat("     nitrogenio, entao o numero que vale mesmo e o de cada cultura.\n\n")

# ---------- 2) SO A SOJA ----------
# subset() separa as linhas em que a coluna cultura vale "Soja".
soja <- subset(dados, cultura == "Soja")
cat("--- SOJA (area retangular, insumo fosfato em litros) ---\n")
cat("Talhoes de soja:", nrow(soja), "\n")
mostrar("Area (m2)      ", soja$area_m2)
mostrar("Area (ha)      ", soja$area_ha)
mostrar("Fosfato (L)    ", soja$total_insumo)
cat("\n")

# ---------- 3) SO O MILHO ----------
milho <- subset(dados, cultura == "Milho")
cat("--- MILHO (area circular / pivo, insumo nitrogenio em kg) ---\n")
cat("Talhoes de milho:", nrow(milho), "\n")
mostrar("Area (m2)      ", milho$area_m2)
mostrar("Area (ha)      ", milho$area_ha)
mostrar("Nitrogenio (kg)", milho$total_insumo)
cat("\n")

# ---------- 4) TABELA COMPLETA ----------
# print() mostra o data.frame inteiro, do jeito que o R formata.
cat("--- TABELA COMPLETA LIDA DO CSV ---\n")
print(dados)
cat("\n")

# ---------- 5) RESUMO EXTRA ----------
# Soma das areas, para saber o tamanho total da fazenda.
if (nrow(dados) > 0) {
  cat("Area total da fazenda:", round(sum(dados$area_ha), 2), "hectares\n")
  cat("Maior talhao:", round(max(dados$area_ha), 2), "ha |",
      "Menor talhao:", round(min(dados$area_ha), 2), "ha\n")
} else {
  cat("O CSV esta vazio. Cadastre talhoes no programa em Python primeiro.\n")
}
