# Feature Map (Implementable Modules → Pilot Scope)

## 1) Finalized Results Patient Brief
**Implements:** plain-language explanation of finalized labs + radiology report text  [oai_citation:12‡CAAI_Temi_Full_Pilot_Proposal.pdf](sediment://file_000000000d6071f58c2920c667906e45)  
**Not included:** reinterpretation of imaging; diagnosis; treatment  [oai_citation:13‡CAAI_Temi_Full_Pilot_Proposal.pdf](sediment://file_000000000d6071f58c2920c667906e45)  

Tool:
- `clinical.get_patient_brief(patient_id, room, encounter_id?)`

## 2) Pre-Entry Staff Snapshot (RN/MD)
**Implements:** flags confusion to nursing staff; prepares clinician encounter  [oai_citation:14‡CAAI_Temi_Full_Pilot_Proposal.pdf](sediment://file_000000000d6071f58c2920c667906e45)  

Tool:
- `clinical.send_staff_snapshot(patient_id, room, reviewed_items, confusion_topics, clarity_score, patient_questions, escalation_requested)`

## 3) Patient-Reported Urinary Status (Observational Intake)
**Implements:** assistive observational intake ONLY (no interpretation/diagnosis)  [oai_citation:15‡CAAI_Temi_IRB_Appendix.pdf](sediment://file_000000009a5c722f97439ad440d54846)  

Tool:
- `clinical.log_urinary_status(patient_id, room, amount, pain_or_burning, color, notes?)`
