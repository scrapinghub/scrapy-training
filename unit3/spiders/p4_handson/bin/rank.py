import argparse
from scrapinghub import Connection


class NoJobsException(Exception):
    pass


def get_latest_job(project):
    for job in project.jobs(state='finished'):
        return job
    else:
        raise NoJobsException('No finished jobs in project {}'.format(project.id))


def fetch_latest_job_items(project):
    job = get_latest_job(project)
    return list(job.items())


def rank_items(items, top=10):
    return sorted(items, key=lambda i: i['score'] * i['number_of_comments'] * i['user_karma'], reverse=True)[:top]


def main(args):
    project = Connection(args.apikey)[args.project_id]
    items = fetch_latest_job_items(project)
    for it in rank_items(items, args.top):
        print(it)


def parse_args():
    parser = argparse.ArgumentParser(description='Rank reddit posts')
    parser.add_argument('--apikey', type=str, help='Scrapinghub API key', required=True)
    parser.add_argument('--top', type=int, default=10, help='Scrapinghub API key')
    parser.add_argument('--project_id', type=int, help='Project ID', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)
