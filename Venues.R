library(ggmap)
library(ggplot2)
library(maps)
venues<- c("Bengaluru","New Delhi","Mumbai","Kolkata","Pune","Hyderabad"
           ,"Mohali","Nagpur","Raipur","Rajkot")
ll.venues<-geocode(venues)
latitude<-ll.venues$lat
longitude<-ll.venues$lon
map(database = "world",regions = "India",exact = T,fill = TRUE,col="yellow",bg="lightblue", ylim=c(-3, 35), mar=c(0,0,0,0))
points(longitude,latitude, col="red", pch=16)


