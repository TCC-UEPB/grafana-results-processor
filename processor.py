import pandas as pd
import utils.date_time
import utils.delete_unused_columns

def process(memory_dataframe, cpu_dataframe, execution_date, logs_data):
    utils.date_time.process_date_time(execution_date, logs_data)
    
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

    processed_data = []
    for data in logs_data:
        start_hour = data['start_time'].split(' ')
        end_hour = data['end_time'].split(' ')

        if(start_hour[1]):
            memory = round( memory_dataframe.loc[data['start_time']:data['end_time'], 'total'].sum(), 2 )
            exec_time = utils.date_time.diff_hours(start_hour[1], end_hour[1])
            cpu = round( cpu_dataframe.loc[data['start_time']:data['end_time'], 'total'].sum(), 2)
        else:
            memory = exec_time = cpu = 0

        memory_per_second = round( (memory / exec_time) if exec_time > 0 else memory, 2 )
        cpu_per_second = round( (cpu / exec_time) if exec_time > 0 else cpu, 2 )
        status = data['status']
        test_round = data['round']

        obj = {
            "Round": test_round,
            "Status": status,
            "MS interrupted": ', '.join(str(e) for e in data['interrupted_ms'] ),
            "Exec time": exec_time,
            "Memory": memory,
            "Memory per second": memory_per_second,
            "Cpu": cpu,
            "Cpu per second": cpu_per_second,
            "Total requests": data['total_requests'],
            "Erro": data['erro']
        }

        processed_data.append(obj)
        
    return processed_data