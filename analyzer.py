"""
Resume Analyzer - compares a resume with a job description (JD).

It tells you:
  1. Match score (% of important JD keywords found in your resume)
  2. Missing keywords you should add (only if you really know them)
  3. Whether the standard resume sections are present
  4. Resume length check

Usage:
    python analyzer.py resume.txt jd.txt
"""

import re
import sys
from collections import Counter

# Common English words that carry no meaning for matching
STOPWORDS = {
    "the", "and", "for", "with", "you", "your", "are", "will", "have", "has",
    "this", "that", "from", "our", "their", "about", "such", "who", "can",
    "all", "any", "one", "per", "etc", "use", "using", "work", "working",
    "role", "team", "good", "strong", "knowledge", "ability", "experience",
    "required", "preferred", "years", "year", "must", "should", "also",
    "we", "hiring", "requirements", "build", "write", "daily", "preferred",
    "or", "in", "of", "to", "a", "an", "is", "as", "on", "at", "be", "by",
}

# Sections an ATS-friendly resume normally has
SECTIONS = ["education", "skills", "projects", "internship", "objective"]


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def tokenize(text):
    """Lowercase the text and split into words (keeps c++, c#, node.js style)."""
    return re.findall(r"[a-zA-Z][a-zA-Z0-9+#.]*", text.lower())


def important_keywords(jd_text, top_n=25):
    """Pick the most frequent meaningful words from the job description."""
    words = [w.strip(".") for w in tokenize(jd_text)]
    words = [w for w in words if len(w) > 1 and w not in STOPWORDS]
    return [w for w, _ in Counter(words).most_common(top_n)]


def analyze(resume_text, jd_text):
    resume_words = set(w.strip(".") for w in tokenize(resume_text))
    keywords = important_keywords(jd_text)

    found = [k for k in keywords if k in resume_words]
    missing = [k for k in keywords if k not in resume_words]
    score = round(100 * len(found) / len(keywords)) if keywords else 0

    sections_present = {s: (s in resume_text.lower()) for s in SECTIONS}
    word_count = len(tokenize(resume_text))

    return score, found, missing, sections_present, word_count


def print_report(score, found, missing, sections_present, word_count):
    print("\n=== RESUME ANALYSIS REPORT ===")
    print(f"Match score : {score}%")
    print(f"Found       : {', '.join(found) or 'none'}")
    print(f"Missing     : {', '.join(missing) or 'none'}")

    print("\nSections check:")
    for section, present in sections_present.items():
        print(f"  [{'x' if present else ' '}] {section.capitalize()}")

    print(f"\nLength: {word_count} words", end=" ")
    if word_count < 150:
        print("(too short - add more detail)")
    elif word_count > 700:
        print("(too long - keep it to 1 page)")
    else:
        print("(good)")

    print("\nTip: add a missing keyword only if you genuinely know it.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python analyzer.py resume.txt jd.txt")
        sys.exit(1)

    resume_text = read_file(sys.argv[1])
    jd_text = read_file(sys.argv[2])
    print_report(*analyze(resume_text, jd_text))


if __name__ == "__main__":
    main()
