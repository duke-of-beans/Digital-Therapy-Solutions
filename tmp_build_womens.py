import sys
sys.stdout.reconfigure(encoding='utf-8')

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Therapy for Women's Mental Health — Platforms That Understand | Digital Therapy Solutions</title>
    <meta name="description" content="Find the best online therapy platforms for women's mental health. Expert-reviewed platforms with therapists specializing in hormonal, relational, and identity-focused care. Updated monthly.">
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
        <a href="index.html">Home</a><span class="breadcrumb__sep">/</span><a href="conditions.html">Conditions</a> / Women\'s Mental Health
    </nav>

        <!-- HERO -->
        <div class="section-wrapper section-wrapper--hero">
            <div class="hero-visual">
                <img src="../assets/hero.webp" alt="Person at home with laptop during an online therapy session" class="hero-image">
            </div>
            <div class="hero-text">
                <h1>Women carry a lot. Therapy built around that reality helps more.</h1>
                <p class="hero-subhead"><em>Hormones, relationships, caregiving, identity &mdash; the full picture matters in treatment.</em></p>
                <p class="hero-subhead hero-subhead--follow">These platforms have the therapist depth to match women with someone who actually understands.</p>
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
                <h2 class="section-heading">Platforms We Recommend for Women\'s Mental Health</h2>
                <p class="section-context">Each platform below was personally tested and clinically reviewed by <strong>Dr. Sarah Chen, LCSW</strong> &mdash; a licensed therapist specializing in women\'s mental health.</p>

                <!-- CARD 1: BetterHelp — Top Pick -->
                <article class="platform-card platform-card--featured reveal">
                    <div class="platform-card__header">
                        <div class="platform-card__logo" style="background:#00796B;color:#fff;font-weight:700;font-size:1.1rem;">
                            <img src="../assets/logos/betterhelp.webp" alt="BetterHelp logo" onerror="this.style.display=\'none\';this.parentElement.style.background=\'#00796B\';this.parentElement.style.color=\'#fff\';this.parentElement.textContent=\'BH\';">
                        </div>
                        <div class="platform-card__identity">
                            <h3 class="platform-card__name">BetterHelp</h3>
                            <p class="platform-card__tagline">Best overall for women &mdash; largest network, easy to find female therapists</p>
                        </div>
                        <div class="platform-card__score">
                            <span class="score-number">4.6</span>
                            <svg class="score-stars" viewBox="0 0 80 16"><polygon points="8,1 10.2,5.5 15.1,6.1 11.5,9.6 12.4,14.5 8,12.1 3.6,14.5 4.5,9.6 0.9,6.1 5.8,5.5" fill="#C4956A"/><polygon points="24,1 26.2,5.5 31.1,6.1 27.5,9.6 28.4,14.5 24,12.1 19.6,14.5 20.5,9.6 16.9,6.1 21.8,5.5" fill="#C4956A"/><polygon points="40,1 42.2,5.5 47.1,6.1 43.5,9.6 44.4,14.5 40,12.1 35.6,14.5 36.5,9.6 32.9,6.1 37.8,5.5" fill="#C4956A"/><polygon points="56,1 58.2,5.5 63.1,6.1 59.5,9.6 60.4,14.5 56,12.1 51.6,14.5 52.5,9.6 48.9,6.1 53.8,5.5" fill="#C4956A"/><polygon points="72,1 74.2,5.5 79.1,6.1 75.5,9.6 76.4,14.5 72,12.1 67.6,14.5 68.5,9.6 64.9,6.1 69.8,5.5" fill="#C4956A"/></svg>
                            <span class="rating-badge rating-badge--top">Top Rated</span>
                        </div>
                    </div>
                    <div class="platform-card__body">
                        <p>Women can specifically request a female therapist on BetterHelp &mdash; and with 30,000+ licensed professionals on the platform, that request actually gets fulfilled. Therapists who specialize in postpartum, hormonal transitions, relationship trauma, and burnout are well represented. Cost runs $65&ndash;100/week; financial aid available.</p>
                    </div>
                    <div class="platform-card__details"><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $65&ndash;100/week</span><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M8 1L2 4v4c0 3.3 2.6 6.4 6 7 3.4-.6 6-3.7 6-7V4L8 1z"/><path d="M6 8l2 2 3-3"/></svg> Financial aid available</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="1.5"/><circle cx="8" cy="8" r="1.5"/></svg> Video</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 4a2 2 0 012-2h1a2 2 0 012 2v7l-2.5 2L2 11V4zM14 4a2 2 0 00-2-2h-1a2 2 0 00-2 2v7l2.5 2L14 11V4z"/></svg> Phone</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3h10a1 1 0 011 1v6a1 1 0 01-1 1H7l-3 3v-3H3a1 1 0 01-1-1V4a1 1 0 011-1z"/></svg> Messaging</span></div>
                    <div class="platform-card__cta">
                        <span class="offer-tag">&#10022; Request a female therapist at signup &mdash; it\'s a standard option</span>
                        <a href="#" class="cta-button">Find a Therapist on BetterHelp</a>
                    </div>
                    <div class="platform-card__meta">
                        <span>Reviewed by Dr. Sarah Chen, LCSW</span>
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
                            <p class="platform-card__tagline">Best with insurance &mdash; strong coverage for women\'s mental health care</p>
                        </div>
                        <div class="platform-card__score">
                            <span class="score-number">4.4</span>
                            <svg class="score-stars" viewBox="0 0 80 16"><polygon points="8,1 10.2,5.5 15.1,6.1 11.5,9.6 12.4,14.5 8,12.1 3.6,14.5 4.5,9.6 0.9,6.1 5.8,5.5" fill="#C4956A"/><polygon points="24,1 26.2,5.5 31.1,6.1 27.5,9.6 28.4,14.5 24,12.1 19.6,14.5 20.5,9.6 16.9,6.1 21.8,5.5" fill="#C4956A"/><polygon points="40,1 42.2,5.5 47.1,6.1 43.5,9.6 44.4,14.5 40,12.1 35.6,14.5 36.5,9.6 32.9,6.1 37.8,5.5" fill="#C4956A"/><polygon points="56,1 58.2,5.5 63.1,6.1 59.5,9.6 60.4,14.5 56,12.1 51.6,14.5 52.5,9.6 48.9,6.1 53.8,5.5" fill="#C4956A"/><polygon points="72,1 74.2,5.5 79.1,6.1 75.5,9.6 76.4,14.5 72,12.1 67.6,14.5 68.5,9.6 64.9,6.1 69.8,5.5" fill="#EDE7DB"/></svg>
                            <span class="rating-badge rating-badge--recommended">Recommended</span>
                        </div>
                    </div>
                    <div class="platform-card__body">
                        <p>Talkspace covers therapy and psychiatry under most major insurance plans &mdash; useful for women managing postpartum depression, anxiety tied to hormonal shifts, or conditions that benefit from both talk therapy and medication management. Messaging format suits women who process better in writing. $10&ndash;50 copay range with insurance.</p>
                    </div>
                    <div class="platform-card__details"><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $10&ndash;50/session w/ insurance</span><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $69&ndash;109/week self-pay</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="1.5"/><circle cx="8" cy="8" r="1.5"/></svg> Video</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="2"/><path d="M2 5l6 4 6-4"/></svg> Messaging</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7"/></svg> Psychiatry</span></div>
                    <div class="platform-card__cta">
                        <span class="offer-tag">&#10022; Therapy and psychiatry in one platform &mdash; useful for hormonal conditions</span>
                        <a href="#" class="cta-button">Check Coverage on Talkspace</a>
                    </div>
                    <div class="platform-card__meta">
                        <span>Reviewed by Dr. Sarah Chen, LCSW</span>
                    </div>
                </article>

                <!-- CARD 3: Brightside -->
                <article class="platform-card reveal reveal-delay-2" data-rank="3">
                    <div class="platform-card__header">
                        <div class="platform-card__logo" style="background:#5C6BC0;color:#fff;font-weight:700;font-size:1.1rem;">
                            <img src="../assets/logos/brightside.webp" alt="Brightside logo" onerror="this.style.display=\'none\';this.parentElement.style.background=\'#5C6BC0\';this.parentElement.style.color=\'#fff\';this.parentElement.textContent=\'BS\';">
                        </div>
                        <div class="platform-card__identity">
                            <h3 class="platform-card__name">Brightside</h3>
                            <p class="platform-card__tagline">Best for anxiety + depression with medication &mdash; integrated care model</p>
                        </div>
                        <div class="platform-card__score">
                            <span class="score-number">4.3</span>
                            <svg class="score-stars" viewBox="0 0 80 16"><polygon points="8,1 10.2,5.5 15.1,6.1 11.5,9.6 12.4,14.5 8,12.1 3.6,14.5 4.5,9.6 0.9,6.1 5.8,5.5" fill="#C4956A"/><polygon points="24,1 26.2,5.5 31.1,6.1 27.5,9.6 28.4,14.5 24,12.1 19.6,14.5 20.5,9.6 16.9,6.1 21.8,5.5" fill="#C4956A"/><polygon points="40,1 42.2,5.5 47.1,6.1 43.5,9.6 44.4,14.5 40,12.1 35.6,14.5 36.5,9.6 32.9,6.1 37.8,5.5" fill="#C4956A"/><polygon points="56,1 58.2,5.5 63.1,6.1 59.5,9.6 60.4,14.5 56,12.1 51.6,14.5 52.5,9.6 48.9,6.1 53.8,5.5" fill="#C4956A"/><polygon points="72,1 74.2,5.5 79.1,6.1 75.5,9.6 76.4,14.5 72,12.1 67.6,14.5 68.5,9.6 64.9,6.1 69.8,5.5" fill="#EDE7DB"/></svg>
                            <span class="rating-badge rating-badge--recommended">Recommended</span>
                        </div>
                    </div>
                    <div class="platform-card__body">
                        <p>Brightside treats anxiety and depression with both therapy and medication management on one platform &mdash; a practical option for women where hormonal changes intersect with mood disorders. Psychiatry appointments available within days. Accepts most major insurance. $95&ndash;349/month depending on plan.</p>
                    </div>
                    <div class="platform-card__details"><span class="detail detail--price"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7M6 6.5c0-.8.9-1.5 2-1.5s2 .7 2 1.5-.9 1.5-2 1.5-2 .7-2 1.5.9 1.5 2 1.5"/></svg> $95&ndash;349/month</span><span class="detail detail--insurance"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M8 1L2 4v4c0 3.3 2.6 6.4 6 7 3.4-.6 6-3.7 6-7V4L8 1z"/><path d="M6 8l2 2 3-3"/></svg> Insurance accepted</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="3" width="12" height="10" rx="1.5"/><circle cx="8" cy="8" r="1.5"/></svg> Therapy</span><span class="detail detail--format"><svg class="detail__icon" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M8 4.5v7"/></svg> Psychiatry integrated</span></div>
                    <div class="platform-card__cta">
                        <span class="offer-tag">&#10022; Therapy and medication managed together &mdash; no separate referrals</span>
                        <a href="#" class="cta-button">Get Started on Brightside</a>
                    </div>
                    <div class="platform-card__meta">
                        <span>Reviewed by Dr. Sarah Chen, LCSW</span>
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
                            <a href="postpartum.html" class="fork-link">Online therapy for postpartum <span>&rarr;</span></a>
                            <a href="anxiety.html" class="fork-link">Online therapy for anxiety <span>&rarr;</span></a>
                            <a href="eating-disorders.html" class="fork-link">Online therapy for eating disorders <span>&rarr;</span></a>
                            <a href="conditions.html" class="fork-link">All conditions <span>&rarr;</span></a>
                        </div>
                    </div>
                    <div class="forks-image">
                        <img src="../assets/video-call-earbuds.webp" alt="Woman during an online therapy session" class="forks-image__img">
                    </div>
                </div>
            </div>
        </div>

        <!-- REVIEWER BIO -->
        <div class="section-wrapper section-wrapper--alt">
            <div class="content-container">
                <h2 class="section-heading">About Our Reviewer</h2>
                <div class="reviewer-card reveal">
                    <div class="reviewer-card__avatar">SC</div>
                    <div class="reviewer-card__content">
                        <h4 class="reviewer-card__name">Dr. Sarah Chen <span class="credential-badge">LCSW</span></h4>
                        <p class="reviewer-card__specialties">Women\'s Mental Health &middot; Postpartum &middot; Anxiety &middot; Identity</p>
                        <div class="reviewer-card__bio">
                            Dr. Chen is a Licensed Clinical Social Worker with 12 years of experience treating women\'s mental health concerns across the lifespan. She reviews all condition guides on Digital Therapy Solutions to ensure clinical accuracy.
                        </div>
                        <a href="#" class="link-subtle">View full bio &rarr;</a>
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

with open(r'D:\Work\Digital-Therapy-Solutions\output\womens-mental-health.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('womens-mental-health.html written OK')
