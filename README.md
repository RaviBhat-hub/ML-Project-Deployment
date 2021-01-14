# ML-Project-Deployment

1) Loan Foreclosure Prediction

   Business Problem at hand: Finacial firm has to deal with foreclosure issues when borrower fails to repay the loan. The foreclosure costs are high so it is better if the
                             lender can predict the foreclosure and take certain actions to retain them.
                             
   
   In the above 'Loan Foreclosure Prediction' repo, below files are present which are required while deploying the application on Heroku platform.
   
   i) <b>templates & static</b>: This is contains html files which are part of Frontend development (UI), this basically deals with the aesthetic look of web app.
   
  ii) Procfile: This contains the command to run the web application once deployed on the server.
   
 iii) NBFC_Loan_Foreclosure.ipynb : This is a jupyter notebook file which contains the EDA, feature engineering and model building part.
 
  iv) RFModel.sav: This the pickle file which contains the Random forest model which is used for Foreclosure prediction.
  
   v) Scalar.sav: This file is used to scale the input values at the backend which are entered by user in the application.
   
  vi) app.py: This is backend part of the web application which gives output/prediction for the values entered by user.
  
 vii) 
