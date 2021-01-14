# ML-Project-Deployment

1) <b>Loan Foreclosure Prediction</b>  (Heroku app link: https://desolate-wildwood-07851.herokuapp.com/ )

   <b>Business Problem at hand</b>: Finacial firm has to deal with foreclosure issues when borrower fails to repay the loan. The foreclosure costs are high so it is 
                                    better if the lender can predict the foreclosure and take certain actions to retain them.
                             
   
   In the above 'Loan Foreclosure Prediction' repo, below files are present which are required while deploying the application on Heroku platform.
   
   i) <b>templates & static</b>: This is contains html files which are part of Frontend development (UI), this basically deals with the aesthetic look of web app.
   
   ii) <b>Procfile</b>: This contains the command to run the web application once deployed on the server.
   
   iii) <b>NBFC_Loan_Foreclosure.ipynb</b> : This is a jupyter notebook file which contains the EDA, feature engineering and model building part.
 
   iv) <b>RFModel.sav</b>: This the pickle file which contains the Random forest model which is used for Foreclosure prediction.
  
    v) <b>Scalar.sav</b>: This file is used to scale the input values at the backend which are entered by user in the application.
   
   vi) <b>app.py</b>: This is backend part of the web application which gives output/prediction for the values entered by user.
  
   vii) <b>requirements.txt</b>: This file contains all required libararies which are necessary to run the application.
   
   
   <b>How to run the application:</b>
   
     i) Open this repository as folder in Pycharm in your local system.

    ii) Create new environment for this project, select python version as 3.6

   iii) Once conda environment is created, do <b>pip install -r requirements.txt</b> in pycharm terminal.

    iv) After that click on app.py and run the application.

     v) If everything goes fine, then this app will run in your local machine.

    vi) Now we have deploy this application on cloud server, i.e Heroku server.

   vii) Open anaconda prompt terminal.

    viii) Navigate to the folder where the above files are present and enter the below set of commands in sequential manner(make sure you have git CLI installed incase of               windows OS:

        git init

        git add .

        git commit -m"this is my project"

        heroku login (make sure you have created Heroku account before executing this command)

        heroku create

        git remote -v

        git push heroku master
        
   Follow the above steps for succesfull deployment of web application onto cloud server.     
        
     
     
