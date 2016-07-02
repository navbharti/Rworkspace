#Read a CSV file from the project path
dat <- read.csv("femaleMiceWeights.csv")

#Download a file from given URL and save as femaleMiceWeights.csv 
install.packages("downloader")
library(downloader) 
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/femaleMiceWeights.csv"
filename <- "femaleMiceWeights.csv" 
download(url, destfile=filename)


View(dat)


library(dplyr)

#
filters the dataset with attribute value Diet=="chow" and select Bodyweight then unlist
controls <- filter(dat, Diet=="chow")
controls <- select(controls, Bodyweight)
unlist(controls)

#This line of code does the same thing as above is done in three lines of code
controls <- filter(dat, Diet=="chow") %>% select(Bodyweight) %>% unlist
controls

#This line of code does the same thing as above is done in three lines of code
treatment <- filter(dat, Diet=="hf") %>% select(Bodyweight) %>% unlist
treatment

#take as observation
obs <- mean(treatment) - mean(controls)

population <-read.csv("femaleControlsPopulation.csv")
population <- unlist(population)

#find the sample of 12 instances from the pupulation dataset and finds means
mean(sample(population, 12))

#NUll Hypothesis = there is no difference
nulls <-vector("numeric", n)
n <- 10000
for(i in 1:n){
  
  control <- sample(population, 12)
  treatment <- sample(population, 12)
  nulls[i] <- mean(treatment)-mean(controls)
  
}

max(nulls)

hist(nulls)

sum(nulls > obs) / n

#finds the p-value
mean(abs(nulls) > obs)

#Normal Distribution
#Are Heights normally distributed?
#How many standard deviations away from the mean?

#Populations, Parameters, and sample estimates
#take random sample
#population averages
#observations
#Sample averages

#central limit theorem(CLT)
#We will remove the lines that contain missing values:

#dat <- na.omit( dat )
install.packages("rafalib")
library(rafalib)
mypar()

qqnorm(nulls)
qqline(nulls)

#t-stat
N <-length(treatment)
obs <- mean(treatment)-mean(controls)
se <- sqrt(
  var(treatment)/N+
    var(controls)/N
  )
tstat <- obs / se
2 * (1 - pnorm(tstat))

#finds the t-stat of two observations
t.test(treatment, controls)
qqnorm(controls)
qqline(controls)

qqnorm(treatment)
qqline(treatment)


##Introduction of inference
