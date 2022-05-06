

# general data analysis functions
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import re
#importing metrics
from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error,max_error, accuracy_score
from sklearn.metrics import precision_score,f1_score, accuracy_score, classification_report,confusion_matrix,classification_report
from xgboost import plot_importance
#unsure
# from scipy import stats


#function to create a dataframe of specific characteristics

#Note: The above function was built off inspiration from a more visually appealing percent formula that I was constantly creating so created this function
# so I can easily just filter based on characteristics I was most interested. I will use this data frame while I perform EDA.
#[Stack Overflow Inspiration-'find percent missing values']
# link: (https://stackoverflow.com/questions/51070985/find-out-the-percentage-of-missing-values-in-each-column-in-the-given-dataset)
def character_df(dataframe):
    ''' Argument: dataframe= 'whatever data frame you select'   ,
    This function returns a dataframe of null counts per column, percent missing, and if categorical its unique values.
    '''
    #create a column of null counts per feature
    isnull_cnt    = dataframe.isnull().sum()
    only_isnull_cnt=[isnull_cnt[null_cnt] for null_cnt in range(len(isnull_cnt))]
    # looking at dtypes
    charac_append = list(dataframe.dtypes)
    #create a column of percentage missing per features
    prct_missing = round(dataframe.isnull().sum() * 100 / len(dataframe),2)
    only_prct=[prct_missing[percent] for percent in range(len(prct_missing))]

    # create a column that lists different variables held within categorical variables
    cat_list=[dataframe[column].unique() if str( dataframe[column].dtypes )=='object' else 'not cat.'  for column in dataframe  ]

    #create a df from all the series outputed above
    df_characteristics = pd.DataFrame({'column_name':dataframe.columns ,'null_count': only_isnull_cnt, 'percent_missing': only_prct, 'categorical_unique': cat_list,'dtypes':charac_append})

    return df_characteristics

# Original Code Inspiration df['z'].fillna(dff.groupby('x')['z'].transform('mean'))
# A function to utilize fillna and transform function to quickly replace NaN values within a dataframe
def fillna_centrl_tendcy(dataframe,change_column,groupby_column,function):
    '''
    Arguments: dataframe = df ,   change_column='column to change', groupby_column = 'column_name' , function = 'mean'
    Note about Function:
    Function to use for transforming the data.
    If a function, must either work when passed a DataFrame or when passed to DataFrame.apply. If func is both list-like and dict-like, dict-like behavior takes precedence(from    transform documentation).
    The function allows for easy fills of na given a dataframe, column to group by, and the function you want to perform('mean','mode','median'),'''
    dataframe[change_column] = dataframe[change_column].groupby( dataframe[groupby_column] ).transform(function)
    return dataframe




# function to print out quick null summary details
def null_reminders(dataframe,column_name,features_to_drop,value_cnt):
    ''' dataframe = df, column_name = 'name', featires_to_drop = list of columns names not wanted , value_cnt=='Yes'
    Note: returns a seperate dataframe
    '''
    # providing reminder of what needs to be replaced/filled
    print('is null sum: ',dataframe[column_name].isnull().sum() )

    #checking if value counts are wanted
    if value_cnt=='Yes':
        print(dataframe[column_name].value_counts() )

    #filter to peek at df potentially looking for a method to fill these 55 observations
    df_column_null = dataframe[   dataframe[column_name].isnull()   ].drop(columns=features_to_drop)
    print('df_column_ shape',df_column_null.shape)
    return df_column_null


####################################### modeling summary functions ##########################

