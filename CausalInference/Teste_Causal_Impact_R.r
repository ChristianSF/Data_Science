
install.packages("CausalImpact")

library(CausalImpact)

set.seed(1)
x1 <- 100 + arima.sim(model = list(ar= 0.999), n = 100)
y <- 1.2 * x1 + rnorm(100)
y[71:100] <- y[71:100] + 10
data <- cbind(y, x1)

head(data)

matplot(data, type = "l")

pre.period <- c(1, 70)
post.period <-c(71, 100)

impact <- CausalImpact(data, pre.period, post.period)

plot(impact)

#Criando variáveis com data e hora

time.points <- seq.Date(as.Date("2016-01-01"), by = 1, length.out = 100)
data <- zoo(cbind(y, x1), time.points)
head(data)

pre.period <- as.Date(c("2016-03-07", "2016-06-14"))
post.period <- as.Date(c("2016-06-15", "2016-09-27"))

impact <- CausalImpact(data, pre.period, post.period)
plot(impact)  


