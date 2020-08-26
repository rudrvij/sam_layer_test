import json
import curves
#import boto3
import pandas as pd

#s3 = boto3.client('s3')

def lambda_handler(event, context):
    rawdata = str(event).replace("'","\"")
    input_js = rawdata
    input_js = json.loads(input_js)
    
    calc_guid = input_js['CalculationGuid']
    
    #s3.put_object(Bucket='sigma-test-input-data-3-4-2020', Body=rawdata, Key = calc_guid +'.json')
    
    result = curves.get_rolled_curve(rawdata)
    #s3.put_object(Bucket='sigma-test-input-data-3-4-2020', Body=result, Key = calc_guid +'_result.json')
    
    return str(result)