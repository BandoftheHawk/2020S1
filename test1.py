#!/usr/bin/env python
# coding: utf-8

# # Basic Python
# ### Beginning Python

# In[1]:


def hello (who):                          # 1
    """Greet somebody"""                  # 2
    print("Hello " + who + "!")           # 3


# 1 Defines a new function/procedure called `hello` which takes a single argument.  Note that python variables are not typed, who could be a string, integer, array ... The line ends with a colon (:) which means we're beginning an indented code block.
# 
# 2 Firstly note that there are no brackets delimiting the body of the procedure, Python instead uses indentation to delimit code blocks. So, getting the indentation right is crucial!
#   
# This line (2) is a documentation string for the procedure which gets associated with it in the python environment. The three double quotes delimit a multi-line string (could use ' or " in this context).
# 
# 3 This is the body of the procedure, ``print`` is a built in command in python. Note that the Python 2.x versions do not use round brackets, this is a major difference with Python 3.x. We also see here the `+` operator used on strings (I'm assuming `who`is a string) to perform concatenation --- thus we have operator overloading based on object type just like other OO languages.
# 

# In[2]:


help(hello)


# In[3]:


hello("Steve")


# Here I'm calling the new procedure with a literal string argument delimited by `"`.

# In[4]:


hello('world')


# And here delimited by `'` --- both of these delimiters are equivalent, use one if you want to include the other in the string, eg `"Steve's"`.

# In[5]:


people =  ['Steve', "Mark", 'Diego']      # 6
for person in people:                     # 7
    hello(person)                         # 8


# 6 This defines a variable people to have a value which is a list of strings, lists are 1-D arrays and the elements can be any python object (including lists).
# 
# 7 A `for` loop over the elements of the list. Again the line ends with a colon indicating a code block to follow.
# 
# 8 Call the procedure with the variable which will be bound to successive elements of the list.
# 

# ### Core Data Types
# 1. Strings
# 2. Numbers (integers, float, complex)
# 3. Lists
# 4. Tuples (inmutable sequences)
# 5. Dictionaries (associative arrays)
# 

# ### Lists

# In[6]:


a = ['one', 'two', 3, 'four']


# In[7]:


a[0]


# In[8]:


a[-1]


# In[9]:


a[0:3]


# In[10]:


len(a)


# In[11]:


len(a[0])


# In[12]:


a[1] = 2
a


# In[13]:


a.append('five')
a


# In[14]:


top = a.pop()
a


# In[15]:


top


# ### List Comprehensions
# List comprehensions are a very powerful feature of Python. They reduce the need to write simple loops.

# In[16]:


a = ['one', 'two', 'three', 'four']
len(a[0])


# In[17]:


b = [w for w in a if len(w) > 3]
b


# In[18]:


c = [[1,'one'],[2,'two'],[3,'three']]
d = [w for [n,w] in c]
d


# ### Tuples
# Tuples are a sequence data type like lists but are immutable:
# * Once created, elements cannot be added or modified.
# 
# Create tuples as literals using parentheses:
# 

# In[19]:


a  = ('one', 'two', 'three')


# Or from another sequence type:

# In[20]:


a = ['one', 'two', 'three']
b = tuple(a)


# Use tuples as fixed length sequences: memory advantages.
# 
# 

# ### Dictionaries
# * Associative array datatype (hash)
# * Store values under some hash key
# * Key can be any immutable type: string, number, tuple

# In[21]:


names = dict()
names['madonna'] = 'Madonna'
names['john'] = ['Dr.', 'John', 'Marshall']
names.keys()


# In[22]:


list(names.keys())


# In[23]:


ages = {'steve':41, 'john':22}
'john' in ages


# In[24]:


41 in ages


# In[25]:


'john' in ages.keys()


# In[26]:


for k in ages:
    print(k, ages[k])


# ### Organising Source Code: Modules
# * In Python, a module is  a single source file wich defines one or more procedures or classes.
# * Load a module with the `import` directive.
# * After importing the module, all functions are grouped in the module namespace.
# * Python provides many useful modules.
# 

# In[27]:


import math
20 * math.log(3)


