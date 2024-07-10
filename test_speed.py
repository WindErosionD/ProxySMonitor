'''
import os
import subprocess
import datetime

def test_speed(subscription_url, proxy_name, output_dir):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_dir, f"speedtest_{current_time}.txt")
    
    command = f"python3 main.py -u '{subscription_url}' -g '{proxy_name}' -M pingonly --skip-requirements-check"
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    with open(output_file, 'w') as f:
        f.write(result.stdout)
        f.write(result.stderr)
    
    print(f"Test result saved to {output_file}")

if __name__ == "__main__":
    import sys
    subscription_url = sys.argv[1]
    proxy_name = sys.argv[2]
    output_dir = sys.argv[3]
    
    test_speed(subscription_url, proxy_name, output_dir)
    '''