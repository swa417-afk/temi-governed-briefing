# Temi Clinical Feature Extensions (HAVOC-Compatible)

**Author:** Sierra Warren  
**Purpose:** Implementable feature extensions for Temi (via HAVOC TemiApp pattern) to support patient briefing and staff readiness using finalized clinical results.

---

## What This Implements (Pilot-Aligned)

This project implements programmable features that support the Temi pilot scope:

- Plain-language explanations of **finalized** labs and **finalized** radiology report text
- Preparation of patients for **upcoming clinician discussions**
- Flagging confusion/distress signals to nursing staff
- **No diagnosis, no treatment recommendations, and no autonomous clinical action**  [oai_citation:2‡CAAI_Temi_Full_Pilot_Proposal.pdf](sediment://file_000000000d6071f58c2920c667906e45)

---

## IRB Alignment (Non-Negotiable)

This implementation is designed to remain within:

- **Minimal risk, assistive observational AI**
- **No alteration to clinical care pathways**
- **Read-only access to finalized clinical data**
- **Patients may decline interaction at any time**
- **Immediate human override, full logging, shutdown capability**  [oai_citation:3‡CAAI_Temi_IRB_Appendix.pdf](sediment://file_000000009a5c722f97439ad440d54846)

---

## What This Does NOT Do

- No diagnosis
- No treatment recommendations
- No reinterpretation of imaging (no re-reading X-rays)
- No autonomous clinical decisions  [oai_citation:4‡CAAI_Temi_Full_Pilot_Proposal.pdf](sediment://file_000000000d6071f58c2920c667906e45)

---

## How It Integrates with HAVOC

This repo provides a “Clinical Extensions Kit” designed to be plugged into HAVOC’s existing tool/action structure:

- `clinical.get_patient_brief` → fetch & render patient brief
- `clinical.send_staff_snapshot` → send RN/MD pre-entry snapshot
- `clinical.log_urinary_status` → patient-reported urinary status intake (observational only)

See: `docs/INTEGRATION_HAVOC.md`

---

## License / Intent

See:
- `LICENSE`
- `VOLUNTARY_PERPETUAL_INSTITUTIONAL_LICENSE_INTENT.md`

## Governed Autonomy Pipeline (Python)

A ROS2-friendly, standalone governed pipeline is included under `temi_autonomy/`.

Processing flow:

`Sensor Input -> ai_processor -> temporal_buffer -> event_bus -> event_executor -> event_publisher`

Runtime policy is configured in `config/event_config.yaml`.
