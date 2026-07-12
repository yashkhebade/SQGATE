const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');
html = html.replace(/<style>[\s\S]*?<\/style>/g, '');
const modified = html.replace('<head>', '<head><script>window.onerror = function(msg, src, ln, col, err) { console.error("INJECTED ERROR:", msg, "LINE:", ln, "COL:", col); if(err) console.error(err.stack); };</script>');
const jsdom = require('jsdom');
const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("log", function (message) {
  console.log("browser console.log:", message);
});
virtualConsole.on("jsdomError", function (error) {
  console.log("jsdom error:", error.stack || error);
});
new jsdom.JSDOM(modified, { runScripts: 'dangerously', virtualConsole });
