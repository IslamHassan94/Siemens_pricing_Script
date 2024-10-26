import os
from datetime import datetime

import pandas as pd

from Script.Config import Config_Setup

input_sheet = Config_Setup.input_sheets_dir + Config_Setup.input_file_name
business_unit = Config_Setup.business_unit
customer_name = Config_Setup.customer_name
material_number = Config_Setup.part_number


def handle_pricing():
    filtered_df = filter_and_adjust_rate(business_unit, customer_name, material_number)
    output_path = Config_Setup.output_path
    os.makedirs(output_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    output_file = os.path.join(output_path, f"Filtered_Pricing_Data_{timestamp}.xlsx")
    filtered_df.to_excel(output_file, index=False)
    print(f"Filtered data saved to {output_file}")


def filter_and_adjust_rate(business_unit_desc, customer_name, material_number):
    df = pd.read_excel(input_sheet)
    filtered_df = df[
        (df['TGL Business Unit Desc'] == business_unit_desc) &
        (df['CM Customer Name 1 (AG)'] == customer_name) &
        (df['Material Number (Siemens)'] == material_number)
        ]
    if not filtered_df.empty:
        filtered_df = (
            filtered_df.loc[filtered_df.groupby('Material Number (Siemens)')['Rate in USD'].idxmax()]
            .assign(**{'Rate in USD': lambda x: x['Rate in USD'] * 1.03})
        )
    return filtered_df


def filter_and_adjust_for_all_customers(business_unit_desc):
    df = pd.read_excel(input_sheet)
    filtered_df = df[df['TGL Business Unit Desc'] == business_unit_desc]

    if not filtered_df.empty:
        filtered_df.loc[:, 'Rate in USD'] *= 1.03
        filtered_df = filtered_df.loc[
            filtered_df.groupby(['CM Customer Name 1 (AG)', 'Material Number (Siemens)'])['Rate in USD'].idxmax()
        ]

    return filtered_df


def handle_pricing_for_all_customers():
    filtered_df = filter_and_adjust_for_all_customers(business_unit)
    output_path = Config_Setup.output_path
    os.makedirs(output_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    output_file = os.path.join(output_path, f"Filtered_Pricing_Data_All_Customers_{timestamp}.xlsx")
    filtered_df.to_excel(output_file, index=False)
    print(f"Filtered data for all customers saved to {output_file}")


def filter_and_adjust_for_material_list(business_unit_desc, customer_name, material_numbers):
    df = pd.read_excel(input_sheet)
    filtered_df = df[
        (df['TGL Business Unit Desc'] == business_unit_desc) &
        (df['CM Customer Name 1 (AG)'] == customer_name) &
        (df['Material Number (Siemens)'].isin(material_numbers))
        ]
    if not filtered_df.empty:
        filtered_df.loc[:, 'Rate in USD'] *= 1.03
        filtered_df = filtered_df.loc[
            filtered_df.groupby('Material Number (Siemens)')['Rate in USD'].idxmax()
        ]

    return filtered_df


def handle_pricing_for_material_list():
    material_numbers = ['6AG4104-5GK30-1JX0', '6ES7718-1CC10-0CC3', '6ES7718-1CB10-0CC3']
    filtered_df = filter_and_adjust_for_material_list(business_unit, customer_name, material_numbers)
    output_path = Config_Setup.output_path
    os.makedirs(output_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    output_file = os.path.join(output_path, f"Filtered_Pricing_Data_Material_List_{timestamp}.xlsx")
    filtered_df.to_excel(output_file, index=False)
    print(f"Filtered data for specified material list saved to {output_file}")


def filter_and_adjust_for_customer(business_unit_desc, customer_name):
    df = pd.read_excel(input_sheet)
    filtered_df = df[
        (df['TGL Business Unit Desc'] == business_unit_desc) &
        (df['CM Customer Name 1 (AG)'] == customer_name)
        ]
    if not filtered_df.empty:
        filtered_df.loc[:, 'Rate in USD'] *= 1.03
        filtered_df = filtered_df.loc[
            filtered_df.groupby('Material Number (Siemens)')['Rate in USD'].idxmax()
        ]

    return filtered_df


def handle_pricing_for_customer():
    filtered_df = filter_and_adjust_for_customer(business_unit, customer_name)
    output_path = Config_Setup.output_path
    os.makedirs(output_path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    output_file = os.path.join(output_path, f"{customer_name}_{timestamp}.xlsx")
    filtered_df.to_excel(output_file, index=False)
    print(f"Filtered data for specified customer saved to {output_file}")
