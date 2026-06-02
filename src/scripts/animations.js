// Animations and Motion Effects

export function initScrollProgress() {
  const scrollBar = document.getElementById('scrollProgress');
  if (!scrollBar) return;

  function updateProgress() {
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled = (window.scrollY / scrollHeight) * 100;
    scrollBar.style.width = scrolled + '%';
  }

  window.addEventListener('scroll', updateProgress);
}

export function initNavScroll() {
  const nav = document.getElementById('nav');
  if (!nav) return;

  function updateNav() {
    if (window.scrollY > 50) {
      nav.classList.add('nav-scrolled');
    } else {
      nav.classList.remove('nav-scrolled');
    }
  }

  window.addEventListener('scroll', updateNav);
}

export function initRevealAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // Stagger children
  document.querySelectorAll('.stagger-children').forEach(container => {
    Array.from(container.children).forEach((child, i) => {
      (child as HTMLElement).style.setProperty('--stagger-index', String(i));
    });
    observer.observe(container);
  });
}

export function initSplitWords() {
  if (typeof gsap === 'undefined') return;

  document.querySelectorAll('[data-anim="split-words"]').forEach(el => {
    const text = el.textContent;
    const words = text?.split(' ') || [];
    el.innerHTML = words.map(w =>
      `<span class="word-wrapper"><span class="word">${w}</span></span>`
    ).join(' ');

    gsap.from((el as HTMLElement).querySelectorAll('.word'), {
      opacity: 0,
      y: '100%',
      duration: 0.8,
      stagger: 0.04,
      ease: 'power3.out',
    });
  });
}

export function initChartResize() {
  let resizeTimeout: NodeJS.Timeout;

  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      if (typeof window.renderChart === 'function') {
        window.renderChart();
      }
    }, 200);
  });
}

export function initAnimations() {
  // Render chart on load
  window.addEventListener('load', () => {
    if (typeof window.renderChart === 'function') {
      window.renderChart();
    }
  });

  initScrollProgress();
  initNavScroll();
  initRevealAnimations();
  initSplitWords();
  initChartResize();
}
