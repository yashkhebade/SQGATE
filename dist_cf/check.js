const https = require('https');
https.get('https://sqgate.online/home/index.html', (res) => {
  let data = '';
  res.on('data', d => data += d);
  res.on('end', () => {
    console.log('Has shareCircuit:', data.includes('function shareCircuit'));
    console.log('Has share-modal:', data.includes('id=\"share-modal\"'));
  });
});
