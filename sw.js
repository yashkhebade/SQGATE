const CACHE_NAME = 'sqgate-cache-v5';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/home/index.html',
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
  '/login_bg.webp',
  '/simulator_preview.webp',
  '/manifest.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        return cache.addAll(ASSETS_TO_CACHE);
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
  // Only intercept GET requests and HTTP/HTTPS schemes (ignore chrome-extension, data, etc)
  if (event.request.method !== 'GET' || !event.request.url.startsWith('http')) return;

  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Return cached response if found
        if (response) {
          return response;
        }
        
        // Otherwise fetch from network
        return fetch(event.request).then((networkResponse) => {
          // Cache the new fetched response for future (only cache same-origin basic responses)
          if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
            const responseToCache = networkResponse.clone();
            caches.open(CACHE_NAME)
              .then((cache) => {
                cache.put(event.request, responseToCache);
              });
          }
          return networkResponse;
        }).catch((err) => {
          // If offline and not in cache, we MUST throw the error so the browser handles the failure natively
          // Returning undefined would cause a TypeError that triggers the global error handler
          throw err;
        });
      })
  );
});
