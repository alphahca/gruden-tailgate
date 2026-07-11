self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('fetch', (e) => {
  // Keeps the app line open and flowing
  e.respondWith(fetch(e.request));
});
