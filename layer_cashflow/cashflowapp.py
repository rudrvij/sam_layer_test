import json
import cashflows
#import boto3
import pandas as pd
import displayfunctions

#s3 = boto3.client('s3')

def cf_lambda_handler(event, context):
    rawdata = str(event["body"]).replace("'","\"")    
    input_js = rawdata.replace("'","\"")    
    
    #calc_guid = input_js['CalculationGuid']
    
    #s3.put_object(Bucket='sigma-test-input-data-3-4-2020', Body=rawdata, Key = calc_guid +'.json')
    
    result = cashflows.get_rolled_curve(input_js)    
    #s3.put_object(Bucket='sigma-test-input-data-3-4-2020', Body=result, Key = calc_guid +'_result.json')
    
    return {
        "statusCode": 200,
        "body": displayfunctions.displayText() + ' - Cashflow  Yield of first maturity point is ' + str(result['Yield'][0])
        }
    