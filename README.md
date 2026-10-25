# K-EL/01 Split-Yoke Elbow Actuator — Comprehensive Release

**Assignment:** Kritva Robotics KR-MECH-INT-001, “Robotic Actuator & Arm Mechanical Design Challenge”  
**Package revision:** 25 October 2026  
**Status:** Concept submission bundle; not a manufacturing or safety release.

## Start here

1. **`Kritva_K_EL01_Design_Report.pdf`** — the concise 3-page design report, within the brief’s 3–5 page expectation.
2. **`Kritva_K_EL01_Comprehensive_Gap_Closure_Plan.pdf`** — the full original-brief coverage map, generated deliverables, ordered future closure gates, acceptance criteria, and 5-day execution plan.
3. **`Kritva_K_EL01_Final_Review_Presentation.pptx`** and its PDF — 8 slides for the required 10-minute presentation.
4. **`Kritva_K_EL01_10_Minute_Presenter_Notes.pdf`** and **`Kritva_K_EL01_Technical_Discussion_QA.pdf`** — speaker script, pacing, and likely 10-minute discussion questions.
5. **`K_EL01_Engineering_Workbook.xlsx`** — editable formula-driven dashboard, input, calculation, efficiency sensitivity, BOM, component, traceability, risk, validation, gap, and supplier query sheets.
6. **`K_EL01_Assembly_Drawing.pdf`** — numbered exploded actuator assembly concept; **`K_EL01_Concept_Drawing.pdf`** — the requested one-page arm + elbow artwork.
7. **`K_EL01_Split_Yoke_Concept.step`** — neutral CAD assembly; **`Build_K_EL01_STEP.py`** — CadQuery source; **`K_EL01_Split_Yoke_Concept.FCMacro`** — optional macro to create an editable FreeCAD document locally.
8. **`Kritva_K_EL01_Technical_QA_Review.pdf`** and **`Kritva_K_EL01_Simulation_and_Verification_Plan.pdf`** — independent consistency review and proposed verification route.
9. **`Submission_Checklist.md`** — final acceptance checklist organised around the source brief, with explicit remaining sign-off gates.
10. **`Kritva_Original_Assignment_Brief.pdf`** — source brief preserved in the package.
11. **`K_EL01_Run_and_View_FreeCAD_Macro.ipynb`** — optional notebook to inspect macro source, preview the STEP model, and launch a local macro run where FreeCAD is installed.
12. **`K_EL01_FreeCAD_Notebook_Starter.zip`** — standalone starter bundle containing the notebook, STEP, macro, CAD builder source, and setup instructions.
13. **`Final_Audit_Summary.md`** — source-to-deliverable verdict, remaining gates, official motor-data caveat and cross-file QA checks.

## What the original brief asks for

- Static gravitational torque for 1.0 kg at 350 mm plus 1.5 kg at 180 mm, with forearm horizontal.
- Preliminary output target and rationale, estimated motor speed/gear ratio for 45 RPM, and a commercially available motor/gearhead candidate with official references.
- Conceptual elbow assembly containing motor, gearhead, output shaft, bearing support, housing and forearm attachment; integrated simplified upper arm, forearm and wrist/payload interface.
- Labelled assembly/drawing, plausible load paths and assembly/maintenance consideration.
- Assumptions/design decisions, simple BOM, two risks with mitigations and all six critical-thinking answers.
- One-page concept artwork with complete-arm three-quarter/isometric view, enlarged actuator/exploded view, labels/load-path arrows, key offsets/link dimensions, torque/speed callout, and trade-off/open issue.
- 3–5 page report and preparation for a 10-minute presentation followed by 10 minutes of technical discussion.

The brief explicitly says no prototype, purchasing, manufacturing-ready drawing or detailed FEA is required. It asks for uncertainty to be documented and inconsistencies to be explained rather than silently ignored.

## Core results

