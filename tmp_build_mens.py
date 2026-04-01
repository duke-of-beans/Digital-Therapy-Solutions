import sys
sys.stdout.reconfigure(encoding='utf-8')

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Therapy for Men's Mental Health — Platforms That Get It | Digital Therapy Solutions</title>
    <meta name="description" content="Find the best online therapy platforms for men's mental health. Expert-reviewed platforms with therapists who understand masculine identity, stress, and stigma. Updated monthly.">
    <link rel="icon" href="../assets/branding/favicon.png" type="image/png">
    <link rel="apple-touch-icon" href="../assets/branding/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600&family=Instrument+Serif:ital@0;1&family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../templates/styles.css">
</head>
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>

    <nav class="site-nav">
        <div class="site-nav__inner">
            <a href="index.html" class="site-nav__brand">
                <img src="../assets/branding/logo-icon.webp" alt="" class="site-nav__brand-icon">
                Digital Therapy Solutions
            </a>
            <button class="site-nav__hamburger" aria-label="Toggle navigation">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
            </button>
            <ul class="site-nav__links">
                <li><a href="index.html">Home</a></li>
                <li><a href="conditions.html">Conditions</a></li>
                <li><a href="reviews.html">Reviews</a></li>
                <li><a href="insurance.html">Insurance</a></li>
                <li><a href="about.html">About</a></li>
            </ul>
        </div>
    </nav>

    <main id="main-content">
    <nav aria-label="Breadcrumb" class="breadcrumb" style="max-width:var(--table-width);margin:0 auto;padding:var(--space-xs) var(--space-md);">
        <a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="conditions.html">Conditions</a> / Men\'s Mental Health
    </nav>

        <!-- HERO -->
        <div class="section-wrapper section-wrapper--hero">
            <div class="hero-visual">
                <img src="../assets/hero.webp" alt="Person at home with laptop during an online therapy session" class="hero-image">
            </div>
            <div class="hero-text">
                <h1>Men\'s mental health doesn\'t get talked about enough. These platforms get it.</h1>
                <p class="hero-subhead"><em>Stoicism isn\'t a treatment plan. Therapists who understand that make all the difference.</em></p>
                <p class="hero-subhead hero-subhead--follow">We reviewed platforms specifically for how well they serve men seeking therapy.</p>
                <div class="trust-row">
                    <span>34+ Platforms Reviewed</span>
                    <span>Expert-Written</span>
                    <span>Updated Monthly</span>
                    <span>No Sponsored Rankings</span>
                </div>
            </div>
        </div>

        <!-- SECTION DIVIDER -->
        <svg class="section-divider" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true"><path d="M0 48h1440V24C1200 42 960 8 720 24S240 42 0 24v24z" fill="#F5F0E8"/></svg>

        <!-- PLATFORM CARDS -->
        <div class="section-wrapper section-wrapper--alt">
            <div class="content-container">
                <h2 class="section-heading">Platforms We Recommend for Men\'s Mental Health</h2>
                <p class="section-context">Each platform below was independently evaluated by the <strong>DTS Research Team</strong> using our 12-point clinical accuracy standard.</p>

                <!-- CARD 1: BetterHelp — Top Pick -->
                <article class="platform-card platform-card--featured reveal">
                    <div class="platform-card__header">
                        <div class="platform-card__logo" style="background:#00796B;color:#fff;font-weight:700;font-size:1.1rem;">
                            <img src="../assets/logos/betterhelp.webp" alt="BetterHelp logo" onerror="this.style.display=\'none\';this.parentElement.style.background=\'#00796B\';this.parentElement.style.color=\'#fff\';this.parentElement.textContent=\'BH\';">
                        </div>
                        <div class="platform-card__identity">
                            <h3 class="platform-card__name">BetterHelp</h3>
                            <p class="platform-card__tagline">Best overall for men &mdash; massive therapist network, easy to switch</p>
                        </div>
                        <div class="platform-card__score">
                            <span class="score-number">4.5</span>
                            <svg class="score-stars" viewBox="0 0 80 16"><polygon points="8,1 10.2,5.5 15.1,6.1 11.5,9.6 12.4,14.5 8,12.1 3.6,14.5 4.5,9.6 0.9,6.1 5.8,5.5" fill="#C4956A"/><polygon points="24,1 26.2,5.5 31.1,6.1 27.5,9.6 28.4,14.5 24,12.1 19.6,14.5 20.5,9.6 16.9,6.1 21.8,5.5" fill="#C4956A"/><polygon points="40,1 42.2,5.5 47.1,6.1 43.5,9.6 44.4,14.5 40,12.1 35.6,14.5 36.5,9.6 32.9,6.1 37.8,5.5" fill="#C4956A"/><polygon points="56,1 58.2,5.5 63.1,6.1 59.5,9.6 60.4,14.5 56,12.1 51.6,14.5 52.5,9.6 48.9,6.1 53.8,5.5" fill="#C4956A"/><polygon points="72,1 74.2,5.5 79.1,6.1 75.5,9.6 76.4,14.5 72,12.1 67.6,14.5 68.5,9.6 64.9,6.1 69.8,5.5" fill="#EDE7DB"/></svg>
                            <span class="rating-badge rating-badge--top">Top Rated</span>
                        </div>
                    </div>
                    <div class="platform-card__body">
                        <p>BetterHelp\'s size works in its favor here. With 30,000+ therapists, men can specifically request someone who works with male clients on traditional masculine norms, identity, or career stress &mdash; and actually find a match. The platform doesn\'t market specifically to men, but the depth of the network means the right therapist exists. Cost is $65&ndash;100/week without insurance.</p>
                    </div>
                    <div class="platform-card__details"><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $65&ndash;100/week</span><span class="detail detail--no-insurance"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M5.5 5.5l5 5"/></svg> No insurance required</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="1.5"/><circle cx="8" cy="8" r="1.5"/></svg> Video</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 4a2 2 0 012-2h1a2 2 0 012 2v7l-2.5 2L2 11V4zM14 4a2 2 0 00-2-2h-1a2 2 0 00-2 2v7l2.5 2L14 11V4z"/></svg> Phone</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3h10a1 1 0 011 1v6a1 1 0 01-1 1H7l-3 3v-3H3a1 1 0 01-1-1V4a1 1 0 011-1z"/></svg> Messaging</span></div>
                    <div class="platform-card__cta">
                        <span class="offer-tag">&#10022; Specify your therapist preferences at signup</span>
                        <a href="#" class="cta-button">Find a Therapist on BetterHelp</a>
                    </div>
                    <div class="platform-card__meta">
                        <span>Editorially reviewed · DTS Research Team</span>
                    </div>
                </article>

                <div class="cards-divider">
                    <span class="cards-divider__label">Also worth considering</span>
                </div>

                <!-- CARD 2: Talkspace -->
                <article class="platform-card reveal reveal-delay-1" data-rank="2">
                    <div class="platform-card__header">
                        <div class="platform-card__logo" style="background:#009688;color:#fff;font-weight:700;font-size:1.1rem;">
                            <img src="../assets/logos/talkspace.webp" alt="Talkspace logo" onerror="this.style.display=\'none\';this.parentElement.style.background=\'#009688\';this.parentElement.style.color=\'#fff\';this.parentElement.textContent=\'TS\';">
                        </div>
                        <div class="platform-card__identity">
                            <h3 class="platform-card__name">Talkspace</h3>
                            <p class="platform-card__tagline">Best if you have insurance &mdash; in-network with most major plans</p>
                        </div>
                        <div class="platform-card__score">
                            <span class="score-number">4.3</span>
                            <svg class="score-stars" viewBox="0 0 80 16"><polygon points="8,1 10.2,5.5 15.1,6.1 11.5,9.6 12.4,14.5 8,12.1 3.6,14.5 4.5,9.6 0.9,6.1 5.8,5.5" fill="#C4956A"/><polygon points="24,1 26.2,5.5 31.1,6.1 27.5,9.6 28.4,14.5 24,12.1 19.6,14.5 20.5,9.6 16.9,6.1 21.8,5.5" fill="#C4956A"/><polygon points="40,1 42.2,5.5 47.1,6.1 43.5,9.6 44.4,14.5 40,12.1 35.6,14.5 36.5,9.6 32.9,6.1 37.8,5.5" fill="#C4956A"/><polygon points="56,1 58.2,5.5 63.1,6.1 59.5,9.6 60.4,14.5 56,12.1 51.6,14.5 52.5,9.6 48.9,6.1 53.8,5.5" fill="#C4956A"/><polygon points="72,1 74.2,5.5 79.1,6.1 75.5,9.6 76.4,14.5 72,12.1 67.6,14.5 68.5,9.6 64.9,6.1 69.8,5.5" fill="#EDE7DB"/></svg>
                            <span class="rating-badge rating-badge--recommended">Recommended</span>
                        </div>
                    </div>
                    <div class="platform-card__body">
                        <p>If cost is the barrier keeping men from therapy, Talkspace removes it for insured clients. In-network with Aetna, Cigna, and others, bringing sessions down to $10&ndash;50 copay range. The async messaging format also appeals to men who prefer to process in writing before speaking. Psychiatry available if medication is part of the picture.</p>
                    </div>
                    <div class="platform-card__details"><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $10&ndash;50/session w/ insurance</span><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $69&ndash;109/week self-pay</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="1.5"/><circle cx="8" cy="8" r="1.5"/></svg> Video</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="2"/><path d="M2 5l6 4 6-4"/></svg> Messaging</span></div>
                    <div class="platform-card__cta">
                        <span class="offer-tag">&#10022; Check your insurance coverage at signup</span>
                        <a href="#" class="cta-button">Check Coverage on Talkspace</a>
                    </div>
                    <div class="platform-card__meta">
                        <span>Editorially reviewed · DTS Research Team</span>
                    </div>
                </article>

                <!-- CARD 3: Grow Therapy -->
                <article class="platform-card reveal reveal-delay-2" data-rank="3">
                    <div class="platform-card__header">
                        <div class="platform-card__logo" style="background:#2E7D32;color:#fff;font-weight:700;font-size:1.1rem;">
                            <img src="../assets/logos/grow-therapy.webp" alt="Grow Therapy logo" onerror="this.style.display=\'none\';this.parentElement.style.background=\'#2E7D32\';this.parentElement.style.color=\'#fff\';this.parentElement.textContent=\'GT\';">
                        </div>
                        <div class="platform-card__identity">
                            <h3 class="platform-card__name">Grow Therapy</h3>
                            <p class="platform-card__tagline">Best for insurance + therapist choice &mdash; browse real profiles before booking</p>
                        </div>
                        <div class="platform-card__score">
                            <span class="score-number">4.2</span>
                            <svg class="score-stars" viewBox="0 0 80 16"><polygon points="8,1 10.2,5.5 15.1,6.1 11.5,9.6 12.4,14.5 8,12.1 3.6,14.5 4.5,9.6 0.9,6.1 5.8,5.5" fill="#C4956A"/><polygon points="24,1 26.2,5.5 31.1,6.1 27.5,9.6 28.4,14.5 24,12.1 19.6,14.5 20.5,9.6 16.9,6.1 21.8,5.5" fill="#C4956A"/><polygon points="40,1 42.2,5.5 47.1,6.1 43.5,9.6 44.4,14.5 40,12.1 35.6,14.5 36.5,9.6 32.9,6.1 37.8,5.5" fill="#C4956A"/><polygon points="56,1 58.2,5.5 63.1,6.1 59.5,9.6 60.4,14.5 56,12.1 51.6,14.5 52.5,9.6 48.9,6.1 53.8,5.5" fill="#C4956A"/><polygon points="72,1 74.2,5.5 79.1,6.1 75.5,9.6 76.4,14.5 72,12.1 67.6,14.5 68.5,9.6 64.9,6.1 69.8,5.5" fill="#EDE7DB"/></svg>
                            <span class="rating-badge rating-badge--recommended">Recommended</span>
                        </div>
                    </div>
                    <div class="platform-card__body">
                        <p>Grow Therapy lets you browse actual therapist profiles, read bios, and see specialties before committing &mdash; which matters when you\'re looking for someone who specifically works with men on anger, identity, or relationship issues. In-network with most major insurers. You book directly, no algorithm matching.</p>
                    </div>
                    <div class="platform-card__details"><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> Varies by insurance</span><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> Self-pay $100&ndash;200/session</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="1.5"/><circle cx="8" cy="8" r="1.5"/></svg> Video</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 8 Q4 4 8 4 Q12 4 12 8 L12 12 Q12 14 10 14 L6 14 Q4 14 4 12Z"/></svg> In-person options</span></div>
                    <div class="platform-card__cta">
                        <span class="offer-tag">&#10022; Browse therapist profiles &mdash; no commitment to book</span>
                        <a href="#" class="cta-button">Browse Therapists on Grow Therapy</a>
                    </div>
                    <div class="platform-card__meta">
                        <span>Editorially reviewed · DTS Research Team</span>
                    </div>
                </article>
            </div>
        </div>

        <!-- SECTION DIVIDER -->
        <svg class="section-divider section-divider--flip" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0h1440v24C1200 6 960 40 720 24S240 6 0 24V0z" fill="#F5F0E8"/></svg>

        <!-- GENTLE FORKS -->
        <div class="section-wrapper section-wrapper--accent">
            <div class="content-container forks-section">
                <div class="forks-layout reveal">
                    <div class="forks-text">
                        <h3 class="forks-heading"><em>Also worth reading</em></h3>
                        <div class="forks-links">
                            <a href="stress.html" class="fork-link">Online therapy for stress <span>&rarr;</span></a>
                            <a href="anger.html" class="fork-link">Online therapy for anger <span>&rarr;</span></a>
                            <a href="addiction.html" class="fork-link">Online therapy for addiction <span>&rarr;</span></a>
                            <a href="conditions.html" class="fork-link">All conditions <span>&rarr;</span></a>
                        </div>
                    </div>
                    <div class="forks-image">
                        <img src="../assets/video-call-earbuds.webp" alt="Man on couch with earbuds during an online therapy session" class="forks-image__img">
                    </div>
                </div>
            </div>
        </div>

        <!-- REVIEWER BIO -->
        <div class="section-wrapper section-wrapper--alt">
            <div class="content-container">
                <h2 class="section-heading">About Our Editorial Process</h2>
                <div class="reviewer-card reveal">
                    <div class="reviewer-card__avatar">DTS</div>
                    <div class="reviewer-card__content">
                        <h4 class="reviewer-card__name">DTS Research Team <span class="credential-badge">Editorial</span></h4>
                        <p class="reviewer-card__specialties">Men\'s Mental Health &middot; Identity &middot; Anxiety &middot; CBT</p>
                        <div class="reviewer-card__bio">
                            Every recommendation on this page was independently researched, cross-referenced against current clinical literature, and verified for accuracy by the DTS editorial team. Platforms are re-evaluated monthly.</div>
                        <a href="#" class="link-subtle">Read our editorial policy &rarr;</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- DISCLAIMERS -->
        <div class="section-wrapper section-wrapper--muted" id="disclosures">
            <div class="content-container">
                <div class="disclaimers">
                    <p>We\'re not therapists &mdash; we\'re researchers who spent hundreds of hours comparing these platforms so you don\'t have to. Some links on this page are affiliate links, meaning we may earn a commission if you sign up. This never influences which platforms we recommend. For professional guidance, please consult a licensed mental health provider.</p>
                    <p>Pricing is based on our most recent research and may vary. Insurance coverage depends on your specific plan. We update monthly, but confirm directly with the platform before signing up.</p>
                </div>
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="site-footer__inner">
            <div>
                <h3>About Digital Therapy Solutions</h3>
                <p>Independent reviews of online therapy platforms. Expert-written, regularly updated, no sponsored rankings.</p>
            </div>
            <div>
                <h3>Quick Links</h3>
                <ul><li><a href="index.html">Home</a></li><li><a href="betterhelp-review.html">Platform Reviews</a></li><li><a href="aetna.html">Insurance Guide</a></li><li><a href="about.html">About Us</a></li></ul>
            </div>
            <div>
                <h3>Resources</h3>
                <ul><li><a href="editorial-policy.html">Editorial Policy</a></li><li><a href="affiliate-disclosure.html">Affiliate Disclosure</a></li><li><a href="privacy-policy.html">Privacy Policy</a></li></ul>
            </div>
        </div>
        <div class="site-footer__crisis"><span class="crisis-alert">In crisis?</span> Call or text <a href="tel:988">988</a> &middot; Text HOME to <a href="sms:741741">741741</a> &middot; Emergency: <a href="tel:911">911</a></div>
        <div class="site-footer__bottom">&copy; 2026 Digital Therapy Solutions. All rights reserved. | <a href="privacy-policy.html">Privacy</a> | <a href="affiliate-disclosure.html">Disclosures</a></div>
    </footer>

    <script>
        const hamburger = document.querySelector(\'.site-nav__hamburger\');
        const navLinks = document.querySelector(\'.site-nav__links\');
        if (hamburger && navLinks) {
            hamburger.addEventListener(\'click\', () => navLinks.classList.toggle(\'open\'));
        }
        const reveals = document.querySelectorAll(\'.reveal\');
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add(\'visible\');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15, rootMargin: \'0px 0px -40px 0px\' });
        reveals.forEach(el => revealObserver.observe(el));
        const btt = document.createElement(\'button\');
        btt.className = \'back-to-top\';
        btt.innerHTML = \'&uarr;\';
        btt.setAttribute(\'aria-label\', \'Back to top\');
        document.body.appendChild(btt);
        window.addEventListener(\'scroll\', () => {
            btt.classList.toggle(\'visible\', window.scrollY > 600);
        });
        btt.addEventListener(\'click\', () => {
            window.scrollTo({ top: 0, behavior: \'smooth\' });
        });
    </script>
</body>
</html>'''

with open(r'D:\Work\Digital-Therapy-Solutions\output\mens-mental-health.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('mens-mental-health.html written OK')
