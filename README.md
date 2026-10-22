# Resume Analyzer

A Python command-line tool that compares a resume with a job description and shows how well they match.

## What it does
- Extracts the most important keywords from a job description
- Calculates a match score (% of those keywords found in the resume)
- Lists missing keywords
- Checks for standard resume sections (Education, Skills, Projects, Internship, Objective)
- Checks resume length

## Tech
Python 3 (standard library only: `re`, `sys`, `collections`). No installation needed.

## How to run
```
python analyzer.py sample_resume.txt sample_jd.txt
```
Replace the two files with your own resume text and a job description text.

## How it works
1. Both texts are lowercased and split into words.
2. Common words (the, and, with...) are removed from the job description.
3. The 25 most frequent remaining words become the keyword list.
4. Score = keywords found in resume / total keywords.

## Limitations
This is a simple keyword-matching tool, not a real ATS. It does not understand meaning or synonyms.

## Future improvements
- Read PDF resumes directly
- Use an AI model for smarter suggestions
- Simple web interface

## Author
Subrat Sahoo
