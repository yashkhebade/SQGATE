const fs = require('fs');
const { JSDOM } = require('jsdom');
const html = fs.readFileSync('puzzle/index.html', 'utf-8');
const dom = new JSDOM(html, { runScripts: 'dangerously' });

setTimeout(() => {
  const document = dom.window.document;
  const lqMain = document.querySelector('.lq-main');
  console.log('lq-main exists:', !!lqMain);
  if (lqMain) {
    const style = dom.window.getComputedStyle(lqMain);
    console.log('lq-main display:', style.display);
    console.log('lq-main height:', style.height);
    console.log('lq-main offsetHeight:', lqMain.offsetHeight);
    
    // Let's see what is rendered inside lq-main
    console.log('lq-main HTML length:', lqMain.innerHTML.length);
    const objHeader = document.querySelector('.lq-card-header');
    if (objHeader) {
      console.log('objHeader text:', objHeader.textContent);
    }
  }
}, 1000);
