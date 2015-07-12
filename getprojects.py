import sys
import requests
import subprocess

def git_installed():
    try:
        git = subprocess.Popen(["git", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = git.communicate()
    except FileNotFoundError:
        return False
    return git.returncode == 0 and result[0].startswith(b"git version")

def main():
    if not git_installed():
        print("You need to install git first.")
    elif len(sys.argv) < 2:
        print("Usage: {} username".format(sys.srgv[0]))
    else:
        url = "https://api.github.com/users/{}/repos".format(sys.argv[1])
        response = requests.get(url)
        if response.status_code == 200:
            for repo in response.json():
                git = subprocess.Popen(["git", "clone", repo["clone_url"]], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                git.wait()
                if git.returncode == 0:
                    print("Successfully cloned {}.".format(repo["full_name"]))
                else:
                    print("Failed to clone {}.".format(repo["full_name"]))
        else:
            print("GitHub user not found: {}".format(sys.argv[1]))
