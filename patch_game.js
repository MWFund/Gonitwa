const fs = require('fs');

const file = 'game.js';
let content = fs.readFileSync(file, 'utf8');

const original = `  function updateLevelPanel() {
    // Update level display text
    var levelDisplay = document.getElementById("level-display");
    if (levelDisplay) {
      levelDisplay.textContent = currentCheckpointLevel + " / 6";
    }

    // Update level dots
    for (var i = 1; i <= 6; i++) {
      var dot = document.getElementById("level-" + i);
      if (dot) {
        dot.classList.remove("completed", "current");
        if (i < currentCheckpointLevel) {
          dot.classList.add("completed");
        } else if (i === currentCheckpointLevel) {
          dot.classList.add("current");
        }
      }
    }
  }`;

const optimized = `  var _cachedLevelElements = null;
  function updateLevelPanel() {
    if (!_cachedLevelElements) {
      _cachedLevelElements = {
        display: document.getElementById("level-display"),
        dots: []
      };
      for (var i = 1; i <= 6; i++) {
        _cachedLevelElements.dots.push(document.getElementById("level-" + i));
      }
    }

    // Update level display text
    if (_cachedLevelElements.display) {
      _cachedLevelElements.display.textContent = currentCheckpointLevel + " / 6";
    }

    // Update level dots
    for (var i = 0; i < 6; i++) {
      var dot = _cachedLevelElements.dots[i];
      if (dot) {
        dot.classList.remove("completed", "current");
        if (i + 1 < currentCheckpointLevel) {
          dot.classList.add("completed");
        } else if (i + 1 === currentCheckpointLevel) {
          dot.classList.add("current");
        }
      }
    }
  }`;

if (content.includes(original)) {
    fs.writeFileSync(file, content.replace(original, optimized), 'utf8');
    console.log("Successfully patched game.js");
} else {
    console.log("Failed to find original content in game.js");
}
