const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER:', msg.text()));

  await page.goto('file:///app/index.html');
  await new Promise(r => setTimeout(r, 1000));
  await page.keyboard.press('Space');
  await new Promise(r => setTimeout(r, 500));
  
  // Expose evaluation code as string that we can inject if needed, 
  // but let's try just getting visual offset. We cannot access closure variables directly.
  await page.click('#root', { offset: { x: 200, y: 400 } }); // Clicking roughly forward center!
  await new Promise(r => setTimeout(r, 500));
  
  await browser.close();
})();
