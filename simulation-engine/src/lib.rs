use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn compute_next_tick(
    gate_types: &[u8],     // 0: AND, 1: OR, 2: NOT, 3: IDLE/LATCH
    current_states: &[u8], // 0 or 1
    input_a: &[i32],       // index of first input gate in current_states, -1 if none
    input_b: &[i32],       // index of second input gate, -1 if none
) -> Vec<u8> {
    let len = current_states.len();
    let mut next_states = vec![0; len];

    for i in 0..len {
        let type_id = gate_types.get(i).copied().unwrap_or(3);
        
        let a_idx = input_a.get(i).copied().unwrap_or(-1);
        let b_idx = input_b.get(i).copied().unwrap_or(-1);

        let val_a = if a_idx >= 0 && (a_idx as usize) < len {
            current_states[a_idx as usize]
        } else {
            0
        };

        let val_b = if b_idx >= 0 && (b_idx as usize) < len {
            current_states[b_idx as usize]
        } else {
            0
        };

        next_states[i] = match type_id {
            0 => val_a & val_b, // AND
            1 => val_a | val_b, // OR
            2 => if val_a == 0 { 1 } else { 0 }, // NOT (uses input A)
            _ => current_states[i], // Keep state for IDLE/LATCH/Inputs
        };
    }
    
    next_states
}
