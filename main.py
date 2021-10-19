import pandas as pd
import json

import processor

mem_list = []
number_test_cases = 1
execution_dates = ['0', '1', '2', '3', '4', '5', '2021-10-13']

for i in range(number_test_cases):
    memory = pd.read_excel("memory-data/Memory-Usage-T6.xlsx")
    cpu = pd.read_excel("cpu-data/CPU-Usage-T6.xlsx")

    # execution_date = execution_date[i]
    execution_date = "2021-10-13"

    with open('test-times/t6.json') as json_file:
        times_of_test = json.load(json_file)
        json_file.close()

    mem_list.append(processor.process(
        memory, cpu, execution_date, times_of_test))

    df = pd.DataFrame(mem_list[i])
    df.to_csv(f'results/test{i}.csv', index=False)
