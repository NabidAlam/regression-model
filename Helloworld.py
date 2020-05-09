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
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import scipy\n",
    "import statsmodels.api as sm\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import sklearn\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
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
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('1.01. Simple linear regression.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
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
     "execution_count": 37,
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
   "execution_count": 44,
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
     "execution_count": 44,
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
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = data['GPA']\n",
    "x1 = data['SAT']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
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
    "pit.scatter(x1,y)\n",
    "pit.xlabel('SAT', fontsize = 20)\n",
    "pit.ylabel('GPA', fontsize = 20)\n",
    "pit.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"simpletable\">\n",
       "<caption>OLS Regression Results</caption>\n",
       "<tr>\n",
       "  <th>Dep. Variable:</th>           <td>GPA</td>       <th>  R-squared:         </th> <td>   0.406</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.399</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   56.05</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Date:</th>             <td>Sat, 09 May 2020</td> <th>  Prob (F-statistic):</th> <td>7.20e-11</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Time:</th>                 <td>06:17:20</td>     <th>  Log-Likelihood:    </th> <td>  12.672</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>No. Observations:</th>      <td>    84</td>      <th>  AIC:               </th> <td>  -21.34</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Residuals:</th>          <td>    82</td>      <th>  BIC:               </th> <td>  -16.48</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>     <td> </td>   \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   \n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "    <td></td>       <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  \n",
       "</tr>\n",
       "<tr>\n",
       "  <th>const</th> <td>    0.2750</td> <td>    0.409</td> <td>    0.673</td> <td> 0.503</td> <td>   -0.538</td> <td>    1.088</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>SAT</th>   <td>    0.0017</td> <td>    0.000</td> <td>    7.487</td> <td> 0.000</td> <td>    0.001</td> <td>    0.002</td>\n",
       "</tr>\n",
       "</table>\n",
       "<table class=\"simpletable\">\n",
       "<tr>\n",
       "  <th>Omnibus:</th>       <td>12.839</td> <th>  Durbin-Watson:     </th> <td>   0.950</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Prob(Omnibus):</th> <td> 0.002</td> <th>  Jarque-Bera (JB):  </th> <td>  16.155</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Skew:</th>          <td>-0.722</td> <th>  Prob(JB):          </th> <td>0.000310</td>\n",
       "</tr>\n",
       "<tr>\n",
       "  <th>Kurtosis:</th>      <td> 4.590</td> <th>  Cond. No.          </th> <td>3.29e+04</td>\n",
       "</tr>\n",
       "</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.<br/>[2] The condition number is large, 3.29e+04. This might indicate that there are<br/>strong multicollinearity or other numerical problems."
      ],
      "text/plain": [
       "<class 'statsmodels.iolib.summary.Summary'>\n",
       "\"\"\"\n",
       "                            OLS Regression Results                            \n",
       "==============================================================================\n",
       "Dep. Variable:                    GPA   R-squared:                       0.406\n",
       "Model:                            OLS   Adj. R-squared:                  0.399\n",
       "Method:                 Least Squares   F-statistic:                     56.05\n",
       "Date:                Sat, 09 May 2020   Prob (F-statistic):           7.20e-11\n",
       "Time:                        06:17:20   Log-Likelihood:                 12.672\n",
       "No. Observations:                  84   AIC:                            -21.34\n",
       "Df Residuals:                      82   BIC:                            -16.48\n",
       "Df Model:                           1                                         \n",
       "Covariance Type:            nonrobust                                         \n",
       "==============================================================================\n",
       "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
       "------------------------------------------------------------------------------\n",
       "const          0.2750      0.409      0.673      0.503      -0.538       1.088\n",
       "SAT            0.0017      0.000      7.487      0.000       0.001       0.002\n",
       "==============================================================================\n",
       "Omnibus:                       12.839   Durbin-Watson:                   0.950\n",
       "Prob(Omnibus):                  0.002   Jarque-Bera (JB):               16.155\n",
       "Skew:                          -0.722   Prob(JB):                     0.000310\n",
       "Kurtosis:                       4.590   Cond. No.                     3.29e+04\n",
       "==============================================================================\n",
       "\n",
       "Warnings:\n",
       "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n",
       "[2] The condition number is large, 3.29e+04. This might indicate that there are\n",
       "strong multicollinearity or other numerical problems.\n",
       "\"\"\""
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = sm.add_constant(x1)\n",
    "results = sm.OLS(y,x).fit()\n",
    "results.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
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
