package edu.uky.havoc.clinical

data class BriefingRequest(
  val patient_id: String,
  val room: String? = null,
  val include_labs: Boolean = true,
  val include_radiology: Boolean = true
)

data class PatientBriefResponse(
  val patient_id: String,
  val brief_text: String,
  val comprehension_questions: List<String>,
  val suggested_questions_for_clinician: List<String>
)

data class StaffSnapshotRequest(
  val patient_id: String,
  val room: String? = null,
  val reviewed_items: List<String>,
  val brief_text: String,
  val clarity_score: Int,
  val patient_questions: List<String>,
  val escalation_requested: Boolean
)

data class UrinaryStatusRequest(
  val patient_id: String,
  val room: String? = null,
  val since_last_check: Boolean = true,
  val amount: String,            // small|medium|large|unknown
  val pain_or_burning: String,   // yes|no|unknown
  val color: String,             // clear|pale_yellow|yellow|dark|red_or_pink|other|unknown
  val notes: String? = null
)
