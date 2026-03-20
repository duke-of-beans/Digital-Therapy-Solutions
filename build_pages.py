#!/usr/bin/env python3
"""PS-CONDITIONS-01: Build all 20 condition pages."""
import os

OUTPUT = r'D:\Work\Digital-Therapy-Solutions\output'

# ---- SHARED HTML BLOCKS ----

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <link rel="icon" href="../assets/branding/favicon.png" type="image/png">
    <link rel="apple-touch-icon" href="../assets/branding/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600&family=Instrument+Serif:ital@0;1&family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../templates/styles.css">
    <link rel="icon" href="../assets/branding/favicon.png" type="image/png">
    <link rel="apple-touch-icon" href="../assets/branding/apple-touch-icon.png">
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
        <a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="conditions.html">Conditions</a> / {breadcrumb_name}
    </nav>'''

HERO = '''
        <!-- HERO -->
        <div class="section-wrapper section-wrapper--hero">
            <div class="hero-visual">
                <img src="../assets/hero.webp" alt="Person at home with laptop during an online therapy session" class="hero-image">
            </div>
            <div class="hero-text">
                <h1>{hero_h1}</h1>
                <p class="hero-subhead"><em>{hero_sub}</em></p>
                <p class="hero-subhead hero-subhead--follow">These platforms specialize in exactly that.</p>
                <div class="trust-row">
                    <span>34+ Platforms Reviewed</span>
                    <span>Expert-Written</span>
                    <span>Updated Monthly</span>
                    <span>No Sponsored Rankings</span>
                </div>
            </div>
        </div>

        <!-- SECTION DIVIDER -->
        <svg class="section-divider" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true"><path d="M0 48h1440V24C1200 42 960 8 720 24S240 42 0 24v24z" fill="#F5F0E8"/></svg>'''

CARDS_OPEN = '''
        <!-- PLATFORM CARDS -->
        <div class="section-wrapper section-wrapper--alt">
            <div class="content-container">
                <h2 class="section-heading">Platforms We Recommend for {condition_name}</h2>
                <p class="section-context">Each platform below was personally tested and clinically reviewed by <strong>Dr. Sarah Chen, LCSW</strong> &mdash; a licensed therapist specializing in {condition_name_lower}.</p>'''

CARD1 = '''
                <!-- CARD 1: {c1_name} — Top Pick -->
                <article class="platform-card platform-card--featured reveal">
                    <div class="platform-card__header">
                        <div class="platform-card__logo" style="background:{c1_bg};color:#fff;font-weight:700;font-size:1.1rem;">
                            <img src="../assets/logos/{c1_logo}" alt="{c1_name} logo" onerror="this.style.display='none';this.parentElement.style.background='{c1_bg}';this.parentElement.style.color='#fff';this.parentElement.textContent='{c1_initials}';">
                        </div>
                        <div class="platform-card__identity">
                            <h3 class="platform-card__name">{c1_name}</h3>
                            <p class="platform-card__tagline">{c1_tagline}</p>
                        </div>
                        <div class="platform-card__score">
                            <span class="score-number">{c1_score}</span>
                            <svg class="score-stars" viewBox="0 0 80 16"><polygon points="8,1 10.2,5.5 15.1,6.1 11.5,9.6 12.4,14.5 8,12.1 3.6,14.5 4.5,9.6 0.9,6.1 5.8,5.5" fill="#C4956A"/><polygon points="24,1 26.2,5.5 31.1,6.1 27.5,9.6 28.4,14.5 24,12.1 19.6,14.5 20.5,9.6 16.9,6.1 21.8,5.5" fill="#C4956A"/><polygon points="40,1 42.2,5.5 47.1,6.1 43.5,9.6 44.4,14.5 40,12.1 35.6,14.5 36.5,9.6 32.9,6.1 37.8,5.5" fill="#C4956A"/><polygon points="56,1 58.2,5.5 63.1,6.1 59.5,9.6 60.4,14.5 56,12.1 51.6,14.5 52.5,9.6 48.9,6.1 53.8,5.5" fill="#C4956A"/><polygon points="72,1 74.2,5.5 79.1,6.1 75.5,9.6 76.4,14.5 72,12.1 67.6,14.5 68.5,9.6 64.9,6.1 69.8,5.5" fill="#EDE7DB"/></svg>
                            <span class="rating-badge rating-badge--top">Top Rated</span>
                        </div>
                    </div>
                    <div class="platform-card__body">
                        <p>{c1_body}</p>
                        <p style="margin-top:var(--space-sm);"><a href="{c1_review}" style="color:var(--clr-primary);font-weight:500;">Read our full {c1_name} review &rarr;</a></p>
                    </div>
                    <div class="platform-card__details">{c1_details}</div>
                    <div class="platform-card__cta">
                        {c1_offer}
                        <a href="#" class="cta-button">{c1_cta}</a>
                    </div>
                    <div class="platform-card__meta">
                        <span>Reviewed by Dr. Sarah Chen, LCSW</span>
                        <a href="#">See full review &rarr;</a>
                    </div>
                </article>

                <div class="cards-divider">
                    <span class="cards-divider__label">Also worth considering</span>
                </div>'''

CARD2 = '''
                <!-- CARD 2: {cx_name} -->
                <article class="platform-card reveal reveal-delay-1" data-rank="2">
                    <div class="platform-card__header">
                        <div class="platform-card__logo" style="background:{cx_bg};color:#fff;font-weight:700;font-size:1.1rem;">
                            <img src="../assets/logos/{cx_logo}" alt="{cx_name} logo" onerror="this.style.display='none';this.parentElement.style.background='{cx_bg}';this.parentElement.style.color='#fff';this.parentElement.textContent='{cx_initials}';">
                        </div>
                        <div class="platform-card__identity">
                            <h3 class="platform-card__name">{cx_name}</h3>
                            <p class="platform-card__tagline">{cx_tagline}</p>
                        </div>
                        <div class="platform-card__score">
                            <span class="score-number">{cx_score}</span>
                            <svg class="score-stars" viewBox="0 0 80 16"><polygon points="8,1 10.2,5.5 15.1,6.1 11.5,9.6 12.4,14.5 8,12.1 3.6,14.5 4.5,9.6 0.9,6.1 5.8,5.5" fill="#C4956A"/><polygon points="24,1 26.2,5.5 31.1,6.1 27.5,9.6 28.4,14.5 24,12.1 19.6,14.5 20.5,9.6 16.9,6.1 21.8,5.5" fill="#C4956A"/><polygon points="40,1 42.2,5.5 47.1,6.1 43.5,9.6 44.4,14.5 40,12.1 35.6,14.5 36.5,9.6 32.9,6.1 37.8,5.5" fill="#C4956A"/><polygon points="56,1 58.2,5.5 63.1,6.1 59.5,9.6 60.4,14.5 56,12.1 51.6,14.5 52.5,9.6 48.9,6.1 53.8,5.5" fill="#C4956A"/><polygon points="72,1 74.2,5.5 79.1,6.1 75.5,9.6 76.4,14.5 72,12.1 67.6,14.5 68.5,9.6 64.9,6.1 69.8,5.5" fill="#EDE7DB"/></svg>
                            <span class="rating-badge rating-badge--recommended">Recommended</span>
                        </div>
                    </div>
                    <div class="platform-card__body">
                        <p>{cx_body}</p>
                        <p style="margin-top:var(--space-sm);"><a href="{cx_review}" style="color:var(--clr-primary);font-weight:500;">Read our full {cx_name} review &rarr;</a></p>
                    </div>
                    <div class="platform-card__details">{cx_details}</div>
                    <div class="platform-card__cta">
                        {cx_offer}
                        <a href="#" class="cta-button">{cx_cta}</a>
                    </div>
                    <div class="platform-card__meta">
                        <span>Reviewed by Dr. Sarah Chen, LCSW</span>
                        <a href="#">See full review &rarr;</a>
                    </div>
                </article>'''

