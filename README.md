# NF_Assignment
Problem Statement:
Primary Goal:- Creating a Hadoop Map Reduce system to process and analyze the huge data.
Absolute Goal:- TO create a high accuracy Recommendation system through data for Netflix.

In this project, We have only focused on the primary goal.

Why Hadoop Map-Reduce?
Ou major concern with the data is 
-> Volume:- The amount of data. The data is huge upto 2 gigbytes.
-> Velocity:- Processing the huge amount of data in a one-to-one way is cumbersome and time cosuming task.
-> Value:- Analysisng and getting insights from the huge data is and apply algorithms on such huge data is a hefty process.

Hadoop helps in processing such huge data using multiple cores of the system in a parellel fashion.
The data is sliced and stored into different datanodes of the HDFS system to process parallely.
This helps in faster processing of read/write functions and also lowers the load on the system by parallely consuming the multiple cores of the CPU.

Map Reduce:- Map Reduce is an algorithm which takes the huge data and divides them into smaller chunks for parallel processing which lowers the network traffic on the processor.
Mapper:- This steps takes the huge data as an input and divides them into smaller chucks and stores them as keys and values in the form of tuples.
Reducer:- The output from the mapper is the input to the reducer . The reducer further reduce the data by combining the similar keys and increasing the couunt which is the value to the key. The output of the reducer is also in a key value format which helps us to better understand the data.

Data Understanding:
The data provided is incomplete to make broad analysis since it does not contain the cast data of the movie, type of movie(i.e, Thriller, Comedy etc)  etc.
The combined data.txt contains the MovieID, User Rating and Date of the rating.
The movies_titles.csv contains the maovie name and the movie ID.

Our Objective.
Get the total no of Customers for a particular movie and their ratings by each customer. Also the average rating for a movie.

We have placed the Movies_titles.csv in the distributed cache instead of saving them in all the different data nodes to reduce latency. This will help in increasing the processor speed.

my_mapper.py file takes all the combined data as the input which contains the movieID, Rating and Date.
This splits the data with "," and stores them in a form of tuples movie_id and value is year,rating

my_reducer.py combine all the data from the mapper connect them with the movie name of the cache file movies_titles.csv.
The output of the reducer provides the movie_id as the key and the (first, last, year, count, avg, name) as the value for the corresponding movie_id.



Problems Faced during execution of the code:
Unable to Install Hadoop in the local machine.
Unable to create a Virtual environment for Hadoop due to low RAM.

Tried the Hadoop Setup from https://www.datasciencecentral.com/profiles/blogs/how-to-install-and-run-hadoop-on-windows-for-beginners.


