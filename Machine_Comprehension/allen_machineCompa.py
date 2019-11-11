from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("bidaf-model-2017.09.15-charpad.tar.gz")



p = "Veera and Venkat from BigTapp Analytics are travelling to London on 15th September 2016. Veera will be attending an Ananlytics Conference on 19th September and Venkat will be visiting a client on 20th September. Veera is planning to play a round of Golf in St Andrews on 23rd September and Venkat is planning to go to Madame Tussads museum on the same day. If time permits both of them might see a T20 cricket match in the Lords's Stadium. Veera is planning to buy an Iphone 7 which costs $700, Venkat has decided to buy a Souvenier to Anantha. Veera can be reached at local mobile number:  +44 20 7621 2800."
q = "what is the veera mobile number?"
#p = 'Having 3.7 Years of experience in IT Industry in special emphasis on development applications using Java, J2EE technologies.Overall exposure of Core Java and Advanced Java Technologies.Pragmatic and competent application engineer with strong communication, presentation and problem solving skills.Strongly skilled in requirements gathering and analysis.'
#q = ''
s = predictor.predict(
  passage=p,
  question=q
)

 
print('RES --->  ',s['best_span_str'])
print('COMPLETED')