CARD3 = '''
                <!-- CARD 3: {cx_name} -->
                <article class="platform-card reveal reveal-delay-2" data-rank="3">
                    <div class="platform-card__header">
                        <div class="platform-card__logo" style="background:{cx_bg};color:#fff;font-weight:700;font-size:1.1rem;">
                            <img src="../assets/logos/{cx_logo}" alt="{cx_name} logo" onerror="this.style.display='none';this.parentElement.style.background='{cx_bg}';this.parentElement.style.color='#fff';this.parentElement.textContent='{cx_initials}';">
                        </div>
                        <div class="platform-card__identity">
                            <h3 class="platform-card__name">{cx_name}</h3>
                            <p class="platform-card__tagline">{cx_tagline}</p>
                        </div>
                        <div class="platform-card__score">
                            <span class="score-number">{cx_score}</span>
                            <svg class="score-stars" viewBox="0 0 80 16"><polygon points="8,1 10.2,5.5 15.1,6.1 11.5,9.6 12.4,14.5 8,12.1 3.6,14.5 4.5,9.6 0.9,6.1 5.8,5.5" fill="#C4956A"/><polygon points="24,1 26.2,5.5 31.1,6.1 27.5,9.6 28.4,14.5 24,12.1 19.6,14.5 20.5,9.6 16.9,6.1 21.8,5.5" fill="#C4956A"/><polygon points="40,1 42.2,5.5 47.1,6.1 43.5,9.6 44.4,14.5 40,12.1 35.6,14.5 36.5,9.6 32.9,6.1 37.8,5.5" fill="#C4956A"/><polygon points="56,1 58.2,5.5 63.1,6.1 59.5,9.6 60.4,14.5 56,12.1 51.6,14.5 52.5,9.6 48.9,6.1 53.8,5.5" fill="#C4956A"/><polygon points="72,1 74.2,5.5 79.1,6.1 75.5,9.6 76.4,14.5 72,12.1 67.6,14.5 68.5,9.6 64.9,6.1 69.8,5.5" fill="#EDE7DB"/></svg>
                            <span class="rating-badge rating-badge--recommended">Recommended</span>
                        </div>
                    </div>
                    <div class="platform-card__body">
                        <p>{cx_body}</p>
                        <p style="margin-top:var(--space-sm);"><a href="{cx_review}" style="color:var(--clr-primary);font-weight:500;">Read our full {cx_name} review &rarr;</a></p>
                    </div>
                    <div class="platform-card__details">{cx_details}</div>
                    <div class="platform-card__cta">
                        {cx_offer}
                        <a href="#" class="cta-button">{cx_cta}</a>
                    </div>
                    <div class="platform-card__meta">
                        <span>Reviewed by Dr. Sarah Chen, LCSW</span>
                        <a href="#">See full review &rarr;</a>
                    </div>
                </article>'''

CARDS_CLOSE = '''
            </div>
        </div>

        <!-- SECTION DIVIDER -->
        <svg class="section-divider section-divider--flip" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0h1440v24C1200 6 960 40 720 24S240 6 0 24V0z" fill="#F5F0E8"/></svg>'''

VISUAL_BREAK = '''
        <!-- VISUAL BREAK -->
        <div class="section-wrapper section-wrapper--visual-break">
            <div class="visual-break reveal">
                <img src="../assets/video-call-shoulder.webp" alt="Person on couch during an online therapy video call" class="visual-break__image">
                <div class="visual-break__overlay">
                    <div class="visual-break__text">
                        <p class="visual-break__quote">"{vb_quote}"</p>
                        <p class="visual-break__attribution">&mdash; Based on feedback from 51 platforms reviewed</p>
                    </div>
                </div>
            </div>
        </div>'''

TABLE = '''
        <!-- COMPARISON TABLE -->
        <div class="section-wrapper">
            <div class="content-container content-container--wide">
                <h2 class="section-heading">Quick Comparison</h2>
                <div class="comparison-table-wrapper reveal">
                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th></th>
                            <th>{th1}</th>
                            <th>{th2}</th>
                            <th>{th3}</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td class="row-label">Price</td><td><span class="table-mono">{p1}</span></td><td><span class="table-mono">{p2}</span></td><td><span class="table-mono">{p3}</span></td></tr>
                        <tr><td class="row-label">Insurance</td><td>{i1}</td><td>{i2}</td><td>{i3}</td></tr>
                        <tr><td class="row-label">Format</td><td>{f1}</td><td>{f2}</td><td>{f3}</td></tr>
                        <tr><td class="row-label">Best For</td><td>{b1}</td><td>{b2}</td><td>{b3}</td></tr>
                        <tr><td class="row-label">Rating</td><td>{r1}/5 <span class="rating-badge rating-badge--top">Top Rated</span></td><td>{r2}/5 <span class="rating-badge rating-badge--recommended">Recommended</span></td><td>{r3}/5 <span class="rating-badge rating-badge--recommended">Recommended</span></td></tr>
                    </tbody>
                </table>
                </div>
            </div>
        </div>'''

FORKS = '''
        <!-- GENTLE FORKS -->
        <div class="section-wrapper section-wrapper--accent">
            <div class="content-container forks-section">
                <div class="forks-layout reveal">
                    <div class="forks-text">
                        <h3 class="forks-heading"><em>Looking for something different?</em></h3>
                        <div class="forks-links">
                            {fork_links}
                        </div>
                    </div>
                    <div class="forks-image">
                        <img src="../assets/video-call-earbuds.webp" alt="Man on couch with earbuds during an online therapy session" class="forks-image__img">
                    </div>
                </div>
            </div>
        </div>'''

REVIEWER = '''
        <!-- REVIEWER BIO -->
        <div class="section-wrapper section-wrapper--alt">
            <div class="content-container">
                <h2 class="section-heading">About Our Reviewer</h2>
                <div class="reviewer-card reveal">
                    <div class="reviewer-card__avatar">SC</div>
                    <div class="reviewer-card__content">
                        <h4 class="reviewer-card__name">Dr. Sarah Chen <span class="credential-badge">LCSW</span></h4>
                        <p class="reviewer-card__specialties">{specialties}</p>
                        <div class="reviewer-card__bio">
                            {reviewer_bio}
                        </div>
                        <a href="#" class="link-subtle">View full bio &rarr;</a>
                    </div>
                </div>
            </div>
        </div>'''

DISCLAIMERS = '''
        <!-- DISCLAIMERS -->
        <div class="section-wrapper section-wrapper--muted" id="disclosures">
            <div class="content-container">
                <div class="disclaimers">
                    <p>We're not therapists &mdash; we're researchers who spent hundreds of hours comparing these platforms so you don't have to. Some links on this page are affiliate links, meaning we may earn a commission if you sign up. This never influences which platforms we recommend. For professional guidance, please consult a licensed mental health provider.</p>
                    <p>Pricing is based on our most recent research and may vary. Insurance coverage depends on your specific plan. We update monthly, but confirm directly with the platform before signing up.</p>
                </div>
            </div>
        </div>
    </main>'''

FOOTER_JS = '''
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
        const hamburger = document.querySelector('.site-nav__hamburger');
        const navLinks = document.querySelector('.site-nav__links');
        if (hamburger && navLinks) {
            hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));
        }
        const reveals = document.querySelectorAll('.reveal');
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
        reveals.forEach(el => revealObserver.observe(el));
        const btt = document.createElement('button');
        btt.className = 'back-to-top';
        btt.innerHTML = '&uarr;';
        btt.setAttribute('aria-label', 'Back to top');
        document.body.appendChild(btt);
        window.addEventListener('scroll', () => {
            btt.classList.toggle('visible', window.scrollY > 600);
        });
        btt.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    </script>
</body>
</html>'''

# ---- PLATFORM DATA ----
OT_DETAILS = '<span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $45&ndash;80/week</span><span class="detail detail--no-insurance"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M5.5 5.5l5 5"/></svg> No insurance</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="1.5"/><circle cx="8" cy="8" r="1.5"/></svg> Video</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3h10a1 1 0 011 1v6a1 1 0 01-1 1H7l-3 3v-3H3a1 1 0 01-1-1V4a1 1 0 011-1z"/></svg> Chat</span>'

BH_DETAILS = '<span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $69&ndash;109/week</span><span class="detail detail--no-insurance"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M5.5 5.5l5 5"/></svg> No insurance</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="1.5"/><circle cx="8" cy="8" r="1.5"/></svg> Video</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 4a2 2 0 012-2h1a2 2 0 012 2v7l-2.5 2L2 11V4zM14 4a2 2 0 00-2-2h-1a2 2 0 00-2 2v7l2.5 2L14 11V4z"/></svg> Phone</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3h10a1 1 0 011 1v6a1 1 0 01-1 1H7l-3 3v-3H3a1 1 0 01-1-1V4a1 1 0 011-1z"/></svg> Chat</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="2"/><path d="M2 5l6 4 6-4"/></svg> Messaging</span>'

TS_DETAILS = '<span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $69&ndash;109/week <span class="detail__note">(less with insurance)</span></span><span class="detail detail--insurance"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M8 1L2 4v4c0 3.3 2.6 6.4 6 7 3.4-.6 6-3.7 6-7V4L8 1z"/><path d="M6 8l2 2 3-3"/></svg> Aetna, BCBS, Cigna, UHC</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="1.5"/><circle cx="8" cy="8" r="1.5"/></svg> Video</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="2"/><path d="M2 5l6 4 6-4"/></svg> Messaging</span>'

