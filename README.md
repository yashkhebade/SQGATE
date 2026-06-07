# SQGATE - Professional Logic Simulator & EDA Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Electron](https://img.shields.io/badge/Electron-v28.0.0-blue.svg)](https://www.electronjs.org/)
[![Node.js](https://img.shields.io/badge/Node.js-v18%2B-green.svg)](https://nodejs.org/)
[![Multiplayer WebSocket](https://img.shields.io/badge/Multiplayer-WebSocket-orange.svg)](#multiplayer-mode)
[![Build Status](https://img.shields.io/badge/Build-Success-success.svg)](#desktop-app-packaging)

**SQGATE** is a high-performance, web-based Electronic Design Automation (EDA) and 8-bit logic simulation platform. Designed to bridge the gap between simple academic logic editors and professional chip-design suites, SQGATE empowers engineers, educators, and hobbyists to design, simulate, analyze, and package complex digital logic circuits.

From simple logic gates to fully custom, microcoded 8-Bit CPU architectures with RAM and ROM, SQGATE handles it all within a sleek, highly-optimized responsive interface.

---

## 🚀 Key Highlights & Capabilities

- **⚡ Real-Time Interactive Simulator**: Sub-millisecond gate propagation delays, step-by-step debug logging, and synchronous clock domain stepping.
- **🌐 Real-Time Multiplayer Collaboration**: Edit schematics simultaneously with teammates in Google Docs fashion, synced over a Node.js WebSocket backend server.
- **📊 Integrated Timing Analysis**: A built-in Waveform Viewer (multi-channel digital oscilloscope) displaying real-time logic changes over clock cycles.
- **📝 Microcoded ROM Hex Editor**: Double-click memory blocks to open a native hex editor and directly write instructions or paste machine code hex dumps.
- **📐 Algebraic & Karnaugh Map (K-Map) Solver**: Generate instant truth tables, Sum-of-Products (SOP) boolean equations, and simplified circuits directly from your visual layout.
- **🛠️ Design Rule Checker (DRC)**: Dynamic syntax/layout checker that warns you of short-circuits, floating/unconnected inputs, and wire loops.
- **💾 Verilog HDL & KiCad Netlist Exporter**: Compile visual layouts into synthesizable, industry-standard Verilog HDL files or KiCad netlists for PCB printing.

---

## 🧩 Component Directory (40+ Logic Elements)

SQGATE features a wide range of highly-optimized logic components grouped into clean categories:

### 1. Logic Gates & Basic Functions
*   `and` / `or` / `not` / `nand` / `nor` / `xor` / `xnor`: Exhaustive standard logic gates.
*   `buffer`: High-impedance buffer and signal booster.
*   `ha` (Half Adder) & `fa` (Full Adder): Core hardware arithmetic units.
*   `add4` (4-Bit Carry-Lookahead Adder): Multi-bit mathematical block.

### 2. Signal Routing & Data Selectors
*   `mux2` / `mux4` (Multiplexers): Select and route digital signals from multiple inputs.
*   `dmux2` / `dmux4` (Demultiplexers): Distribute one signal to multiple outputs.
*   `enc4` (4:2 Priority Encoder) & `dec2` (2:4 Decoder): Control line compression.

### 3. Multi-bit Buses & Splitters
*   `merge4` / `merge8`: Compress 4 or 8 individual wires into a single clean bus wire.
*   `split4` / `split8`: Expand a 4-bit or 8-bit bus into individual signal wires.

### 4. Sequential Logic & Flip-Flops
*   `sr` (SR Latch) & `dlatch` (D-Type Latch): Level-sensitive memory.
*   `dff` / `jkff` / `tff` (Flip-Flops): Edge-triggered state machines.
*   `count8` (8-Bit Counter): Synchronous count-up/count-down register with clear.
*   `shift8` (8-Bit Shift Register): Load and shift data serially or in parallel.

### 5. Memory Modules
*   `rom8` (256-Byte Read-Only Memory): Features a full Hex Editor modal interface.
*   `ram8` (256-Byte Random Access Memory): Read/Write memory syncing on the rising edge of a clock.

### 6. Arithmetic Unit
*   `alu8` (8-Bit Arithmetic Logic Unit): Supports addition, subtraction, AND, OR, XOR, SHL, SHR, and NOT operations, complete with Overflow, Underflow, and Zero flags.

### 7. Input / Output & Display
*   `input` (Toggle Switch) & `clock` (Pulse Generator): Controllable inputs.
*   `const0` / `const1`: Ground (GND) and VCC logic lines.
*   `led` / `seg7` (7-Segment Display) / `hexdisp` (Hexadecimal Monitor): Real-time output feedback.

---

## ⌨️ Keyboard Shortcuts Reference

Quickly navigate, build, and debug your schematics using the unified keyboard command system. Toggle the overlay with `?`.

| Category | Shortcut | Action |
| :--- | :--- | :--- |
| **Canvas** | `Ctrl + K` | Open Spotlight Search to place any component |
| | `Ctrl + MouseWheel` | Zoom Canvas In / Out |
| | `Space + Drag` | Pan Canvas |
| **Editing** | `Delete` / `Backspace` | Delete selected components or wires |
| | `Ctrl + C` / `Ctrl + V` | Copy / Paste selection |
| | `Ctrl + Z` / `Ctrl + Y` | Undo / Redo last design change |
| **Wiring** | `Esc` | Cancel current wire routing |
| | `Ctrl + R` | Auto-route wires orthogonally |
| **Simulation** | `P` | Play / Pause continuous execution |
| | `S` | Step simulation by 1 tick |
| | `C` | Toggle clock state manually |
| | `T` | Reset simulation state |
| **Help** | `?` | Toggle Help Overlay |

---

## 📦 Desktop App Packaging & Installation

### Local Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/SQGATE.git
   cd SQGATE
   ```
2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```
3. **Run in development mode (browser/Electron):**
   ```bash
   npm start
   ```

### Desktop App Packaging (Windows)
The application can be packaged into a standalone desktop application (`.exe`) with a custom brand icon:
```bash
# Package the Electron desktop app
npm run pack
```
Once complete, the standalone application folder will be generated at `dist\win-unpacked\`, containing `SQGATE.exe` with its custom app icon baked in.

---

## 🌐 Multiplayer Mode

SQGATE supports real-time multiplayer logic design.
1. **Start the WebSocket Hub:**
   ```bash
   node node-server/server.js
   ```
2. **Connect client nodes:**
   Multiple Electron instances or web browsers can connect to the shared room coordinates to interactively build the same schematic.

---

## 🧪 Automated Test Suite

A comprehensive Node.js test script verifies the logic of all 30+ gate and module types against multiple test vectors.

To run the automated suite:
```bash
node test_gates.js
```
The suite executes 310+ test assertions covering arithmetic overflows, clock transitions, register loading, and ALU operations.

Designed and refined through collaboration between multiple Large Language Models (LLMs) and a student deeply passionate about CPU architecture and computer systems.
