# Backend Schema

## Overview
SQGATE is primarily a client-side application. The backend serves only one purpose: **Anonymous AI Telemetry**. There is no traditional "user backend" or database where user logic is stored; users manage their own saves via local storage or by exporting JSON.

## Supabase Schema
The PostgreSQL database running on Supabase captures structural representations of circuits for ML training.

### Table: `circuit_telemetry`

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | `UUID` | Primary Key, Auto-generated. |
| `created_at` | `TIMESTAMPTZ` | Timestamp of submission. |
| `gate_count` | `INTEGER` | Total number of logic gates used in the circuit. |
| `wire_count` | `INTEGER` | Total number of connection wires. |
| `topology_json` | `JSONB` | A sanitized mathematical representation of nodes and edges. Does not contain any user-defined labels or metadata. |

## Data Flow Rules
1. **Trigger:** Fires silently when a guest user simulates a circuit (e.g., changes an input state resulting in successful propagation).
2. **Opt-Out Condition:** If `localStorage.getItem('_user')` exists (meaning the user authenticated with an email), the telemetry bypasses the network request entirely.
3. **No PII:** Absolutely no IP addresses, browser agents, or identifiable data are transmitted to the Supabase endpoint.
