 
**Abstract**

A client wants to launch a new web-based application for recommending movies to its subscribers. The purpose of the model is to recommend similar movies based on the content. This model will apply the text transformation and modeling techniques to create a movie recommender system and then deploy the entire system using a web application. The data was obtained from the Kaggle website. The dataset has details for 45,000 movies, but only a sample was used. The data was cleaned and preprocessed. TfidfVectorizer was used to transform text to feature vectors. Cosine similarity matrix was created using these vectors to measure similarity between the vectors. This matrix was used to recommend movies based on their title, genre and director. The movie recommender was deployed as a web-based application using streamlit. The output of the system gives five movie recommendations based on the input provided by the user.

**Design**

The project is designed around the four components as illustrated in the following data pipeline. The data is extracted from the website by downloading the required files and later stored in the pandas dataframe. The data is cleaned and prepared for the modeling. The movie recommender system is created based on the title, genre or director inputs provided by the user. The concept of feature vectors and cosine similarity is leveraged for the recommender system. The streamlit app is built and deployed through GitHub.

![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/16a97ef6-b384-4203-afdc-ad98d2d0dfd1)

![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/82f153e4-fd3e-4990-b3ab-7aaa4bb6d636)

![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/a6ae57c6-2894-4ac0-92d3-adf4aaea7894)

![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/d899c8ae-8231-4fd3-8454-5ae4fb85f98f)

![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/79f09dca-ce5e-4684-9e69-a0177c938459)

![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/5e730adb-c086-4685-8496-0b05f3faea76)

![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/9ddf0d83-c6b1-486e-8c62-39b24a774f1e)



**Data**

The data was obtained from the kaggle website - https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset . The dataset has details for 45,000 movies, that includes cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, vote counts and vote averages. A subsample of the data was used to ease uploading on the GitHub. The movies that had more than 600 votes were used in the sample.

The data was cleaned and preprocessed. I used TfidfVectorizer to transform text to feature vectors. Cosine similarity matrix was created using these vectors to measure similarity between the vectors. This matrix was used to recommend movies based on their title, genre and director.

**Algorithms**

•	Data preprocessing:

o	Cleaning

o	Custom fine-tuning

o	Vectorization (TfidfVectorizer)

o	Cosine similarity matrix 


•	Recommender Model:

o	Custom functions using cosine similarity matrix to return 5 similar movies

o	Choice of three inputs provided to the user


•	GitHub repository to store data and outputs


•	Data Visualization:

o	Streamlit app deployed through GitHub


**Tools**

•	Pandas and Numpy: For cleaning data and preprocessing.

•	NLTK, scikit-learn: For preprocessing and modeling data.

•	Streamlit: For creating the web application.

•	GitHub: For storing data and deploying streamlit app.


**Communication**

The following examples are from the streamlit app:

![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/585d1a23-c91f-4304-9b20-208b4cb05518)


![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/dfdcd7da-b9a5-4512-abfd-ef0fb2c77436)


![image](https://github.com/Himani0924/data_engineering_movie_recommender/assets/99743248/667270e0-d997-46cd-85bc-ab5bb742dfaa)

 


# Check the application here - (https://himani0924-data-engineering-recommender-o5en0i.streamlit.app/)
