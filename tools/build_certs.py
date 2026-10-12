"""Generate certifications.html from the CERTS list below.

Edit CERTS, then run:  python3 tools/build_certs.py
Each entry: (title, issuer, issued, note, category, credential_url, featured)
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CERTS = [
    ("Machine Learning University — AICOD", "Amazon", "Mar 2026", "", "ai", "https://drive.google.com/file/d/14YLofGOXDPajJXoGU7zkvl8UcS2Kyqod/view?usp=sharing", True),
    ("Machine Learning University — AIFUN", "Amazon Web Services", "Feb 2026", "", "ai", "https://drive.google.com/file/d/1xHYR9XxlEhe1ZlI7EsP-z-SiT1NueKWz/view?usp=sharing", True),
    ("OCI 2024 Generative AI Certified Professional", "Oracle", "Jul 2024", "ID OC5117906", "ai", "https://drive.google.com/file/d/1_0bpCjKd9hlJNSIzI2iEFgmc5gCAtSvY/view?usp=sharing", True),
    ("AWS Academy Graduate — Cloud Foundations", "Amazon Web Services", "May 2022", "", "cloud", "https://www.credly.com/badges/af96cb7b-d1a2-49dc-ae7c-9452e858cc90", True),
    ("CyberOps Associate", "Cisco", "Jan 2023", "", "security", "https://www.credly.com/badges/d3baa946-cdc1-4af1-8b9d-0a18cd8600c5", True),
    ("SQL and Relational Databases 101", "IBM (cognitiveclass.ai)", "Feb 2025", "", "data", "https://courses.cognitiveclass.ai/certificates/9720abbef7dc42de90206864f57ef0e9", True),

    ("Google Analytics Individual Qualification", "Google", "Feb 2025", "Expired Feb 2026", "data", "https://skillshop.credential.net/24fc77ec-8056-4b21-b123-37b9d24d1896", False),
    ("Basic Human Subject Protections + Good Clinical Practice", "CITI Program", "Jun 2024", "Valid to Jun 2027", "data", "https://www.citiprogram.org/verify/?w91f70707-e7b3-45cc-a947-f86db870013b-63147509", False),
    ("Google Digital Garage", "Google", "Feb 2023", "", "dev", "https://drive.google.com/file/d/1aVefvzjTzXsjVtzZ4Ln3lT7w-nZ04eCg/view?usp=share_link", False),
    ("Introduction to Cybersecurity", "Cisco", "May 2021", "", "security", "https://www.credly.com/badges/522e3f38-6b19-45ec-be95-d6b9bd8a982e", False),
    ("Cybersecurity Essentials", "Cisco", "May 2021", "", "security", "https://www.credly.com/badges/818085e1-01c0-4421-bb52-1b7cc3c23d46", False),
    ("Cloud Core", "IBM", "May 2021", "", "cloud", "https://www.credly.com/badges/677c6fc5-7139-4ed6-811e-ce02db4567b5", False),
    ("Front End Web Development", "Great Learning", "Jul 2022", "", "dev", "https://drive.google.com/file/d/1CsC65nD2EWGTKa657JIcX1bphi3MpbJY/view?usp=drivesdk", False),
    ("Blockchain Technology and Applications", "IETE", "May 2022", "", "dev", "https://drive.google.com/file/d/1PR9KKQA-6xIURvHMu3IVPmvVydfXqJid/view?usp=sharing", False),
    ("Artificial Intelligence Primer", "Infosys", "May 2022", "", "ai", "https://drive.google.com/file/d/1rkrf8ir8gpGtK9xhBnB-0i3e8hVPj2n9/view?usp=sharing", False),
    ("AVR Microcontroller Programming", "Microchip Technology", "May 2021", "", "dev", "https://drive.google.com/file/d/1-nuDL9yOAvyt0SfKnCsoi71GO_6BAACK/view?usp=sharing", False),
    ("Version Control with Git", "Atlassian", "May 2021", "", "dev", "https://drive.google.com/file/d/1OYuQxcxp9UusE8aK3YLHdppcMebeLzUL/view?usp=sharing", False),
    ("Aruba Networking Basics", "HPE Aruba Networking", "May 2021", "", "cloud", "https://drive.google.com/file/d/1CFWw2i5qw-hE3C4Cp1u1oLI_JZvjs02a/view?usp=sharing", False),
    ("IBM Development Skills", "IBM", "Aug 2021", "", "dev", "https://drive.google.com/file/d/1P8nnUusJ8_XAklDRZX9tzwQTG6PA4cLt/view?usp=sharing", False),
    ("Java Fundamentals", "Oracle", "Sep 2021", "", "dev", "https://drive.google.com/file/d/1_7jY5ZYl69RBAiMt4ABJjT4cV9l5oxga/view?usp=sharing", False),
    ("Java Training", "Spoken Tutorial, IIT Bombay", "Aug 2021", "", "dev", "https://drive.google.com/file/d/1uU991ib0LaRWyRmdGll9AAigMwuL4VsF/view?usp=sharing", False),
    ("Database Programming with SQL", "Oracle", "Sep 2021", "", "data", "https://drive.google.com/file/d/1NNYHTxXto1hwTXzlvfwZ-OeTk4m7GYqw/view?usp=sharing", False),
    ("Intel Distribution of OpenVINO Toolkit for Computer Vision", "Intel", "May 2021", "", "ai", "https://drive.google.com/file/d/1cSgU0TnNC66XiQS43foMx1UfiFj9NMo-/view?usp=sharing", False),
    ("Python for Data Science", "Great Learning", "May 2022", "", "data", "https://drive.google.com/file/d/1M5v87BMah-H8n28mDxopEvGlS9enWgJr/view?usp=sharing", False),
    ("Intro to Cybersecurity · Intro to IoT · Cybersecurity Essentials", "Cisco Networking Academy", "May 2021", "", "security", "https://drive.google.com/file/d/1dmnz2d4ZZpnZR2B7zNaqD6IgP4u042PD/view?usp=sharing", False),
    ("Introduction to Cloud Identity", "Google", "May 2021", "", "cloud", "https://drive.google.com/file/d/1fBmvHOHukniy37QuLrbZnMafx8aPLPDS/view?usp=sharing", False),
    ("Artificial Intelligence: Digital Skills", "Accenture", "May 2021", "", "ai", "https://drive.google.com/file/d/1LmIUyENl-jfxFhvh7Pg1MKpC1VTVbK8J/view?usp=sharing", False),

    ("IGNITE 2023 Internship", "LTIMindtree", "Feb 2023", "", "intern", "https://drive.google.com/file/d/136QRC5dEWvIm_Is2Jefrl_i3Vf_vh9Ra/view?usp=drive_link", False),
    ("Web Application Developer Internship", "Suntek Corp Solutions", "Sep 2022", "", "intern", "https://drive.google.com/file/d/1g88lU3kcm1Df-00rn-GQjQreLqMDrgip/view?usp=sharing", False),
    ("DRDO Internship", "Defence Research and Development Organisation", "Apr 2022", "", "intern", "https://drive.google.com/file/d/13483s6f3SbGwkTv1UZJ_sJOo53MiBwjW/view?usp=sharing", False),
]

CATS = {
    "ai": ("AI & ML", '<path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3"/><rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 10h4v4h-4z"/>'),
    "cloud": ("Cloud", '<path d="M7 18a4 4 0 0 1-.5-8A6 6 0 0 1 18 9a4.5 4.5 0 0 1-.5 9z"/>'),
    "security": ("Security", '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9.5 12.5l2 2 3.5-4"/>'),
    "data": ("Data", '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3 3 7 3s7-1.3 7-3V6M5 12v6c0 1.7 3 3 7 3s7-1.3 7-3v-6"/>'),
    "dev": ("Development", '<path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>'),
    "intern": ("Internships", '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>'),
}


def icon(cat):
    return f'<span class="icon" aria-hidden="true"><svg viewBox="0 0 24 24">{CATS[cat][1]}</svg></span>'


def card(c, i, big):
    title, issuer, issued, note, cat, url, _ = c
    meta = f"{escape(issuer)} · {escape(issued)}"
    note_html = f'<span class="cert-note">{escape(note)}</span>' if note else ""
    cls = "card cert big" if big else "card cert"
    return (
        f'          <a class="{cls}" data-cat="{cat}" href="{escape(url)}" target="_blank" rel="noopener" data-reveal style="--d:{(i % 3) * 90}ms">\n'
        f'            <div class="panel-top">{icon(cat)}<span class="num-badge">{escape(CATS[cat][0].upper())}</span></div>\n'
        f'            <h3>{escape(title)}</h3>\n'
        f'            <p>{meta}</p>{note_html}\n'
        f'            <span class="go">Show credential <span class="sr-only">for {escape(title)} (opens in new tab)</span>→</span>\n'
        f'          </a>'
    )


featured = [c for c in CERTS if c[6]]
rest = [c for c in CERTS if not c[6]]

src = (ROOT / "projects.html").read_text()
head, _, _ = src.partition("  <main id=\"main\">")
_, _, tail = src.partition("  </main>")
head = (head.replace("<title>Projects — Navya Boga</title>", "<title>Certifications — Navya Boga</title>")
        .replace('content="Projects by Navya Boga: ML emblem detection, e-commerce platform, real-time chat, facial recognition."',
                 f'content="{len(CERTS)} certifications earned by Navya Boga across AI, cloud, security, data, and development."')
        .replace(' aria-current="page"', "")
        .replace('href="certifications.html">', 'href="certifications.html" aria-current="page">'))

chips = ['<button type="button" class="chip" aria-pressed="true" data-filter="all">All</button>']
for key, (label, _) in CATS.items():
    n = sum(1 for c in rest if c[4] == key)
    if n:
        chips.append(f'<button type="button" class="chip" aria-pressed="false" data-filter="{key}">{label} <span>{n}</span></button>')

main = f'''  <main id="main">
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow" data-reveal>Certifications</p>
        <h1 class="split">Always <span class="grad">learning.</span></h1>
        <p class="lead" data-reveal style="--d:400ms">{len(CERTS)} certifications across AI, cloud, security, data, and software development. Each card links to the credential.</p>
      </div>
    </section>

    <section aria-labelledby="feat-h" style="padding-top:0">
      <div class="wrap">
        <p class="eyebrow" data-reveal>Featured</p>
        <h2 id="feat-h" class="title split">Highlights</h2>
        <div class="cards certs" style="margin-top:3rem">
{chr(10).join(card(c, i, True) for i, c in enumerate(featured))}
        </div>
      </div>
    </section>

    <section aria-labelledby="all-h" style="padding-top:2rem">
      <div class="wrap">
        <p class="eyebrow" data-reveal>Everything else</p>
        <h2 id="all-h" class="title split">All certifications</h2>
        <div class="chips" role="group" aria-label="Filter certifications by category" data-reveal>
          {chr(10).join("          " + ch if j else ch for j, ch in enumerate(chips))}
        </div>
        <p class="sr-only" aria-live="polite" id="cert-count"></p>
        <div class="cards certs" id="cert-grid" style="margin-top:2rem">
{chr(10).join(card(c, i, False) for i, c in enumerate(rest))}
        </div>
      </div>
    </section>
'''

(ROOT / "certifications.html").write_text(head + main + "  </main>" + tail)
print(f"wrote certifications.html: {len(featured)} featured, {len(rest)} others")
