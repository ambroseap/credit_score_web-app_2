 # save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':

        R_ESTATE = request.form['R_ESTATE']
        MARRIED = request.form['MARRIED']

        CODE_GENDE = request.form['CODE_GENDE']
        FLAG_OWN_CA = request.form['FLAG_OWN_CA']
        NAME_CONTRACT_T = request.form['NAME_CONTRACT_T']
        CNT_CHILDREN = float(request.form['CNT_CHILDREN'])
        AMT_INCOME_TOTAL = float(request.form['AMT_INCOME_TOTAL'])
        AMT_CREDIT = float(request.form['AMT_CREDIT'])
        AMT_GOODS_PRICE = float(request.form['AMT_GOODS_PRICE'])
        FLAG_MOBIL = float(request.form['FLAG_MOBIL'])






         #R_ESTATE
        if (R_ESTATE == "Y"):
             R_ESTATE_yes=1
        else:
             R_ESTATE_yes=0


        # gender
        if (CODE_GENDE == "M"):
            male=1
        else:
            male=0

        # FLAG_OWN_CAR
        if(FLAG_OWN_CA=="Y"):
            FLAG_OWN_CAR_yes = 1
        else:
            FLAG_OWN_CAR_yes=0

        #

        # NAME_CONTRACT_TYPE
        if (NAME_CONTRACT_T=="Revolving loans"):
            NAME_CONTRACT_TYPE_1=1
        else:
            NAME_CONTRACT_TYPE_1=0

        # MARRIED
        if(MARRIED=='Married'):
            Married_1 = 1
            Married_2 = 0
            Married_3 = 0
            Married_4 = 0
            Married_5 = 0


        elif(MARRIED == 'Separated'):
            Married_1 = 0
            Married_2 = 1
            Married_3 = 0
            Married_4 = 0
            Married_5 = 0

        elif(MARRIED=="Single / not married"):
            Married_1 = 0
            Married_2 = 0
            Married_3 = 1
            Married_4 = 0
            Married_5 = 0
        elif(MARRIED=="Unknown"):
            Married_1 = 0
            Married_2 = 0
            Married_3 = 0
            Married_4 = 1
            Married_5 = 0
        elif(MARRIED=="Widow"):
            Married_1 = 0
            Married_2 = 0
            Married_3 = 0
            Married_4 = 0
            Married_5 = 1

        else:
            Married_1 = 0
            Married_2 = 0
            Married_3 = 0
            Married_4 = 0
            Married_5 = 0




        CNT_CHILDREN = np.log(CNT_CHILDREN)
        AMT_INCOME_TOTAL = np.log(AMT_INCOME_TOTAL)
        AMT_CREDIT = np.log(AMT_CREDIT)
        AMT_GOODS_PRICE = np.log(AMT_GOODS_PRICE)
        FLAG_MOBIL = np.log(FLAG_MOBIL)




        prediction = model.predict([[FLAG_MOBIL, AMT_GOODS_PRICE, AMT_CREDIT, CNT_CHILDREN, AMT_INCOME_TOTAL,  NAME_CONTRACT_TYPE_1, FLAG_OWN_CAR_yes, male, R_ESTATE_yes,  Married_1,Married_2, Married_3, Married_4, Married_5]])

        # print(prediction)

        if prediction==1:
            prediction=" <  GOOD  >"
        else:
            prediction=" <  BAD   >"




        return render_template("prediction.html", prediction_text="loan status is very{}".format(prediction))



    else:
        return render_template("prediction.html")



if __name__ == "__main__":
    app.run(debug=True)
