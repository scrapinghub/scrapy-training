#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple monitor jobs checker for the last 24 hours
"""

from __future__ import print_function

import argparse
import os

import boto
from datetime import datetime
from datetime import timedelta
from scrapinghub import Project, Connection

# Configure your SES credentials here
AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''

# Configure the Mail-from here
DEFAULT_MAIL_FROM = 'Custom Notification <noreply@yourdomain.com>'


def send_email(recipients, subject, body, mail_from=DEFAULT_MAIL_FROM):
    """Send an email using AWS Simple Email Service
    """
    ses = boto.connect_ses(AWS_ACCESS_KEY, AWS_SECRET_KEY)
    ses.send_email(mail_from, subject, body, recipients)
    print('Email sent to %s' % ', '.join(recipients))


def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')


def has_job_error(job):
    success_reason = 'no_reason'
    return (job.info.get('errors_count', 0) > 0
            or job.info.get('close_reason') != success_reason)


def is_job_newer_than(job, since_time):
    cancelled_before_starting = ('updated_time' not in job.info
                                 and job.info.get('close_reason') == 'cancelled')
    if cancelled_before_starting:
        return False
    return since_time <= parse_date(job.info['updated_time'])


def get_last_24h_jobs(apikey, project_id):
    """Fetch jobs that finished in the last 24 hours
    """
    project = Project(Connection(apikey), project_id)
    since_time = datetime.utcnow() - timedelta(hours=24)
    jobs = [
        job for job in project.jobs(state='finished')
        if is_job_newer_than(job, since_time)
    ]
    return jobs


def render_report(jobs_with_error):
    """Build a text report for the jobs with errors
    """
    output = []
    for job in jobs_with_error:
        errors_count = job.info.get('errors_count', 0)
        close_reason = job.info.get('close_reason')

        job_id = job.info["id"].split('/')
        url = 'https://app.scrapinghub.com/p/{0}/job/{1}/{2}'.format(
            job_id[0], job_id[1], job_id[2])

        error_message = ['Errors found for job "{0}" ({1}):'.format(
            job.info['spider'], url)]
        if errors_count > 0:
            error_message.append('    There were {} error{}.'.format(
                errors_count, '' if errors_count == 1 else 's'))

        success_reasons = ('no_reason', 'finished')
        if close_reason not in success_reasons:
            error_message.append('    Close reason should not be "{}".'.format(
                close_reason))
        output.append('\n'.join(error_message))

    return '\n\n'.join(output)


def main(args):
    job_list = get_last_24h_jobs(args.apikey, args.project_id)
    jobs_with_errors = [job for job in job_list if has_job_error(job)]

    if jobs_with_errors:
        report = render_report(jobs_with_errors)
        if args.mail:
            subject = 'Scrapy Cloud - jobs with errors'
            send_email(args.mail, subject, body=report)
        else:
            print(report)
    else:
        print('No errors found.')


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('--apikey', default=os.getenv('SHUB_APIKEY', None),
                        help='API key to use for scrapinghub (will fallback '
                             'to SHUB_APIKEY variable)')
    parser.add_argument('project_id', type=int,
                        help='Project ID to get info from.')
    parser.add_argument('--mail', action='append', help='Send output as email')
    args = parser.parse_args()

    if not args.apikey:
        parser.error('Please provide an API key with --apikey option')
    return args


if '__main__' == __name__:
    main(parse_args())