# function to calculate predictions and plot confusion matrix for each iteration
def preds_N_cm(model,X_train,y_train,X_test,y_test):
    y_pred = model.predict(X_test)
    predictions = [round(value) for value in y_pred]
    # evaluate predictions with accuracy, precision, f1 scores (micro/macro)
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    print()
    #preds = model.predict(X_test)
    # Average is assigned micro
    precisionScore_sklearn_microavg = precision_score(y_test, y_pred, average='micro', zero_division=0)
    precisionScore_sklearn_macroavg = precision_score(y_test, y_pred, average='macro',zero_division=0)
    # Average is assigned macro
    f1_score_sklearn_macro = f1_score(y_test, y_pred, average='macro')
    f1_score_sklearn_micro = f1_score(y_test, y_pred, average='micro')
    # Printing micro and macro average precision score
    print('(micro) precision score: ',precisionScore_sklearn_microavg,'        (macro) precision score: ', precisionScore_sklearn_macroavg)
    print('(micro) f1 score: ',f1_score_sklearn_micro,'               (macro) f1 score: ',f1_score_sklearn_macro)
    print()
    print('XGBoost Classificaition Report')
    print(classification_report(y_test,y_pred))
    
    # printing confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # creating nice plot of conf matrix
    cm_df = pd.DataFrame(cm,
                         index = ['0','1','2','3','4'],
                         columns = ['0','1','2','3','4'])
    
    #Plotting the confusion matrix
    plt.figure(figsize=(12,8))
    sns.heatmap(cm_df, annot=True)
    plt.title('Confusion Matrix')
    plt.ylabel('Actal Values')
    plt.xlabel('Predicted Values')
    plt.show()



def plot_xgb_importance(model,num_features=10):
    plt.rcParams["figure.figsize"] = (12, 5)

    importance = plot_importance(model, max_num_features=10) # top 10 most important features
    importance;
####################################### preprocessing function ##########################
# to pass in a series using apply functions
def pre_process(sentences):
    '''
    inputs:
    sentences = text
    description:
    The function is utilized to remove emoticons, urls (https,eee,etc), special characters,
    and new line break stings('\n'). (Does NOT remove spaces).
    use cases:
    This was specifically created to pass in use df['new_column']=df['text_column'].apply(pre_preprocess)
    OR individual strings.
    '''
    # removing emoticons
    sentences = re.sub(':d', '', str(sentences)).strip()
    sentences = re.sub(':p', '', str(sentences)).strip()

    # removing urls
    sentences = re.sub('(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*','  ', sentences)

    # removing special characters (https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string)
    sentences = re.sub('[^A-Za-z0-9]+', ' ', str(sentences))

    sentences = re.sub('[^a-zA-Z\s]', '', str(sentences)).rstrip()

    # removing the '\n' new line breaks in sentences
    sentences = sentences.replace('\n',' ')

    return sentences

# this is a mertic function used to quickly append to a an exisitng dataframe to easily compare iterations
def metric_reg(model,X_train,y_train,X_test,y_test):
    #regular R2 value
    R2_train = model.score(X_train,y_train)
    R2_test = model.score(X_test,y_test)


    #manual adjusted r2 score
    k= X_train.shape[1] # returns the # of features in model
    n=len(y_train)      # returns the # of rows/observations
    R2_train_adj = 1 - ((1-R2_train)*(n-1)/(n-k-1))
    #manual adjusted r2 score
    kt= X_test.shape[1] # returns the # of features in model
    nt=len(y_test)      # returns the # of rows/observations
    R2_test_adj = 1 - ((1-R2_test)*(nt-1)/(nt-kt-1))


    # MSE
    y_pred = model.predict(X_train)
    mse_train = mean_squared_error(y_train, y_pred)
    # MSE
    y_predt = model.predict(X_test)
    mse_test = mean_squared_error(y_test, y_predt)

    # Training RMSE
    RMSE_train = (mean_squared_error(y_train, y_pred, squared = False))
    # Testing RMSE
    RMSE_test = (mean_squared_error(y_test, y_predt, squared = False))

    #MAE
    mae_train = mean_absolute_error(y_train, y_pred)
    mae_test = mean_absolute_error(y_test, y_predt)


    # calculate residuals
    residuals  = y_train - y_pred
    residualst = y_test - y_predt

    #SSE
    SSE_train = sum(residuals**2)
    SSE_test = sum(residualst**2)

    #max error (max residual error captues worst case error b./w perdicted values and true value)
    max_error_train = max_error(y_train, y_pred)
    max_error_test = max_error(y_test, y_predt)

    column_names=['R2_train','R2test','R2_adj_train','R2_test_adj','mse_train',
    'mse_test','RMSE_train','RMSE_test','max_error_train','max_error_test']

    list_metric = [R2_train,R2_test,R2_train_adj,R2_test_adj,mse_train,mse_test,RMSE_train,
    RMSE_test,RMSE_test,max_error_train,max_error_test]


    dictionary = dict(zip(column_names,list_metric))
    #print(dictionary)

    df =  pd.DataFrame([dictionary])

    return df
