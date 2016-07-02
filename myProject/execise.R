#Dowload babies.txt and store as babies
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/babies.txt"
filename <- basename(url)
download(url, destfile=filename)
babies <- read.table("babies.txt", header=TRUE)

#split into two birth weight datasets
bwt.nonsmoke <- filter(babies, smoke==0) %>% select(bwt) %>% unlist
bwt.smoke <- filter(babies, smoke==1) %>% select(bwt) %>% unlist

#we can look for the true population difference in means between smoking and non-smoking birth weights
library(rafalib)
mean(bwt.nonsmoke)-mean(bwt.smoke)
popsd(bwt.nonsmoke)
popsd(bwt.smoke)

#Power Calculations Exercises #1
#seed at 1 and take a random sample of N=5 measurements from each of the smoking and nonsmoking datasets
set.seed(1)
N <- 30
