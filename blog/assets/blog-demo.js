document.addEventListener("DOMContentLoaded", () => {
  const demos = document.querySelectorAll(".sqgate-mini-demo");
  
  demos.forEach(demo => {
    const type = demo.getAttribute("data-demo-type");
    
    // Build UI based on type
    let inputs = [];
    let outputs = [];
    let logicBlockName = "Logic Block";
    
    if (type === "barrel-shifter") {
      inputs = ["Data[0]", "Data[1]", "Shift_En"];
      outputs = ["Out[0]", "Out[1]"];
      logicBlockName = "2-Bit Shifter";
    } else if (type === "fifo") {
      inputs = ["Write_En", "Read_En"];
      outputs = ["Full", "Empty"];
      logicBlockName = "Async FIFO";
    } else if (type === "adder") {
      inputs = ["A", "B", "Cin"];
      outputs = ["Sum", "Cout"];
      logicBlockName = "Full Adder";
    } else {
      inputs = ["In_A", "In_B"];
      outputs = ["Out"];
      logicBlockName = "Logic Gate";
    }

    let html = `
      <div class="demo-header">
        <h3 class="demo-title">Interactive Demo: ${logicBlockName}</h3>
      </div>
      <div class="demo-canvas-container">
        <div class="demo-input-group">
          ${inputs.map((inp, i) => `
            <div class="demo-switch" data-index="${i}">
              <div class="switch-btn"></div>
              <span>${inp}</span>
            </div>
          `).join('')}
        </div>
        
        <div class="demo-logic-block">
          ${logicBlockName}
        </div>
        
        <div class="demo-output-group">
          ${outputs.map((out, i) => `
            <div class="demo-led" data-out-index="${i}">
              <div class="led-bulb"></div>
              <span>${out}</span>
            </div>
          `).join('')}
        </div>
      </div>
    `;
    
    demo.innerHTML = html;
    
    // Add interactivity
    const switches = demo.querySelectorAll(".demo-switch");
    const leds = demo.querySelectorAll(".demo-led");
    
    // State array for inputs
    let inputStates = new Array(inputs.length).fill(false);
    
    switches.forEach((sw, idx) => {
      sw.addEventListener("click", () => {
        sw.classList.toggle("active");
        inputStates[idx] = sw.classList.contains("active");
        evaluateLogic(type, inputStates, leds);
      });
    });
    
    // Initial evaluation
    evaluateLogic(type, inputStates, leds);
  });
  
  function evaluateLogic(type, inputs, leds) {
    let outStates = new Array(leds.length).fill(false);
    
    if (type === "barrel-shifter") {
      // Data[0], Data[1], Shift_En
      let d0 = inputs[0];
      let d1 = inputs[1];
      let shift = inputs[2];
      outStates[0] = shift ? d1 : d0;
      outStates[1] = shift ? d0 : d1; // simple rotate
    } else if (type === "fifo") {
      // Write_En, Read_En
      let w = inputs[0];
      let r = inputs[1];
      outStates[0] = w && !r; // Full if writing but not reading
      outStates[1] = !w && r; // Empty if reading but not writing
    } else if (type === "adder") {
      // A, B, Cin
      let a = inputs[0];
      let b = inputs[1];
      let c = inputs[2];
      outStates[0] = a ^ b ^ c; // Sum
      outStates[1] = (a && b) || (b && c) || (a && c); // Cout
    } else {
      // AND gate default
      outStates[0] = inputs[0] && inputs[1];
    }
    
    leds.forEach((led, idx) => {
      if (outStates[idx]) {
        led.classList.add("active");
      } else {
        led.classList.remove("active");
      }
    });
  }
});
