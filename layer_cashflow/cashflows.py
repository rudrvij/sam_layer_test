import json
import pandas as pd

def get_rolled_curve(input_json):
    
    input_json = json.loads(input_json)
    
    cons_curve = pd.DataFrame(input_json['ConsultantCurveData'])
    st_daily_curve = pd.DataFrame(
            input_json['StartDateDailyCurveData']['CurveDataList']
        )
    ed_daily_curve = pd.DataFrame(input_json['EndDateDailyCurveData']['CurveDataList'])
    
    return cons_curve
