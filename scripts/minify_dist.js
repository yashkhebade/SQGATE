const fs = require('fs');
const path = require('path');
const { minify } = require('terser');
const CleanCSS = require('clean-css');

const distDir = path.join(__dirname, '../dist_cf');
const cleanCssInstance = new CleanCSS({ level: 2 });

async function processDir(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            await processDir(fullPath);
        } else {
            if (file.endsWith('.js') && !file.endsWith('.min.js')) {
                const code = fs.readFileSync(fullPath, 'utf8');
                try {
                    const result = await minify(code);
                    if (result.code) {
                        fs.writeFileSync(fullPath, result.code);
                        console.log('Minified JS:', fullPath);
                    }
                } catch (e) {
                    console.error('Error minifying JS:', fullPath, e);
                }
            } else if (file.endsWith('.css') && !file.endsWith('.min.css')) {
                const code = fs.readFileSync(fullPath, 'utf8');
                const result = cleanCssInstance.minify(code);
                if (result.styles) {
                    fs.writeFileSync(fullPath, result.styles);
                    console.log('Minified CSS:', fullPath);
                } else {
                    console.error('Error minifying CSS:', fullPath, result.errors);
                }
            }
        }
    }
}

processDir(distDir).then(() => console.log('Minification complete.')).catch(console.error);
