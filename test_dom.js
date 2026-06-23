const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf8');

const dom = new JSDOM('<script>class ResizeObserver { observe() {} unobserve() {} disconnect() {} }; window.HTMLCanvasElement.prototype.getContext = function () { return { fillRect: function() {}, clearRect: function(){}, getImageData: function(x, y, w, h) { return { data: new Array(w*h*4) }; }, putImageData: function() {}, createImageData: function(){ return []}, setTransform: function(){}, drawImage: function(){}, save: function(){}, fillText: function(){}, restore: function(){}, beginPath: function(){}, moveTo: function(){}, lineTo: function(){}, closePath: function(){}, stroke: function(){}, translate: function(){}, scale: function(){}, rotate: function(){}, arc: function(){}, fill: function(){}, measureText: function(){ return { width: 0 }; }, transform: function(){}, rect: function(){}, clip: function(){}, }; };</script>' + html, { runScripts: "dangerously", resources: "usable" });

const window = dom.window;

let store = {};
window.localStorage = {
  getItem: (key) => store[key] || null,
  setItem: (key, val) => store[key] = val,
  removeItem: (key) => delete store[key],
  clear: () => store = {}
};

window.localStorage.setItem('lgf_session', JSON.stringify({email:'khebadeyash1234@gmail.com', name:'K'}));
window.localStorage.setItem('lgf_user_khebadeyash1234@gmail.com', JSON.stringify({projects:{}}));

setTimeout(() => {
  try {
    window.authLoad();
    const grid = window.document.getElementById('proj-grid');
    console.log("proj-grid content length:", grid.innerHTML.length);
    console.log("Is '+New Project' inside grid?:", grid.innerHTML.includes('New Project'));
  } catch(e) {
    console.error("Error:", e);
  }
  process.exit(0);
}, 1000);
