import os
import subprocess
from data_preprocess import build_result_json, read_json_files
from gen_results.a_proxy_mul_ping_gen_results import export_images
'''
def create_cron_job(subscription_url, proxy_name, output_dir, minute, hour, day_of_week):
    cron_command = f"python3 /path/to/test_speed.py {subscription_url} {proxy_name} {output_dir}"
    cron_time = f"{minute} {hour} * * {day_of_week}"
    cron_job = f"{cron_time} {cron_command}\n"
    
    # Get current crontab
    current_crontab = subprocess.run("crontab -l", shell=True, capture_output=True, text=True).stdout
    
    # Add new cron job
    with open("temp_cron", "w") as f:
        f.write(current_crontab)
        f.write(cron_job)
    
    # Install the cron job
    subprocess.run("crontab temp_cron", shell=True)
    os.remove("temp_cron")
    print("Cron job has been set.")

def main():
    subscription_url = input("Enter the subscription URL: ")
    proxy_name = input("Enter the proxy name: ")
    output_dir = input("Enter the output directory: ")
    
    print("Enter the time to run the speed test (24-hour format):")
    hour = input("Hour (0-23): ")
    minute = input("Minute (0-59): ")
    day_of_week = input("Day of the week (0-6, where 0 is Sunday): ")
    
    create_cron_job(subscription_url, proxy_name, output_dir, minute, hour, day_of_week)
'''
if (__name__ == "__main__"):
    folder_path = './'
    build_result_json(folder_path)
    export_images(folder_path)




    