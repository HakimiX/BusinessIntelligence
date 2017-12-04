# Assignment 8 - Population and Deep Learning

## Part 1 - Accuracy and Recall

### Accuracy and Precision

### Precision and Recall

![Text](https://github.com/HakimiX/BusinessIntelligence/blob/master/Assignment8/Model/model.jpg)

## Part 2 - Population and T-test

The `brain_size.csv` dataset contains female and male height. We were not sure whether to compare male and female together or separately, so we have done both

### Individual Gender Comparison

Dataframe average height male and female
```python
Dataframe Average Height: Female 65.765
Dataframe Average Height: Male 71.41
```

Population average height 
```python
Denmark average height: 71
US average height: 68.4
```

Dataframe average female height 65.76 inches compared to Denmark average female height 66.44 inches
```python
t_test, population_mean = stats.ttest_1samp(height_from_dataframe_female, 66)
```
```python
T-test: 1.49511066685  Popmean:  0.15131013469
```

Dataframe average female height 65.76 inches compared to USA average female height 65.77 inches
```python
t_test, population_mean = stats.ttest_1samp(height_from_dataframe_female, 65)
```
```python
T-test: 1.49511066685  Popmean:  0.15131013469
```

Dataframe average male height 71 inches compared to Denmark average male height 71.88 inches
```python
t_test, population_mean = stats.ttest_1samp(height_from_dataframe_male, 72)
```
```python
T-test: -0.825318221249  Popmean:  0.419433209147
```

Dataframe average male height 71 inches compared to USA average male height 69.2 inches
```python
T-test: 3.37121510713  Popmean:  0.00320647462375
```

### Population Comparison

Dataframe both male and female height compared to Denmark
```python
T-test: -3.85063165253  Popmean:  0.00042684721728
```

Dataframe both male and female height compared to USA
```python
T-test: 0.937718588959  Popmean:  0.354160229104
````





