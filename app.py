from flask import Flask, render_template, request
import pickle
import pandas
import numpy as np

final_req = pandas.read_pickle(open('final.pkl','rb'))
sim = pandas.read_pickle(open('distance.pkl','rb'))


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', chaptername = list(final_req['ChapterName'].values),)

@app.route('/recommend_chapters', methods=['get'])
def recommend():
    user_input = request.form.get('user_input')
    index=final_req[final_req['ChapterName']== user_input].index[0]
    distance = sim[index]
    chapters_list = sorted(list(enumerate(distance)),reverse = True, key=lambda x:x[1])[1:6]
    data = []
    for i in chapters_list:
        x = final_req.iloc[i[0]].ChapterName
        data.append(x)
    print(data)
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=False)
