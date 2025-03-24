#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 10:09:45 2025

@author: mliu
"""

# define URL params and connection params
url_params = {
    'drivername': 'redshift+redshift_connector',
    'database': 'edwreplica',
    'host': 'edwreplica.ci0plcdfijlw.us-west-2.redshift.amazonaws.com',
    'port': '5432'
}

conn_params = {
    'iam': True,
    'credentials_provider': "BrowserSamlCredentialsProvider",
    'idp_host': 'upgrad.okta.com',
    'cluster_identifier': "edwreplica",
    'region': 'us-west-2',
    'ssl_insecure': False,
    'login_url': 'https://credify.okta.com/home/credify_redshiftedwreplica_1/0oaqxcjwbrgAmKpy11t7/alnqxcqe50QhfN4IS1t7'
}