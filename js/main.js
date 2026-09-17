/* ============================================================
   Jeong AI. Shared page behaviour.
   DOM contract: #site-header, #mobile-toggle, #main-nav,
   #audit-form, #newsletter-form. Anything absent is skipped.
   ============================================================ */

(function () {
  'use strict';

  // ---------- MASTHEAD NAV (phone) ----------
  var toggle = document.getElementById('mobile-toggle');
  var nav = document.getElementById('main-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = toggle.classList.toggle('active');
      nav.classList.toggle('open', isOpen);
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        toggle.classList.remove('active');
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        toggle.classList.remove('active');
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // ---------- SMOOTH SCROLL for same-page anchors ----------
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var id = this.getAttribute('href');
      if (id.length < 2) return;
      var target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
        history.replaceState(null, '', id);
      }
    });
  });

  // ---------- WEB3FORMS ----------
  function wireForm(form, opts) {
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var originalText = btn.textContent;
      btn.textContent = opts.sending;
      btn.disabled = true;

      fetch('https://api.web3forms.com/submit', { method: 'POST', body: new FormData(form) })
        .then(function (res) { return res.json(); })
        .then(function (json) {
          if (!json.success) throw new Error(json.message || 'Submission failed');
          btn.textContent = opts.done;
          btn.classList.add('is-success');
          form.reset();
          if (typeof gtag === 'function') gtag('event', opts.event, { event_category: opts.category });
          setTimeout(function () {
            btn.textContent = originalText;
            btn.classList.remove('is-success');
            btn.disabled = false;
          }, 4000);
        })
        .catch(function () {
          btn.textContent = opts.failed;
          btn.classList.add('is-error');
          setTimeout(function () {
            btn.textContent = originalText;
            btn.classList.remove('is-error');
            btn.disabled = false;
          }, 6000);
        });
    });
  }

  wireForm(document.getElementById('audit-form'), {
    sending: 'Sending',
    done: 'Received. We will be in touch.',
    failed: 'Something went wrong. Email info@jeongai.com',
    event: 'generate_lead',
    category: 'audit_form'
  });

  wireForm(document.getElementById('newsletter-form'), {
    sending: 'Sending',
    done: 'You are on the list.',
    failed: 'Something went wrong. Try again.',
    event: 'sign_up',
    category: 'newsletter'
  });

})();
