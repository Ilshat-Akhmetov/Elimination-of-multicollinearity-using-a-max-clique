## Elimination of multicollinearity using a max clique
Multicollinearity often occurs in data. It can be a big problem, especially
when you use a linear model (Linear Regression, Logistic Regression), because a model's coefficient 
became too unstable and heavily reliant on a data sample.

In this project i would like to introduce a method to eliminate multicollinearity. 
It uses Bron–Kerbosch algorithm to find a biggest subset of independent features in a dataset.

By dependent features here i mean features which are too much correlated with each other. 
There are different approaches to define if features are correlated or not. For example, it 
may be supposed that two features are correlated if absolute value of their correlation
is bigger than a threshold. 

Many data scientist 
suppose that if absolute value of correlation of two features is more than **0.8** then they are correlated, 
in fact **0.8** is a commonly accepted benchmark,  but actually it is up to 
researcher to select it.

Here i use Boston dataset as an example. That is the correlation matrix of features initially.
<img src="corr_before.png" alt="Corr before"/>
Let the threshold to be equal 0.6.
If absolute correlation's value of features i and j is bigger than threshold, then 
corr[i,j] = 0 which means features are not connected, else 1.
<img src="conn_graph.png" alt="Connection graph"/>
That is what we get after removing all correlated features.
<img src="corr_after.png" alt="Corr after"/>

An example how to use this program you may find in jupyter-notebook **Presentation.ipyng** file.

Here is short description.

To import it write: *from CliqueFinder import CliqueFinder*. 
Object CliqueFinder has 3 init parameters:
* ** corr_matrix ** - precalculated correlation matrix, format - pd.DataFrame 
* ** features_data **  -  dataset used to calculate correlation matrix, format - pd.DataFrame
* ** target_data **  -  an array containing target's values, format - pd.Series or np.array

First you have to create an instance of *CliqueFinder*. Let its name be *cliqFinderObj*: 
* *cliqFinderObj = CliqueFinder(corr_matrix, features_data, target_data) *  

To get optimal subset of features you must fit object CliqueFinder
with method fit: 
* *cliqFinderObj.fit(feature_target_corr_func, threshold)*

Here:

* **feature_target_corr_func** - function measuring dependency between feature and target. 
For example, it may be mutual information or pearson's correlation. 
Anyway,it must me a function with two input parameters - data and target arrays and one output - a dependency value 
with type *float* or *int*. It required to calculate a subset of features 
which have the biggest sum of absolute values of dependencies between target and uncorrelated features.
* **threshold** - optional parameter, by default equals 0.8. If absolute value of correlation of two features 
is more than threshold then they are supposed to be correlated, else - not.

After **fit** methods successfully ran you may get optimal subset of independent features or subset of features 
which must be excluded from a dataset by methods **get_best_clique** and **get_out_of_clique_features** respectively.
* cliqFinderObj.get_best_clique()
* cliqFinderObj.get_out_of_clique_features()



