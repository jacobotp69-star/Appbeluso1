const fs = require('fs');
const path = require('path');

const poisPath = path.join(__dirname, '..', 'src', 'data', 'pois.ts');
const publicPath = path.join(__dirname, '..', 'public');

const content = fs.readFileSync(poisPath, 'utf8');

// Simple regex to find image URLs
const imgRegex = /"\/assets\/pois\/[^"]+"/g;
const matches = content.match(imgRegex);

if (!matches) {
    console.log("No images found in pois.ts");
    process.exit(0);
}

const missing = [];
const existing = [];

matches.forEach(m => {
    const url = m.replace(/"/g, '');
    const filePath = path.join(publicPath, url.replace(/^\//, ''));
    if (!fs.existsSync(filePath)) {
        missing.push({ url, filePath });
    } else {
        existing.push(url);
    }
});

console.log(`Total images in pois.ts: ${matches.length}`);
console.log(`Missing images: ${missing.length}`);
missing.forEach(m => console.log(`MISSING: ${m.url}`));
