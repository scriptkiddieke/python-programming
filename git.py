import os
import subprocess
from datetime import datetime, timedelta

# Configure these variables
REPO_PATH = r'C:\Users\alexm\Desktop\Projects\python'  # Using raw string for Windows path
COMMIT_MESSAGE = 'Hack the contribution graph'
START_DATE = '2023-06-07'
DAYS = 100
DAYS_TO_SKIP = 2  # Number of days to skip after each commit
TEMP_FILE_NAME = 'temp.txt'
BRANCH_NAME = 'main'

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
    git_status = run_command('git status')
    print(git_status)  # Print git status for debugging
    commit_output = run_command(f'git commit -m "{COMMIT_MESSAGE} {counter}"', env=env)
    print(commit_output)  # Print commit output for debugging

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
    push_output = run_command(f'git push origin {BRANCH_NAME}')
    print(push_output)  # Print push output for debugging

if __name__ == "__main__":
    main()
