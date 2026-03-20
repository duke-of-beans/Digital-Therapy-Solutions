"""Trim over-length meta descriptions to <=160 chars."""
import os, re

OUTPUT = r'D:\Work\Digital-Therapy-Solutions\output'

FIXES = {
    'bipolar.html': 'Best online therapy for bipolar disorder. Expert-reviewed platforms with mood disorder specialists, medication support, and insurance. Updated monthly.',
    'eating-disorders.html': 'Best online therapy for eating disorders. Expert-reviewed platforms for anorexia, bulimia, and binge eating. Insurance options included. Updated monthly.',
    'grief.html': 'Best online therapy for grief and loss. Expert-reviewed platforms for bereavement and life transitions. Real pricing and insurance details. Updated monthly.',
    'stress.html': 'Best online therapy for stress management. Expert-reviewed CBT platforms to reduce chronic stress. Real pricing and insurance options. Updated monthly.',
    'relationship.html': 'Best online therapy for relationship issues. Expert-reviewed platforms for dating, family, and friendship challenges. Individual therapy options. Updated monthly.',
    'teen.html': 'Best online therapy for teens and adolescents. Expert-reviewed platforms with youth-specialist therapists and parental involvement options. Updated monthly.',
    'burnout.html': 'Best online therapy for burnout. Expert-reviewed platforms for chronic work stress and emotional exhaustion recovery. Real pricing included. Updated monthly.',
    'chronic-pain.html': 'Best online therapy for chronic pain. Expert-reviewed platforms for the mental health impact of long-term conditions. Insurance coverage included. Updated monthly.',
    'loneliness.html': 'Best online therapy for loneliness and isolation. Expert-reviewed platforms for building connection and coping with chronic loneliness. Updated monthly.',
    'self-esteem.html': 'Best online therapy for self-esteem and confidence. Expert-reviewed platforms for inner critic work and self-worth. Real pricing and insurance. Updated monthly.',
}

for filename, new_desc in FIXES.items():
    path = os.path.join(OUTPUT, filename)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{new_desc}">',
        html, count=1
    )
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed {filename}: {len(new_desc)} chars")

print("Done.")
