const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER:', msg.text()));

  // Navigate to the local page
  await page.goto('file://e:/chess_project/Gonitwa/index.html');
  
  // Wait for the game to initialize
  await new Promise(r => setTimeout(r, 1000));

  // Press SPACE to start the game
  await page.keyboard.press('Space');
  await new Promise(r => setTimeout(r, 500));
  
  // Evaluate the player coordinates
  let pos = await page.evaluate(() => {
    return { row: player.row, col: player.col };
  });
  console.log('Player start:', pos);

  // Figure out the screen coordinates for player's cell
  let coords = await page.evaluate(() => {
    let pr = player.row;
    let pc = player.col;
    let rootEl = document.getElementById("root");
    let rect = rootEl.getBoundingClientRect();
    let SIZE = 400;
    let HORIZON_Y = 100;
    let NUM_CELLS = 8;
    let scale = rect.width / SIZE;
    let progress = window.progress;
    
    // Reverse engineer reverseProject
    // We want reverseProject.res.x = (pc + 0.5) / NUM_CELLS
    // We want reverseProject.res.y = (pr - progress + 0.5) / NUM_CELLS
    
    // forward project:
    let A_Y = 0.5;
    let B_Y = 1.3;
    let C_Y = 0.2;
    let A_S = -0.3;
    let B_S = 1;
    let C_S = 0.4;
    
    let logicalY = (pr - progress + 0.5) / NUM_CELLS;
    let logicalX = (pc + 0.5) / NUM_CELLS;
    
    let projY = A_Y * logicalY * logicalY + B_Y * logicalY + C_Y;
    let s = A_S * projY * projY + B_S * projY + C_S;
    let projX = logicalX * s + (1 - s) / 2;
    
    let docX = projX * SIZE * scale + rect.left;
    let docY = (projY * SIZE + HORIZON_Y) * scale + rect.top;
    
    return { x: docX, y: docY };
  });

  console.log('Moving mouse to', coords.x, coords.y);
  await page.mouse.move(coords.x, coords.y);
  await page.mouse.down();
  await new Promise(r => setTimeout(r, 100));
  
  let dragged = await page.evaluate(() => player.dragged);
  console.log('Is dragged after mousedown?', dragged);

  // Drag up (forward 1 row)
  await page.mouse.move(coords.x, coords.y - 120);
  await new Promise(r => setTimeout(r, 100));
  
  let targetRowCol = await page.evaluate(() => {
    return { targetRow: mouseRow, targetCol: mouseCol };
  });
  console.log('Target after dragging:', targetRowCol);

  await page.mouse.up();
  await new Promise(r => setTimeout(r, 200));

  let finalPos = await page.evaluate(() => {
    return { row: player.row, col: player.col };
  });
  console.log('Player final:', finalPos);

  await browser.close();
})();
