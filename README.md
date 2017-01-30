#Studying Swiss products (How are Swiss products perceived throughout the world?)

##Abstract:
The goal of this project would be to figure out the perception of Swiss products throughout the world using the Amazon Review dataset. The original dataset includes information about products from all over the world and their reviews (probably, we still have to examine the original dataset). We are going to extract only Swiss products and make statistically valid conclusions based on user ratings.

##Data description: 
The dataset mentioned above consists of entries that include information about products, their categories, reviews, etc. The example of such an entry is:
```
asin                                                     B0009YJ238
brand                                                        Nestle
categories        [[Pet Supplies, Dogs, Treats, Cookies, Biscuit...
description       Busy Bone, 7 OZ, Small/Medium Dog Treat, Twist...
helpful                                                      [0, 0]
imUrl             http://ecx.images-amazon.com/images/I/31ToYepJ...
overall                                                           5
price                                                          3.49
related                                                         NaN
reviewText        I adore my six-month-old dog, Midge.  She's ev...
reviewTime                                              01 22, 2007
reviewerID                                           A3MTXMDJ7JQSFO
reviewerName                                            A. Ruminski
salesRank                                  {'Pet Supplies': 487454}
summary                                     Busy bone = happy owner
title                                        BusyBone MED Dog Treat
unixReviewTime                                           1169424000
```

##Feasibility and Risks: 
The dataset we’ll be dealing with will include products from entire world and one of the challenges will be to come up with a strategy to filter/identify Swiss products from this data since there is no such information (about the country of origin of products). We therefore need to come up with a way to detect products of Swiss origin (Swiss brands, Swiss authors, etc.) Apart from this, it however seems feasible to extract ratings of these products and make statistical conclusions about them.

##Deliverables: 
Different options are possible. The exact representation of result will be determined during implementation. For instance: we can make statistics of product ratings for all products considering one company, author, etc., in order to understand differences in popularity of products within each group. Moreover, we can categorize products (i.e. books, watches, etc.) and obtain information of products that are most rated and least rated in each category, make some ratings about companies within each category. We can investigate which category of Swiss products is the most and least rated. Results we get for Swiss products can be compared with products from other countries (for which we could also make statistics). 

##Timeplan:
* *November*: We will focus more on our homework, do theoretical preparation, do brainstorming about implementation. 
* *Early December*: We should be done with data gathering which we will need for extraction Swiss data from dataset and we will start implementation of such extraction.
* *Mid-December/Late December*: We should be done with extracting Swiss data from dataset and make vast majority of data processing.
* *January*: Make final improvement and complete project by end-January.
