import random

def get_adjective():
    """
    Return a randomly chosen adjective
    from this list of adjectives:
        "adorable", "adventurous", "aggressive",
        "agreeable", "alert", "alive", "amused",
        "angry", "annoyed", "anxious", "arrogant",
        "attractive", "average", "bad, "beautiful",
        "bewildered", "black", "bloody","blue-eyed",
        "blushing", "bored", "brainy",
    """
    adj=["adorable", "adventurous", "aggressive",
        "agreeable", "alert", "alive", "amused",
        "angry", "annoyed", "anxious", "arrogant",
        "attractive", "average", "bad," "beautiful",
        "bewildered", "black", "bloody","blue-eyed",
        "blushing", "bored", "brainy"]
    word = random.choice(adj)
    return word
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the",""]

# Randomly choose and return a determiner.
    word = random.choice(words)
    return word
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
# returns a randomly chosen preposition
    prep = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(prep)
    return word
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns=["bird","boy","car","cat","child","dog","girl","man","rabbit","woman"]
    else:
        nouns=["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    
    """
    if tense=='past':
        verbs=["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense=='present':
        if quantity==1:
            verbs=["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs=["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense=='future':
            verbs=["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    # Randomly choose and return a verb.
    verb = random.choice(verbs)
    return verb
def get_prepositional_phrase(quantity):
    """
    Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
# calls the get_preposition, get_determiner, and get_noun functions
    prep=get_preposition()
    det=get_determiner(quantity)
    noun=get_noun(quantity)
# create the prepositional phrase
    prep_phrase=f"{prep} {det} {noun}"
    return prep_phrase
def make_sentence(quantity, tense):
    """
    Build and return a sentence with six words:
    a determiner, a noun, and a verb, plus a three word pepositional phrase. 
    The grammatical quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
# calls the get_determiner, get_noun,get_preposiositonal phrase and get_verb functions
    det=get_determiner(quantity)
    adj=get_adjective()
    noun=get_noun(quantity)
    verb=get_verb(quantity,tense)
    prep_phrase=get_prepositional_phrase(quantity)
# capitalize the first word of the sentence
    cap=det.capitalize()
# create the sentence, with a capitialized first word and a period
    sentence=f"{cap} {adj} {noun} {verb} {prep_phrase}."
    return sentence
def main():
    """
    Runs the program.
    for use of the lab we will call it 6 times, using these parameters
    single	past
    single	present
	single	future
	plural	past
	plural	present
	plural	future
    """
    print(make_sentence(1,'past'))
    print(make_sentence(1,'present'))
    print(make_sentence(1,'future'))
    print(make_sentence(2,'past'))
    print(make_sentence(5,'present'))
    print(make_sentence(3,'future'))

main()