# ### Defining Modules
# * A module is a source file containing Python code
#     * Usually class/function definitions.
# * First non comment item can be a docstring for the module.
# 
# ```python
# # my python module
# """This is a python module to
# do something interesting"""
# 
# def foo(x):
#    'foo the x'
#    print('the foo is ' + str(x))
# ```

# # NLTK
# NLTK is a Python module

# In[28]:


import nltk


# Let's do some simple statistics on the Gutenberg corpus

# In[29]:


nltk.download('gutenberg')
nltk.corpus.gutenberg.fileids()


# In[30]:


emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)


# In[31]:


nltk.download('punkt')
from nltk.corpus import gutenberg
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)


# ### Counting Words

# In[32]:


import collections
emma_counter = collections.Counter(emma)
emma_counter.most_common(10)


# In[33]:


emma_counter['Emma']


# ### Exercises
# 1. Identify the 10 most common words in each file of the Gutenberg corpus. Can you see any similarities among them?
# 2. Find the most frequent word with length of at least 7 characters.
# 3. Find the words that are longer than 7 characters and occur more than 7 times.

# ### Count Bigrams
# A bigram is a sequence of two words.

# In[34]:


list(nltk.bigrams([1,2,3,4,5,6]))


# In[35]:


list(nltk.bigrams(emma))[:5]


# * A bigram is an ngram where n is 2
# * A trigram is an ngram where n is 3

# In[36]:


list(nltk.ngrams(emma,4))[:5]


# ### Exercises
# 1. Find the most frequent bigram in Austin's Emma.
# 2. Find the most frequent bigram that begins with 'the'.

# # Text Processing in Python

# ### Sorting
# * The function `sorted()` returns a sorted copy.
# * Sequences can be sorted in place with the `sort()` method.
# * Python 3 does not support sorting of lists with mixed contents.

# In[37]:


foo = [2,5,9,1,11]
sorted(foo)


# In[38]:


foo


# In[39]:


foo.sort()


# In[40]:


foo


# In[41]:


foo2 = [2,5,6,1,'a']
sorted(foo2)


# ### Sorting with a custom sorting criterion

# In[42]:


l = ['a','abc','b','c','aa','bb','cc']


# In[43]:


sorted(l)


# In[44]:


sorted(l,key=len)


# In[45]:


sorted(l,key=len,reverse=True)


# In[46]:


def my_len(x):
    return -len(x)


# In[47]:


sorted(l,key=my_len)


# In[48]:


sorted(l,key = lambda x: -len(x))


# ### Exercises
# You're given data of the following form:
# 
# ```python
# namedat = dict()
# namedat['mc'] = ('Madonna', 45)
# namedat['sc'] = ('Steve', 41)
# ```
# 
# 1. How would you print a list ordered by name?
# 2. How would you print a list ordered by age?

# ### Strings in Python
# * String is a base type.
# * Strings are sequences and can use operations like lists or tuples.

# In[49]:


foo = "A string"
len(foo)


# In[50]:


foo[0]


# In[51]:


foo[0:3]


# In[52]:


multifoo = """A multiline 
string"""


# In[53]:


multifoo


# In[54]:


"my string".capitalize()


# In[55]:


capitalize("my string")


# In[56]:


"my string".upper()


# In[57]:


"My String".lower()


# In[58]:


a = "my string with my other text"
a.count("my")


# In[59]:


a.find("with")


# In[60]:


a.find("nothing")


# ### Split
# * `split(sep)` is a central string operation.
# * It splits a string wherever `sep` occurs (blank space by default)

# In[61]:


foo = "one :: two :: three"
foo.split()


# In[62]:


foo.split('::')


# In[63]:


foo.split(' :: ')


# In[64]:


"this is a test".split()


# ### Join
# * Join is another useful function/method in the string module.
# * It takes a list and joins the elements using some delimiter.
# 

# In[65]:


text="this is some text to analyse"
words=text.split()
print(words)
words.sort()
print(words)
print(", ".join(words))


# ### Replace

# In[66]:


def censor(text):
   'replace bad words in a text with XXX'
   badwords = ['poo', 'bottom']
   for b in badwords:
      text = text.replace(b, 'XXX')
   return text