- Payload torque: `1.0 × 9.81 × 0.350 = 3.4335 N·m`.
- Forearm/hand torque: `1.5 × 9.81 × 0.180 = 2.6487 N·m`.
- Static gravity torque: **6.0822 N·m**.
- Preliminary target: **12.1644 N·m** using an explicit assumed **2×** multiplier (not a certified safety factor).
- Ideal output power at target torque and 45 RPM: **57.32 W** before losses.
- 91:1 ratio gives **4095 RPM** nominal motor speed requirement, only about **375 RPM** under the candidate motor’s listed 4470 RPM nominal speed.
- At an assumed 40% reducer efficiency, simplified motor-side screen: **0.334 N·m**, **143.3 W**, **3.64 A**.
- At 30% assumed efficiency, the simplified motor torque/current and 180 W label screens fail.
- The CAD-derived bearing centres are at Y=11 mm and Y=61 mm, with a forearm centre plane at Y=111 mm: **50 mm bearing spacing and 50 mm overhang** in the idealized static reaction model.
- Nominal 12 mm smooth-spindle stress screen: bending **7.23 MPa**, torsion **35.85 MPa**, combined von Mises **62.52 MPa**, with SI-to-mm conversion written explicitly. This excludes notches, fatigue, impact, dynamic loads and deflection.
- At 1° average no-load backlash, the arc at the 350 mm payload radius is about **6.11 mm**; assembled joint error is not established by this number.

## Candidate components and supplier questions

- Motor candidate: maxon EC-i 52, 48 V, part 579165.
- Reducer candidate: maxon GP 52 C, 91:1, part 223094.
- Encoder candidate: maxon ENX16EASY06, 512 CPT configuration candidate.
- Controller candidate: maxon EPOS4 Disk 60/8 CAN, part 688770.
- Support bearings: 2 × SKF 6201-2RSH.
- Flexible coupling candidate: KTR ROTEX GS size 19, 98 Shore A spider; hub bores/order codes are not frozen.

Official references are listed in the report and `Component_Research.csv`; the workbook reproduces the research register. The motor page labels the candidate 180 W class while listed nominal torque × speed gives about 198 W by arithmetic; the package asks maxon to clarify the applicable rating point and loaded curve. Separately, Maxon support explains that EC-i iron-winding motors do not have a single straight-line speed/torque characteristic: the published 0.321 rpm/mNm gradient is speed-dependent and must not be extrapolated as a constant slope. Source: https://support.maxongroup.com/hc/en-us/articles/360013761160-Motor-data-and-simulation. The exact configured drive combination is still open; a maximum gearbox efficiency is not treated as guaranteed efficiency at the design point.

## Important limitations / next actions

1. Obtain mission profile: duty, speed trajectory, acceleration/deceleration, reversals, impacts/stops, life, accuracy/backlash/stiffness, thermal environment, power-loss holding and complete link mass/inertia.
2. Obtain supplier-confirmed configured motor/gearhead/encoder/controller combination, torque-speed curve at 4095 RPM, output performance at 45 RPM and target torque, loaded efficiency, thermal limits, regen restrictions, and written response on the power convention.
3. Freeze coupling hubs, bores/keying, service factor, speed, stiffness and misalignment; finalize spindle/keyway/retention/material/fit, bearing life and axial load, fasteners, carrier stiffness and full CAD interfaces.
4. Open STEP in FreeCAD (or an equivalent native CAD system) and save `.FCStd` if a native file is desired. FreeCAD was not installed in this authoring environment, so no `.FCStd` file is claimed. The brief allows equivalent CAD; STEP plus builder source and macro are included.
5. Do not claim FEA, prototype, supplier validation, physical performance, safety certification or manufacturing readiness. The validation plan defines how to obtain the missing evidence if authorized later.

## File integrity and regeneration

- `DELIVERY_INDEX.csv` lists the final package contents.
- `SHA256SUMS.txt` contains SHA-256 hashes for the files included in the final archive except the checksum file itself.
- `CHANGELOG.md` lists consistency corrections made during this revision.
- `SHA256SUMS.txt` checksums are regenerated for the exact archive contents; the notebook is included as a convenience, not as a substitute for local FreeCAD installation.
- Source builders for the neutral CAD, artwork, workbook and supporting documents are included. Internal QA render images and temporary export folders are deliberately excluded from the delivered archive.
