#Aprendendo R

glass <- read.csv(file.choose(), header = FALSE, sep = ",")
head(glass)

colnames(glass) <- c("id", "ri", "na", "mg", "al", "si", "k", "ca", "ba", "fe", "tipo")
head(glass)

class(glass$tipo)

glass$tipo <- as.factor(glass$tipo)
class(glass$tipo)

summary(glass)

cor(glass[,2:10])

library(lattice)
cor <- cor(glass[,2:10])
rgb.pallete <- colorRampPalette(c("yellow", "orange"), space = "rgb")
levelplot(cor, main = "Correlação Dados de Vidros", xlab="", ylab="", col.regions=rgb.pallete(120))

pairs(glass[2:10], main = "Glass Data", pch = 21, bg = c("red", "green3", "blue","yellow","purple","deeppink")[unclass(glass$tipo)])
