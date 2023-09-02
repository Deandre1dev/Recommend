# Import spacy module.
import spacy
nlp = spacy.load('en_core_web_md')

# list to store the sentences that will be used to compared.
li = []    

# Sentence to compare.
compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Open movie file for reading and loop through each line.
f = open("movies.txt", "r")

for line in f:
    (li.append(line)) # Appends each line of text into the list li.

# Dictionary used to filter which movie will be the best recommendation.
filtr = {}

# List that will be used to find the highest recommendation.


# Function to get movie recomendation.
def recommend_movie(sentence_to_compare, sentences):

    model_sentence = nlp(sentence_to_compare)

    for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        filtr.update({similarity:sentence})
   
        # Sorting the dictionary.
        new = (dict(sorted(filtr.items())))

        # Adding the sorted dictionary items into a temporary list which then can be used to retrive the highest recommendation.
        temp = list(new.items())   

    # printing result.
    print("Next movie recommendation is : " + str(temp[-1][1]))

recommend_movie(compare,li)