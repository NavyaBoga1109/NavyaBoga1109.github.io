/* Navya Boga — portfolio interactions.
   Progressive enhancement: without JS (or with reduced motion) all content is visible and static. */
(() => {
  const root = document.documentElement;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  root.classList.add("js");

  /* ---------- Mobile menu ---------- */
  const menuBtn = document.querySelector(".menu-btn");
  const menu = document.getElementById("menu");
  if (menuBtn && menu) {
    menuBtn.addEventListener("click", () => {
      const open = menu.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", String(open));
    });
  }

  /* ---------- Footer year ---------- */
  document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

  /* ---------- Certification filters (works with or without motion) ---------- */
  const chips = [...document.querySelectorAll(".chip[data-filter]")];
  const certCards = [...document.querySelectorAll("#cert-grid .cert")];
  const certCount = document.getElementById("cert-count");
  chips.forEach((chip) => chip.addEventListener("click", () => {
    const f = chip.dataset.filter;
    chips.forEach((c) => c.setAttribute("aria-pressed", String(c === chip)));
    let shown = 0;
    certCards.forEach((card) => {
      const match = f === "all" || card.dataset.cat === f;
      card.hidden = !match;
      if (match) { shown++; card.classList.add("in"); }
    });
    if (certCount) certCount.textContent = `${shown} certifications shown`;
  }));

  if (reduce) return; // everything below is motion only

  /* ---------- Page transition curtain ---------- */
  const curtain = document.createElement("div");
  curtain.className = "curtain";
  curtain.setAttribute("aria-hidden", "true");
  document.body.appendChild(curtain);
  requestAnimationFrame(() => requestAnimationFrame(() => curtain.classList.add("gone")));
  window.addEventListener("pageshow", (e) => { if (e.persisted) curtain.classList.replace("cover", "gone"); });

  document.addEventListener("click", (e) => {
    const a = e.target.closest("a[href]");
    if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
    const url = new URL(a.href, location.href);
    const internalPage = url.origin === location.origin && /\.html$|\/$/.test(url.pathname) && !a.target && !a.hasAttribute("download");
    if (!internalPage || (url.pathname === location.pathname && url.hash)) return;
    e.preventDefault();
    curtain.classList.remove("gone");
    curtain.classList.add("cover");
    setTimeout(() => (location.href = url.href), 450);
  });

  /* ---------- Split headlines into words ---------- */
  document.querySelectorAll(".split").forEach((el) => {
    const label = el.textContent.trim().replace(/\s+/g, " ");
    el.setAttribute("aria-label", label);
    let i = 0;
    const wrap = (node) => {
      [...node.childNodes].forEach((child) => {
        if (child.nodeType === Node.TEXT_NODE) {
          const frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(" ")); return; }
            const w = document.createElement("span");
            w.className = "w";
            w.setAttribute("aria-hidden", "true");
            const inner = document.createElement("span");
            inner.textContent = part;
            inner.style.setProperty("--i", i++);
            w.appendChild(inner);
            frag.appendChild(w);
          });
          child.replaceWith(frag);
        } else if (child.nodeType === Node.ELEMENT_NODE) {
          wrap(child);
        }
      });
    };
    wrap(el);
  });

  /* ---------- Reveal on enter ---------- */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      en.target.classList.add("in");
      io.unobserve(en.target);
    });
  }, { threshold: 0.15, rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll("[data-reveal], .split").forEach((el) => io.observe(el));

  /* ---------- Counters ---------- */
  const countIO = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      const el = en.target;
      const target = parseFloat(el.dataset.count);
      const decimals = (el.dataset.count.split(".")[1] || "").length;
      const start = performance.now();
      const dur = 1600;
      const tick = (t) => {
        const p = Math.min(1, (t - start) / dur);
        const eased = 1 - Math.pow(1 - p, 4);
        el.textContent = (target * eased).toFixed(decimals);
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      countIO.unobserve(el);
    });
  }, { threshold: 0.6 });
  document.querySelectorAll("[data-count]").forEach((el) => countIO.observe(el));

  /* ---------- Cursor glow on cards ---------- */
  document.querySelectorAll(".card").forEach((card) => {
    card.addEventListener("pointermove", (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty("--mx", `${e.clientX - r.left}px`);
      card.style.setProperty("--my", `${e.clientY - r.top}px`);
    });
  });

  /* ---------- Scroll-linked effects (single rAF loop) ---------- */
  const progress = document.querySelector(".progress");
  const heroInner = document.querySelector(".hero-inner");
  const pin = document.querySelector(".pin");
  const track = pin && pin.querySelector(".track");
  const litWords = [...document.querySelectorAll(".statement .lit")];
  const timeline = document.querySelector(".timeline");
  const parallax = [...document.querySelectorAll("[data-parallax]")];
  const mobile = window.matchMedia("(max-width: 760px)");

  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  let ticking = false;

  const update = () => {
    ticking = false;
    const vh = window.innerHeight;
    const sy = window.scrollY;
    const max = document.documentElement.scrollHeight - vh;

    if (progress) progress.style.setProperty("--p", max > 0 ? sy / max : 0);

    // Hero: recede into the screen as you scroll away
    if (heroInner) {
      const p = clamp(sy / (vh * 0.9));
      heroInner.style.transform = `translateY(${p * 80}px) scale(${1 - p * 0.12})`;
      heroInner.style.opacity = String(1 - p * 1.1);
      heroInner.style.filter = `blur(${p * 10}px)`;
    }

    // Pinned horizontal gallery
    if (pin && track && !mobile.matches) {
      const r = pin.getBoundingClientRect();
      const span = pin.offsetHeight - vh;
      const p = clamp(-r.top / span);
      const dist = track.scrollWidth - window.innerWidth + 80;
      track.style.transform = `translate3d(${-p * Math.max(0, dist)}px,0,0)`;
    } else if (track) {
      track.style.transform = "";
    }

    // Statement words light up as they cross the reading line
    const line = vh * 0.62;
    litWords.forEach((w) => w.classList.toggle("on", w.getBoundingClientRect().top < line));

    // Timeline fill
    if (timeline) {
      const r = timeline.getBoundingClientRect();
      timeline.style.setProperty("--tl", clamp((vh * 0.6 - r.top) / r.height));
    }

    // Gentle parallax
    parallax.forEach((el) => {
      const r = el.parentElement.getBoundingClientRect();
      const p = (r.top + r.height / 2 - vh / 2) / vh;
      el.style.transform = `translate3d(0, ${p * -40 * (parseFloat(el.dataset.parallax) || 1)}px, 0)`;
    });
  };

  // Split statement paragraphs into individually lit words
  document.querySelectorAll(".statement p:not(.eyebrow)").forEach((p) => {
    const html = p.innerHTML;
    p.setAttribute("aria-label", p.textContent.trim().replace(/\s+/g, " "));
    const tmp = document.createElement("div");
    tmp.innerHTML = html;
    const out = [];
    tmp.childNodes.forEach((n) => {
      const hl = n.nodeType === Node.ELEMENT_NODE && n.tagName === "EM";
      n.textContent.split(/\s+/).filter(Boolean).forEach((word) => {
        out.push(`<span class="lit${hl ? " hl" : ""}" aria-hidden="true">${word.replace(/</g, "&lt;")}</span>`);
      });
    });
    p.innerHTML = out.join(" ");
  });
  litWords.push(...document.querySelectorAll(".statement .lit"));

  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  update();
})();
