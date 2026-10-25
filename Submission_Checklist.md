# KR-MECH-INT-001 — Submission checklist and final handoff

This checklist is keyed to the three-page original Kritva Robotics problem statement included as `Kritva_Original_Assignment_Brief.pdf`. Check each item before submitting. “Prepared” refers to concept-stage evidence, not physical or supplier validation.

## A. Technical report and calculations

- [x] Static torque calculation for the horizontal forearm using the specified 1.0 kg / 350 mm payload and 1.5 kg / 180 mm forearm-hand mass.
- [x] Preliminary output-torque target and explicit explanation that 2× static torque is an assumption, not a certified factor.
- [x] Output target of 45 RPM, ratio estimate, and required nominal motor speed.
- [x] Ideal output power screen and reducer-efficiency sensitivity with failure cases called out.
- [x] Units and assumptions shown for spindle bending, torsion, combined von Mises screen, overhang moment and backlash arc.
- [x] Motor/gearbox references and unresolved power-rating inconsistency surfaced rather than guessed away.
- [x] Assumptions, design rationale, two risks with mitigations, and responses to all Q1–Q6.
- [x] Report PDF is 3 pages, within the brief’s approximately 3–5 pages; editable DOCX is included.

## B. CAD, assembly drawing and artwork

- [x] Neutral STEP assembly for elbow concept and simplified arm / payload interface included.
- [x] CAD builder source and FreeCAD macro included for editing/regeneration.
- [x] Separate labelled assembly drawing included as PDF/SVG/PNG.
- [x] One-page concept artwork included as PDF/SVG/PNG; shows simplified arm, enlarged/exploded elbow, labels, load paths, COM offsets, illustrative 300 mm upper-arm and 350 mm forearm link lengths, torque/speed and trade-off/open question.
- [x] Drawing labels and assembly/load-path description agree with the split-yoke + bearing-supported spindle + flexible coupling concept.
- [ ] If a native FreeCAD project is specifically desired, open `K_EL01_Split_Yoke_Concept.FCMacro` in an installed FreeCAD environment, execute it, inspect the tree/model, save the resulting `.FCStd`, and add it to the package. FreeCAD was not available during this build; no `.FCStd` is claimed.
- [ ] Before using the model beyond concept review, verify the full assembly tree, bearing/cap retention, all physical interfaces, service sequence, cable/fastener/tool access, part clearances, motion envelope and collision cases in a CAD application. STEP geometry validity is not a substitute for these checks.

## C. Component selection and BOM

- [x] Candidate BLDC motor, planetary gearhead, encoder, controller, bearings and flexible coupling are listed with manufacturer references.
- [x] BOM contains main items and quantities, clearly separating candidate catalogue components from custom concept parts and TBD interfaces.
- [x] Supplier clarification list captures exact configured part numbers, motor torque-speed curve, efficiency, power-rating interpretation, hub interface, encoder/controller configuration, thermal/duty and holding requirements.
- [ ] Obtain written vendor confirmation of the configured motor + gearbox + feedback stack and operation at the required speed/torque/duty before claiming performance compliance.
- [ ] Confirm motor winding / supply voltage, torque-speed curve, gearhead allowable input speed and loaded efficiency, controller current/thermal limits, encoder details, coupling hubs/bores/keying, bearing fit/life/axial-load limits and optional holding-brake behavior.

## D. Presentation and technical discussion

- [x] Eight-slide presentation in editable PPTX and PDF.
- [x] Timed presenter notes total 10 minutes.
- [x] Technical discussion prep file covers likely questions for the following 10-minute discussion.
- [ ] Rehearse aloud with a timer and reduce slide narration if it exceeds 10 minutes.
- [ ] Be ready to state which values are specified, which are assumptions, which are catalogue candidates, and which remain unverified; do not describe the concept as tested or production-ready.

## E. Final package hygiene

- [x] Original brief is preserved unchanged inside the release.
- [x] Traceability, risk, gap closure, verification and supplier-question registers are included in spreadsheet/CSV form.
- [x] SHA-256 manifest and delivery index are included.
- [x] Internal render previews and temporary office-export folders are excluded from the deliverable archive.
- [ ] Before actual submission, follow the evaluator’s naming/upload convention if one exists, and include the whole package archive or the specific formats requested by the recruiter/evaluator.

## F. Explicit scope boundary

The assignment says a physical prototype, purchases, manufacturing-ready drawings and detailed FEA are not required. They have not been performed. The design remains a concept and must not be manufactured or operated from these files. The main technical closure gates are the supplier-configured drive operating point, mission profile/duty and thermal analysis, shaft/keyway/fatigue/deflection, bearing life and fits, coupling/hub interfaces, output accuracy/backlash, power-loss hold/braking, detailed CAD fit/collision checks and later supervised verification if authorized.
