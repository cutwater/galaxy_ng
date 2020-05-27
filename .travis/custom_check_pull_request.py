import os
import subprocess


def get_commit_list(commit_range):
    git_range = '..'.join(commit_range)
    result = subprocess.run([
        'git', 'rev-list', '--no-merges', git_range
    ], encoding='utf-8')
    return result.stdout.strip().split('\n')


def main():
    commit_range = os.getenv('TRAVIS_COMMIT_RANGE').split('...')
    for commit in get_commit_list(commit_range):
        print(commit)


if __name__ == "__main__":
    main()
