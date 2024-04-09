import json
import boto3

def get_params_from_ssm(param_name):
    try:
        return_val = {}
        ssm = boto3.client('ssm')
        response = ssm.get_parameters(Names=[param_name], WithDecryption=True)
        parameter_value = response['Parameters'][0]['Value']
        return_val = json.loads(parameter_value)

        return return_val
    except:
        raise Exception(f"Could not load parameters from {param_name}")