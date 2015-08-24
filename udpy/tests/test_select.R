library(dplyr)

data.names <- c('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class')
data.data <- read.table("data/iris.data", sep = ',', header = FALSE)
names(data.data) <- data.names
data.data <- data.data %>% head(5)

#Generate comma separated source data
data.data %>% write.csv(file = "data/iris_test.csv")

#Generate tab separated source data
data.data %>% write.table(file = "data/iris_test.tsv", sep = "\t")

#Generate data to test numeric column selection
data.data %>% dplyr::select(sepal_length) %>% write.csv(file = "data/iris_select_sepal_length.csv")

#Generate data to test text column selection
data.data %>% dplyr::select(class) %>% write.csv(file = "data/iris_select_class.csv")
