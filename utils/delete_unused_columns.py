def delete(data_frame):
    del data_frame["ct_cadvisor"]
    del data_frame["ct_grafana"]
    del data_frame["ct_node-exporter"]
    del data_frame["ct_prometheus"]

    return data_frame