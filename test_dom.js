const fs = require('fs');
const html = fs.readFileSync('puzzle/index.html', 'utf-8');
const { JSDOM } = require('jsdom');
const dom = new JSDOM(html);
const lqMain = dom.window.document.querySelector('.lq-main');
if (lqMain) {
  console.log("lq-main parent:", lqMain.parentElement.className);
} else {
  console.log("lq-main not found!");
}
const lqRoot = dom.window.document.querySelector('.lq-root');
if (lqRoot) {
  console.log("lq-root parent:", lqRoot.parentElement.tagName);
  console.log("lq-root children:", Array.from(lqRoot.children).map(c => c.className || c.tagName).join(', '));
}
