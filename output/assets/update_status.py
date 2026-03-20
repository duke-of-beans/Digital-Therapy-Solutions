import sys, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

p = Path(r'D:\Work\Digital-Therapy-Solutions\STATUS.md')
content = p.read_text(encoding='utf-8')

# Update Last Updated
content = re.sub(r'Last Updated: \S+', 'Last Updated: 2026-03-20', content)

# Mark PS-PLATFORMS-01 complete
content = content.replace(
    '| PS-PLATFORMS-01 | 31 remaining platform review pages | ⬜ QUEUED (blocked: affiliate apps) | — |',
    '| PS-PLATFORMS-01 | 31 review pages + affiliate toggle system | ✅ COMPLETE | TBD |'
)

# Update Reviews count
content = content.replace(
    '### Reviews (3 live / 34 total)',
    '### Reviews (34 live / 34 total) ✅ COMPLETE'
)

# Mark all 31 review pages as checked
slugs = [
    'adhd-online','amwell','bend-health','brightline','brightside','calmerry','cerebral',
    'circle-medical','doctor-on-demand','done-adhd','faithful-counseling','gay-therapy-center',
    'grow-therapy','headspace','headway','inclusive-therapists','klarity','lunajoy',
    'manatee-health','mindful-care','nocd','open-path','our-relationship','our-ritual',
    'pride-counseling','psychology-today','regain','simplepractice','talkiatry',
    'teen-counseling','therapyden'
]

# Replace stub entry
content = content.replace(
    '- [ ] 31 pages — see PS-PLATFORMS-01',
    '- [x] ' + ', '.join(f'{s}-review.html' for s in slugs[:10]) + '\n' +
    '- [x] ' + ', '.join(f'{s}-review.html' for s in slugs[10:20]) + '\n' +
    '- [x] ' + ', '.join(f'{s}-review.html' for s in slugs[20:])
)

# Add PS-PLATFORMS-01 notes section
notes = '''
## PS-PLATFORMS-01 Notes
- 31 new review pages built — all follow betterhelp-review.html structure
- All 34 review pages (including 3 existing) use data-affiliate-status="pending" pending CTA pattern
- assets/activate-affiliate.py ready: py assets/activate-affiliate.py --platform [slug] --url [url]
- .cta-button--pending CSS added to templates/styles.css
- reviews.html: all 34 cards live-linked, 0 stubs
- output/sitemap.xml regenerated: 97 URLs
- Quality gate: 0 failures, 97 pages

'''
content = content.replace('## PS-DESIGN-QA-02 Notes', notes + '## PS-DESIGN-QA-02 Notes')

# Update Open Items
content = content.replace('## Open Items\n- None.', '## Open Items\n- None. Next: PS-DESIGN-01 (MORPH-26 design intelligence pass)')

p.write_text(content, encoding='utf-8')
print('STATUS.md updated')
