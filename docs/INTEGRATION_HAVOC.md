# HAVOC Integration Guide (Minimal Patch)

## Goal
Add clinical tools to HAVOC’s existing tool/action routing with minimal changes.

## Add These Tool Names
- `clinical.get_patient_brief`
- `clinical.send_staff_snapshot`
- `clinical.log_urinary_status`

## Required Wiring
1) Instantiate `ClinicalApiClient(baseUrl)` from HAVOC config (properties).
2) In HAVOC tool dispatcher, route tool names to:
   - `client.getPatientBrief(...)`
   - `client.sendStaffSnapshot(...)`
   - `client.logUrinaryStatus(...)`
3) Before speaking patient brief, run:
   - `ClinicalGuardrails.sanitizePatientText(brief_text)`

## Notes (Pilot/IRB)
- Finalized-only, read-only.
- No diagnosis/treatment/autonomous action.  [oai_citation:16‡CAAI_Temi_Full_Pilot_Proposal.pdf](sediment://file_000000000d6071f58c2920c667906e45)
- Patient may decline; human override; full logging; shutdown.  [oai_citation:17‡CAAI_Temi_IRB_Appendix.pdf](sediment://file_000000009a5c722f97439ad440d54846)
