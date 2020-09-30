# Analisando Dados com R e Spark

# Definindo o diretório de instalação do Spark (o módulo SparkR está dentro do diretório do Spark)
if (nchar(Sys.getenv("SPARK_HOME")) < 1) {
  Sys.setenv(SPARK_HOME = "/opt/Spark")
}

# Carrregando o SparkR no RStudio
library(SparkR, lib.loc = c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib")))

# Criando a sessão SparkR
sparkR.session(master = "local[*]", sparkConfig = list(spark.driver.memory = "2g"))

# Importando um arquivo JSON do diretório de exemplos do Spark e criando um dataframe no R
pessoas <- read.df("/opt/Spark/examples/src/main/resources/people.json", "json")

# Visualizando o dataframe
head(pessoas)

# O SparkR automaticamente cria um schema para o dataframe
printSchema(pessoas)

# Utilizando SQL para criar a tabela temporária spark_table
sql("CREATE TABLE IF NOT EXISTS spark_table (key INT, value STRING)")

# Carregando dados de exemplo na tabela temporária
sql("LOAD DATA LOCAL INPATH '/opt/Spark/examples/src/main/resources/kv1.txt' INTO TABLE spark_table")

# Aplicando linguagem SQL no objeto
resultado <- sql("FROM spark_table SELECT key, value")

# Visualizando o resultado
head(resultado)

# Criando um dataframe
df <- as.DataFrame(faithful)

# Visualizando os dados, aplicando as funções select, filter e summarize com group by 
df
head(select(df, df$eruptions))
head(select(df, "eruptions"))
head(filter(df, df$waiting < 50))
head(summarize(groupBy(df, df$waiting), count = n(df$waiting)))

# Criando e visualizando modelos de Machine Learning
families <- c("gaussian", "poisson")
train <- function(family) {
  model <- glm(Sepal.Length ~ Sepal.Width + Species, iris, family = family)
  summary(model)
}

# Sumário dos modelos
model.summaries <- spark.lapply(families, train)

# Sumário de cada modelo
print(model.summaries)

# Criando um modelo Naive Bayes

# Usando Spark Naive bayes

# Criando um dataframe R
titanic <- as.data.frame(Titanic)

# Criando um dataframe Spark
titanicDF <- createDataFrame(titanic[titanic$Freq > 0, -5])
nbDF <- titanicDF
nbTestDF <- titanicDF

# Criando o modelo
nbModel <- spark.naiveBayes(nbDF, Survived ~ Class + Sex + Age)

# Sumário do modelo
summary(nbModel)

# Previsões
nbPredictions <- predict(nbModel, nbTestDF)
showDF(nbPredictions)




