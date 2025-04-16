#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 09:36:28 2025

@author: mliu
"""

import redshift_connector
import pandas as pd
 
# Connects to Redshift cluster using Okta MFA Browser Plugin
conn = redshift_connector.connect(
    iam=True,
    ssl=True,
    host='edwreplica.ci0plcdfijlw.us-west-2.redshift.amazonaws.com',
    port=5432,
    database='edwreplica',
    cluster_identifier='edwreplica',
    region='us-west-2',
    login_url='https://credify.okta.com/home/credify_redshiftedwreplica_1/0oaqxcjwbrgAmKpy11t7/alnqxcqe50QhfN4IS1t7',
    credentials_provider='BrowserSamlCredentialsProvider',
)


cursor: redshift_connector.Cursor = conn.cursor()

fraud_cmd = """ select distinct account_number as loan_id
                from spectrum_transact.s_account_e30 e30
                join loanreview.loan_in_review lir on e30.account_number = lir.id
                where is_fraud='Y'
                and lir.product_type = 'PERSONAL_LOAN' ;
            """
            
cursor.execute(fraud_cmd)
fraud_df: pd.DataFrame = cursor.fetch_dataframe()