# Assignment 6 - Multivariate Linear Regression and Logistic Regression

## Part 1

Description

```python
print("Mean Absolute Error (MAE)")
print("Training Data: ", str(metrics.mean_absolute_error(y_train, linear_regr.predict(x_and_z_train))))
print("Test Data: ", str(metrics.mean_absolute_error(y_test, predict_regr)))
print("Root-Mean-Square Error (RMSE)")
print("Training Data: ", str(sqrt(metrics.mean_squared_error(y_train, linear_regr.predict(x_and_z_train)))))
print("Test Data: ", str(sqrt(metrics.mean_squared_error(y_test, predict_regr))))
```

__Output__

```python
generate_scatterplot(dataframe)
```

```python
Mean Absolute Error (MAE)
Training Data:  1764.12753535
Test Data:  1881.77653759
```

```python
Root-Mean-Square Error (RMSE)
Training Data:  4770.080814835201
Test Data:  4802.906732149257
```

![Text](https://github.com/HakimiX/BusinessIntelligence/blob/master/Assignment6/model/scatterplot.png)

## Part 2

Description

```python
kfold_cross_validation()
```

__Output__

```python
Mean Absolute Error (MAE):  1591.68000068
Root Mean Square Error (RMSE) 3334.552249265342

Mean Absolute Error (MAE):  1812.81216074
Root Mean Square Error (RMSE) 4527.852669954314

Mean Absolute Error (MAE):  1820.37222788
Root Mean Square Error (RMSE) 5096.989223276516

Mean Absolute Error (MAE):  1659.37330299
Root Mean Square Error (RMSE) 3761.72868571144

Mean Absolute Error (MAE):  1617.54678443
Root Mean Square Error (RMSE) 4336.504650837724

Mean Absolute Error (MAE):  1985.21536731
Root Mean Square Error (RMSE) 5430.989457210941

Mean Absolute Error (MAE):  1904.01750946
Root Mean Square Error (RMSE) 4756.354507065226

Mean Absolute Error (MAE):  1603.83026461
Root Mean Square Error (RMSE) 3979.3357206926044

Mean Absolute Error (MAE):  2117.69508541
Root Mean Square Error (RMSE) 6639.777765199327

Mean Absolute Error (MAE):  1759.35255138
Root Mean Square Error (RMSE) 5186.751373833896
```

```python
Mean Absolute Error (MAE) Average,  1787.18952549
Root Mean Square Error (RMSE) Average,  1787.18952549
```

## Part 3

__Shape and Size__

There are many important differences between benign and malignant tumors, some of them include: Growth rate, Cellular apperance (shape).

When dealing with breast cancer, tumors are graded based on a scale of one to three indicating how aggresive the cancerous cells are:
* Low grade (1) - Well differentiated
* Intermediate grade (2) - Moderately differentiated
* High grade (3) - Poorly differentiated 

Low grade tumors look more like normal tissue and high grade tumors look abnormal and less like normal tissue. The shape of a tumor may be a sign of malignancy, therefor it may be crucial to look into the shape of a tumor and determine where it fits on the "Tumor Grades". Average shape - `Average Shape:  0.766259398496`

According to pathologsts, when looking at tumor cells, it is often obvious whether they are normal, benign og cancerous cells. Cancer cells often have abnormal chromosomes, making them larger and darker. Sometimes the difference may be subtle. 

```python
logistic_regression()
```

__Output__

![Text](https://github.com/HakimiX/BusinessIntelligence/blob/master/Assignment6/model/Breast_cancer_dataset.jpg)

```python
Accuracy:  0.80701754386
Accuracy:  0.736842105263
Accuracy:  0.736842105263
Accuracy:  0.824561403509
Accuracy:  0.736842105263
Accuracy:  0.789473684211
Accuracy:  0.719298245614
Accuracy:  0.771929824561
Accuracy:  0.771929824561
Accuracy:  0.767857142857
Accuracy:  0.771929824561
Accuracy:  0.877192982456
Accuracy:  0.859649122807
Accuracy:  0.80701754386
Accuracy:  0.929824561404
Accuracy:  0.982456140351
Accuracy:  0.859649122807
Accuracy:  0.947368421053
Accuracy:  0.894736842105
Accuracy:  0.946428571429
Accuracy:  0.80701754386
Accuracy:  0.912280701754
Accuracy:  0.877192982456
Accuracy:  0.912280701754
Accuracy:  0.912280701754
Accuracy:  0.964912280702
Accuracy:  0.894736842105
Accuracy:  0.929824561404
Accuracy:  0.894736842105
Accuracy:  0.964285714286
```

```python
Average Size:  0.887625313283
```

```python
Average Shape:  0.766259398496
```








