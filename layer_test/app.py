import json
import curves
#import boto3
import pandas as pd
import displayfunctions

#s3 = boto3.client('s3')

def lambda_handler(event, context):
    #rawdata = str(event["body"]).replace("'","\"")
    rawdata = "{'CalculationGuid': '7badf4ca-48f9-433e-a5ad-cd501d3e3403','ConsultantCurveData': [{'Maturity': 1,'Yield': 1.2},{'Maturity': 2,'Yield': 0.2},{   'Maturity': 3,'Yield': 1.3}],'StartDateDailyCurveData': {'AsOfDate': '2020-01-02T00:00:00','CurveDataList': [{'Maturity': 1,'Yield': 1.2}]}, 'EndDateDailyCurveData': {'AsOfDate': '2020-01-02T00:00:00','CurveDataList': [{'Maturity': 1,'Yield': 1.3}]}}"
    input_js = rawdata.replace("'","\"")
    #input_js = json.loads(input_js)
    
    #calc_guid = input_js['CalculationGuid']
    
    #s3.put_object(Bucket='sigma-test-input-data-3-4-2020', Body=rawdata, Key = calc_guid +'.json')
    
    result = curves.get_rolled_curve(input_js)    
    #s3.put_object(Bucket='sigma-test-input-data-3-4-2020', Body=result, Key = calc_guid +'_result.json')
    
    return {
        "statusCode": 200,
        "body": displayfunctions.displayText() + ' - Yield of first maturity point is ' + str(result['Yield'][0])
        }
    