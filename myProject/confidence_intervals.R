set.seed(1)

chowPopulation <-read.csv("femaleControlsPopulation.csv")
chowPopulation <- unlist(chowPopulation)

mu_chow <- mean(chowPopulation)
print (mu_chow)

N <- 30
chow <- sample(chowPopulation, N)
print(mean(chow))

se 