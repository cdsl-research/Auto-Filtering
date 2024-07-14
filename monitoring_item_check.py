import subprocess
import yaml
from prometheus_api_client import PrometheusConnect
import datetime

def get_prometheus_rules():
    try:
        # Execute kubectl command
        result = subprocess.run(
            ["kubectl", "get", "PrometheusRule", "-n", "monitoring", "-o", "yaml"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing kubectl command: {e}")
        print(e.output)
        return None

def extract_expr_from_rules(yaml_data):
    expr_dict = {}
    data = yaml.safe_load(yaml_data)
    
    if 'items' in data:
        for item in data['items']:
            groups = item.get('spec', {}).get('groups', [])
            for group in groups:
                group_name = group.get('name', 'unknown_group')
                for rule in group.get('rules', []):
                    alert_name = rule.get('alert', 'unknown_alert')
                    expr = rule.get('expr', 'unknown_expr')
                    expr_dict[f"{group_name}_{alert_name}"] = expr
    
    return expr_dict

def get_prometheus_query_result(url, query, start_time=None, end_time=None, step='60m'):
    """
    Execute a specified PromQL query on a Prometheus server and obtain the result.

    Parameters:
    - url: URL of the Prometheus server
    - query: PromQL query to execute
    - start_time: Start time for the query (optional)
    - end_time: End time for the query (optional)
    - step: Step between data points (optional, default is 1 minute)

    Returns:
    - Result of the query execution (in JSON format)
    """
    # Establish connection to the Prometheus server
    prom = PrometheusConnect(url=url, disable_ssl=True)
    
    # Use current time if start_time and end_time are not provided
    if not start_time:
        start_time = datetime.datetime.now() - datetime.timedelta(hours=1)
    if not end_time:
        end_time = datetime.datetime.now()
    
    # Execute the query
    result = prom.custom_query_range(
        query=query,
        start_time=start_time,
        end_time=end_time,
        step=step
    )
    
    return result


def weight():
    query = "1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)"

    url = "http://outside-prometheus-m:9090/"
    output = get_prometheus_query_result(url, query, start_time=None, end_time=None, step='60m')
    
    # Extract unique instances
    instances = set(item['metric']['instance'] for item in output)

    # Print unique instances
    target_count = 0
    # print("Unique Instances:")
    for instance in instances:
        #print(instance)
        target_count +=1
    # print(target_count)


    # Define instance and device keywords to filter
    instances_and_devices = [
        ('192.168.100.226:9100', 'outside-nfs3'),
        ('192.168.100.68:9100', 'outside-nfs3'),
        ('192.168.100.70:9100', 'outside-nfs3'),
        ('192.168.100.228:9100', 'outside-nfs3'),
        ('192.168.100.227:9100', 'outside-nfs3')
    ]

    # Filter metrics by instance and device
    filtered_metrics = [
        item for item in output
        if any(instance in item['metric']['instance'] and device in item['metric']['device'] for instance, device in instances_and_devices)
    ]
    
    # Print filtered metrics
    # print("Filtered Metrics:")
    # for metric in filtered_metrics:
    #     print(metric)
    return target_count,filtered_metrics,instances









