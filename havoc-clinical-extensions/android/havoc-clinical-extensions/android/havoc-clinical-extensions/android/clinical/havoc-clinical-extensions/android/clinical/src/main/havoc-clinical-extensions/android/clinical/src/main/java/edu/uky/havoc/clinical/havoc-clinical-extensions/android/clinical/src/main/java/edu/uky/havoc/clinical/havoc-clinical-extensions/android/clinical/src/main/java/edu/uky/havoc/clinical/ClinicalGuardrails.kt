package edu.uky.havoc.clinical

object ClinicalGuardrails {
  // lightweight client-side backstop; backend should also enforce
  private val prohibited = listOf(
    "diagnosis", "you have", "you likely have", "treatment", "i recommend",
    "start taking", "stop taking", "increase your dose", "decrease your dose"
  )

  const val DISCLAIMER =
    "I’m an assistive system. I can explain what your finalized report says in plain language, " +
    "but I can’t provide medical advice, diagnose conditions, or recommend treatment. " +
    "Your care team will explain what this means for you."

  fun sanitizePatientText(text: String): String {
    val lower = text.lowercase()
    val violates = prohibited.any { lower.contains(it) }
    return if (violates) {
      "$DISCLAIMER\n\nI can summarize the wording in your finalized report and help you prepare questions for your care team."
    } else {
      if (text.startsWith(DISCLAIMER)) text else "$DISCLAIMER\n\n$text"
    }
  }
}
