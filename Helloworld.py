{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import scipy\n",
    "import statsmodels.api as sm\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import sklearn\n",
    "sns.set()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import statsmodels.api as sm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('1.01. Simple linear regression.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
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
       "      <th>SAT</th>\n",
       "      <th>GPA</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1714</td>\n",
       "      <td>2.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1664</td>\n",
       "      <td>2.52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1760</td>\n",
       "      <td>2.54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1685</td>\n",
       "      <td>2.74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1693</td>\n",
       "      <td>2.83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>79</th>\n",
       "      <td>1936</td>\n",
       "      <td>3.71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>1810</td>\n",
       "      <td>3.71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>1987</td>\n",
       "      <td>3.73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <td>1962</td>\n",
       "      <td>3.76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>83</th>\n",
       "      <td>2050</td>\n",
       "      <td>3.81</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>84 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     SAT   GPA\n",
       "0   1714  2.40\n",
       "1   1664  2.52\n",
       "2   1760  2.54\n",
       "3   1685  2.74\n",
       "4   1693  2.83\n",
       "..   ...   ...\n",
       "79  1936  3.71\n",
       "80  1810  3.71\n",
       "81  1987  3.73\n",
       "82  1962  3.76\n",
       "83  2050  3.81\n",
       "\n",
       "[84 rows x 2 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
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
       "      <th>SAT</th>\n",
       "      <th>GPA</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>84.000000</td>\n",
       "      <td>84.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1845.273810</td>\n",
       "      <td>3.330238</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>104.530661</td>\n",
       "      <td>0.271617</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1634.000000</td>\n",
       "      <td>2.400000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1772.000000</td>\n",
       "      <td>3.190000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1846.000000</td>\n",
       "      <td>3.380000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1934.000000</td>\n",
       "      <td>3.502500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2050.000000</td>\n",
       "      <td>3.810000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               SAT        GPA\n",
       "count    84.000000  84.000000\n",
       "mean   1845.273810   3.330238\n",
       "std     104.530661   0.271617\n",
       "min    1634.000000   2.400000\n",
       "25%    1772.000000   3.190000\n",
       "50%    1846.000000   3.380000\n",
       "75%    1934.000000   3.502500\n",
       "max    2050.000000   3.810000"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = data['GPA']\n",
    "x1 = data['SAT']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pit' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-226f014c0c71>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mscatter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mpit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mxlabel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'SAT'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfontsize\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mpit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mylabel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'GPA'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfontsize\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mpit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'pit' is not defined"
     ]
    }
   ],
   "source": [
    "pit.scatter(x1,y)\n",
    "pit.xlabel('SAT', fontsize = 20)\n",
    "pit.ylabel('GPA', fontsize = 20)\n",
    "pit.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = sm.add_constant(x1)\n",
    "results = sm.OLS(y,x).fit()\n",
    "results.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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RUlJCV588UWMGTMGU6dORWFhoWz3YiuNy2jnzp2IiIjA2LFj8c4775j8e3H2MkpISEBkZCQiIyOxcuVKAMChQ4cwduxYhIeH4/3339cf26K+awI5lFOnTglRUVFCcHCwcP369Qb7CgoKhJEjRwo//fSTIAiCEBkZKZw8eVIQBEF47bXXhM8//1wQBEF48cUXhd27dwuCIAgJCQnCypUr7XcDdmCojIYNGyb8+OOPgiAIwoIFC4SkpCRBEJovizfffFNYv369IAiCsGvXLuFPf/qTvW/DphqXUV5envD0008Lt2/fFgRBEJYtWyZs2rRJEISWWUYHDx4UYmJihKqqKkGr1QrTpk0Tvv76a0Gj0QjXrl0TqqurhVmzZgn79+8XBKFlfddY03AwSUlJWLZsGdq3b99k38qVKzF58mR0794dP//8MyorK9G/f38AwMSJE7Fnzx5UV1fju+++w7PPPttguzMxVEa1tbUoKytDbW0tqqqq4OnpabQs9u/fj7FjxwIAoqKicODAAVRXV9v/ZmykcRlduHAB/fv31/97xIgR2LdvX4stI7VajcWLF8PDwwPu7u7o1asXrly5gm7duqFLly5wc3PD2LFjsWfPnhb3XWPQcDDLly/HwIEDm2y/cuUKcnJyMG3aNABAQUEB1Gq1fr9arcbt27dx9+5d+Pj4wM3NrcF2Z2KojN544w288MILePrpp3H37l2MHj3aaFnULz83Nzf4+Pjgzp079r0RG2pcRn369MHp06dx69Yt1NbWYs+ePSgqKmqxZdS7d299ELhy5QpSU1OhUqkafKfat2+P27dvt7jvGoOGk/jXv/6FKVOmwMPDAwCg0+mgUv06xbEgCFCpVPr/r6/xv51NYWEhVq1ahd27dyM7Oxv9+vVDfHy8WWUhCAJcXJz369KjRw8sXLgQ8+bNw9SpU/Hoo4/C3d29xZfRpUuXMGvWLCxatAhdunQx+J1qad815/qEW7CMjAxERETo/92xY8cGHZNFRUVo3749AgICUFpaitraWgAPflANNXU5k2PHjuGRRx5B165d4eLigt/97nfIyckxWhbt27dHUVERAKCmpgbl5eXw9/eX7R5sraqqCn379kVycjL++c9/okOHDujSpUuLLqPjx49jxowZWLhwISZMmNDkO1VXFi3tu8ag4QTu3LmDyspKdOnSRb+tU6dO8PT0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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(x1,y)\n",
    "yhat = 0.0017*x1 + 0.275\n",
    "fig = plt.plot(x1, yhat, lw = 4, c='orange', label = 'regression line')\n",
    "plt.xlabel('SAT', fontsize = 20)\n",
    "plt.ylabel('GPA', fontsize = 20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
