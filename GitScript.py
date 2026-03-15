import subprocess

log_result = subprocess.run(["git", "log", "--pretty=oneline"], capture_output=True)
print("Commits:", len(log_result.stdout.splitlines()))

log_result_commits_only = subprocess.run(["git", "log", '--pretty=format:"%s"'], capture_output=True).stdout.splitlines()
print("Last Commit Message:", log_result_commits_only[-1].decode('utf-8'))
