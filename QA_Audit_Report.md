# K-EL/01 Technical QA Audit

**Audit date:** 25 October 2026  
**Source of truth:** `Kritva_Original_Assignment_Brief.pdf` (3 pages).

## Executive finding

The revised release covers the assignment-stage requirements: calculation, documented candidate drive, equivalent CAD, separate concept and assembly drawings, BOM, three-page report (within the requested 3–5 pages), six critical-thinking answers, risks, and preparation for the required presentation/discussion. The neutral STEP re-imported through CadQuery with valid geometry; it contains 21 solids. These checks do not validate kinematics, interference, strength, manufacturability, thermal performance or safety.

## Corrected consistency issues

- Architecture wording aligned to the actual CAD: KTR ROTEX GS size 19 flexible coupling candidate plus independent nominal Ø12 mm spindle; no longer describes a custom split-clamp keyed sleeve as the implemented architecture.
- Encoder candidate aligned to ENX16EASY06 at 512 CPT rather than a stale 1024 CPT reference.
- Load plane and bearing geometry derived from CAD coordinates: bearing centres Y=11 and 61 mm; forearm centre plane Y=111 mm; spacing and overhang each 50 mm.
- Shaft stress equations explicitly convert torque/moment in N·m to N·mm for mm-based formulas. Nominal stress results: bending 7.2283 MPa, torsional shear 35.8523 MPa, combined von Mises 62.5173 MPa.
- Presentation, speaker script, technical Q&A, editable calculation workbook, numbered assembly drawing, gap closure plan and verification plan added. The one-page artwork now explicitly labels the illustrative 350 mm forearm-link length. The FreeCAD notebook is included as a preview/run helper.

## Reproducible main calculations

| Quantity | Result |
|---|---:|
| Payload torque | 3.4335 N·m |
| Forearm/hand torque | 2.6487 N·m |
| Total static | 6.0822 N·m |
| Assumed 2× target | 12.1644 N·m |
| Ideal output power at target and 45 RPM | 57.3234 W |
| Motor speed with 91:1 | 4095 RPM |
| Gravity force | 24.525 N |
| Overhang moment | 1.22625 N·m = 1226.25 N·mm |
| Bearing reactions (idealized) | 49.05 N outboard / 24.525 N inboard opposite direction |
| Bending / torsional shear / von Mises | 7.23 / 35.85 / 62.52 MPa |
| 1° backlash arc at 350 mm | 6.109 mm |

## Remaining open engineering gates

1. Supplier-confirmed configured combination and loaded torque-speed/thermal point; clarify the 180 W class label versus nominal Tω≈198 W arithmetic. Maxon support notes EC-i iron-winding speed/torque characteristics are nonlinear and speed-dependent, so the published 0.321 rpm/mNm gradient must not be extrapolated as a constant slope: https://support.maxongroup.com/hc/en-us/articles/360013761160-Motor-data-and-simulation.
2. Mission profile, duty cycle, acceleration, impacts, peak/RMS torque and thermal limits.
3. Coupling hub bore/keying, service factor, torsional stiffness and misalignment.
4. Spindle material/condition, keyway/shoulder stress concentration, fatigue, deflection and retention.
5. Bearing fit, life, axial load and oscillatory duty; carrier stiffness, bolts and flange/root plate strength.
6. Position error budget and power-loss holding safe state; brake/controller/regen safety.
7. Detailed CAD interference/access/cabling review and optional FEA only once geometry/load cases are frozen.
8. Physical tests only if later authorized. The original assignment says they are not required.

## CAD and document checks

- Report PDF: 3 pages (fits the 3–5 page range).
- QA review: 2 pages; gap closure plan: 3 pages; simulation/verification plan: 2 pages.
- Presentation PDF: 8 slides; content covers the expected 10-minute design walkthrough and leaves speaker notes/Q&A separately editable.
- Drawing PDFs: one-page A3 landscape output.
- Native FreeCAD `.FCStd` not produced because FreeCAD is not installed in this environment. Macro is supplied to create it in a FreeCAD installation; neutral STEP is a permitted equivalent CAD deliverable. Assembly/service sequence is described as a proposal only: bearing retention, cap retention, tool reach, cabling and collision-free access are not proven by the current envelope CAD.

## Final status

Assignment concept package complete, with open technical questions surfaced and assigned closure methods. Not manufacturing-ready, not supplier-frozen, not physically validated, and not safety-certified.
