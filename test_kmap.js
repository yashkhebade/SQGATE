const fs = require('fs');
const { JSDOM } = require('jsdom');
const html = fs.readFileSync('k-map/index.html', 'utf-8');
const dom = new JSDOM(html, { runScripts: 'dangerously' });
dom.window.addEventListener('error', (event) => {
  console.log('ERROR in kmap:', event.error);
});
setTimeout(() => console.log('Done kmap'), 1000);
