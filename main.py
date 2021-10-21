import pandas as pd
import json

import processor

mem_list = []
number_test_cases = 2
execution_dates = ["2021-10-06", "2021-10-18", "2021-10-19", "3", "4", "5", "2021-10-13"]

for i in range(number_test_cases):
    memory = pd.read_excel(f"memory-data/Memory-Usage-T{i}.xlsx")
    cpu = pd.read_excel(f"cpu-data/CPU-Usage-T{i}.xlsx")

    with open(f"test-logs-data/t{i}.json") as json_file:
        data_logs_of_test = json.load(json_file)
        json_file.close()

    execution_date = execution_dates[i]

    mem_list.append(processor.process(
        memory, cpu, execution_date, data_logs_of_test))

    df = pd.DataFrame(mem_list[i])
    df.to_csv(f"results/test{i}.csv", index=False)
