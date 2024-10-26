# config_setup.py

import yaml

config = yaml.safe_load(open("../../config.yml"))
input_sheets_dir = config['Input_Sheets']['input_folder']
input_file_name = config['Input_Sheets']['input_file_name']
business_unit = config['TGL_Business_Unit_Desc']
customer_name = config['CM_Customer_Name']
part_number = config['Part_Number']
output_path = config['output']
handle_all = config['actions']['handle_all_customers']
