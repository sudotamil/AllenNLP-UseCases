from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("/home/bigtapp/Downloads/ner-model-2018.04.26.tar.gz")
r =predictor.predict(
  sentence="Software Developer, CTS, Chennai from NOV 2016 to Now Date."
)

#print(r)
l1 = r['tags']
l2 = r['words']
for i in zip(l1,l2):
    print(i)




