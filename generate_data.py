import pandas as pd
import json

import processor


def generate(isTotal):
    data_list = []

    with open("data/execution_dates.json") as json_file:
        execution_dates = json.load(json_file)
        json_file.close()

    number_test_cases = len(execution_dates)

    for i in range(number_test_cases):
        memory = pd.read_excel(f"data/memory/Memory-Usage-T{i}.xlsx")
        cpu = pd.read_excel(f"data/cpu/CPU-Usage-T{i}.xlsx")

        path_logs_data = f"data/test-logs/total/t{i}.json" if isTotal else f"data/test-logs/requests/t{i}.json"

        with open(path_logs_data) as json_file:
            data_logs = json.load(json_file)
            json_file.close()

        execution_date = execution_dates[i]

        data_list.append(processor.process(
            memory, cpu, execution_date, data_logs))

        path_to_result = f"results/total/test{i}.csv" if isTotal else f"results/requests/test{i}.csv"

        df = pd.DataFrame(data_list[i])
        df.to_csv(path_to_result, index=False)
