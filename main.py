import pandas as pd
import json

import memory_processor

mem_list = []
number_test_cases = 1

for i in range (number_test_cases):
    memory = pd.read_excel("memory-data/Memory-Usage-T6.xlsx")
    execution_date = "2021-10-13"

    with open('test-times/t6.json') as json_file:
        times_of_test = json.load(json_file)
        json_file.close()

    mem_list.append( memory_processor.process(memory, execution_date, times_of_test) )

    # for mem in mem_list:
    #     for key in mem:
    #         print(f'Mem: {key}', end='\n')

    print( mem_list[0][0]['exec_time'] )
    print( mem_list[0][0]['cpu'] )