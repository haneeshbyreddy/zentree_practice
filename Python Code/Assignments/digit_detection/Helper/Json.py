import json, time

class Json:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def add_data(cls, conf, accuracy, start_time):
        json_file = "data/accuracy.json"
        with open(json_file, mode='r', encoding='utf-8') as read_file:
            json_arr = json.load(read_file)
            conf_exists = False
            for entry in json_arr:
                if {k: entry[k] for k in conf} == conf:
                    entry['accuracy'].append(accuracy.item())
                    entry['time_taken'].append(round(time.time() - start_time, 2))
                    conf_exists = True
                    break
            if not conf_exists:
                json_arr.append(conf | {'accuracy': [accuracy.item()], 'time_taken': [round(time.time()-start_time,2)]})
        with open(json_file, mode='w', encoding='utf-8') as write_file:
            json.dump(json_arr, write_file, skipkeys=True)