# In[67]:


censor("this is all poo and more poo")


# ### Text Preprocessing with NLTK
# #### Tokenisation

# In[68]:


import nltk
nltk.download("punkt")
text = "This is a sentence. This is another sentence."
nltk.sent_tokenize(text)


# In[69]:


for s in nltk.sent_tokenize(text):
    for w in nltk.word_tokenize(s):
        print(w)
    print()


# #### Part of speech tagging
# 
# * Often it is useful to know whether a word is a noun, or an adjective, etc. These are called **parts of speech**.
# * NLTK has a part of speech tagger that tags a list of tokens.
# * The default list of parts of speech is fairly detailed but we can set a simplified version (called `universal` by NLTK).
# 
# List of universal tagsets:
# 
# | Tag | Meaning | English Examples |
# | --- | --- | --- |
# | `ADJ` | adjective | new, good, high, special, big, local |
# | `ADP` | adposition | on, of, at, with, by, into, under |
# | `ADV` | adverb | really, already, still, early, now |
# | `CONJ` | conjunction | and, or, but, if, while, although |
# | `DET` | determiner, article | the, a, some, most, every, no, which |
# | `NOUN` | noun | year, home, costs, time, Africa |
# | `NUM` | numeral | twenty-four, fourth, 1991, 14:24 |
# | `PRT` | particle | at, on, out, over per, that, up, with |
# | `PRON` | pronoun | he, their, her, its, my, I, us |
# | `VERB` | verb | is, say, told, given, playing, would |
# | `.` | punctuation marks | . , ; ! |
# | `X` | other | ersatz, esprit, dunno, gr8, univeristy |
# 

# ![WordPosPipeline](WordPosPipeline.png)

# In[70]:


nltk.download("averaged_perceptron_tagger")
nltk.pos_tag(["this", "is", "a", "test"])


# In[71]:


nltk.download("universal_tagset")
nltk.pos_tag(["this", "is", "a", "test"], tagset="universal")


# In[72]:


nltk.pos_tag(nltk.word_tokenize("this is a test"), tagset="universal")


# ![SentPosPipeline](SentPosPipeline.png)

# In[73]:


text = "This is a sentence. This is another sentence."
text_sent_tokens = [nltk.word_tokenize(s) for s in nltk.sent_tokenize(text)]
text_sent_tokens


# In[74]:


nltk.pos_tag_sents(text_sent_tokens, tagset="universal")


# At the time of running this notebook (February 2020), there is a bug in NLTK that generates the above error. The bug is documented here: https://stackoverflow.com/questions/54051402/currently-nltk-pos-tag-only-supports-english-and-russian-i-e-lang-eng-or-la
# 
# Let's implement `my_pos_tag_sents` that replicates the intended original behaviour:

# In[75]:


def my_pos_tag_sents(text_sent_tokens, tagset="universal"):
    return [nltk.pos_tag(s, tagset=tagset) for s in text_sent_tokens]


# In[76]:


my_pos_tag_sents(text_sent_tokens, tagset="universal")


# #### Stemming
# 
# * Often it is useful to remove information such as verb form, or the difference between singular and plural.
# * NLTK offers stemming, which removes suffixes.
#     * The Porter stemmer is a popular stemmer.
# * The remaining stem is not a word but can be used, for example, by search engines (we'll see more of this in another lecture).

# In[77]:


s = nltk.PorterStemmer()


# In[78]:


s.stem("books")


# In[79]:


s.stem("running")


# In[80]:


s.stem("run")


# In[81]:


s.stem("goes")


# In[82]:


[s.stem(w) for w in nltk.word_tokenize("I'm running and he goes")]


# ### Exercises
# 1.  What is the sentence with the largest number of tokens
#     in Austen's "Emma"?
# 2. What is the most frequent part of speech in Austen's "Emma"?
# 3. What is the number of distinct stems in Austen's "Emma"?
# 4. What is the most ambiguous stem in Austen's "Emma"?
#     (meaning, which stem in Austen's "Emma" maps to the
#     largest number of distinct tokens?)