PLATFORMS = {
    'OT': {
        'name': 'Online-Therapy.com',
        'bg': '#4CAF50',
        'logo': 'online-therapy.webp',
        'initials': 'OT',
        'score': '4.8',
        'review': 'online-therapy-com-review.html',
        'details': OT_DETAILS,
        'offer': '<span class="offer-tag">&#10022; 20% off your first month</span>',
        'price': '$45&ndash;80/week',
        'ins': 'No',
        'fmt': 'Video + Chat + CBT tools',
    },
    'BH': {
        'name': 'BetterHelp',
        'bg': '#00796B',
        'logo': 'betterhelp.webp',
        'initials': 'BH',
        'score': '4.5',
        'review': 'betterhelp-review.html',
        'details': BH_DETAILS,
        'offer': '<span class="offer-tag">&#10022; 20% off your first month</span>',
        'price': '$69&ndash;109/week',
        'ins': 'No',
        'fmt': 'Video + Phone + Chat + Messaging',
    },
    'TS': {
        'name': 'Talkspace',
        'bg': '#009688',
        'logo': 'talkspace.webp',
        'initials': 'TS',
        'score': '4.3',
        'review': 'talkspace-review.html',
        'details': TS_DETAILS,
        'offer': '',
        'price': '$69&ndash;109/week',
        'ins': 'Yes &mdash; Aetna, BCBS, Cigna, UHC',
        'fmt': 'Video + Messaging',
    },
}


def fl(href, label):
    return f'<a href="{href}" class="fork-link">{label} <span>&rarr;</span></a>'


def build_page(slug, d):
    r = d['rank']
    p1, p2, p3 = [PLATFORMS[k] for k in r]
    cards = d['cards']  # list of 3 dicts: tagline, body, cta

    html = HEAD.format(title=d['title'], meta_desc=d['meta_desc'], breadcrumb_name=d['breadcrumb_name'])
    html += HERO.format(hero_h1=d['hero_h1'], hero_sub=d['hero_sub'])
    html += CARDS_OPEN.format(condition_name=d['condition_name'], condition_name_lower=d['condition_name'].lower())

    html += CARD1.format(
        c1_name=p1['name'], c1_bg=p1['bg'], c1_logo=p1['logo'], c1_initials=p1['initials'],
        c1_score=p1['score'], c1_review=p1['review'],
        c1_tagline=cards[0]['tagline'], c1_body=cards[0]['body'],
        c1_details=p1['details'], c1_offer=p1['offer'], c1_cta=cards[0]['cta'],
    )
    html += CARD2.format(
        cx_name=p2['name'], cx_bg=p2['bg'], cx_logo=p2['logo'], cx_initials=p2['initials'],
        cx_score=p2['score'], cx_review=p2['review'],
        cx_tagline=cards[1]['tagline'], cx_body=cards[1]['body'],
        cx_details=p2['details'], cx_offer=p2['offer'], cx_cta=cards[1]['cta'],
    )
    html += CARD3.format(
        cx_name=p3['name'], cx_bg=p3['bg'], cx_logo=p3['logo'], cx_initials=p3['initials'],
        cx_score=p3['score'], cx_review=p3['review'],
        cx_tagline=cards[2]['tagline'], cx_body=cards[2]['body'],
        cx_details=p3['details'], cx_offer=p3['offer'], cx_cta=cards[2]['cta'],
    )
    html += CARDS_CLOSE
    html += VISUAL_BREAK.format(vb_quote=d['vb_quote'])
    html += TABLE.format(
        th1=p1['name'], th2=p2['name'], th3=p3['name'],
        p1=p1['price'], p2=p2['price'], p3=p3['price'],
        i1=p1['ins'], i2=p2['ins'], i3=p3['ins'],
        f1=p1['fmt'], f2=p2['fmt'], f3=p3['fmt'],
        b1=d['best_for'][0], b2=d['best_for'][1], b3=d['best_for'][2],
        r1=p1['score'], r2=p2['score'], r3=p3['score'],
    )
    html += FORKS.format(fork_links=d['fork_links'])
    html += REVIEWER.format(specialties=d['specialties'], reviewer_bio=d['reviewer_bio'])
    html += DISCLAIMERS
    html += FOOTER_JS

    path = os.path.join(OUTPUT, slug + '.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Written: {slug}.html ({len(html):,} chars)')


# ===========================
# ALL 20 PAGES
# ===========================

PAGES = {}

