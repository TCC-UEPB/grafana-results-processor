import pandas as pd
import utils.date_time
import utils.delete_unused_columns

def process(memory_dataframe, cpu_dataframe, execution_date, times):
    utils.date_time.process_date_time(execution_date, times)
    
    utils.delete_unused_columns.delete(memory_dataframe)
    utils.delete_unused_columns.delete(cpu_dataframe)

    # converter atributo para data
    memory_dataframe['Time'] = pd.to_datetime(memory_dataframe['Time'], format="%d/%m/%Y")
    cpu_dataframe['Time'] = pd.to_datetime(cpu_dataframe['Time'], format="%d/%m/%Y")

    # colocar a data como indice para fazer uma série temporal
    memory_dataframe = memory_dataframe.set_index(pd.DatetimeIndex(memory_dataframe['Time']))
    cpu_dataframe = cpu_dataframe.set_index(pd.DatetimeIndex(cpu_dataframe['Time']))
    
    del memory_dataframe['Time']
    del cpu_dataframe['Time']

    # soma os valores de consumo de memória (em bytes) de cada MS e divide por 1e9 para termos o valor em Gigabyte
    memory_dataframe['total'] = memory_dataframe.sum(axis=1) / 1e9
    
    # soma os valores de consumo de cpu já em porcentagem
    cpu_dataframe['total'] = cpu_dataframe.sum(axis=1)

    data = []
    test_round = 1
    for time in times:
        start_hour = time['start_time'].split(' ')
        end_hour = time['end_time'].split(' ')

        memory = round( memory_dataframe.loc[time['start_time']:time['end_time'], 'total'].sum(), 2 )
        exec_time = utils.date_time.diff_hours(start_hour[1], end_hour[1])
        cpu = round( cpu_dataframe.loc[time['start_time']:time['end_time'], 'total'].sum(), 2)

        memory_per_second = round( (memory / exec_time) if exec_time > 0 else memory, 2 )
        cpu_per_second = round( (cpu / exec_time) if exec_time > 0 else cpu, 2 )

        d = {
            "Round": test_round,
            "Status": "F" if test_round > 1 else "P",
            "MS interrupted": "",
            "Exec time": exec_time,
            "Memory": memory,
            "Memory per second": memory_per_second,
            "Cpu": cpu,
            "Cpu per second": cpu_per_second,
            "Total requests": "",
            "Erro": ""
        }

        data.append(d)
        test_round += 1
        
    return data