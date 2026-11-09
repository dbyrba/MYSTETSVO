/**
 * MYSTETSVO — Art & Culture Hub
 * Lightweight interactive UI & UX script
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Drawer Toggle & Backdrop
  const menuToggle = document.getElementById('menu-toggle');
  const navLinks = document.querySelectorAll('.nav a');
  
  if (menuToggle) {
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 760) {
          menuToggle.checked = false;
        }
      });
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && menuToggle.checked) {
        menuToggle.checked = false;
      }
    });
  }

  // 2. City Selector persistence & toast
  const citySelect = document.querySelector('.city-select select');
  if (citySelect) {
    const savedCity = localStorage.getItem('mystetstvo_city');
    if (savedCity) {
      citySelect.value = savedCity;
    }
    citySelect.addEventListener('change', (e) => {
      localStorage.setItem('mystetstvo_city', e.target.value);
      showToast(`Обрано місто: ${e.target.value}. Події адаптовано.`);
    });
  }

  // 3. Search Bar feedback
  const searchInput = document.querySelector('.search-field input');
  if (searchInput) {
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        const query = searchInput.value.trim();
        if (query) {
          showToast(`Пошук за запитом «${query}» виконано`);
        }
      }
    });
  }

  // 4. Video Showcase Play/Pause Overlay Enhancements
  const video = document.getElementById('main-art-video');
  const playBtn = document.getElementById('video-play-btn');
  if (video && playBtn) {
    playBtn.addEventListener('click', () => {
      if (video.paused) {
        video.play();
        playBtn.style.opacity = '0';
        playBtn.style.pointerEvents = 'none';
      } else {
        video.pause();
        playBtn.style.opacity = '1';
        playBtn.style.pointerEvents = 'auto';
      }
    });

    video.addEventListener('play', () => {
      playBtn.style.opacity = '0';
      playBtn.style.pointerEvents = 'none';
    });

    video.addEventListener('pause', () => {
      playBtn.style.opacity = '1';
      playBtn.style.pointerEvents = 'auto';
    });
  }

  // 5. Gallery Filtering
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-grid .gallery-item');
  if (filterBtns.length > 0 && galleryItems.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.getAttribute('data-filter');

        galleryItems.forEach(item => {
          const category = item.getAttribute('data-category');
          if (filter === 'all' || category === filter) {
            item.style.display = '';
            item.style.opacity = '0';
            setTimeout(() => { item.style.opacity = '1'; }, 20);
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // 6. Events Filtering
  const eventFilterBtns = document.querySelectorAll('.events-filter-btn');
  const eventCards = document.querySelectorAll('.events-page .event-card, .events-section .event-card');
  if (eventFilterBtns.length > 0 && eventCards.length > 0) {
    eventFilterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        eventFilterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const type = btn.getAttribute('data-filter');

        eventCards.forEach(card => {
          const cardType = card.getAttribute('data-type');
          if (type === 'all' || cardType === type) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // 7. "В календар" Button
  const calendarButtons = document.querySelectorAll('.calendar-button');
  calendarButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const card = btn.closest('.event-card');
      const title = card ? card.querySelector('h3')?.textContent : 'Подію';
      showToast(`«${title}» успішно додано до вашого Google Календаря`);
    });
  });

  // 8. Registration Modal RSVP
  const registerModal = document.getElementById('register-modal');
  const registerBtns = document.querySelectorAll('.event-register');
  const modalCloseBtns = document.querySelectorAll('.modal-close, .modal-backdrop');

  if (registerModal) {
    registerBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const card = btn.closest('.event-card');
        const title = card ? card.querySelector('h3')?.textContent : 'Подія';
        const modalEventName = document.getElementById('modal-event-name');
        if (modalEventName) modalEventName.textContent = title;
        registerModal.classList.add('is-open');
      });
    });

    const regForm = document.getElementById('register-form');
    if (regForm) {
      regForm.addEventListener('submit', (e) => {
        e.preventDefault();
        registerModal.classList.remove('is-open');
        showToast('Дякуємо! Реєстрацію підтверджено. Квиток надіслано на email.');
        regForm.reset();
      });
    }
  }

  // Lightbox Modal for Artworks
  const artworkModal = document.getElementById('artwork-modal');
  const artworkCards = document.querySelectorAll('.gallery-item, .artwork-zoom-trigger');
  if (artworkModal) {
    artworkCards.forEach(item => {
      item.addEventListener('click', (e) => {
        if (e.target.closest('a') && !e.target.closest('.artwork-zoom-trigger')) return;
        const img = item.querySelector('img');
        const title = item.querySelector('strong')?.textContent || item.querySelector('h2')?.textContent || 'Художній твір';
        const author = item.querySelector('span')?.textContent || 'Резидент MYSTETSVO';
        
        const modalImg = artworkModal.querySelector('.modal-art-img');
        const modalTitle = artworkModal.querySelector('.modal-art-title');
        const modalAuthor = artworkModal.querySelector('.modal-art-author');

        if (modalImg && img) modalImg.src = img.src;
        if (modalTitle) modalTitle.textContent = title;
        if (modalAuthor) modalAuthor.textContent = author;

        artworkModal.classList.add('is-open');
      });
    });
  }

  // Close modals on click
  modalCloseBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      if (e.target === btn) {
        document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('is-open'));
      }
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('is-open'));
    }
  });

  // 9. Contact Forms Submission
  const contactForms = document.querySelectorAll('.contact-form');
  contactForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      showToast('Дякуємо! Ваше звернення надіслано кураторам хабу.');
      form.reset();
    });
  });

  // Newsletter
  const newsletterForms = document.querySelectorAll('.newsletter form');
  newsletterForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      showToast('Ви успішно підписалися на культурний дайджест MYSTETSVO!');
      form.reset();
    });
  });
});

// Toast notification helper
function showToast(message) {
  let toast = document.getElementById('site-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'site-toast';
    toast.className = 'toast';
    toast.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--sand);flex-shrink:0;"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg><span id="toast-text"></span>`;
    document.body.appendChild(toast);
  }
  const textElem = toast.querySelector('#toast-text');
  if (textElem) textElem.textContent = message;
  toast.classList.add('show');
  
  clearTimeout(window._toastTimeout);
  window._toastTimeout = setTimeout(() => {
    toast.classList.remove('show');
  }, 4000);
}
