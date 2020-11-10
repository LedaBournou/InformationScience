# Chapter 3: Getting started


![](images/Hello_World_Brainfuck.png)

"Hello world" program in __[Brainfuck](https://en.wikipedia.org/wiki/Brainfuck)__


## Getting started

A good scholarly way to get started is reading the introductions to some of the books mentioned in the course description - especially *Handbook of Information Science*, but also *Modern Information Retrieval* or *Information Architecture*.

But let's open up things a bit more anecdotally, with the story of [Paul Otlet and the Internet before the Internet](https://daily.jstor.org/internet-before-internet-paul-otlet/)...


## Manipulating Information

The case of Otlet shows several things, but above all it makes it clear that information (or metadata in this case) never just *is*. It is *always already* manipulated in order to present it in a certain way (Derrida pun intended). So we could say that at the heart of information retrieval is **manipulating information**, i.e. selecting, grouping, filtering, ordering, sorting, ranking. (For those of you who know [SQL](https://en.wikipedia.org/wiki/SQL), notice how this resembles the `select` statement? For those of you who don't, don't worry, we'll look into it later on.)

In programming terms, most of this boils down to string operations, like testing metadata for certain criteria or sorting them. And while manipulating strings might seem easy, things can get complicated really easily.

### Example: sorting strings

Let's look at the example of sorting strings. Suppose our task is presenting an alphabetized list of contact persons. The alphabet is a recognizable and expected key for such a list, so that makes sense. 

Of course, in Python you can just do this:

contacts = ["Doe, John", "Poppins, Mary", "Doe, Jane"]
sorted_contacts = sorted(contacts)
print(sorted_contacts)

But suppose you are dealing with a language where there is no built-in sorting method. (And believe me, there are!) How would you go about sorting a list of strings?

Let me simplify the problem. Somewhere along the line you will have to represent individual characters as numbers, e.g. a = 1, b = 2, and then sort numbers.

So let's think about the root issue: how do you sort a list of numbers?

numbers = [7, 8, 1, 7, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

Of course, the sorting algorithm is a well-known chapter in Computer Science. Some of you might be familiar with different kinds of sorts, like merge sort, insertion sort or (my favourite) bubble sort. For some Python implementations, see this [Tutorialspoint article](https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm).

But if you have never studied it, writing your own sort for the first time will not be an easy exercise. I challenge you, if you've never done it. For a bit of fun, here's another kind of sort I recently implemented in Python: *random sort*. Very time-inefficient, but perfectly functional!

def random_sort(InputList):
    from random import shuffle
    check = 0
    while check == 0:
        shuffle(InputList)
        test = 0
        for unsorted in InputList:
            if unsorted >= test:
                check = 1
            else:
                check = 0
                break
            test = unsorted
    return InputList

print(random_sort(numbers))

And that's only the first part of the problem: sorting a list of numbers. Now try to think how this would help to sort lists of strings. First of all, how would you translate characters to numbers? 

One way is to use [Unicode](https://en.wikipedia.org/wiki/Unicode) code points for numbers:


for char in "Doe, John":
    print(ord(char), end=",")

But of course when the case changes, the numbers will also change:

for char in "doe, john":
    print(ord(char),end=",")

You can account for that by converting all strings to lower case first, but what happens in the case of `Étienne` versus `Etienne`, which are usually interchangeable?

for char in "Étienne".lower():
    print(char + " = " + str(ord(char)))
print("\n")
for char in "Etienne".lower():
    print(char + " = " + str(ord(char)))

And, by the way, do you know the encoding of the strings the list will contain? And why does that matter?

You can see how complex seemingly trivial tasks of information retrieval, like alphabetizing a list, really are. We've gone from iTunes to bits and bytes, one of the most fundamental concepts in computer science, really quickly.

## Assignment: Onegram Counter

You probably know about Google Book's [Ngram Viewer](https://books.google.com/ngrams): when you enter phrases into it, it displays a graph showing how those phrases have occurred in a corpus of books (e.g., "British English", "English Fiction", "French") over the selected years. 

Your assignment for this course is something similar: build a Python function that can take the file `data/corpus.txt` (UTF-8 encoded) from this repo as an argument and print a count of the 100 most frequent 1-grams (i.e. *single words*).

In essence the job is to do this:

from collections import Counter
import os

def onegrams(file):
    with open(file, 'r') as corpus:
        text = corpus.read()
        # .casefold() is better than .lower() here
        # https://www.programiz.com/python-programming/methods/string/casefold
        normalize = text.casefold()
        words = normalize.split(' ')
        count = Counter(words) 
        return count

ngram_viewer = onegrams(os.path.join('data', 'corpus.txt'))
print(ngram_viewer.most_common(100))

However, you can't use the `collections` library. Moreover, try to think about what else may be suboptimal in this example. For instance, in this code all of the text is loaded into memory in one time (with the `read()` method). What would happen if we tried this on a really big text file? **Most importantly, the count is also wrong**. Check by counting in an editor, for instance, and try to find out why.

If this is an easy task for you, you can also think about the graphical representation of the 1-gram count.