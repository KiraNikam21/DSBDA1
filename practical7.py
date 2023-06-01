{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bc787c53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nltk in /home/design/anaconda3/lib/python3.9/site-packages (3.6.5)\n",
      "Requirement already satisfied: click in /home/design/anaconda3/lib/python3.9/site-packages (from nltk) (8.0.3)\n",
      "Requirement already satisfied: joblib in /home/design/anaconda3/lib/python3.9/site-packages (from nltk) (1.1.0)\n",
      "Requirement already satisfied: regex>=2021.8.3 in /home/design/anaconda3/lib/python3.9/site-packages (from nltk) (2021.8.3)\n",
      "Requirement already satisfied: tqdm in /home/design/anaconda3/lib/python3.9/site-packages (from nltk) (4.62.3)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d5e54b04",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to /home/design/nltk_data...\n",
      "[nltk_data]   Unzipping tokenizers/punkt.zip.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import nltk\n",
    "nltk.download('punkt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1ca21bf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Hello Mr. Smith, how are you doing today?', 'The weather is great, and city is awesome.', 'The sky is pinkish - blue.', \"You shouldn'teat cardboard\"]\n"
     ]
    }
   ],
   "source": [
    "from nltk.tokenize import sent_tokenize\n",
    "text=\"Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish - blue. You shouldn'teat cardboard\"\n",
    "\n",
    "tokenized_text=sent_tokenize(text)\n",
    "print(tokenized_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d711525a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Hello', 'Mr.', 'Smith', ',', 'how', 'are', 'you', 'doing', 'today', '?', 'The', 'weather', 'is', 'great', ',', 'and', 'city', 'is', 'awesome', '.', 'The', 'sky', 'is', 'pinkish', '-', 'blue', '.', 'You', \"shouldn'teat\", 'cardboard']\n"
     ]
    }
   ],
   "source": [
    "from nltk.tokenize import word_tokenize\n",
    "tokenized_word=word_tokenize(text)\n",
    "print(tokenized_word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cdc9594c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<FreqDist with 25 samples and 30 outcomes>\n"
     ]
    }
   ],
   "source": [
    "from nltk.probability import FreqDist\n",
    "fdist = FreqDist(tokenized_word)\n",
    "print(fdist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b8d805fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('is', 3), (',', 2)]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fdist.most_common(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5e6dcda9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "fdist.plot(30,cumulative=False)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bdd80bb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "sent = \"Albert Einstein was born in Ulm, Germany in 1879.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9d0153fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Albert', 'Einstein', 'was', 'born', 'in', 'Ulm', ',', 'Germany', 'in', '1879', '.']\n"
     ]
    }
   ],
   "source": [
    "tokens=nltk.word_tokenize(sent)\n",
    "print(tokens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a1cc594b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package averaged_perceptron_tagger to\n",
      "[nltk_data]     /home/design/nltk_data...\n",
      "[nltk_data]   Package averaged_perceptron_tagger is already up-to-\n",
      "[nltk_data]       date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[('Albert', 'NNP'),\n",
       " ('Einstein', 'NNP'),\n",
       " ('was', 'VBD'),\n",
       " ('born', 'VBN'),\n",
       " ('in', 'IN'),\n",
       " ('Ulm', 'NNP'),\n",
       " (',', ','),\n",
       " ('Germany', 'NNP'),\n",
       " ('in', 'IN'),\n",
       " ('1879', 'CD'),\n",
       " ('.', '.')]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download('averaged_perceptron_tagger') \n",
    "nltk.pos_tag(tokens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "968a86cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'such', 'about', 'won', 'mightn', 'what', 'be', \"wasn't\", 'am', 'who', \"aren't\", 'nor', 'than', 'shouldn', \"should've\", 'm', 'wouldn', 'their', 'are', \"haven't\", 'doing', 'once', 'all', 's', 'doesn', 'is', 'them', 'or', 'have', 'against', 'above', 'an', 'down', 'y', \"mustn't\", 'had', 'yourselves', 'himself', 'very', 'aren', 'were', 'here', 're', 'both', 'own', 'only', 'but', 'off', \"you'd\", \"shouldn't\", 'as', 'that', 'before', 'most', 'mustn', 'yours', 'i', 'having', 'then', 'whom', 'we', 'been', 'ma', 'myself', 'theirs', 'being', \"hadn't\", 'hasn', 'not', 'at', 'how', 'any', 'these', 'can', 'he', 'she', 'until', 'herself', 'do', 'didn', 'so', 'where', 'themselves', 'ourselves', 'over', 'couldn', \"doesn't\", \"didn't\", \"it's\", 'the', 'by', 'her', 'll', 'this', 'other', 'now', 'isn', 'on', 'don', 'which', \"you're\", \"weren't\", 'each', 'some', 'up', 'will', 'your', 'hers', 'out', 'they', 'same', 'during', 'its', \"you've\", 'there', 'no', 'yourself', 'with', \"she's\", 'just', 'itself', \"that'll\", 'more', 'for', \"couldn't\", 'and', 'him', 'o', \"you'll\", 'needn', \"wouldn't\", 've', 'should', 'again', \"won't\", 'through', 'if', 'few', 'between', 'to', 'weren', 'has', \"hasn't\", 'why', 'does', 'our', 'it', \"shan't\", 'ours', \"needn't\", 'after', 'further', 'hadn', 'shan', 'too', 'ain', \"don't\", 'while', 'those', 'a', 'under', 'in', 'when', \"isn't\", 'because', 'of', 'me', 'his', 'was', 'from', 'haven', 't', 'wasn', 'd', 'my', 'you', 'into', \"mightn't\", 'below', 'did'}\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to /home/design/nltk_data...\n",
      "[nltk_data]   Unzipping corpora/stopwords.zip.\n"
     ]
    }
   ],
   "source": [
    "nltk.download('stopwords')\n",
    "from nltk.corpus import stopwords\n",
    "stop_words=set(stopwords.words(\"english\"))\n",
    "print(stop_words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6ce54f7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tokenized Sentence: ['Albert', 'Einstein', 'was', 'born', 'in', 'Ulm', ',', 'Germany', 'in', '1879', '.']\n",
      "Filterd Sentence: ['Albert', 'Einstein', 'born', 'Ulm', ',', 'Germany', '1879', '.']\n"
     ]
    }
   ],
   "source": [
    "filtered_sent=[]\n",
    "for w in tokens:\n",
    "    if w not in stop_words:\n",
    "        filtered_sent.append(w)\n",
    "print(\"Tokenized Sentence:\",tokens)\n",
    "print(\"Filterd Sentence:\",filtered_sent)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "320f8d81",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Filtered Sentence: ['Albert', 'Einstein', 'born', 'Ulm', ',', 'Germany', '1879', '.']\n",
      "Stemmed Sentence: ['albert', 'einstein', 'born', 'ulm', ',', 'germani', '1879', '.']\n"
     ]
    }
   ],
   "source": [
    "from nltk.stem import PorterStemmer\n",
    "from nltk.tokenize import sent_tokenize, word_tokenize\n",
    "ps = PorterStemmer()\n",
    "stemmed_words=[]\n",
    "for w in filtered_sent:\n",
    "    stemmed_words.append(ps.stem(w))\n",
    "print(\"Filtered Sentence:\",filtered_sent)\n",
    "print(\"Stemmed Sentence:\",stemmed_words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "7ee02a69",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package wordnet to /home/design/nltk_data...\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lemmatized Word: dog\n",
      "Stemmed Word: dog\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data]   Package wordnet is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "nltk.download('wordnet')\n",
    "from nltk.stem.wordnet import WordNetLemmatizer\n",
    "lem = WordNetLemmatizer()\n",
    "from nltk.stem.porter import PorterStemmer\n",
    "stem = PorterStemmer()\n",
    "word = \"dogs\"\n",
    "print(\"Lemmatized Word:\",lem.lemmatize(word,\"n\"))\n",
    "print(\"Stemmed Word:\",stem.stem(word))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "3e803843",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import sklearn as sk\n",
    "import math\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "77a7072c",
   "metadata": {},
   "outputs": [],
   "source": [
    "first_sentence = \"Data Science is the sexiest job of the 21st century \"\n",
    "second_sentence = \"machine learning is the key for data science\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ede8c0d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "first_sentence= first_sentence.split(\" \")\n",
    "second_sentence=second_sentence.split(\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "16fecf06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'sexiest', 'century', '', 'for', 'science', 'job', 'key', '21st', 'the', 'learning', 'Science', 'data', 'machine', 'Data', 'of', 'is'}\n"
     ]
    }
   ],
   "source": [
    "total =set(first_sentence).union(set(second_sentence))\n",
    "print(total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "99e5d49e",
   "metadata": {},
   "outputs": [],
   "source": [
    "wordDictA = dict.fromkeys(total, 0)\n",
    "wordDictB = dict.fromkeys(total, 0)\n",
    "for word in first_sentence:\n",
    "    wordDictA[word]+= 1\n",
    "for word in second_sentence :\n",
    "    wordDictB[word]+= 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "46448a94",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sexiest</th>\n",
       "      <th>century</th>\n",
       "      <th></th>\n",
       "      <th>for</th>\n",
       "      <th>science</th>\n",
       "      <th>job</th>\n",
       "      <th>key</th>\n",
       "      <th>21st</th>\n",
       "      <th>the</th>\n",
       "      <th>learning</th>\n",
       "      <th>Science</th>\n",
       "      <th>data</th>\n",
       "      <th>machine</th>\n",
       "      <th>Data</th>\n",
       "      <th>of</th>\n",
       "      <th>is</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   sexiest  century     for  science  job  key  21st  the  learning  Science  \\\n",
       "0        1        1  1    0        0    1    0     1    2         0        1   \n",
       "1        0        0  0    1        1    0    1     0    1         1        0   \n",
       "\n",
       "   data  machine  Data  of  is  \n",
       "0     0        0     1   1   1  \n",
       "1     1        1     0   0   1  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame([wordDictA, wordDictB])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "7e20001c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def computeTF(wordDict, doc):\n",
    "    tfDict = { }\n",
    "    corpusCount = len(doc )\n",
    "    for word, count in wordDict.items():\n",
    "        tfDict[word] = count/float(corpusCount)\n",
    "    return(tfDict)#running our sentences through the f t\n",
    "tfFirst = computeTF(wordDictA, first_sentence)\n",
    "tfSecond = computeTF(wordDictB, second_sentence)#Converting todataframe for visualization\n",
    "tf = pd.DataFrame([tfFirst,tfSecond])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "3fbf529b",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (4185472167.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_4683/4185472167.py\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    sklearn.feature_extraction.text import TfidfVectorizer\u001b[0m\n\u001b[0m                                    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c23dde8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
