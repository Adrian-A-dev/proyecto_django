// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/app/css/estilos.css',
    '/static/app/img/png/bmw.png',
    '/static/app/img/png/mercedes-benz.png',
    '/static/app/img/png/nissan.png',
    '/static/app/img/png/subaru.png',
    '/static/app/img/png/suzuki.png',
    '/static/app/img/png/toyota.png',
    '/static/app/img/icono.png',
    '/static/app/img/menuiconwhite.png',
    '/static/images/icons/splash-640x1136.png',
    '/static/images/icons/splash-750x1334.png',
    '/static/images/icons/splash-1242x2208.png',
    '/static/images/icons/splash-1125x2436.png',
    '/static/images/icons/splash-828x1792.png',
    '/static/images/icons/splash-1242x2688.png',
    '/static/images/icons/splash-1536x2048.png',
    '/static/images/icons/splash-1668x2224.png',
    '/static/images/icons/splash-1668x2388.png',
    '/static/images/icons/splash-2048x2732.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
/*self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});*/

self.addEventListener("fetch", function(event){
    event.respondWith(
        fetch(event.request)
            .then(function(result){
                return caches.open(staticCacheName)
                    .then(function(c){
                        c.put(event.request.url, result.clone())
                        return result;
                    })
            
            })        
            .catch(function(e){
                return caches.match(event.request)

            })
    )
})

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');


var firebaseConfig = {
    apiKey: "AIzaSyCPfBDlHf1l-T0pdPNuDMvk4V4iyPaGx08",
    authDomain: "carwash-7f42d.firebaseapp.com",
    projectId: "carwash-7f42d",
    storageBucket: "carwash-7f42d.appspot.com",
    messagingSenderId: "1029481259531",
    appId: "1:1029481259531:web:d0ffc1f53d72535065dd0e"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);


  let messaging  = firebase.messaging();

  
messaging.setBackgroundMessageHandler(function(payload) {

    let title = payload.notification.title;
    let options = {
        body: payload.notification.body,
        icon: payload.notification.icon
    }

    self.registration.showNotification(title, options);
});