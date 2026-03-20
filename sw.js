// Simple cache-first Service Worker for a static PWA (GitHub Pages friendly)
const CACHE_NAME = 'gonitwa-pwa-v1';

const ASSETS = [
  './',
  './index.html',
  './game.js',
  './manifest.webmanifest',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(
      keys.map((key) => (key === CACHE_NAME ? Promise.resolve() : caches.delete(key)))
    );
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  event.respondWith((async () => {
    // 1) Try cache (ignoring query params)
    const cached = await caches.match(event.request, { ignoreSearch: true });
    if (cached) return cached;

    // 2) Fall back to network, then cache same-origin responses
    try {
      const res = await fetch(event.request);

      const url = new URL(event.request.url);
      if (url.origin === self.location.origin) {
        const cache = await caches.open(CACHE_NAME);
        cache.put(event.request, res.clone());
      }

      return res;
    } catch (e) {
      // 3) Offline fallback to the app shell
      const fallback = await caches.match('./index.html');
      if (fallback) return fallback;
      throw e;
    }
  })());
});
