# coding=utf8

from itertools import islice

import pandas as pd

from analytics.topic_prediction_classification import get_prediction
from analytics.topic_prediction_classification import topic, sub_topic_homologacion, sub_topic_pqr, sub_subtopic

dataframe = pd.read_excel('../analytics/TRAINING_SET/training_topic_v2.xlsx')
df_topic = pd.read_csv('FRECUENCY_SET/frecuency_topic_v2.csv', sep=',', parse_dates=[0], header=0, encoding='latin1')

headers = []

#analysis = 'TEMATICA'
analysis = 'SUBTEMATICA'
#sub_analysis = 'ALL'
sub_analysis = 'HOMOLOGACION'
#sub_analysis = 'PQR'

if analysis == 'TEMATICA' and sub_analysis == 'ALL':

    for category in dataframe[analysis].unique():
        header = analysis + ' - ' + category
        headers.append(header)

    tematica_classification_table = pd.DataFrame(data=0, index=headers, columns=headers)

    for index, row in dataframe.iterrows():

        observed = analysis + ' - ' + row[1]
        predicted = get_prediction(row[0], dataframe=df_topic, prediction=topic)
        tematica_classification_table.ix[observed, predicted] += 1

    print('Observed / Predicted')
    print(tematica_classification_table)

if analysis == 'SUBTEMATICA' and sub_analysis == 'HOMOLOGACION':

    filtered_dataframe = dataframe.loc[dataframe['TEMATICA'] == sub_analysis]

    for category in filtered_dataframe[analysis].unique():
        header = analysis + ' - ' + category
        headers.append(header)

    tematica_classification_table_homologacion = pd.DataFrame(data=0, index=headers, columns=headers)

    for index, row in dataframe.iterrows():
        if row[1] == 'HOMOLOGACION':
            observed = analysis + ' - ' + row[2]
            predicted = get_prediction(row[0], dataframe=df_topic, prediction=sub_topic_homologacion)
            try:
                tematica_classification_table_homologacion.ix[observed, predicted] += 1
            except KeyError:
                pass

    sheet_name = ('{} - {}'.format(analysis, sub_analysis))
    tematica_classification_table_homologacion.to_excel
    writer = pd.ExcelWriter('Classification_Table.xlsx')
    tematica_classification_table_homologacion.to_excel(writer, sheet_name)
    writer.save()

if analysis == 'SUBTEMATICA' and sub_analysis == 'PQR':

    filtered_dataframe = dataframe.loc[dataframe['TEMATICA'] == sub_analysis]

    for category in filtered_dataframe[analysis].unique():
        header = analysis + ' - ' + category
        headers.append(header)

    tematica_classification_table_pqr = pd.DataFrame(data=0, index=headers, columns=headers)

    for index, row in dataframe.iterrows():
        if row[1] == 'PQR':
            observed = analysis + ' - ' + row[2]
            predicted = get_prediction(row[0], dataframe=df_topic, prediction=sub_topic_pqr)
            tematica_classification_table_pqr.ix[observed, predicted] += 1

    sheet_name = ('{} - {}'.format(analysis, sub_analysis))
    tematica_classification_table_pqr.to_excel
    writer = pd.ExcelWriter('Classification_Table.xlsx')
    tematica_classification_table_pqr.to_excel(writer, sheet_name)
    writer.save()
