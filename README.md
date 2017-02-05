#Studying Swiss products (How are Swiss products perceived throughout the world?)

##Abstract:
The goal of this project would be to figure out the perception of Swiss products throughout the world using the Amazon Review dataset. The original dataset includes information about products from all over the world and their reviews (probably, we still have to examine the original dataset). We are going to extract only Swiss products and make statistically valid conclusions based on user ratings.

##Data description: 
The dataset mentioned above contains product reviews and metadata from Amazon, including 142.8 million reviews spanning May 1996 - July 2014.

This dataset includes reviews (ratings, text, helpfulness votes), product metadata (descriptions, category information, price, brand, and image features), and links (also viewed/also bought graphs). Detailed information: http://jmcauley.ucsd.edu/data/amazon/

##Feasibility and Risks: 
The dataset we’ll be dealing with will include products from entire world and one of the challenges will be to come up with a strategy to filter/identify Swiss products from this data since there is no such information (about the country of origin of products). We therefore need to come up with a way to detect products of Swiss origin (Swiss brands, Swiss authors, etc.) Apart from this, it however seems feasible to extract ratings of these products and make statistical conclusions about them.

##Deliverables: 
Different options are possible. The exact representation of result will be determined during implementation. For instance: we can make statistics of product ratings for all products considering one company, author, etc., in order to understand differences in popularity of products within each group. Moreover, we can categorize products (i.e. books, watches, etc.) and obtain information of products that are most rated and least rated in each category, make some ratings about companies within each category. We can investigate which category of Swiss products is the most and least rated. Results we get for Swiss products can be compared with products from other countries (for which we could also make statistics).

P.S. Json files with data used in project.ipynb are too big to upload them on GitHub. Dropbox link: https://www.dropbox.com/s/h205bk0pdn2uj41/ada_project_datasets.zip?dl=0

##Timeplan:
* *November*: We will focus more on our homework, do theoretical preparation, do brainstorming about implementation. 
* *Early December*: We should be done with data gathering which we will need for extraction Swiss data from dataset and we will start implementation of such extraction.
* *Mid-December/Late December*: We should be done with extracting Swiss data from dataset and make vast majority of data processing.
* *January*: Make final improvement and complete project by end-January.
