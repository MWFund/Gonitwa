// Mocking window and document for game.js which is not fully node-friendly
global.window = {
  onload: () => {},
  Math: Math,
  setInterval: () => 999,
  clearInterval: () => {},
  addEventListener: () => {},
  document: {
    readyState: 'loading', // Prevent the setInterval in game.js from proceeding
    createElement: () => ({ appendChild: () => {}, style: {}, setAttribute: () => {}, setAttributeNS: () => {}, addEventListener: () => {}, children: [] }),
    body: { appendChild: () => {} },
    getElementById: () => ({ appendChild: () => {}, style: {}, getBoundingClientRect: () => ({ left: 0, width: 720 }) }),
    addEventListener: () => {}
  }
};
global.document = global.window.document;
global.Uint8Array = Uint8Array;
global.Uint16Array = Uint16Array;
global.Uint32Array = Uint32Array;
global.Audio = class { play() {} };
global.jsfxr = () => 'mock_data';

const assert = require('assert');
const { ellipseEq } = require('./game.js');

function testEllipseEq() {
  console.log('Running tests for ellipseEq...');

  // x²/a² + y²/b² = 1 => y = sqrt((1 - x²/a²) * b²)

  // Test Case 1: x = 0, should return b
  let result = ellipseEq(0, 5, 10);
  assert.strictEqual(result, 10, 'x=0 should return b');

  // Test Case 2: x = a, should return 0
  result = ellipseEq(5, 5, 10);
  assert.strictEqual(result, 0, 'x=a should return 0');

  // Test Case 3: x = -a, should return 0
  result = ellipseEq(-5, 5, 10);
  assert.strictEqual(result, 0, 'x=-a should return 0');

  // Test Case 4: Standard point
  // For x = 3, a = 5, b = 10
  // y = sqrt((1 - 9/25) * 100) = sqrt((16/25) * 100) = sqrt(0.64 * 100) = sqrt(64) = 8
  result = ellipseEq(3, 5, 10);
  assert.strictEqual(result, 8, 'x=3, a=5, b=10 should return 8');

  console.log('All ellipseEq tests passed!');
}

try {
  testEllipseEq();
  process.exit(0);
} catch (error) {
  console.error('Test failed!');
  console.error(error.message);
  process.exit(1);
}
