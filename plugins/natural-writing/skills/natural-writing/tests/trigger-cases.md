# Semantic trigger cases

Run each prompt in a fresh authenticated Claude Code session with the plugin enabled. These cases test intent matching, not literal phrases.

## Should route to Natural Writing

1. “This sounds like someone who doesn't know me wrote it. Keep the point, but make it sound like one of my emails.”
2. “Tighten this note for the CFO. Don't change any numbers or qualifications.”
3. “Turn these notes into a candid LinkedIn post that doesn't feel polished by committee.”
4. “The onboarding screen is technically correct but stiff. Improve the labels and error text without changing behavior.”
5. “Why does this memo feel oddly synthetic? Show me what is causing that, but don't rewrite it.”
6. “I wrote this too quickly. Make it ready to send, but don't make it more corporate.”
7. “Use these three old messages as the pattern for a new reply.”
8. “Draft the update from these facts. It should be direct enough that a busy executive reads the whole thing.”
9. “The content is accurate, but it reads like a template. Fix that without adding personality I don't have.”
10. “Can you make the ending land without adding a motivational wrap-up?”

Pass if Claude loads `natural-writing:natural-writing` even though none of these prompts uses the phrases “humanize,” “AI slop,” or “less robotic.”

## Should not route to Natural Writing

1. “Fix this TypeScript compile error.”
2. “Resize this image to 1200 by 630.”
3. “Summarize these logs to find the failing service.”
4. “Change the button color to the existing primary token.”

Pass if Claude does not load Natural Writing unless prose quality becomes a material part of the requested deliverable.
