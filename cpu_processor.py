import pandas as pd
import utils.date_time
import utils.delete_unused_columns

def process(cpu_dataframe, execution_date, times):
    utils.date_time.process_date_time(execution_date, times)
    utils.delete_unused_columns.delete(cpu_dataframe)

    # converter atributo para data
    cpu_dataframe['Time'] = pd.to_datetime(cpu_dataframe['Time'], format="%d/%m/%Y")

    # colocar a data como indice para fazer uma série temporal
    cpu_dataframe = cpu_dataframe.set_index(pd.DatetimeIndex(cpu_dataframe['Time']))
    del cpu_dataframe['Time']

    # soma os valores de consumo de cpu e divide por 100 para termos o valor em porcentagem
    cpu_dataframe['total'] = cpu_dataframe.sum(axis=1) / 100

    data = []
    for time in times:
        # soma o total de memória utilizada no período (start_time - end_time) e arredonda o valor para duas casas decimais
        
        start_hour = time['start_time'].split(' ')
        end_hour = time['end_time'].split(' ')

        d = {
            "exec_time": utils.date_time.diff_hours(start_hour[1], end_hour[1]),
            "cpu": round(cpu_dataframe.loc[time['start_time']:time['end_time'], 'total'].sum(), 2)
        }

        data.append(d)
        
    return data