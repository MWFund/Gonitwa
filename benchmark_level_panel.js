// Mock document
const document = {
  getElementById: function(id) {
    if (id === "level-display") {
      return { textContent: "" };
    }
    if (id.startsWith("level-")) {
      return {
        classList: {
          remove: function() {},
          add: function() {}
        }
      };
    }
    return null;
  }
};

let currentCheckpointLevel = 3;

// Original function
function updateLevelPanelOriginal() {
  var levelDisplay = document.getElementById("level-display");
  if (levelDisplay) {
    levelDisplay.textContent = currentCheckpointLevel + " / 6";
  }

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
}

// Optimization function
let cachedElements = null;
function updateLevelPanelOptimized() {
  if (!cachedElements) {
    cachedElements = {
      levelDisplay: document.getElementById("level-display"),
      dots: []
    };
    for (var i = 1; i <= 6; i++) {
      cachedElements.dots.push(document.getElementById("level-" + i));
    }
  }

  if (cachedElements.levelDisplay) {
    cachedElements.levelDisplay.textContent = currentCheckpointLevel + " / 6";
  }

  for (var i = 0; i < 6; i++) {
    var dot = cachedElements.dots[i];
    if (dot) {
      dot.classList.remove("completed", "current");
      if (i + 1 < currentCheckpointLevel) {
        dot.classList.add("completed");
      } else if (i + 1 === currentCheckpointLevel) {
        dot.classList.add("current");
      }
    }
  }
}

// Benchmark
const ITERS = 1000000;

let startOriginal = performance.now();
for(let i=0; i<ITERS; i++) {
    currentCheckpointLevel = (i % 6) + 1;
    updateLevelPanelOriginal();
}
let endOriginal = performance.now();

let startOptimized = performance.now();
for(let i=0; i<ITERS; i++) {
    currentCheckpointLevel = (i % 6) + 1;
    updateLevelPanelOptimized();
}
let endOptimized = performance.now();

console.log("Original:  " + (endOriginal - startOriginal).toFixed(2) + " ms");
console.log("Optimized: " + (endOptimized - startOptimized).toFixed(2) + " ms");
let diff = ((endOriginal - startOriginal) / (endOptimized - startOptimized));
console.log("Improvement: " + diff.toFixed(2) + "x faster");
