from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
from pathlib import Path
from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler, StringIndexer
import sys
import os
import time

#static values
working_directory = '/opt/airflow/sparkFiles/jars/*'
# reading parameters

directory = r'/opt/airflow/sparkFiles/tempfiles'

# start a spark session and set up its configuration
spark = (
                SparkSession.builder.appName("Spark Multilayer")
                .master("local[*]")
                .config("spark.driver.memory", "8g")
                .config("spark.driver.maxResultSize", "2g")
                .config('spark.driver.extraClassPath', working_directory)
                .config("spark.mongodb.input.uri", 'mongodb://ismp00v9003sa.interseguro.com.pe:27017/vis_data')
                .config("spark.mongodb.output.uri", 'mongodb://ismp00v9003sa.interseguro.com.pe:27017/vis_data')
                .config("spark.mongodb.input.partitioner", "MongoSamplePartitioner")
                .config("partitionSizeMB", "32")
                .getOrCreate()
        )

# Obtenemos la estructura elegida
#df = spark.read.format("libsvm")\
#    .load("/opt/airflow/sparkFiles/tempfiles/ds_covid.csv")
df = spark.read.csv('/opt/airflow/sparkFiles/tempfiles/ds_covid_final.csv', header=True, inferSchema=True)
df.show(10)
df.printSchema()

# usamos vectorAssembler
vectorAssembler = VectorAssembler(inputCols = ['Edad','Sexo','Distrito'], outputCol = 'features')
v_df = vectorAssembler.transform(df)
v_df.show(10)

# obtenemos features
indexer = StringIndexer(inputCol = 'Estado', outputCol = 'label')
i_v_df = indexer.fit(v_df).transform(v_df)
i_v_df.show(10)

# Validando la data
i_v_df.select('Estado','label').groupBy('Estado','label').count().show()

# Split the data into train and test
splits = i_v_df.randomSplit([0.6, 0.4], 1)
train_df = splits[0]
test_df = splits[1]
train_df.count(), test_df.count(), i_v_df.count()
#train.show()
#test.show()

# specify layers for the neural network:
# input layer of size 4 (features), two intermediate of size 5 and 4
# and output of size 3 (classes)
layers = [3,5,5,3]

# create the trainer and set its parameters
trainer = MultilayerPerceptronClassifier(maxIter=100, layers=layers, blockSize=128, seed=1234)

# train the model
model = trainer.fit(train_df)

# grabamos en pred_df
pred_df = model.transform(test_df)
pred_df.select('Id','features','label','rawPrediction','probability','prediction').show(5)
# 

evaluator = MulticlassClassificationEvaluator(labelCol = 'label', predictionCol = 'prediction', metricName = 'accuracy')
mlpacc = evaluator.evaluate(pred_df)
print("Test set accuracy = " + str(mlpacc))

# compute accuracy on the test set
#esult = model.transform(test_df)
#predictionAndLabels = result.select("prediction", "label")
#evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
#print("Test set accuracy = " + str(evaluator.evaluate(predictionAndLabels)))
# $example off$

spark.stop()