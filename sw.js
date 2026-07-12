const CACHE_NAME = 'sqgate-cache-v59';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/cookie-consent.js',
  '/circuit-simulator/index.html',
  '/fsm/index.html',
  '/k-map/index.html',
  '/puzzle/index.html',
  '/contact.html',
  '/pricing.html',
  '/privacy.html',
  '/refund.html',
  '/terms.html',
  '/truth-table-generator.html',
  '/verilog-simulator.html',
  '/icon.webp',
  '/login_bg_v3.png',
  '/simulator_preview.webp',
  '/manifest.json',
  '/blog/assets/blog-demo.css',
  '/blog/assets/blog-demo.js'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        // Cache each asset individually so one failure doesn't block the whole install
        return Promise.allSettled(
          ASSETS_TO_CACHE.map(url => cache.add(url).catch(err => {
            console.warn('SW: Failed to cache', url, err);
          }))
        );
      })
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  // Only intercept GET requests and HTTP/HTTPS schemes
  if (event.request.method !== 'GET' || !event.request.url.startsWith('http')) return;

  const url = new URL(event.request.url);
  const isHTML = event.request.mode === 'navigate' ||
                 url.pathname.endsWith('.html') ||
                 url.pathname.endsWith('/');

  if (isHTML) {
    // NETWORK-FIRST for HTML pages: always try network, fall back to cache
    event.respondWith(
      fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
            const responseToCache = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseToCache);
            });
          }
          return networkResponse;
        })
        .catch(() => {
          // Offline: fall back to cache
          return caches.match(event.request);
        })
    );
  } else {
    // CACHE-FIRST for static assets (images, JS, CSS, fonts)
    event.respondWith(
      caches.match(event.request)
        .then((response) => {
          if (response) return response;
          return fetch(event.request).then((networkResponse) => {
            if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
              const responseToCache = networkResponse.clone();
              caches.open(CACHE_NAME).then((cache) => {
                cache.put(event.request, responseToCache);
              });
            }
            return networkResponse;
          });
        })
        .catch((err) => {
          throw err;
        })
    );
  }
});
