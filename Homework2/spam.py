
# Spam filtering

# 1. Scan entire text (including headers and embedded html and javascript)

#    words ::= a-zA-Z0-9-'$
#    separators ::= everything else

# 2. Ignore tokens that are all digits, html comments, etc.

# 3. Count the number of times each token occurs (case-insensitive)
#  --> a giant hash for each corpus
#      [(word, #OfOccurrences)]
#
#  Two hash tables, one for the spam corpus, the other for the non-spam


# 4. Create a third hash table (token: prob(spam|token))
#
#
#         (let ((g (* 2 (or (gethash word good) 0)))
#               (b (or (gethash word bad) 0)))
#            (unless (< (+ g b) 5)
#              (max .01
#                   (min .99 (float (/ (min 1 (/ b nbad))
#                                      (+ (min 1 (/ g ngood))
#                                         (min 1 (/ b nbad)))))))))
#         let() defines local variables, so g & b are variables with the given values;
#         or() is often used to set default values as in (or expression defaultValue)
#         unless() is the opposite of if();
#         arithmetic operators are prefix, so (+ 1 1) means 1+1;
#         min() works the same way in both languages.
#         Explanation:
#
#              set g = 2 * the word's good value (or 0 if there is no value)
#              set b = the word's bad value (or 0)
#              if g+b > 5
#                   return max(0.01, min(0.99, min(1.0, b/nbad) / (min(1.0, g/ngood) + min(1.0, b/nbad))))
#              else
#                   return 0

# biases good numbers by doubling their counts
# only considers words that occur more than 5 times


# 5. most interesting (furthest from a neutral .5) are used to determine the spam-ity of the email

#
# (let ((prod (apply #'* probs)))
#   (/ prod (+ prod (apply #'* (mapcar #'(lambda (x)
#                                          (- 1 x))
#                                      probs)))))
# the apply() multiplies the given list elements together;
# the mapcar() applies the given function to each element of the given list.
# Explanation:
#
#      set prod = the produce of the elements of probs
#      return prod / (prod + (the product of the complement of the elements of probs))

# cutoff for spam detection (0.9)


## First Step: Load in the corpus and count up word occurrences for both

# Sample SPAM/HAM corpus
# spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
# ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
spam_corpus = ["I", "am", "spam", "spam", "I", "am", "I", "do", "not", "like", "that", "spamiam", "spam", "spam", "spam", "spam", "spam", "spam"]
for i in range(0, 50):
    spam_corpus.append("spam")
ham_corpus = ["do", "i", "like", "green", "eggs", "and", "ham", "i", "do"]


# merge together the two lists into all tokens
all_tokens = spam_corpus + ham_corpus
all_tokens = list(dict.fromkeys(all_tokens))

spam_counts = {}
ham_counts = {}

for token in all_tokens:
    spam_counts[token] = 0
    ham_counts[token] = 0


def prob(token):
    good = 2 * ham_counts[token]
    bad = spam_counts[token]
    n_bad = 2
    n_good = 2
    # count threshold of 1
    if good + bad >= 1:
        return max(0.01, min(0.99, min(1.0, bad / n_bad) / (min(1.0, good / n_good) + min(1.0, bad / n_bad))))
    else:
        return 0

# Determine occurrences of each word in each corpus:
# - the spam corpus
for token in spam_corpus:
    spam_counts[token] += 1

# - the ham corpus
for token in ham_corpus:
    ham_counts[token] += 1

# just to verify that my occurrence tables are rational
print(all_tokens)
print("spam: " + str(spam_counts))
print("ham: " + str(ham_counts))

## Second Step: Calculate spam probabilities for each token


#              set g = 2 * the word's good value (or 0 if there is no value)
#              set b = the word's bad value (or 0)
#              if g+b > 5
#                   return max(0.01, min(0.99, min(1.0, b/nbad) / (min(1.0, g/ngood) + min(1.0, b/nbad))))
#              else
#                   return 0

# finding the probabilities
probabilities = {}
for token in all_tokens:
    probabilities[token] = prob(token)


# grabbing the first 15 values furthest from 50%
def get_top_interesting_values(values, limit=15):
    # calculate the probability that the message is spam given each word separately
    probabilities = {}
    for i in values:
        probabilities[i] = prob(i)

    # sort the probabilities by how "interesting" each value is
    # i.e. how far away from 50% it is
    sorted_values = sorted(probabilities.items(), key=lambda x: -abs(x[1]-0.5))

    count = 0
    interesting = []

    # grab the most "interesting" values to evaluate the email
    for item in sorted_values:
        interesting.append(item[1])
        count += 1
        # stop once we hit get 15 or so values
        if count > limit:
            break

    return interesting

print(probs)

from functools import reduce

def is_spam(featured_probs):
    prod = reduce((lambda x, y: x * y), featured_probs)
    compl = reduce((lambda x, y: x * y), list(map(lambda x: 1 - x, featured_probs)))
    value = prod / (prod + compl)
    return value
print(value)

