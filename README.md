# Data Analysis of Successful Movies
  This project was done by Menachi Korn and Atiar Rahman. Our objective was to analyze data about movies to make suggestions as to what kind of movies can be potentially successful in the future. 

  We first scraped data from Box Office Mojo to get the top grossing movies for every year from 1989 to 2019. Then two APIs were called to get rating, director and budget info among other information. This information was put into a Pandas Dataframe as well as a SQL database.
The data was then analyzed to first see if there is any correlation between critic ratings and movie world wide gross. The dataframe was also cleaned to remove movies that did not gross The graph below shows if the there is any correlation between a movie's world wide gross and it's metascore.

![Graphs](https://github.com/codekorn/mod_1_movies/blob/master/graphs/World%20Wide%20Gross%20vs%20Metascore.png)

This next graph observes the relationship between a movie's world wide gross and it's rotten tomatoes critic score. 
![Graphs](https://github.com/codekorn/mod_1_movies/blob/master/graphs/World%20Wide%20Gross%20vs%20Rotten%20Tomatoes%20Score.png)

The next graph observes the same relationship but between a movie's world wide gross and it's IMDB score. 
![Graphs](https://github.com/codekorn/mod_1_movies/blob/master/graphs/Worldwide%20Gross%20vs%20IMDB%20score.png)

These graphs led us to the conclusion that there was hardly a correlation between critic's scores and a movie's success in the box office. Movies that had great reviews can still perform terribly in the box office and sometimes can do just as well as movies that had terrible reviews.

  Next, we decided to explore if a movie's success was correlated with it's rating. The graph below shows the average world wide gross grouped by rating. 
![Graphs](https://github.com/codekorn/mod_1_movies/blob/master/graphs/average_world_wide_gross.png)

At first glance what might assume that rated G movies were doing the best while Rated R movies were doing the worst. However, upon looking at the standard deviation for the world wide gross grouped by rating, one can see that Rated R movies vary the least. 

![Graphs](https://github.com/codekorn/mod_1_movies/blob/master/graphs/std_world_wide_gross.png)

Next, we looked at the average profit percentage grouped by rating as well as the standard deviation of the profit percentage.
![Graphs](https://github.com/codekorn/mod_1_movies/blob/master/graphs/averageprofitpercentageperrating.png)
![Graphs](https://github.com/codekorn/mod_1_movies/blob/master/graphs/std_profit_percentage_per_rating.png)

Looking at these graphs, R Rated movies on average make a large profit off their budget, but this profit percentage can vary tremendously. R Rated movies were also amongst second largest group of movies after PG13 movies in our dataframe. Due to this and it's large profit percentage, we decided to look deeper R Rated movies. 

  First, we looked at R Rated movied and divided them into sets based on their budget. Then we looked at the profit percentage for each of these sets. This can be seen below. 
  
  ![Graphs](https://github.com/codekorn/mod_1_movies/blob/master/graphs/margin.png)
  
Based on this graph, it is obvious that movies that had a budget between 0 an 10 million performed much better than movies in any other set. Since movies in this set did so much better than any other movie, we zoomed in to the graph by setting a limit on the y-axis, so that the performance of the other sets could be seen. 

![Graphs](https://github.com/codekorn/mod_1_movies/blob/master/graphs/margin1.png)


