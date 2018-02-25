import pandas
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

score = []
@app.route('/getRecommendations', methods=['GET'])
def get_recommendation():
    job=request.args.get('current_job')
    return json.dumps(score)



if __name__ == '__main__':
    variables = pandas.read_csv('linkedin_data.csv')
    Y = variables[['n_prev_tenures']]
    X = variables[['beauty']]
    X_norm = (X - X.mean()) / (X.max() - X.min())
    Y_norm = (Y - Y.mean()) / (Y.max() - Y.min())

    Nc = range(1, 20)
    kmeans = [KMeans(n_clusters=i) for i in Nc]
    kmeans
    score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
    print score
    app.run()

