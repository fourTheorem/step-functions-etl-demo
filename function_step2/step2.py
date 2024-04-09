import json
import os
from utils.shared import get_params_from_ssm

STAGE = os.environ['STAGE']
SERVICE_NAME = os.environ['SERVICE_NAME']
STEP_NAME = '2'

def handle_event(event, context):
    param_name = f'/{STAGE}/{SERVICE_NAME}/etl_params'
    param_dict = get_params_from_ssm(param_name)
    data_source = param_dict[f'source_step{STEP_NAME}']
    data_destination = param_dict[f'destination_step{STEP_NAME}']
    
    return f"{event['body']}. Step={STEP_NAME}, STAGE={STAGE}, Data Source={data_source}, Data Destination={data_destination}"