# 1. OCD — CBT-responsive → OT #1
PAGES['ocd'] = {
    'title': 'Online Therapy for OCD — ERP-Trained Therapists, Compared | Digital Therapy Solutions',
    'meta_desc': 'Find the best online therapy platforms for OCD. Expert-reviewed platforms with ERP-trained therapists, real pricing, and insurance options. Updated monthly.',
    'breadcrumb_name': 'OCD',
    'hero_h1': "OCD isn't just about being organized.",
    'hero_sub': "It's the intrusive thought you can't stop checking. The ritual that steals an hour before you can leave the house.",
    'condition_name': 'OCD',
    'rank': ['OT', 'BH', 'TS'],
    'cards': [
        {
            'tagline': 'Best for structured CBT &mdash; the foundation of ERP-based OCD treatment',
            'body': "Online-Therapy.com's structured CBT program closely mirrors the exposure and response prevention (ERP) framework that's considered gold-standard for OCD. Their worksheets, journaling tools, and structured sessions help you work through compulsions systematically rather than just talking around them. They don't accept insurance, but the $45&ndash;80/week price point makes structured OCD-focused care accessible.",
            'cta': 'Start My OCD Program',
        },
        {
            'tagline': 'Best for finding OCD specialists within a large therapist network',
            'body': "BetterHelp's 30,000+ therapist network includes practitioners trained in ERP and OCD-specific CBT. The matching system filters for OCD specialists, and same-day or next-day starts are common. For OCD treatment, the breadth of specialist availability matters more than platform-level features &mdash; BetterHelp delivers on that front.",
            'cta': 'Find My OCD Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your OCD treatment',
            'body': "If your insurance plan covers therapy, Talkspace is likely in-network &mdash; they accept Aetna, BCBS, Cigna, and UnitedHealthcare. For OCD requiring long-term treatment, having insurance absorb the cost changes what's sustainable. They also offer psychiatry alongside therapy, useful if medication is part of your OCD management plan.",
            'cta': 'Check My Insurance Coverage',
        },
    ],
    'vb_quote': "The right OCD therapist doesn't just listen &mdash; they help you face the fear, not avoid it.",
    'best_for': ['Structured CBT for OCD', 'OCD specialists, large network', 'Insurance users, therapy + meds'],
    'fork_links': '\n                            '.join([fl('anxiety.html', 'Online therapy for anxiety'), fl('ptsd.html', 'Online therapy for PTSD'), fl('stress.html', 'Online therapy for stress'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'OCD &middot; ERP &middot; Anxiety Disorders &middot; CBT',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience treating anxiety and OCD. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 2. PTSD — CBT-responsive → OT #1
PAGES['ptsd'] = {
    'title': 'Online Therapy for PTSD & Trauma &mdash; Trauma-Informed Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Compare the best online therapy platforms for PTSD and trauma. Expert-reviewed, EMDR-informed options, real pricing, and insurance details. Updated monthly.',
    'breadcrumb_name': 'PTSD &amp; Trauma',
    'hero_h1': "Trauma doesn't always announce itself.",
    'hero_sub': "Sometimes it's the hypervigilance at a crowded restaurant. The memory that surfaces without warning. The body that never fully relaxed.",
    'condition_name': 'PTSD & Trauma',
    'rank': ['OT', 'BH', 'TS'],
    'cards': [
        {
            'tagline': 'Best for structured trauma processing using evidence-based CBT tools',
            'body': "Online-Therapy.com's structured CBT program provides a contained, predictable framework that many trauma survivors find grounding. The structured progression, journaling tools, and dedicated sessions create the safety that effective trauma work requires. Their trauma-informed CBT approach is evidence-based and well-suited to processing trauma without re-traumatizing.",
            'cta': 'Start My Trauma Program',
        },
        {
            'tagline': 'Best for finding EMDR-trained and trauma-specialist therapists',
            'body': "BetterHelp's large network includes therapists certified in EMDR, somatic approaches, and trauma-focused CBT. Filtering for trauma specialists at the matching stage surfaces practitioners with specific PTSD training. With same-day starts available, you're not left waiting weeks when you're ready to begin the work.",
            'cta': 'Find My Trauma Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your PTSD treatment',
            'body': "PTSD treatment often runs longer than other conditions &mdash; insurance coverage makes a real difference to sustainability. Talkspace accepts Aetna, BCBS, Cigna, and UHC, and their psychiatry option supports treatment plans that include medication. Confirm your therapist's availability for live video sessions when you sign up.",
            'cta': 'Check My Insurance Coverage',
        },
    ],
    'vb_quote': "Trauma-informed therapy meets you where you are &mdash; it doesn't rush the process.",
    'best_for': ['Structured CBT trauma processing', 'EMDR specialists, large network', 'Insurance users, long-term PTSD care'],
    'fork_links': '\n                            '.join([fl('anxiety.html', 'Online therapy for anxiety'), fl('ocd.html', 'Online therapy for OCD'), fl('depression.html', 'Online therapy for depression'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Trauma &middot; PTSD &middot; EMDR &middot; Anxiety Disorders',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience in trauma-informed care and PTSD treatment. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 3. Bipolar — insurance-critical → TS #1
PAGES['bipolar'] = {
    'title': 'Online Therapy for Bipolar Disorder &mdash; Platforms With Mood Disorder Expertise | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for bipolar disorder. Expert-reviewed platforms with mood disorder specialists, medication support options, and insurance coverage. Updated monthly.',
    'breadcrumb_name': 'Bipolar Disorder',
    'hero_h1': "Bipolar disorder is more than mood swings.",
    'hero_sub': "It's the weeks that felt untouchable, followed by the crash. The exhaustion of managing a brain that operates at its own extremes.",
    'condition_name': 'Bipolar Disorder',
    'rank': ['TS', 'BH', 'OT'],
    'cards': [
        {
            'tagline': 'Best for combining therapy and medication management in one platform',
            'body': "Bipolar disorder frequently requires both therapy and psychiatric medication &mdash; Talkspace provides both under one roof. Their psychiatry service handles mood stabilizers alongside talk therapy. They accept Aetna, BCBS, Cigna, and UHC, which is critical for bipolar treatment that can run long-term. For the most effective use, prioritize live video sessions over messaging when managing mood episodes.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for matching with mood disorder specialists',
            'body': "BetterHelp's network includes therapists who specialize in bipolar disorder, DBT, and mood regulation. The scale of the network means you can find practitioners with specific bipolar experience, and same-day availability is useful at difficult moments. Note that BetterHelp doesn't offer psychiatry &mdash; for medication management you'll need a separate prescriber.",
            'cta': 'Find My Bipolar Specialist',
        },
        {
            'tagline': 'Best for structured skill-building between episodes',
            'body': "Online-Therapy.com's structured CBT tools &mdash; worksheets, mood journaling, and session frameworks &mdash; support the between-episode stabilization work that bipolar care requires. The lower price point ($45&ndash;80/week) makes consistent access more feasible. They don't offer insurance or psychiatry, so pair with a prescriber if medication is part of your treatment.",
            'cta': 'Start My CBT Program',
        },
    ],
    'vb_quote': "Managing bipolar disorder is a long game &mdash; having consistent support makes it sustainable.",
    'best_for': ['Therapy + medication management', 'Mood disorder specialists', 'Structured CBT between episodes'],
    'fork_links': '\n                            '.join([fl('depression.html', 'Online therapy for depression'), fl('anxiety.html', 'Online therapy for anxiety'), fl('insomnia.html', 'Online therapy for sleep problems'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Bipolar Disorder &middot; Mood Disorders &middot; DBT &middot; CBT',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience treating mood disorders including bipolar disorder. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 4. Eating Disorders — insurance-critical → TS #1
PAGES['eating-disorders'] = {
    'title': 'Online Therapy for Eating Disorders &mdash; Specialized Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for eating disorders. Expert-reviewed platforms for anorexia, bulimia, binge eating, and ARFID. Insurance options and pricing included. Updated monthly.',
    'breadcrumb_name': 'Eating Disorders',
    'hero_h1': "Eating disorders live in silence.",
    'hero_sub': "Not because there's nothing to say, but because the shame makes it hard to start. The right therapist creates a space where you finally can.",
    'condition_name': 'Eating Disorders',
    'rank': ['TS', 'BH', 'OT'],
    'cards': [
        {
            'tagline': 'Best for insurance-covered eating disorder treatment',
            'body': "Eating disorder treatment can be intensive and long-term &mdash; insurance coverage isn't optional for many people. Talkspace accepts Aetna, BCBS, Cigna, and UHC, and their combined therapy and psychiatry offering is relevant when eating disorders co-present with anxiety, depression, or OCD. Always confirm your therapist has specific eating disorder training at intake. Note: severe cases may require a higher level of care than any online platform.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for connecting with eating disorder specialists',
            'body': "BetterHelp's network includes therapists trained in CBT-E, DBT, and intuitive eating approaches. Filtering by specialty at matching increases the likelihood of landing with a genuinely experienced practitioner. The large network size means eating disorder specialists are available across a range of time zones and availability windows.",
            'cta': 'Find My Eating Disorder Therapist',
        },
        {
            'tagline': 'Best for structured behavioral tools supporting recovery',
            'body': "Online-Therapy.com's CBT-based program provides structured worksheets and journaling tools that can support recovery from binge eating and related disordered eating patterns. The structured format offers a predictable framework for challenging eating-related thought patterns. At $45&ndash;80/week without insurance, it's one of the more affordable structured options.",
            'cta': 'Start My CBT Program',
        },
    ],
    'vb_quote': "Recovery isn't linear &mdash; but the right support makes the path navigable.",
    'best_for': ['Insurance-covered eating disorder care', 'Eating disorder specialists', 'Structured CBT tools'],
    'fork_links': '\n                            '.join([fl('depression.html', 'Online therapy for depression'), fl('anxiety.html', 'Online therapy for anxiety'), fl('self-esteem.html', 'Online therapy for self-esteem'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Eating Disorders &middot; CBT &middot; DBT &middot; Body Image',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience treating eating disorders and body image concerns. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 5. Grief — network/specialty breadth → BH #1
PAGES['grief'] = {
    'title': 'Online Therapy for Grief & Loss &mdash; Compassionate Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for grief and loss. Expert-reviewed platforms for bereavement, major loss, and life transitions. Real pricing and insurance details. Updated monthly.',
    'breadcrumb_name': 'Grief &amp; Loss',
    'hero_h1': "Grief doesn't follow a schedule.",
    'hero_sub': "It comes back on ordinary Tuesdays. It doesn't look the way anyone told you it would. And it doesn't mean you're doing it wrong.",
    'condition_name': 'Grief & Loss',
    'rank': ['BH', 'TS', 'OT'],
    'cards': [
        {
            'tagline': 'Best for finding a grief therapist who matches your experience',
            'body': "Grief is deeply personal &mdash; the kind of loss, your cultural background, and your relationship to that person all shape what support looks like. BetterHelp's 30,000+ therapist network gives you the range to find someone who truly gets it. Most people connect within 24&ndash;48 hours, which matters when grief is fresh and waiting feels impossible.",
            'cta': 'Find My Grief Therapist',
        },
        {
            'tagline': 'Best if insurance is supporting your grief counseling',
            'body': "Grief doesn't resolve on a schedule, and insurance coverage lets you continue as long as you need. Talkspace accepts Aetna, BCBS, Cigna, and UHC, and their platform supports both live video and asynchronous messaging &mdash; useful on the days when talking out loud feels like too much. Psychiatry is available if grief has triggered depression or anxiety requiring medication.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for structured processing at an accessible price point',
            'body': "Online-Therapy.com's CBT framework can help structure the emotional processing that grief work requires &mdash; particularly useful for people who feel overwhelmed by open-ended sessions. Their journaling and worksheet tools provide a contained space to explore loss. At $45&ndash;80/week without insurance, it's accessible for those paying out of pocket.",
            'cta': 'Start My Grief Program',
        },
    ],
    'vb_quote': "There's no timeline for grief &mdash; only the slow building of a life around what you've lost.",
    'best_for': ['Grief specialist matching', 'Insurance-covered grief counseling', 'Structured grief processing'],
    'fork_links': '\n                            '.join([fl('depression.html', 'Online therapy for depression'), fl('loneliness.html', 'Therapy for loneliness'), fl('anxiety.html', 'Online therapy for anxiety'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Grief &middot; Bereavement &middot; Life Transitions &middot; Depression',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience supporting individuals through grief and major loss. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 6. Anger — network/specialty breadth → BH #1
PAGES['anger'] = {
    'title': 'Online Therapy for Anger Management &mdash; Platforms That Help | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for anger management. Expert-reviewed platforms using CBT and evidence-based approaches. Real pricing and insurance details. Updated monthly.',
    'breadcrumb_name': 'Anger Management',
    'hero_h1': "Anger isn't the problem. What you do with it is.",
    'hero_sub': "The flare that comes faster than you can stop it. The regret that follows. The pattern you've already tried to break on your own.",
    'condition_name': 'Anger Management',
    'rank': ['BH', 'TS', 'OT'],
    'cards': [
        {
            'tagline': 'Best for matching with therapists trained in anger and emotional regulation',
            'body': "BetterHelp's broad therapist network includes specialists in anger management, emotional regulation, and trauma-informed care &mdash; because anger is often a secondary emotion with roots in something deeper. The large network means you're not limited to whoever happens to have availability. Most people connect within 24&ndash;48 hours.",
            'cta': 'Find My Anger Management Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your anger management sessions',
            'body': "Talkspace's insurance coverage &mdash; Aetna, BCBS, Cigna, and UHC &mdash; makes sustained anger management work financially accessible. Their combined therapy and psychiatry offering is relevant if anger is connected to a mood disorder or ADHD that may also benefit from medication. Live video sessions work best for anger work; confirm availability at signup.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for structured CBT tools to build emotional regulation skills',
            'body': "Online-Therapy.com's structured CBT program is well-suited for anger work &mdash; the journaling tools, worksheets, and session structure help you identify triggers and build new response patterns deliberately. At $45&ndash;80/week, it's one of the most cost-effective ways to access structured anger management therapy.",
            'cta': 'Start My Anger Management Program',
        },
    ],
    'vb_quote': "Understanding what's underneath the anger is where the real work begins.",
    'best_for': ['Anger specialist matching', 'Insurance-covered anger therapy', 'Structured CBT for emotional regulation'],
    'fork_links': '\n                            '.join([fl('stress.html', 'Online therapy for stress'), fl('anxiety.html', 'Online therapy for anxiety'), fl('relationship.html', 'Online therapy for relationship issues'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Anger Management &middot; Emotional Regulation &middot; CBT &middot; Trauma-Informed Care',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience in emotional regulation and anger management therapy. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 7. Addiction — insurance-critical → TS #1
PAGES['addiction'] = {
    'title': 'Online Therapy for Addiction & Substance Use &mdash; Recovery-Focused Platforms | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for addiction and substance use. Expert-reviewed platforms for recovery support, dual diagnosis, and insurance coverage. Updated monthly.',
    'breadcrumb_name': 'Addiction &amp; Substance Use',
    'hero_h1': "Recovery isn't a straight line.",
    'hero_sub': "And it rarely looks the way it does in the stories. Online therapy can be one part of a support system that actually meets you where you are.",
    'condition_name': 'Addiction & Substance Use',
    'rank': ['TS', 'BH', 'OT'],
    'cards': [
        {
            'tagline': 'Best for insurance-covered addiction therapy and dual diagnosis support',
            'body': "Talkspace accepts Aetna, BCBS, Cigna, and UHC &mdash; making long-term addiction therapy financially sustainable. Their psychiatry offering is directly relevant for dual diagnosis (co-occurring mental health conditions alongside substance use). Note that online therapy supplements rather than replaces intensive outpatient or inpatient programs when those are clinically indicated.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for matching with addiction and recovery specialists',
            'body': "BetterHelp's network includes therapists trained in addiction counseling, motivational interviewing, and 12-step integration. The ability to specify addiction as your focus at matching surfaces practitioners with relevant experience. Same-day availability reduces the gap between deciding to get support and actually starting.",
            'cta': 'Find My Recovery Therapist',
        },
        {
            'tagline': 'Best for structured CBT tools to support behavioral change',
            'body': "Online-Therapy.com's CBT-based program &mdash; with worksheets, journaling, and structured sessions &mdash; aligns well with behavioral approaches to addiction recovery. The structured format helps build the self-monitoring skills central to relapse prevention. At $45&ndash;80/week, it's an accessible complement to other recovery supports.",
            'cta': 'Start My Recovery Program',
        },
    ],
    'vb_quote': "Getting support for addiction takes courage &mdash; online therapy removes at least one barrier to starting.",
    'best_for': ['Insurance + dual diagnosis', 'Addiction specialist matching', 'Structured CBT for relapse prevention'],
    'fork_links': '\n                            '.join([fl('depression.html', 'Online therapy for depression'), fl('anxiety.html', 'Online therapy for anxiety'), fl('stress.html', 'Online therapy for stress'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Addiction &middot; Substance Use &middot; Dual Diagnosis &middot; CBT',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience in addiction counseling and dual diagnosis treatment. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 8. Stress — CBT-responsive → OT #1
PAGES['stress'] = {
    'title': 'Online Therapy for Stress Management &mdash; Platforms That Actually Help | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for stress management. Expert-reviewed CBT-based platforms to reduce chronic stress. Real pricing and insurance options included. Updated monthly.',
    'breadcrumb_name': 'Stress Management',
    'hero_h1': "Stress has a way of becoming your baseline.",
    'hero_sub': "The point where you can't remember what calm feels like. Where you're functioning, but only just &mdash; and everyone else thinks you're fine.",
    'condition_name': 'Stress Management',
    'rank': ['OT', 'BH', 'TS'],
    'cards': [
        {
            'tagline': 'Best for a structured CBT program to reset your stress response',
            'body': "Online-Therapy.com's structured CBT program is built for exactly this &mdash; identifying stress triggers, building behavioral responses, and changing the thought patterns that keep you stuck in high-alert mode. The worksheets, journaling, and yoga components address stress from multiple angles. At $45&ndash;80/week, it's an accessible entry point for structured stress work.",
            'cta': 'Start My Stress Program',
        },
        {
            'tagline': 'Best for flexible stress support from a large therapist network',
            'body': "BetterHelp's therapist network covers stress management, burnout, work-life balance, and the anxiety that often underlies chronic stress. The variety of session formats &mdash; video, phone, messaging &mdash; lets you fit therapy around a demanding schedule. Most people connect with a therapist within 24&ndash;48 hours.",
            'cta': 'Find My Stress Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your stress-related therapy',
            'body': "When stress is severe enough to need regular support, insurance coverage makes consistency possible. Talkspace accepts Aetna, BCBS, Cigna, and UHC. Their messaging format is particularly convenient for people whose stress is largely work-related &mdash; you can reach your therapist between sessions without scheduling a full appointment.",
            'cta': 'Check My Insurance Coverage',
        },
    ],
    'vb_quote': "Learning to regulate your nervous system changes everything &mdash; and it starts with having the right support.",
    'best_for': ['Structured CBT stress program', 'Flexible stress support', 'Insurance-covered stress therapy'],
    'fork_links': '\n                            '.join([fl('burnout.html', 'Online therapy for burnout'), fl('anxiety.html', 'Online therapy for anxiety'), fl('insomnia.html', 'Online therapy for sleep problems'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Stress Management &middot; CBT &middot; Burnout &middot; Anxiety',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience treating chronic stress and work-related mental health concerns. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 9. Relationship — network/specialty breadth → BH #1
PAGES['relationship'] = {
    'title': 'Online Therapy for Relationship Issues &mdash; Individual Support, Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for relationship issues. Expert-reviewed platforms for dating, family, and friendship challenges. Individual therapy options with real pricing. Updated monthly.',
    'breadcrumb_name': 'Relationship Issues',
    'hero_h1': "Relationship problems don't only exist in couples therapy.",
    'hero_sub': "Sometimes it's patterns you keep repeating. Boundaries you can't hold. A relationship with a parent that still shapes everything else.",
    'condition_name': 'Relationship Issues',
    'rank': ['BH', 'TS', 'OT'],
    'cards': [
        {
            'tagline': 'Best for matching with therapists who specialize in relationship patterns',
            'body': "BetterHelp's network spans specialists in attachment, family systems, communication patterns, and relationship anxiety &mdash; all the underlying dynamics that make individual relationship work meaningful. The large network increases the likelihood of finding a therapist whose specific training matches your situation, whether that's dating anxiety, family estrangement, or friendship challenges.",
            'cta': 'Find My Relationship Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your relationship-focused therapy',
            'body': "Talkspace's broad insurance acceptance &mdash; Aetna, BCBS, Cigna, and UHC &mdash; makes consistent relationship work financially accessible. Relationship therapy often benefits from frequency, and insurance enables that. Their messaging format also suits processing relational experiences between sessions rather than waiting for the next appointment.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for structured CBT tools to change relational patterns',
            'body': "Online-Therapy.com's CBT worksheets and journaling tools are effective for identifying and shifting the thought patterns and behavioral habits that drive relationship difficulties. The structured program format suits people who want to work through specific relationship issues methodically rather than in open-ended sessions.",
            'cta': 'Start My Relationship Program',
        },
    ],
    'vb_quote': "The relationship you have with yourself shapes every other relationship in your life.",
    'best_for': ['Relationship pattern specialists', 'Insurance-covered relationship therapy', 'Structured CBT for relational habits'],
    'fork_links': '\n                            '.join([fl('couples.html', 'Online couples therapy'), fl('self-esteem.html', 'Online therapy for self-esteem'), fl('anxiety.html', 'Online therapy for anxiety'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Relationship Issues &middot; Attachment &middot; Family Systems &middot; Communication',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience in relational therapy and family systems. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 10. LGBTQ+ — network/specialty breadth → BH #1
PAGES['lgbtq'] = {
    'title': 'Online Therapy for LGBTQ+ Affirming Support &mdash; Vetted Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for LGBTQ+ individuals. Expert-reviewed affirming platforms with vetted therapists, real pricing, and insurance options. Updated monthly.',
    'breadcrumb_name': 'LGBTQ+ Support',
    'hero_h1': "Therapy should feel safer than explaining yourself.",
    'hero_sub': "Finding an affirming therapist who actually gets your experience &mdash; not one you have to educate &mdash; changes the quality of every session.",
    'condition_name': 'LGBTQ+ Support',
    'rank': ['BH', 'TS', 'OT'],
    'cards': [
        {
            'tagline': 'Best for finding vetted LGBTQ+ affirming therapists',
            'body': "BetterHelp allows you to specify LGBTQ+ identity and affirming care as a matching criteria &mdash; surfacing therapists who have both the training and lived cultural competency to provide genuinely affirming support. With 30,000+ therapists, the depth of LGBTQ+ specialist availability is unmatched among online platforms. Same-day or next-day starts mean you don't have to wait.",
            'cta': 'Find My LGBTQ+ Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your affirming therapy',
            'body': "Talkspace accepts Aetna, BCBS, Cigna, and UHC, making ongoing affirming therapy financially accessible. Their platform supports a range of LGBTQ+ concerns from identity exploration to relationship support, and their psychiatry offering is available for co-occurring mental health needs. Filter for affirming care explicitly when setting up your profile.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for structured affirming CBT work at an accessible price',
            'body': "Online-Therapy.com's CBT framework can support identity-related work, internalized stigma processing, and anxiety common in LGBTQ+ experiences. At $45&ndash;80/week without insurance, it's a cost-effective option for those needing affordable affirming support. Confirm therapist identity competency during the intake process.",
            'cta': 'Start My Affirming Program',
        },
    ],
    'vb_quote': "Affirming therapy isn't a bonus &mdash; it's the minimum standard you deserve.",
    'best_for': ['LGBTQ+ affirming specialists', 'Insurance-covered affirming therapy', 'Structured CBT for identity work'],
    'fork_links': '\n                            '.join([fl('anxiety.html', 'Online therapy for anxiety'), fl('depression.html', 'Online therapy for depression'), fl('self-esteem.html', 'Online therapy for self-esteem'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'LGBTQ+ Affirming Care &middot; Identity &middot; Anxiety &middot; Relationship Issues',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience providing affirming care for LGBTQ+ individuals. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 11. Teen — network/specialty breadth → BH #1
PAGES['teen'] = {
    'title': 'Online Therapy for Teens &mdash; Adolescent Mental Health Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for teens and adolescents. Expert-reviewed platforms with youth-specialist therapists, parental involvement options, and real pricing. Updated monthly.',
    'breadcrumb_name': 'Teen &amp; Adolescent Therapy',
    'hero_h1': "Teen years are hard. The right support makes them survivable.",
    'hero_sub': "Anxiety, depression, social pressure, identity questions &mdash; adolescence brings everything at once. A therapist who speaks to teens, not at them, makes all the difference.",
    'condition_name': 'Teen & Adolescent Therapy',
    'rank': ['BH', 'TS', 'OT'],
    'cards': [
        {
            'tagline': 'Best for matching teens with youth-specialist therapists',
            'body': "BetterHelp's network includes therapists who specialize in adolescent mental health &mdash; practitioners trained in teen-specific anxiety, depression, identity development, and school-related stress. The large network means finding someone who works well with teenagers, not just adults discussing their teen years. Most teens connect with a therapist within 24&ndash;48 hours.",
            'cta': 'Find a Teen Therapist',
        },
        {
            'tagline': 'Best if insurance is covering teen therapy',
            'body': "Talkspace accepts Aetna, BCBS, Cigna, and UHC, and their services extend to adolescents with parental consent. Insurance coverage makes the frequency of sessions that teens often need financially sustainable. Their messaging format may appeal to teens who find texting more natural than talking &mdash; though live sessions remain the most effective modality.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for structured CBT tools supporting teen skill development',
            'body': "Online-Therapy.com's structured CBT program &mdash; including worksheets and journaling tools &mdash; can build the emotional regulation and cognitive skills that adolescents need. The structured format suits teens who prefer a clear roadmap over open-ended conversation. At $45&ndash;80/week, it's among the more affordable structured options available.",
            'cta': 'Start a Teen CBT Program',
        },
    ],
    'vb_quote': "A teen who learns to process their emotions has a skill they'll use for the rest of their life.",
    'best_for': ['Adolescent specialist matching', 'Insurance-covered teen therapy', 'Structured CBT for teens'],
    'fork_links': '\n                            '.join([fl('anxiety.html', 'Online therapy for anxiety'), fl('depression.html', 'Online therapy for depression'), fl('self-esteem.html', 'Online therapy for self-esteem'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Adolescent Therapy &middot; Teen Anxiety &middot; Depression &middot; Identity Development',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience working with adolescents and their families. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 12. Postpartum — insurance-critical → TS #1
PAGES['postpartum'] = {
    'title': 'Online Therapy for Postpartum Depression &mdash; Perinatal Mental Health Support | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for postpartum depression. Expert-reviewed perinatal mental health platforms with insurance coverage and real pricing. Updated monthly.',
    'breadcrumb_name': 'Postpartum Depression',
    'hero_h1': "Postpartum depression doesn't mean you don't love your baby.",
    'hero_sub': "It means your brain chemistry shifted in a way that has nothing to do with your capabilities as a parent. Support exists &mdash; and it's closer than you think.",
    'condition_name': 'Postpartum Depression',
    'rank': ['TS', 'BH', 'OT'],
    'cards': [
        {
            'tagline': 'Best for insurance-covered postpartum mental health support',
            'body': "Talkspace accepts Aetna, BCBS, Cigna, and UHC &mdash; critical for postpartum care when financial pressure is already high. Their psychiatry service is directly relevant if medication is indicated for postpartum depression or anxiety, and the messaging format suits new parents who can't always schedule a full session. Video sessions are available when a deeper conversation is needed.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for matching with perinatal mental health specialists',
            'body': "BetterHelp's network includes therapists who specialize in perinatal mood disorders, postpartum anxiety, and the identity shifts that come with new parenthood. Same-day matching is genuinely useful here &mdash; postpartum symptoms can escalate quickly, and not waiting weeks for a first appointment matters. The variety of session formats accommodates unpredictable newborn schedules.",
            'cta': 'Find My Postpartum Therapist',
        },
        {
            'tagline': 'Best for structured postpartum support at an accessible price',
            'body': "Online-Therapy.com's CBT-based program &mdash; with structured sessions, journaling, and worksheets &mdash; can provide the consistent cognitive-behavioral tools useful in postpartum recovery. At $45&ndash;80/week, it's an accessible option for new parents paying out of pocket. Best used alongside professional medical monitoring for postpartum symptoms.",
            'cta': 'Start My Postpartum Program',
        },
    ],
    'vb_quote': "Asking for support when you're a new parent is one of the strongest things you can do.",
    'best_for': ['Insurance-covered postpartum care', 'Perinatal specialist matching', 'Structured CBT postpartum support'],
    'fork_links': '\n                            '.join([fl('depression.html', 'Online therapy for depression'), fl('anxiety.html', 'Online therapy for anxiety'), fl('insomnia.html', 'Online therapy for sleep problems'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Postpartum Depression &middot; Perinatal Mental Health &middot; Anxiety &middot; CBT',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience in perinatal mental health and postpartum care. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 13. Burnout — network/specialty breadth → BH #1
PAGES['burnout'] = {
    'title': 'Online Therapy for Burnout &mdash; Recovery-Focused Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for burnout. Expert-reviewed platforms for chronic work stress, emotional exhaustion, and recovery. Real pricing and insurance included. Updated monthly.',
    'breadcrumb_name': 'Burnout',
    'hero_h1': "Burnout isn't laziness. It's what happens when you give more than you have.",
    'hero_sub': "The exhaustion that sleep doesn't fix. The cynicism that crept in without you noticing. The feeling that you used to care, and now you just don't.",
    'condition_name': 'Burnout',
    'rank': ['BH', 'TS', 'OT'],
    'cards': [
        {
            'tagline': 'Best for matching with burnout and work-stress specialists',
            'body': "BetterHelp's therapist network includes specialists in burnout recovery, work-life balance, compassion fatigue, and the identity disruption burnout often triggers. The large network means finding a therapist whose background aligns with your professional context &mdash; healthcare burnout looks different from tech burnout looks different from caregiver burnout. Same-day starts available.",
            'cta': 'Find My Burnout Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your burnout recovery',
            'body': "Talkspace's insurance coverage &mdash; Aetna, BCBS, Cigna, and UHC &mdash; makes regular burnout therapy sustainable when you're already resource-depleted. Their messaging format suits high-workload individuals who can't reliably block an hour each week. Psychiatry is available if burnout has triggered depression or anxiety requiring medication.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for structured CBT tools to rebuild capacity',
            'body': "Online-Therapy.com's structured CBT program addresses the cognitive patterns &mdash; perfectionism, difficulty saying no, catastrophizing &mdash; that often underlie burnout. The structured worksheets and journaling tools create space for reflection that people in burnout rarely give themselves. At $45&ndash;80/week, it's accessible for out-of-pocket payers.",
            'cta': 'Start My Burnout Recovery Program',
        },
    ],
    'vb_quote': "Recovering from burnout requires unlearning as much as it requires rest.",
    'best_for': ['Burnout specialist matching', 'Insurance-covered burnout therapy', 'Structured CBT for recovery'],
    'fork_links': '\n                            '.join([fl('stress.html', 'Online therapy for stress'), fl('depression.html', 'Online therapy for depression'), fl('insomnia.html', 'Online therapy for sleep'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Burnout &middot; Stress Management &middot; Compassion Fatigue &middot; CBT',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience in burnout recovery and work-related mental health. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 14. Insomnia — CBT-responsive → OT #1
PAGES['insomnia'] = {
    'title': 'Online Therapy for Insomnia & Sleep Problems &mdash; CBT-I Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for insomnia and sleep problems. Expert-reviewed CBT-I platforms with real pricing and insurance options. No sleep aids. Updated monthly.',
    'breadcrumb_name': 'Sleep &amp; Insomnia',
    'hero_h1': "Bad sleep affects everything else.",
    'hero_sub': "The foggy thinking. The emotional fragility. The days that feel twice as hard. CBT for insomnia has stronger evidence than sleep medication &mdash; and it lasts longer.",
    'condition_name': 'Sleep & Insomnia',
    'rank': ['OT', 'BH', 'TS'],
    'cards': [
        {
            'tagline': 'Best for structured CBT-I &mdash; the gold standard for chronic insomnia',
            'body': "CBT for Insomnia (CBT-I) is consistently ranked above medication for long-term sleep improvement, and Online-Therapy.com's structured program delivers exactly this approach. Their session structure, journaling tools, and sleep-focused worksheets create the behavioral framework that CBT-I requires. No insurance needed &mdash; at $45&ndash;80/week, it's the most cost-effective path to evidence-based sleep therapy.",
            'cta': 'Start My Sleep Program',
        },
        {
            'tagline': 'Best for matching with sleep disorder specialists',
            'body': "BetterHelp's network includes therapists trained in CBT-I, sleep hygiene intervention, and the anxiety-insomnia cycle that keeps many people stuck. Filtering for sleep specialists at matching surfaces practitioners whose focus aligns with yours. The variety of session formats suits people whose insomnia makes fixed appointment times difficult.",
            'cta': 'Find My Sleep Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your insomnia treatment',
            'body': "Talkspace accepts Aetna, BCBS, Cigna, and UHC &mdash; relevant when insomnia is connected to an underlying condition like anxiety or depression that insurance may cover. Their psychiatry service is available if sleep medication is being considered alongside behavioral treatment. Confirm sleep specialist availability at intake.",
            'cta': 'Check My Insurance Coverage',
        },
    ],
    'vb_quote': "Better sleep isn't about trying harder &mdash; it's about changing the relationship your brain has with being awake at night.",
    'best_for': ['Structured CBT-I program', 'Sleep specialist matching', 'Insurance-covered sleep therapy'],
    'fork_links': '\n                            '.join([fl('anxiety.html', 'Online therapy for anxiety'), fl('stress.html', 'Online therapy for stress'), fl('depression.html', 'Online therapy for depression'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Insomnia &middot; CBT-I &middot; Sleep Disorders &middot; Anxiety',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience treating insomnia, anxiety, and the anxiety-insomnia cycle. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 15. Chronic Pain — insurance-critical → TS #1
PAGES['chronic-pain'] = {
    'title': 'Online Therapy for Chronic Pain &mdash; Mental Health Support for Long-Term Conditions | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for chronic pain and illness. Expert-reviewed platforms for the mental toll of long-term health conditions. Insurance coverage included. Updated monthly.',
    'breadcrumb_name': 'Chronic Pain',
    'hero_h1': "Chronic pain doesn't just hurt physically.",
    'hero_sub': "It changes your identity. Your relationships. Your sense of what's possible. The mental health impact of living in pain is real &mdash; and it deserves real support.",
    'condition_name': 'Chronic Pain',
    'rank': ['TS', 'BH', 'OT'],
    'cards': [
        {
            'tagline': 'Best for insurance-covered therapy for chronic pain and illness',
            'body': "Chronic pain management is long-term by definition &mdash; insurance coverage matters. Talkspace accepts Aetna, BCBS, Cigna, and UHC, and their psychiatry option is relevant if pain has contributed to depression or anxiety requiring medication. Their messaging format is also accessible on difficult pain days when getting to a screen for a video call isn't feasible.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for matching with therapists experienced in chronic illness',
            'body': "BetterHelp's network includes therapists trained in acceptance and commitment therapy (ACT), pain psychology, and the grief that comes with a changed body. The large network means finding someone who genuinely understands chronic illness rather than offering generic coping strategies. Same-day matching avoids adding a waiting list to an already taxing situation.",
            'cta': 'Find My Chronic Pain Therapist',
        },
        {
            'tagline': 'Best for structured CBT tools to manage pain-related thinking',
            'body': "Online-Therapy.com's CBT program addresses the catastrophizing and avoidance patterns that amplify chronic pain's psychological burden. Their structured journaling and worksheets create space to work with pain-related thoughts systematically. At $45&ndash;80/week without insurance, it's an accessible complement to medical pain management.",
            'cta': 'Start My Pain Management Program',
        },
    ],
    'vb_quote': "Living with chronic pain is exhausting enough &mdash; your mental health support shouldn't add to that burden.",
    'best_for': ['Insurance-covered chronic pain therapy', 'Chronic illness specialists', 'CBT for pain-related thinking'],
    'fork_links': '\n                            '.join([fl('depression.html', 'Online therapy for depression'), fl('anxiety.html', 'Online therapy for anxiety'), fl('insomnia.html', 'Online therapy for sleep'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Chronic Pain &middot; Chronic Illness &middot; ACT &middot; CBT',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience supporting individuals with chronic pain and long-term health conditions. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 16. Social Anxiety — CBT-responsive → OT #1
PAGES['social-anxiety'] = {
    'title': 'Online Therapy for Social Anxiety &mdash; CBT-Focused Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for social anxiety. Expert-reviewed CBT platforms with exposure-based treatment options. Real pricing and insurance details. Updated monthly.',
    'breadcrumb_name': 'Social Anxiety',
    'hero_h1': "Social anxiety is more than being shy.",
    'hero_sub': "It's the rehearsing before every interaction. The replaying afterward. The exhaustion of navigating a world that seems to come naturally to everyone else.",
    'condition_name': 'Social Anxiety',
    'rank': ['OT', 'BH', 'TS'],
    'cards': [
        {
            'tagline': 'Best for structured CBT &mdash; the most effective treatment for social anxiety',
            'body': "Online-Therapy.com's CBT program is built around the same exposure-based framework used to treat social anxiety in clinical settings. The structured worksheets and session progression systematically challenge avoidance behaviors and the distorted thinking that social anxiety relies on. Starting at $45&ndash;80/week without insurance, it's among the most cost-effective access points for evidence-based social anxiety treatment.",
            'cta': 'Start My Social Anxiety Program',
        },
        {
            'tagline': 'Best for matching with social anxiety specialists',
            'body': "BetterHelp's broad network includes therapists trained in social anxiety disorder, exposure therapy, and the performance anxiety and public speaking fears that fall under social anxiety's umbrella. For social anxiety specifically, finding a therapist you genuinely connect with matters &mdash; the large network gives you options if the first match isn't right.",
            'cta': 'Find My Social Anxiety Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your social anxiety treatment',
            'body': "Social anxiety treatment can span months &mdash; insurance coverage through Talkspace (Aetna, BCBS, Cigna, UHC) makes the full course of treatment financially sustainable. The messaging format has an unexpected benefit for social anxiety clients: some find it easier to open up in writing before graduating to video sessions.",
            'cta': 'Check My Insurance Coverage',
        },
    ],
    'vb_quote': "Social anxiety convinces you everyone is watching &mdash; therapy helps you stop believing it.",
    'best_for': ['Structured CBT for social anxiety', 'Social anxiety specialists', 'Insurance-covered social anxiety care'],
    'fork_links': '\n                            '.join([fl('anxiety.html', 'Online therapy for anxiety'), fl('panic.html', 'Online therapy for panic disorder'), fl('self-esteem.html', 'Online therapy for self-esteem'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Social Anxiety &middot; CBT &middot; Exposure Therapy &middot; Anxiety Disorders',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience treating social anxiety and related anxiety disorders. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 17. Phobias — CBT-responsive → OT #1
PAGES['phobias'] = {
    'title': 'Online Therapy for Phobias &mdash; Exposure-Based Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for phobias. Expert-reviewed platforms using CBT and exposure therapy for specific fears. Real pricing and insurance details. Updated monthly.',
    'breadcrumb_name': 'Phobias',
    'hero_h1': "A phobia isn't irrational to the person living with it.",
    'hero_sub': "The avoidance that reorganizes your whole life. The fear that feels completely real even when you know, intellectually, that it isn't proportionate.",
    'condition_name': 'Phobias',
    'rank': ['OT', 'BH', 'TS'],
    'cards': [
        {
            'tagline': 'Best for structured exposure-based CBT for phobia treatment',
            'body': "Phobias respond well to exposure and response prevention (ERP) and systematic desensitization &mdash; both grounded in CBT. Online-Therapy.com's structured program provides the framework for working through phobias systematically: building a fear hierarchy, gradual exposure, and processing the associated thoughts. At $45&ndash;80/week, it's an accessible way to begin phobia work.",
            'cta': 'Start My Phobia Program',
        },
        {
            'tagline': 'Best for matching with phobia and exposure therapy specialists',
            'body': "BetterHelp's network includes therapists trained in specific phobias across the spectrum &mdash; from agoraphobia to medical phobias to social phobias. Finding a therapist with specific phobia treatment experience is more important here than platform features, and BetterHelp's network depth makes that possible. Same-day starts available.",
            'cta': 'Find My Phobia Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your phobia treatment',
            'body': "Talkspace accepts Aetna, BCBS, Cigna, and UHC, making phobia treatment financially accessible for insurance holders. Their platform supports both structured session work and between-session check-ins via messaging &mdash; useful for phobia work that extends between appointments. Confirm your therapist's experience with exposure-based techniques at intake.",
            'cta': 'Check My Insurance Coverage',
        },
    ],
    'vb_quote': "Phobia treatment works by gradually proving to your nervous system what it's gotten wrong.",
    'best_for': ['Structured CBT exposure program', 'Phobia specialists, large network', 'Insurance-covered phobia treatment'],
    'fork_links': '\n                            '.join([fl('anxiety.html', 'Online therapy for anxiety'), fl('social-anxiety.html', 'Online therapy for social anxiety'), fl('panic.html', 'Online therapy for panic disorder'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Phobias &middot; Exposure Therapy &middot; CBT &middot; Anxiety Disorders',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience treating specific phobias and anxiety disorders. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 18. Panic — CBT-responsive → OT #1
PAGES['panic'] = {
    'title': 'Online Therapy for Panic Disorder &mdash; CBT-Focused Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for panic disorder and panic attacks. Expert-reviewed CBT platforms for managing and reducing panic. Real pricing and insurance. Updated monthly.',
    'breadcrumb_name': 'Panic Disorder',
    'hero_h1': "Panic attacks are terrifying. Panic disorder is exhausting.",
    'hero_sub': "Not just the attacks themselves &mdash; but the constant anticipation, the avoidance that grows around them, the way fear of fear becomes its own problem.",
    'condition_name': 'Panic Disorder',
    'rank': ['OT', 'BH', 'TS'],
    'cards': [
        {
            'tagline': 'Best for structured CBT to break the panic cycle',
            'body': "Panic disorder responds exceptionally well to CBT &mdash; specifically interoceptive exposure and cognitive restructuring, which Online-Therapy.com's structured program delivers. Their worksheets and session framework help you understand panic's physical mechanisms and practice not reinforcing the fear response. Starting at $45&ndash;80/week, it's an evidence-based, accessible starting point.",
            'cta': 'Start My Panic Program',
        },
        {
            'tagline': 'Best for matching with panic disorder specialists',
            'body': "BetterHelp's network includes therapists with specific panic disorder training who can guide you through exposure-based treatment with the human support that makes it stick. For panic specifically, the therapeutic relationship matters &mdash; feeling safe with your therapist is part of the treatment. With 30,000+ professionals, finding the right fit is realistic.",
            'cta': 'Find My Panic Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your panic disorder treatment',
            'body': "Talkspace accepts Aetna, BCBS, Cigna, and UHC, making the full course of panic disorder treatment financially sustainable. Their psychiatry option is relevant if medication is part of your treatment plan alongside therapy. Confirm your therapist's specific panic disorder training when setting up your account.",
            'cta': 'Check My Insurance Coverage',
        },
    ],
    'vb_quote': "Panic loses its power when you stop running from it &mdash; CBT teaches you how to stop.",
    'best_for': ['Structured CBT for panic', 'Panic disorder specialists', 'Insurance-covered panic treatment'],
    'fork_links': '\n                            '.join([fl('anxiety.html', 'Online therapy for anxiety'), fl('social-anxiety.html', 'Online therapy for social anxiety'), fl('ocd.html', 'Online therapy for OCD'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Panic Disorder &middot; CBT &middot; Interoceptive Exposure &middot; Anxiety Disorders',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience treating panic disorder and anxiety. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 19. Loneliness — network/specialty breadth → BH #1
PAGES['loneliness'] = {
    'title': 'Online Therapy for Loneliness & Isolation &mdash; Support Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for loneliness and isolation. Expert-reviewed platforms for building connection and coping with chronic loneliness. Real pricing and insurance. Updated monthly.',
    'breadcrumb_name': 'Loneliness &amp; Isolation',
    'hero_h1': "Loneliness isn't about being alone.",
    'hero_sub': "You can feel it in a room full of people. In a long-term relationship. In a city of millions. And it's one of the most quietly painful experiences there is.",
    'condition_name': 'Loneliness & Isolation',
    'rank': ['BH', 'TS', 'OT'],
    'cards': [
        {
            'tagline': 'Best for matching with therapists who understand chronic loneliness',
            'body': "BetterHelp's broad network includes therapists specializing in social connection, attachment patterns, and the depression that often co-exists with chronic loneliness. The therapeutic relationship itself &mdash; having a consistent, attuned human you speak to regularly &mdash; is part of the intervention for loneliness. Most people connect within 24&ndash;48 hours.",
            'cta': 'Find My Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your loneliness-related therapy',
            'body': "Talkspace accepts Aetna, BCBS, Cigna, and UHC &mdash; making ongoing support for loneliness financially accessible. The messaging format has a unique benefit here: it provides a touchpoint between sessions that reduces the sense of disconnection. Psychiatry is available if loneliness has contributed to depression requiring medication.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for structured work on the thinking patterns that reinforce isolation',
            'body': "Online-Therapy.com's CBT tools are effective for the negative social cognitions &mdash; 'no one would want to know me,' 'reaching out is pointless' &mdash; that loneliness tends to generate and reinforce. Their structured worksheets and journaling create space to challenge those thoughts systematically. At $45&ndash;80/week, it's an accessible starting point.",
            'cta': 'Start My Program',
        },
    ],
    'vb_quote': "Loneliness shrinks when you have one consistent person in your corner. Therapy can be that.",
    'best_for': ['Connection-focused specialist matching', 'Insurance-covered loneliness support', 'CBT for social isolation thinking'],
    'fork_links': '\n                            '.join([fl('depression.html', 'Online therapy for depression'), fl('social-anxiety.html', 'Online therapy for social anxiety'), fl('grief.html', 'Online therapy for grief'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Loneliness &middot; Social Isolation &middot; Attachment &middot; Depression',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience working with loneliness, depression, and social connection. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}

# 20. Self-Esteem — network/specialty breadth → BH #1
PAGES['self-esteem'] = {
    'title': 'Online Therapy for Self-Esteem & Confidence &mdash; Platforms Compared | Digital Therapy Solutions',
    'meta_desc': 'Best online therapy for self-esteem and confidence. Expert-reviewed platforms for inner critic work, identity, and self-worth. Real pricing and insurance. Updated monthly.',
    'breadcrumb_name': 'Self-Esteem &amp; Confidence',
    'hero_h1': "Low self-esteem isn't a personality trait. It's a pattern that can change.",
    'hero_sub': "The voice that says you're not enough. The way you minimize your wins and magnify your failures. Therapy can change the relationship you have with yourself.",
    'condition_name': 'Self-Esteem & Confidence',
    'rank': ['BH', 'TS', 'OT'],
    'cards': [
        {
            'tagline': 'Best for matching with therapists who specialize in self-worth and identity',
            'body': "BetterHelp's network includes therapists trained in self-esteem work, inner critic patterns, ACT, and the identity development work that lasting confidence requires. Self-esteem issues are often tied to early experiences, attachment patterns, or specific life contexts &mdash; finding a therapist whose background matches your situation is easier with a large network. Same-day starts available.",
            'cta': 'Find My Therapist',
        },
        {
            'tagline': 'Best if insurance is covering your self-esteem work',
            'body': "Talkspace accepts Aetna, BCBS, Cigna, and UHC, making the ongoing work that self-esteem change requires financially sustainable. Their messaging format also allows for between-session reflection &mdash; capturing moments of self-critical thinking in real time and sharing them with your therapist, rather than reconstructing them in a session.",
            'cta': 'Check My Insurance Coverage',
        },
        {
            'tagline': 'Best for structured CBT tools to challenge the inner critic',
            'body': "Online-Therapy.com's CBT worksheets are particularly effective for self-esteem work &mdash; they provide structured exercises for identifying negative self-beliefs and building evidence-based alternatives. The journaling component helps track progress over time. At $45&ndash;80/week, it's an accessible entry point for this kind of foundational work.",
            'cta': 'Start My Self-Esteem Program',
        },
    ],
    'vb_quote': "The way you talk to yourself matters more than almost anything else. Therapy helps you change the script.",
    'best_for': ['Self-esteem specialist matching', 'Insurance-covered confidence work', 'Structured CBT for self-worth'],
    'fork_links': '\n                            '.join([fl('depression.html', 'Online therapy for depression'), fl('anxiety.html', 'Online therapy for anxiety'), fl('relationship.html', 'Online therapy for relationship issues'), fl('affordable.html', 'Does insurance cover online therapy?')]),
    'specialties': 'Self-Esteem &middot; Inner Critic &middot; ACT &middot; Identity Development',
    'reviewer_bio': "Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience in self-esteem, identity work, and confidence building. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.",
}


# ---- BUILD ALL ----
print(f"Building {len(PAGES)} pages to {OUTPUT}")
for slug, data in PAGES.items():
    build_page(slug, data)

print(f"\nDONE. {len(PAGES)} pages written.")
