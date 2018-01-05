from   flask   import request, jsonify
from   os.path import isfile
from   sklearn import svm
import pickle


MODEL_FILE = 'model.p'


class Model(object):

    __model_loaded = False

    def __init__(self):
        self.__model = svm.SVC()
        if isfile(MODEL_FILE):
            self.__load_model()

    def __load_model(self):
        fp = open(MODEL_FILE, 'rb')
        self.__model = pickle.load(fp)
        self.__model_loaded = True

    def __save_model(self):
        fp = open(MODEL_FILE, 'wb')
        pickle.dump(self.__model, fp)

    def __load_request_data(self):
        self.__request_data = request.get_json(force=True)

    def predict(self):
        if self.__model_loaded:
            self.__load_request_data()    
            record = self.__request_data
            label = self.__model.predict([[
                record['septal_length'],
                record['septal_width'],
                record['petal_length'],
                record['petal_width']
            ]])
            return jsonify(label=label[0]) 
        else:
            return jsonify(success=False)

    def train(self):
        features, labels = [], []
        self.__load_request_data()
        for record in self.__request_data:
            features.append([
                record['septal_length'],
                record['septal_width'],
                record['petal_length'],
                record['petal_width']
            ])
            labels.append(record['species'])
        self.__model.fit(features, labels)
        self.__save_model()
        return jsonify(success=True)

