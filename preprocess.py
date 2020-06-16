#import os
#os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
#import tensorflow as tf
import sys
import numpy as np
import pickle


#word_index=tf.keras.datasets.imdb.get_word_index()
#reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
#pickle.dump( word_index, open( "word_index.p", "wb" ),protocol=2 )
#pickle.dump( reverse_word_index, open( "reverse_word_index.p", "wb" ),protocol=2 )

word_index=pickle.load( open( "word_index.p", "rb" ) )
reverse_word_index = pickle.load( open( "reverse_word_index.p", "rb" ) )



#model=tf.keras.models.load_model('./sentimentanalysis8968/1/')

def encode(s):
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    s=s.lower()
    for x in filters:
        s=s.replace(x,' ')
    s=" ".join(s.split())
    l=s.split(' ')
    l=l[:min(1000,len(l))]
    result=[1]
    for word in l:
        i=word_index.get(word)
        if i is None or i>9999:
            result.append(2)
        else:
            result.append(word_index.get(word)+3)
    array=np.array(result, dtype="int32")
    paddedArray=np.pad(array,(0,1000-len(array)),'constant',constant_values=(0,))
    return paddedArray
    
phrase=sys.argv[1]
encoded_phrase=encode(phrase)
print(encoded_phrase)
#print(model(np.array([encoded_phrase],dtype='float32')).numpy()[0][0])


    
