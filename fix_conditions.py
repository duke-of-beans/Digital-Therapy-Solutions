"""Add the 4 missing live cards (burnout, social-anxiety, phobias, panic) to conditions.html."""
import re

with open('output/conditions.html', 'r', encoding='utf-8') as f:
    html = f.read()

INSERT_BEFORE = "<!-- STUB: Men's Mental Health -->"

NEW_CARDS = """
                    <!-- LIVE: Burnout -->
                    <div class="hub-card">
                        <div style="font-size:2rem;">&#x1F525;</div>
                        <div class="hub-card__name">Burnout</div>
                        <div class="hub-card__desc">Recognizing and recovering from chronic stress and emotional exhaustion</div>
                        <a href="burnout.html" class="hub-card__cta">Read Guide &rarr;</a>
                    </div>

                    <!-- LIVE: Social Anxiety -->
                    <div class="hub-card">
                        <div style="font-size:2rem;">&#x1F610;</div>
                        <div class="hub-card__name">Social Anxiety</div>
                        <div class="hub-card__desc">CBT-based platforms for social anxiety disorder and fear of judgment</div>
                        <a href="social-anxiety.html" class="hub-card__cta">Read Guide &rarr;</a>
                    </div>

                    <!-- LIVE: Phobias -->
                    <div class="hub-card">
                        <div style="font-size:2rem;">&#x26A0;&#xFE0F;</div>
                        <div class="hub-card__name">Phobias</div>
                        <div class="hub-card__desc">Exposure-based therapy for specific fears and avoidance patterns</div>
                        <a href="phobias.html" class="hub-card__cta">Read Guide &rarr;</a>
                    </div>

                    <!-- LIVE: Panic Disorder -->
                    <div class="hub-card">
                        <div style="font-size:2rem;">&#x1F4A8;</div>
                        <div class="hub-card__name">Panic Disorder</div>
                        <div class="hub-card__desc">Breaking the panic cycle with evidence-based CBT treatment</div>
                        <a href="panic.html" class="hub-card__cta">Read Guide &rarr;</a>
                    </div>

                    """

if INSERT_BEFORE in html:
    html = html.replace(INSERT_BEFORE, NEW_CARDS + INSERT_BEFORE)
    print("Inserted 4 new live cards.")
else:
    print("ERROR: Insert anchor not found!")

# Update section context paragraph
html = re.sub(
    r'<p class="section-context">.*?</p>',
    '<p class="section-context">24 full condition guides live &mdash; expert-written and updated monthly.</p>',
    html,
    count=1
)

with open('output/conditions.html', 'w', encoding='utf-8') as f:
    f.write(html)

live = html.count('class="hub-card"')
stub = html.count('hub-card--stub')
print(f"Live: {live}, Stubs: {stub}, Total: {live + stub}")

hrefs = re.findall(r'href="([^"]+)" class="hub-card__cta"', html)
print(f"\nAll {len(hrefs)} live card hrefs:")
for h in hrefs:
    print(f"  {h}")

missing = [s for s in ['burnout.html','social-anxiety.html','phobias.html','panic.html'] if s not in hrefs]
print(f"\nStill missing: {missing if missing else 'None - all present!'}")
