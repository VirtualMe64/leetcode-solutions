import tempfile
import zipfile
import tqdm
from functools import lru_cache

from utils import *
from config import *

data = open("README.md", "r", encoding="utf-8").read()
parts = data.split("\n##")
modifiedParts = []

@lru_cache(maxsize=None)
def getSolutions():
    return os.listdir(OUTPUT_DIR)

def findSolutionPath(question_id):
    files = getSolutions()

    for file in files:
        if file.startswith(f"{question_id:04d}_"):
            return f"{file}"
    return None

def generateSolutionTable():
    table_data = []

    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(INPUT_ZIP, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        INPUT_DIR = temp_dir # kinda hacky but works -- maybe fix later
        submissions = list(get_accepted_submissions(INPUT_DIR))
        for submission in tqdm.tqdm(submissions, desc="Processing submissions"):
            infos = [get_info(s) for s in submission]
            languages = sorted(set(info.lang_name for info in infos))
            solutionPath = findSolutionPath(infos[0].question_id)
            
            if solutionPath:
                table_data.append((infos[0].question_id, infos[0].title_slug, languages, solutionPath))
    
    table = "| ID | Question | Solution | Languages |\n |----|----------|----------|-----------|\n"

    for question_id, title_slug, languages, solutionPath in sorted(table_data):
        question_link = f"https://leetcode.com/problems/{title_slug}/"
        solution_link = f"{OUTPUT_DIR}/{solutionPath}"

        table += f"| {question_id} "
        table += f"| [{" ".join(title_slug.split('-')).title()}]({question_link}) "
        table += f"| [Solution]({solution_link}) "
        table += f"| {', '.join(languages)} |\n"
    
    return table

def generateSolutionTableBlock():
    return f" Solution Table\n\n{generateSolutionTable()}\n"

found = False
for part in parts:
    if part.startswith(" Solution Table"):
        modifiedParts.append(generateSolutionTableBlock())
        found = True
    else:
        modifiedParts.append(part)

if not found:
    modifiedParts.append(generateSolutionTableBlock())

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n##".join(modifiedParts))