const assert = require('assert');
const fs = require('fs');
const path = require('path');

// Extract the mathematical functions statically.
// This avoids side effects from running the entire game module in a mocked DOM.
const code = fs.readFileSync(path.join(__dirname, '../game.js'), 'utf8');

const quadraticEqMatch = code.match(/function quadraticEq\s*\([\s\S]*?\)\s*\{[\s\S]*?\}/);
if (!quadraticEqMatch) throw new Error("Could not find quadraticEq in game.js");

eval(quadraticEqMatch[0]);

describe('quadraticEq', function() {
    it('should compute standard quadratic equations correctly', function() {
        assert.strictEqual(quadraticEq(0, 1, 0, 0), 0, "x=0, 1x^2 => 0");
        assert.strictEqual(quadraticEq(2, 1, 0, 0), 4, "x=2, 1x^2 => 4");
        assert.strictEqual(quadraticEq(-3, 1, 0, 0), 9, "x=-3, 1x^2 => 9");
    });

    it('should handle complex coefficients', function() {
        assert.strictEqual(quadraticEq(0, 2, 3, 4), 4, "x=0, 2x^2+3x+4 => 4");
        assert.strictEqual(quadraticEq(1, 2, 3, 4), 9, "x=1, 2x^2+3x+4 => 9");
        assert.strictEqual(quadraticEq(-1, 2, 3, 4), 3, "x=-1, 2x^2+3x+4 => 3");
        assert.strictEqual(quadraticEq(5, 2, 3, 4), 69, "x=5, 2x^2+3x+4 => 69");
    });

    it('should handle zero coefficients appropriately', function() {
        assert.strictEqual(quadraticEq(10, 0, 0, 0), 0, "x=10, 0x^2+0x+0 => 0");
        assert.strictEqual(quadraticEq(10, 0, 5, 0), 50, "x=10, 0x^2+5x+0 => 50");
        assert.strictEqual(quadraticEq(10, 0, 0, 100), 100, "x=10, 0x^2+0x+100 => 100");
    });

    it('should handle floating point operations correctly', function() {
        assert.strictEqual(quadraticEq(0.5, 2, 1, 0.5), 1.5, "x=0.5, 2x^2+x+0.5 => 1.5");
        assert.strictEqual(quadraticEq(1.5, 1.5, -2.5, 1.25).toFixed(4), "0.8750", "x=1.5, 1.5x^2 - 2.5x + 1.25 => 0.875");
    });
});
