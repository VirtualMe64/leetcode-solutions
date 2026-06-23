import os
import json
from dataclasses import dataclass

@dataclass
class Submission:
    id: int
    question_id: int
    lang: str
    lang_name: str
    time: str
    timestamp: int
    status: int
    status_display: str
    runtime: str
    url: str
    is_pending: str
    title: str
    memory: str
    code: str
    compare_result: str
    title_slug: str
    has_notes: bool
    flag_type: int
    frontend_id: int

# read the submissions dir and extract the accepted submissions
# yields lists of paths to the accepted submissions
def get_accepted_submissions(input_dir):
    for filename in os.listdir(input_dir):
        base = os.path.join(input_dir, filename, 'Accepted')
        if not os.path.exists(base):
            continue
        yield [os.path.join(input_dir, filename, 'Accepted', submission)
                for submission in os.listdir(base)]

# todo: use leetcoed api to get info about percentile, difficulty, etc
def get_info(submission_path : str) -> Submission:
    with open(os.path.join(submission_path, 'info.txt'), encoding='utf-8') as f:
        data = json.load(f)
    return Submission(**data)