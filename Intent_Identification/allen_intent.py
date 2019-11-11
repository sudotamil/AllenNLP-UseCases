import re
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords

request = "Being a movie buff Ravi wanted a credit card, which will have more offers on movie tickets, and he is expecting complimentary movie tickets as well."

from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("srl-model-2018.05.25.tar.gz")
res = predictor.predict(
  sentence=request
)


def removeStopWords(txt):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(txt)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]  
    filtered_sentence = [] 
  
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w)
    return ' '.join(filtered_sentence)   


verbWithDesc = []
verbs = res['verbs']
for i in verbs:
    verbWithDesc.append(i['verb'] +'|'+ i['description'])

ps = PorterStemmer()

labels = ['buy', 'dining', 'entertainment', 'exchange', 'offers', 'shopping', 'travel', 'look']


for i in verbWithDesc:
    if len(i.split(":")) >= 3:
        a = i.split("|")
        verb = ps.stem(a[0]).strip()
        desc = a[1]
        o = re.findall(r'[^[.*]+]', desc)
        if len(o) >= 3:
            actor = str(o[0].split(":")[1]).replace("]","").strip()
            #intent = ps.stem(o[1].split(":")[1]).replace("]","")
            intent = verb
            obj = removeStopWords(str(o[2].split(":")[1]).replace("]",""))
            print("-------------------------------------------------------")
            print("ACTOR  : ",actor ,"\nINTENT : ", intent ,"\nOBJECT : ", obj)
            print("-------------------------------------------------------")
            


