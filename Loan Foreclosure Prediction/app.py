from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
import pandas as pd
import sklearn

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
@cross_origin()

def homepage():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
@cross_origin()

def predict():
    if request.method=='POST':
            scaler_file = 'Scalar.sav'
            model_file = 'RFmodel.sav'

            scaler = pickle.load(open(scaler_file,'rb'))
            model = pickle.load(open(model_file,'rb'))
            #reading input by users
            BALANCE_TENURE = float(request.form['BALANCE_TENURE'])
            COMPLETED_TENURE = float(request.form['COMPLETED_TENURE'])
            CURRENT_INTEREST_RATE_CHANGES = float(request.form['CURRENT_INTEREST_RATE_CHANGES'])
            DIFF_EMI_AMOUNT_MAX_MIN = float(request.form['DIFF_EMI_AMOUNT_MAX_MIN'])
            DIFF_ORIGINAL_CURRENT_TENOR = float(request.form['DIFF_ORIGINAL_CURRENT_TENOR'])
            FOIR = float(request.form['FOIR'])
            LAST_RECEIPT_AMOUNT = float(request.form['LAST_RECEIPT_AMOUNT'])
            NET_LTV = float(request.form['NET_LTV'])
            NET_RECEIVABLE = float(request.form['NET_RECEIVABLE'])
            NUM_EMI_CHANGES = float(request.form['NUM_EMI_CHANGES'])
            NUM_LOW_FREQ_TRANSACTIONS = float(request.form['NUM_LOW_FREQ_TRANSACTIONS'])
            OUTSTANDING_PRINCIPAL = float(request.form['OUTSTANDING_PRINCIPAL'])
            PAID_INTEREST = float(request.form['PAID_INTEREST'])
            PAID_PRINCIPAL = float(request.form['PAID_PRINCIPAL'])
            PRODUCT = request.form['PRODUCT']
            if(PRODUCT=="LAP"):
                PRODUCT_LAP = 1
                PRODUCT_STHL = 0
                PRODUCT_STLAP = 0

            elif(PRODUCT=="STHL"):
                PRODUCT_LAP = 0
                PRODUCT_STHL = 1
                PRODUCT_STLAP = 0

            elif(PRODUCT=="STLAP"):
                PRODUCT_LAP = 0
                PRODUCT_STHL = 0
                PRODUCT_STLAP = 1

            else:
                PRODUCT_LAP = 0
                PRODUCT_STHL = 0
                PRODUCT_STLAP = 0

            data = [BALANCE_TENURE,COMPLETED_TENURE,CURRENT_INTEREST_RATE_CHANGES,DIFF_EMI_AMOUNT_MAX_MIN,DIFF_ORIGINAL_CURRENT_TENOR,
                    FOIR,LAST_RECEIPT_AMOUNT,NET_LTV,NET_RECEIVABLE,NUM_EMI_CHANGES,NUM_LOW_FREQ_TRANSACTIONS,OUTSTANDING_PRINCIPAL,
                    PAID_INTEREST,PAID_PRINCIPAL,PRODUCT_LAP,PRODUCT_STHL,PRODUCT_STLAP]

            prediction = model.predict([data])
            print('Prediction:',prediction[0])
            if prediction[0]==1:
                return render_template('results.html',prediction_text = "Customer will foreclose the loan!!")
            else:
                return render_template('results.html',prediction_text = "Customer will not foreclose the loan")

    else:
        return render_template('index.html')

if __name__=='__main__':
    #app.run(host='127.0.0.1',port=8001,debug=True)
    app.run(debug=True)





            










