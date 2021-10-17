import pandas as pd
import utils.date_time
import utils.delete_unused_columns

def process(memory_dataframe, execution_date, times):
    utils.date_time.process_date_time(execution_date, times)
    utils.delete_unused_columns.delete(memory_dataframe)

    # converter atributo para data
    memory_dataframe['Time'] = pd.to_datetime(memory_dataframe['Time'], format="%d/%m/%Y")

    # colocar a data como indice para fazer uma série temporal
    memory_dataframe = memory_dataframe.set_index(pd.DatetimeIndex(memory_dataframe['Time']))
    del memory_dataframe['Time']

    # soma os valores de consumo de memória (em bytes) de cada MS e divide por 1e9 para termos o valor em Gigabyte
    memory_dataframe['total'] = memory_dataframe.sum(axis=1) / 1e9

    data = []
    for time in times:
        # soma o total de memória utilizada no período (start_time - end_time) e arredonda o valor para duas casas decimais
        
        start_hour = time['start_time'].split(' ')
        end_hour = time['end_time'].split(' ')

        d = {
            "exec_time": utils.date_time.diff_hours(start_hour[1], end_hour[1]),
            "cpu": round(memory_dataframe.loc[time['start_time']:time['end_time'], 'total'].sum(), 2)
        }

        data.append(d)
        
    return data