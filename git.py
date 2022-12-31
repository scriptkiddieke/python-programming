import os
import subprocess
from datetime import datetime, timedelta

# Configure these variables
REPO_PATH = r'C:\Users\alexm\Desktop\Projects\python'  # Using raw string for Windows path
COMMIT_MESSAGE = 'Hack the contribution graph'
START_DATE = '2023-01-01'
DAYS = 20
DAYS_TO_SKIP = 2  # Number of days to skip after each commit
TEMP_FILE_NAME = 'temp.py'

def run_command(command, env=None):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True, env=env)
    return result.stdout.strip()

def change_date_and_commit(date, counter):
    """Change the date, make a change in a file, and make a commit."""
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date
    env['GIT_COMMITTER_DATE'] = date
    
    with open(TEMP_FILE_NAME, 'a') as temp_file:
        temp_file.write(f'Commit number {counter}\n')
    
    run_command('git add .')
    run_command(f'git commit -m "{COMMIT_MESSAGE} {counter}"', env=env)

def main():
    # Ensure we're in the correct directory
    os.chdir(REPO_PATH)
    
    start_date = datetime.strptime(START_DATE, '%Y-%m-%d')
    commit_counter = 1
    
    for i in range(DAYS):
        commit_date = start_date + timedelta(days=i * (DAYS_TO_SKIP + 1))  # Adjust the date to skip days
        commit_date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
        print(f"Creating commit for {commit_date_str}")
        change_date_and_commit(commit_date_str, commit_counter)
        commit_counter += 1
    
    # Push the changes
    run_command('git push origin main')

if __name__ == "__main__":
    main()
