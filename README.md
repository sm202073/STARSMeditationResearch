## STARSMeditationResearch

As part of Computer Science Research Scholars/Student Ambassadors at Illinois, Sana Madhavan and Anushree Tiberwal have collected mindful meditation scripts focused on two major categories: sleep and anxiety and stress meditations. With Professor Roxana Girju as our research mentor, we have started exploratory analysis of the ~100 text-based script corpora in each category, exploring NLP in meditation. 

# LDA Modeling
Latent Dirichlet Allocation (LDA) Topic Modeling is a popular form of statistical topic modeling with input data. It looks at a document to determine a set of topics that are likely to have generated that collection of words. There are 2 parts:

The words within a document (a known factor)
Probability of words belonging to a topic (to be calculated)

LDA objectives:

Determine how many words belong to a specific topic
How many documents belong to a specific topic because of a certain word

This can be modeled with with a cluster of bars in a graph into unsupervised topics. This output is in the respecive category folders as a png. We have run the model using Python LDA model packages. 

Next steps: 
Using the MFTM (Multi-faceted topic modeling package), we will scale the topic model to generic categories and use the Python scripts to specify parameters.

# ccLDA Modeling 
In the ccMix model, the probability that a word comes from the collection-specific distribution versus the shared distribution depends on a single user-defined parameter λC, which we automatically learn the probability of. The nature of the λC parameter is quite restrictive in that it is the same regardless of the topic and collection. In our model, this probability depends on the collection and topic, which should allow for a more accurate fitting of the data, as some topics may be shared across the collections to a different degree than others. 
Additionally, ccLDA allows the topic distributions for each document to come from non-uniform Dirichlet priors that depends on the document’s collection, so we can easily determine if a topic is not shared among all collections, and thus we can automatically remove or set aside such topics. 

Next steps:
Implement the ccLDA model in the MFTM package as specified by Girju and Paul (2009). 

##Predictive Analysis
As the second phase of the project, we will build a predictive NLP model to capture/generate mindful language. 

