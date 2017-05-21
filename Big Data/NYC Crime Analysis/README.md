
### Big Data Term Project (Codes included are my sole contributions)
This is a the final project for big data class. I am one of the co-authors. 

### Data: 
NYPD Compliant Data Historic (https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i) 

### Enviorment: 
Codes are executed in PySpark enviorment.
#### Command maybe usefule: 
scp NYPD_Complaint_Data_Historic.csv YOUR_NETID@dumbo.es.its.nyu.edu:/home/YOUR_NETID
hadoop fs -copyFromLocal NYPD_Complaint_Data_Historic.csv 
spark-submit CODE_NAME.py /user/YOUR_NETIT/NYPD_Complaint_Data_Historic.csv  
hadoop fs -getmerge CODE_NAME.out CODE_NAME.out

### Data Quality and Summary:
This part uses PySpark to aggregate date by each column and find any missing values or potential errors 

### Data Trend: 
This part uses PySpark to aggregate 2 or more columns together and see the trend

### Data Analysis: 
This part uses PySpark to aggregare the NYPD Compliant Data and left join with 2 other datasets on the latitude/longtitude 


