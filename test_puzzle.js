const fs = require('fs');
const { JSDOM } = require('jsdom');
const html = fs.readFileSync('puzzle/index.html', 'utf-8');
const dom = new JSDOM(html, { runScripts: 'dangerously' });
dom.window.addEventListener('error', (event) => {
  console.log('ERROR in puzzle:', event.error);
});
setTimeout(() => console.log('Done puzzle'), 1000);
