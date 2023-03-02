# NewsScraping
Our main motivation behind this project was to be able to have a deep dive into fields like data scraping, natural language processing and deep learning models. 
# NEWS SCRAPING USING NewsAPI and Spyder
## Using BERT and K-NN Algo to give user recommendations


<p align="center" width="100%">
    <img width="33%" src="https://www.webstrategicmarketing.com/wp-content/uploads/2020/08/google-bert-1200x900.jpg"> 
    <img width="30%" src="https://www.pngall.com/wp-content/uploads/2016/05/Python-Logo-Free-Download-PNG.png"> 
    <img width="33%" src="https://const.fr/wp-content/uploads/2013/07/spiders.jpg"> 
</p>

**In this project we have implemented a model which inculcates various applications of Artificial Intelligence into one. 
It consists of web scraping and subsequent data collection using Crawlers and NewsAPI’s, Transformer model such as BERT, clustering algorithms such as K-means, Agglomerative clustering, and finally a frontend framework using Flask to recommend news articles to the end user.**  

## Key Pointers


- A Recommender System basically analyzes reader’s past article history and reading behaviour to suggest any future articles they might be inclined to read .
- Utilising the power of Scrapy and NewsAPI  to extract news articles from famous agencies such as Hindustan Times , Reuters, BBC and CNN we preprocessed the extracted data which was then finally passed into the BERT model. 
- A similarity measure was then used to find the cosine similarity between the outputs of the BERT model , and then concluded by by applying clustering techniques to recommend articles.


# Important reference material to understand the code

1. [What is Scrappy and what is its use here?](https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/)
2. [NewsAPI and the necessary documentation to implement it](https://newsapi.org/)
3. [What is BERT?](https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270)
4. [How can we do the code implementation of Bert?](https://neptune.ai/blog/how-to-code-bert-using-pytorch-tutorial#:~:text=BERT%20uses%20two%20training%20paradigms,a%20big%20corpus%20like%20Wikipedia)


Apart from these key reference materials, I have created inline links all across the README Doc for anyone looking to understand the code with clearer comprehension.
## How to understand the flow of the code?
Through the projects life cycle, we used PyCharm, Google Colab and Jupyter Notebook for the work. PyCharm for Spyder Crawlers, Google Colab for NewsAPI, and Jupyter for BERT and KNN implementation. Some things to understand are:

- First we used PyCharm to create Spyder crawlers that scrapped news articles from the internet.
- Then on Google Colab, we used [NewsAPI to take out news articles in masses, afterwhich we used Pandas Libraries to store all the articles with the necessary documentation into CSV files.](https://docs.newscatcherapi.com/knowledge-base/guides-and-tutorials/export-news-into-a-csv-with-python)

- All the data was then stored into CSV files, and then we headed to Jupyter Notebook where implemented BERT Algo on it, which provided us the cosine similarities between articles.
- We transported the cosine similarities into a KNN algo, but also had an alternate manual approach, the google colab code for which is attached to the repository. 


The code is straight and simple, and is one of the million ways we can use BERT as a tangible application in todays world.














   
