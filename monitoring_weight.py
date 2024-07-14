from monitoring_item_check import weight

def monitoring_weight():
    Weight_all = weight()
    Weight_All = Weight_all[0]
    Weight_metric = Weight_all[1]
    Weight_target = Weight_all[2]
    
    # Define elements to check for in device
    elements = {target.replace(':9100', '') for target in Weight_target}
    
    # Initialize count dictionary
    count_dict = {elem: 0 for elem in elements}
    
    for Weight_item in Weight_metric:
        device = Weight_item['metric']['device']
        matched_elem = next((elem for elem in elements if elem in device), None)
        if matched_elem:
            count_dict[matched_elem] += 1
    
    # Set default value to 1 for elements that were not found
    for elem in elements:
        if count_dict[elem] == 0:
            count_dict[elem] = 1
    
    return count_dict


def weight_calculation():
    Weight_all = weight()
    Weight_All = Weight_all[0]
    Weight_target = monitoring_weight()
    
    # Calculate Weight_target / Weight_All for each key in the dictionary
    result = {}
    for key, value in Weight_target.items():
        if ':' in key:
            ip, port = key.split(':')
            result[f'{ip}:{port}'] = value / Weight_All
        else:
            result[f'{key}:9100'] = value / Weight_All
    
    return result




