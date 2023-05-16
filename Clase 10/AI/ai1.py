#pip install imageai
from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
#https://github.com/fchollet/deep-learning-models/releases/
#https://github.com/fchollet/deep-learning-models/releases/tag/v0.5
prediction.setModelPath( "resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()

predictions, percentage_probabilities = prediction.predictImage("manzanita.png", result_count=10)
for index in range(len(predictions)):
    print(predictions[index] , " : " , percentage_probabilities[index])