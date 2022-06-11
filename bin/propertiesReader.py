from jproperties import Properties


def get_properties_scope():
    configs = Properties()
    with open('../configs/config.properties', 'rb') as config_file:
        configs.load(config_file)
    return configs


def get_token():
    return get_properties_scope().get('token').data


def get_account_id():
    return get_properties_scope().get('account_id').data


def get_positions_report_file_name():
    return get_properties_scope().get('positions_report_file_name').data


def get_total_report_file_name():
    return get_properties_scope().get('total_report_file_name').data
