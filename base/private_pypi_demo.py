from quant_core import data_core

if __name__ == '__main__':
    # code_list_param = ['000001.MF', '000003.MF']
    code_list_param = None
    column_list_param = ['id1', 'code1', 'fund_management_company1']
    data = data_core.DataRepo('devs')
    df_tmp = data.get_fund_info(column_list_param, input_code_list=code_list_param)
    print(df_tmp)
