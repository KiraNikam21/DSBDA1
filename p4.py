{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "04b681f2",
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
       "      <th>sepal.length</th>\n",
       "      <th>sepal.width</th>\n",
       "      <th>petal.length</th>\n",
       "      <th>petal.width</th>\n",
       "      <th>species</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Setosa</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   sepal.length  sepal.width  petal.length  petal.width species\n",
       "0           5.1          3.5           1.4          0.2  Setosa\n",
       "1           4.9          3.0           1.4          0.2  Setosa\n",
       "2           4.7          3.2           1.3          0.2  Setosa\n",
       "3           4.6          3.1           1.5          0.2  Setosa\n",
       "4           5.0          3.6           1.4          0.2  Setosa"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "df=pd.read_csv(\"iris.csv\")\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "17978d6b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Setosa', nan, 'Versicolor', 'Virginica', 'sertosa', 'kjnswkaefrs'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.species.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ea6f05fa",
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
       "      <th>sepal.length</th>\n",
       "      <th>sepal.width</th>\n",
       "      <th>petal.length</th>\n",
       "      <th>petal.width</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>species</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Setosa</th>\n",
       "      <td>49</td>\n",
       "      <td>49</td>\n",
       "      <td>48</td>\n",
       "      <td>49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Versicolor</th>\n",
       "      <td>50</td>\n",
       "      <td>50</td>\n",
       "      <td>50</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Virginica</th>\n",
       "      <td>49</td>\n",
       "      <td>49</td>\n",
       "      <td>49</td>\n",
       "      <td>49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>kjnswkaefrs</th>\n",
       "      <td>18</td>\n",
       "      <td>18</td>\n",
       "      <td>18</td>\n",
       "      <td>18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sertosa</th>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             sepal.length  sepal.width  petal.length  petal.width\n",
       "species                                                          \n",
       "Setosa                 49           49            48           49\n",
       "Versicolor             50           50            50           50\n",
       "Virginica              49           49            49           49\n",
       "kjnswkaefrs            18           18            18           18\n",
       "sertosa                20           20            20           20"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(df.species).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4cc9abed",
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
       "      <th>sepal.length</th>\n",
       "      <th>sepal.width</th>\n",
       "      <th>petal.length</th>\n",
       "      <th>petal.width</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>species</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Setosa</th>\n",
       "      <td>4.3</td>\n",
       "      <td>2.3</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Versicolor</th>\n",
       "      <td>4.9</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Virginica</th>\n",
       "      <td>4.9</td>\n",
       "      <td>2.2</td>\n",
       "      <td>4.5</td>\n",
       "      <td>1.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>kjnswkaefrs</th>\n",
       "      <td>4.5</td>\n",
       "      <td>4.5</td>\n",
       "      <td>4.5</td>\n",
       "      <td>4.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sertosa</th>\n",
       "      <td>3.3</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.3</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             sepal.length  sepal.width  petal.length  petal.width\n",
       "species                                                          \n",
       "Setosa                4.3          2.3           1.0          0.1\n",
       "Versicolor            4.9          2.0           3.0          1.0\n",
       "Virginica             4.9          2.2           4.5          1.4\n",
       "kjnswkaefrs           4.5          4.5           4.5          4.5\n",
       "sertosa               3.3          1.0           3.3          1.0"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(df.species).min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "20e6b65e",
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
       "      <th>sepal.length</th>\n",
       "      <th>sepal.width</th>\n",
       "      <th>petal.length</th>\n",
       "      <th>petal.width</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>species</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Setosa</th>\n",
       "      <td>5.8</td>\n",
       "      <td>4.2</td>\n",
       "      <td>1.9</td>\n",
       "      <td>0.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Versicolor</th>\n",
       "      <td>7.0</td>\n",
       "      <td>3.4</td>\n",
       "      <td>5.1</td>\n",
       "      <td>1.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Virginica</th>\n",
       "      <td>7.9</td>\n",
       "      <td>3.8</td>\n",
       "      <td>6.9</td>\n",
       "      <td>2.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>kjnswkaefrs</th>\n",
       "      <td>6.3</td>\n",
       "      <td>4.5</td>\n",
       "      <td>6.3</td>\n",
       "      <td>4.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sertosa</th>\n",
       "      <td>5.1</td>\n",
       "      <td>5.4</td>\n",
       "      <td>5.1</td>\n",
       "      <td>5.4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             sepal.length  sepal.width  petal.length  petal.width\n",
       "species                                                          \n",
       "Setosa                5.8          4.2           1.9          0.6\n",
       "Versicolor            7.0          3.4           5.1          1.8\n",
       "Virginica             7.9          3.8           6.9          2.5\n",
       "kjnswkaefrs           6.3          4.5           6.3          4.5\n",
       "sertosa               5.1          5.4           5.1          5.4"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(df.species).max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a9216e57",
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
       "      <th>sepal.length</th>\n",
       "      <th>sepal.width</th>\n",
       "      <th>petal.length</th>\n",
       "      <th>petal.width</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>species</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Setosa</th>\n",
       "      <td>0.341465</td>\n",
       "      <td>0.355807</td>\n",
       "      <td>0.173703</td>\n",
       "      <td>0.104083</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Versicolor</th>\n",
       "      <td>0.516171</td>\n",
       "      <td>0.313798</td>\n",
       "      <td>0.469911</td>\n",
       "      <td>0.197753</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Virginica</th>\n",
       "      <td>0.634590</td>\n",
       "      <td>0.325817</td>\n",
       "      <td>0.553706</td>\n",
       "      <td>0.275533</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>kjnswkaefrs</th>\n",
       "      <td>0.770027</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.770027</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sertosa</th>\n",
       "      <td>0.738704</td>\n",
       "      <td>1.805722</td>\n",
       "      <td>0.738704</td>\n",
       "      <td>1.805722</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             sepal.length  sepal.width  petal.length  petal.width\n",
       "species                                                          \n",
       "Setosa           0.341465     0.355807      0.173703     0.104083\n",
       "Versicolor       0.516171     0.313798      0.469911     0.197753\n",
       "Virginica        0.634590     0.325817      0.553706     0.275533\n",
       "kjnswkaefrs      0.770027     0.000000      0.770027     0.000000\n",
       "sertosa          0.738704     1.805722      0.738704     1.805722"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(df.species).std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4f836eb5",
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
       "      <th>sepal.length</th>\n",
       "      <th>sepal.width</th>\n",
       "      <th>petal.length</th>\n",
       "      <th>petal.width</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>species</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Setosa</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.4</td>\n",
       "      <td>1.45</td>\n",
       "      <td>0.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Versicolor</th>\n",
       "      <td>5.9</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.35</td>\n",
       "      <td>1.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Virginica</th>\n",
       "      <td>6.5</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.60</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>kjnswkaefrs</th>\n",
       "      <td>4.5</td>\n",
       "      <td>4.5</td>\n",
       "      <td>6.30</td>\n",
       "      <td>4.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sertosa</th>\n",
       "      <td>3.3</td>\n",
       "      <td>1.0</td>\n",
       "      <td>5.10</td>\n",
       "      <td>5.4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             sepal.length  sepal.width  petal.length  petal.width\n",
       "species                                                          \n",
       "Setosa                5.0          3.4          1.45          0.2\n",
       "Versicolor            5.9          2.8          4.35          1.3\n",
       "Virginica             6.5          3.0          5.60          2.0\n",
       "kjnswkaefrs           4.5          4.5          6.30          4.5\n",
       "sertosa               3.3          1.0          5.10          5.4"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(df.species).median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "279bed1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 187 entries, 0 to 186\n",
      "Data columns (total 5 columns):\n",
      " #   Column        Non-Null Count  Dtype  \n",
      "---  ------        --------------  -----  \n",
      " 0   sepal.length  187 non-null    float64\n",
      " 1   sepal.width   187 non-null    float64\n",
      " 2   petal.length  186 non-null    float64\n",
      " 3   petal.width   187 non-null    float64\n",
      " 4   species       186 non-null    object \n",
      "dtypes: float64(4), object(1)\n",
      "memory usage: 7.4+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "59d64f32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "sepal.length    0\n",
       "sepal.width     0\n",
       "petal.length    1\n",
       "petal.width     0\n",
       "species         1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d42ad990",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "species\n",
       "Versicolor     50\n",
       "Setosa         49\n",
       "Virginica      49\n",
       "sertosa        20\n",
       "kjnswkaefrs    18\n",
       "dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " df.value_counts(\"species\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d2be1cf1",
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
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    " \n",
    " \n",
    "sns.countplot(x='species', data=df, )\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "38f2493d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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b9dee23p/Pnzg6+++uqqo20fffRR8DPPPHPSggJWqxWLpW1ouummmyqByp7tadfv3xNkSFkIIc52a14L5tnUwfwucCTPpg5mzWunVZ5v5syZ5d9++23A0ZJ6u3btci8qKnKrra01DRs2LD0zMzNj2rRpAysrK00AMTExgx977LGokSNHpr3++utBTz/9dPjREnzTp08fCEaB+ltuuSUO4ODBg5YLLrggKS0tLTMtLS3z66+/9gH43e9+F5GSkpKVkpKS9dRTT4Wf2C+73c69994bm5KSkpWampr5yiuvBAEsWLDAb8yYMamXXnppYlpaWtbpfO2d6e0nXA18pZTSwByt9csnHqCUuge4ByAurtujDUIIIbpjzWvBfPnLeKyNxgNYzRF3vvxlPACj7uxWMozIyEjb0KFDaz/66KOAm2++uWLevHnBEyZMqP7Tn/4UtXTp0t3+/v72J554IvL3v/99xLPPPnsYwNPT075u3bpdAOHh4UP279+/xcvLS5eUlJhPvP59990XN2nSpOr/9//+X47VaqWystK8bNky73fffTdk3bp1O7TWjBw5MuO8886rnjBhQv3R8958883ALVu2eO3YsWPb4cOHLaNHj8648MILawA2b97ss2HDhm3p6emnlUO6M739hDtBaz0CmAY8oJSafOIBWuuXtdbZWuvssLCwXu6OEEIIB0ueiWkNtkdZG00seSbmdC573XXXlb3//vtBAB9//HFwQkJCY05Ojufo0aPT09PTM997772QAwcOtFYkuuWWW8qP/jktLa3+yiuvTHzppZeC3dzc2uQf/uGHH/x+9rOfFYNRkSgkJMS2ePFi34svvrjC39/fHhAQYL/kkkvKFy1a5Hf8ecuWLfO77rrryiwWCwMGDLCOGTOm5vvvv/cGGDJkSG1vBlvo5YCrtT7U8nsR8B9gdG/eTwghxCmqKWq/DF9H7V100003VSxfvtz/+++/925oaDCNGDGibuLEiVU7d+7cvnPnzu05OTnbPvjgg/1Hj/fz87Mf/fOiRYv2PPDAA8Xr1q3zGTp0aGZzc5uSuW10pS5AZ8d4e3vbO3yzh/RawFVK+Sil/I7+GbgQ2Npb9xNCCNENvuHtP9V11N5FAQEB9rFjx1bfddddCVdddVXZlClTateuXet7tORedXW1afPmzW2q+thsNnJyctwvvfTS6pdeeim/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slJTUzOnT58+EGDRokXew4cPT8/IyMgcPnx4+qZNmzw666czyRyuEEKcxcrmvxdc9Oc/x+uWZP7W4mL3oj//OR4g+IYZ3U6G8fHHH/tHRkY2L168eC9AaWmp+fzzz0/57LPP9kZHR1tfeeWVoMceeyzm3//+dx5ARUWFec2aNbsA9u7d6zl9+vTK22+/vRwgNTU18x//+MeBSy65pOaRRx6Jfvzxx6Nff/31g88991zk/v37t3h5eemSkhIzwNChQxtWr169083NjU8++cTv5z//eeyXX37ZJzJWScAVQoizWOlLL8XoEyrn6MZGU+lLL8WcTsAdMWJE/RNPPDHg/vvvj7n88ssrQ0JCrHv27PE699xzUwHsdjthYWGtdW9vuOGGdu9VWlpqrq6uNl9yySU1AHfffXfptddeOxAgLS2t/sorr0y87LLLKm666aYKgLKyMvP111+fmJeX56mUalNNyJVkSFkIIc5i1pKSdsvwddTeVUOGDGlcv3799sGDB9c/8cQTMe+9915QcnJy/c6dO7fv3Llz++7du7cvX758z9Hj/fz8TrlU36JFi/Y88MADxevWrfMZOnRoZnNzM48//njMOeecU71nz55t//vf//Y2NTX1mTjXZzoihKvkl9fx340FvPDdHpbsLqKq/rSqkgnRr1hCQ9v9hu+ovavy8vLc/Pz87LNmzSp75JFHjqxdu9anrKzM8s033/gANDY2qrVr17a7EtnX19dWVVVlAggJCbH5+/vbFi5c6Avw2muvhYwbN67GZrORk5Pjfumll1a/9NJL+dXV1ebKykpzVVWVOTY2tglgzpw5oafzNfQ0GVIWZ7Xi6gYeeW8ja/eXt7b9alo6d00aiMnUZ0aihOg1IbNmFRw/hwugPDzsIbNmnVZ5vnXr1nn98pe/jDWZTFgsFv3SSy/tt1gs+qGHHoqrrq4222w2df/99x/Jzs5uOPHcm266qez+++9PmD17dsSHH36Y88Ybb+Tef//98Q899JApLi6ucf78+XlWq1XdeOONidXV1Wattbr33nuPhIaG2h5//PHCu+66K/G5556LnDRpUtXpfA09TcrzibPasj3FzHxttUObp5uJLx+eTHyoj4t6JUTX9UR5vrL57wWXvvRSjLWkxN0SGtoUMmtWwenM357tpDyfEO1oaGpb47qh2U6T7ZSnk4Tot4JvmFEm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\n",
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
    "# importing packages\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "sns.scatterplot(x='sepal.length', y='sepal.width',\n",
    "\t\t\t\thue='species', data=df, )\n",
    "\n",
    "# Placing Legend outside the Figure\n",
    "plt.legend(bbox_to_anchor=(1, 1), loc=2)\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3a7ee4be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAdwAAAEGCAYAAADPBiS8AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAABP50lEQVR4nO3dd3jV5dnA8e9zzsnee4cAIQsII2EoIOCgDtwLxV0FREXbaq3VtlatVWv7tloVRRSpA2etIkWrIiCoEDYBAgTCCmSS5GTn5DzvH78k5HACCWSH+3NduSRPfuM+tHrnmbfSWiOEEEKIzmXq7gCEEEKIM4EkXCGEEKILSMIVQgghuoAkXCGEEKILSMIVQgghuoCluwNoLjg4WMfFxXV3GEII0WusW7euUGsd0t1xiNb1qIQbFxdHRkZGd4chhBC9hlJqX3fHINpGhpSFEEKILiAJVwghhOgCknCFEEKILtCj5nCFEEK037p160ItFsvrwBCkY9WV7MBWm812Z1paWv7xP5SEK4QQfYzFYnk9PDw8OSQk5KjJZJID87uI3W5XBQUFKUeOHHkduOz4n0vCFUIAULlpE7XZe7CXW3GJicE8aBCe0dHdHZY4PUMk2XY9k8mkQ0JCSo8cOTKkpZ9LwhVCULV1K/nPPEvVhg1NbeFPPoHntdd2Y1SiHUySbLtHw997i8P4MrYvhKB2716HZAtQ8Pd/UJWZ2U0RCdH3SMIVQlBvLXduKy5G19Z2QzSir3j44YfD4+PjByckJKQkJSWlfPvtt14nuvaFF14IysnJcenK+LqaDCkLIXCNiwOLBWy2pjavSZMwh8iJgeL0fP31115ffvml/5YtW7Z5eHjow4cPW2pqatSJrn/77beDhw8fXhUXF1fXlXF2JenhCiGwDE4h6q9/xbV/HLi44POzKQTPmIGbLJo6I7z9477A0X/6emj/33yRNvpPXw99+8d9ge195qFDh1wCAwNtHh4eGiAiIsIWFxdXt3LlSs9Ro0YlDh48OHn8+PGD9u3b5/Lmm28GbN261fOWW24ZkJSUlFJeXq7+85//+CQnJ6ckJCSkXHvttXFVVVUKYPbs2VEDBw4cnJCQkDJjxoxogHfffdcvNTU1KTk5OeXss89OOHDgQI/sTCqte868enp6upazlIXoPtW7d2OvqcElOBiXsLDuDke0gVJqndY6vXnbpk2bcoYNG1bYlvvf/nFf4JOLt/WrsdmbOmBuFpP9d1NT9t00tl/x6cZVWlpqGjNmTFJ1dbVp/PjxZTfccEPx+eefXzF27NjEL774YndkZKRt3rx5AV999ZXfhx9+mDN69OjE559//sA555xTWVlZqQYMGDD0q6++ykpNTa258sor40aMGFE5c+bMojFjxiTv2bNnq8lkorCw0BwcHFxfUFBgDgoKqjeZTPztb38L3r59u/u8efMOnm7s7bVp06bgYcOGxR3f3iN/CxBCdA/3+PjuDkF0sRe+2RXVPNkC1Njsphe+2RXVnoTr5+dn37p167alS5f6fPPNNz633nrrwF/+8pe5u3bt8jj33HMTAOx2OyEhIU5DyJs2bXKPjo6uSU1NrQG47bbbil566aXQRx55JN/Nzc0+bdq0fpdccknp9ddfXwqwd+9e1yuuuCK6oKDApba21hQTE1NzunF3Jkm4QghxBiuw1rieSvupsFgsTJ061Tp16lRrampq1dy5c0Pi4+OrNm7cuONk951o5NXFxYWNGzdu/+yzz3wXLVoU8Morr4T++OOPO++9997Y+++//8j06dNLFy9e7PPEE09Etjf2ziBzuEIIcQYL8XFrcSn6idrbatOmTW5btmxxa/x+w4YNHoMGDaouLi62fP31114ANTU1KiMjwx3A29u7vrS01AwwfPjw6kOHDrlu3brVDWDhwoVBEyZMsJaWlpqKi4vN119/fencuXMPbN++3RPAarWaY2Nj6wAWLFgQ1J64O5P0cIUQ4gw257xBh1qaw51z3qBD7XluWVmZec6cObFlZWVms9ms4+Liat566619e/fuLZgzZ06s1Wo119fXq7vvvjsvPT29+pZbbim87777+j300EP2jIyM7XPnzs259tprB9bX1zNs2LDKBx98sCA/P98yderU+MbVzk899dQBgEcffTT3hhtuGBgWFlabnp5esX//freTR9c9ZNGUEEL0Yu1dNAXGwqkXvtkVVWCtcQ3xcaudc96gQ+2Zvz3TyaIpIYQQLbppbL9iSbCdT+ZwhRBCiC4gCVcIIYToAp06pKyUygGsQD1gO36eQQghhDhTdMUc7mStdZsn74UQQoi+SIaUhRBCiC7Q2QlXA18ppdYppWa0dIFSaoZSKkMplVFQUNDJ4QghhOhso0ePTvz44499m7c98cQToTfddFPs6T7znXfe8fvtb38bfjr3enp6jjjd93akzk6447TWI4GLgHuUUuccf4HW+jWtdbrWOj1ESoEJIUSvd+211xa99957DhWHPv7448Cbbrqp1a1HtmYlIpubPn166dNPP32kg0I85fd3hE5NuFrr3IZ/5gP/BkZ35vuEEEKchrXzA3k+YSiP+6fxfMJQ1s5vV3m+m2+++eg333zj11hSLysryzU/P9+loqLCNHz48KSUlJTkiy66aEBpaakJICoqauiDDz4YkZaWlvjGG28EPPXUU6GNJfimTp06AIwC9bfccksswIEDBywXXHDBwMTExJTExMSU//3vf14Ajz/+eNigQYMGDxo0aPATTzwRenxcdrudmTNnRg8aNGhwQkJCyrx58wIAFi9e7DNmzJiESy+9tH9iYuLg9nz2k+m0RVNKKS/ApLW2Nvx5CvBEZ71PCCHEaVg7P5AvH+mHrcbogJXnufLlI/0AGPXz0zoMIzw8vH7YsGEVH3/8sd9NN91U8tZbbwWOGzfO+uc//zlixYoVO319fe2PPvpo+JNPPhn2/PPPHwZwd3e3r1u3LgsgNDQ0dd++fVs8PDx0YWGh+fjnz5o1K3bChAnW3//+99k2m43S0lLzypUrPd99992gdevWbddak5aWlnzeeedZx40bV9V438KFC/23bNnisX379szDhw9bRo8enTxlypRygM2bN3tt2LAhMykpqV1nSJ9MZ/Zww4DvlVKbgDXAF1rrpZ34PiGEEKdq+bNRTcm2ka3GxPJno9rz2Ouuu674/fffDwD45JNPAuPi4mqys7PdR48enZSUlJSyaNGioP379zdVJLrllluONv45MTGx6sorr+z/8ssvB7q4uDidP7x69Wqfhx56qACMikRBQUH13333nffFF19c4uvra/fz87NfcsklR5ctW+bT/L6VK1f6XHfddcUWi4WYmBjbmDFjyr///ntPgNTU1IrOTLbQiT1crfUeYFhnPV8IIUQHKM9vuQzfidrbaPr06SWPPfZYzPfff+9ZXV1tGjlyZGVWVlbZ559/vrel6318fOyNf162bNmu//73vz6ffvqp/3PPPRe5a9eura29ry11AU52jaenp/2EP+wgsi1ICCHOZN6hLffqTtTeRn5+fvaxY8da77zzzrirrrqqeNKkSRUZGRnejSX3rFarafPmzU5Vferr68nOzna9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\n",
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
    "# importing packages\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "sns.scatterplot(x='petal.length', y='petal.width',\n",
    "\t\t\t\thue='species', data=df, )\n",
    "\n",
    "# Placing Legend outside the Figure\n",
    "plt.legend(bbox_to_anchor=(1, 1), loc=2)\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "077ab84f",
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
       "      <th>sepal.length</th>\n",
       "      <th>sepal.width</th>\n",
       "      <th>petal.length</th>\n",
       "      <th>petal.width</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>sepal.length</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.256156</td>\n",
       "      <td>0.314101</td>\n",
       "      <td>-0.339089</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sepal.width</th>\n",
       "      <td>0.256156</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.138662</td>\n",
       "      <td>-0.271336</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>petal.length</th>\n",
       "      <td>0.314101</td>\n",
       "      <td>-0.138662</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.710206</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>petal.width</th>\n",
       "      <td>-0.339089</td>\n",
       "      <td>-0.271336</td>\n",
       "      <td>0.710206</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              sepal.length  sepal.width  petal.length  petal.width\n",
       "sepal.length      1.000000     0.256156      0.314101    -0.339089\n",
       "sepal.width       0.256156     1.000000     -0.138662    -0.271336\n",
       "petal.length      0.314101    -0.138662      1.000000     0.710206\n",
       "petal.width      -0.339089    -0.271336      0.710206     1.000000"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.corr(method='pearson')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d865154",
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
