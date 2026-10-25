# Final source-to-deliverable audit — KR-MECH-INT-001

**Audit date:** 25 October 2026  
**Disposition:** Aligned to the original brief at conceptual-submission scope, with explicitly disclosed supplier/CAD validation gates. This is not a manufacturing, safety, or performance release.

## Requirement coverage

| Original brief objective | Evidence in this package | Audit disposition |
|---|---|---|
| Calculate static elbow gravity torque from 1.0 kg at 350 mm and 1.5 kg at 180 mm | `Calculations.csv`, `K_EL01_Engineering_Workbook.xlsx`, report | Covered. Static result is 6.0822 N·m for the specified horizontal-arm case. |
| State preliminary output torque target and justify margin | Report, workbook, sensitivity CSV | Covered with an explicit assumed 2× multiplier: 12.1644 N·m. It is not represented as a certified safety factor. |
| Estimate motor speed/gear reduction for 45 RPM | Report, workbook, calculation CSV | Covered. 91:1 yields a nominal 4095 RPM kinematic input target. Actual loaded operation remains unverified. |
| Select a commercial motor/gearhead candidate with official source references | `Component_Research.csv`, report reference section, `Supplier_Clarifications.csv` | Covered as a shortlist, not a supplier-frozen, orderable stack. The 180 W class label versus nominal T×ω arithmetic requires manufacturer clarification. |
| Concept actuator with motor, reducer, spindle, bearings, housing and forearm attachment | STEP assembly, builder script, FreeCAD macro, assembly drawing | Covered at envelope-concept level. Exact retention, fits, interfaces and physical assembly have not been verified. |
| Integrate simplified upper arm, forearm and wrist/payload interface | STEP assembly and concept artwork | Covered. Upper-arm and forearm lengths (300 mm and 350 mm) are illustrative, not assignment-prescribed dimensions. Artwork now labels both. |
| Show plausible torque/radial load paths and consider assembly/maintenance | Both drawings, report, gap plan and verification plan | Conceptual coverage. A proposed service sequence is stated; bearing/cap retention, tool reach, cables and collision-free service are open CAD checks. |
| BOM with quantity/model/vendor where known; two risks and mitigations | `BOM.csv`, report, `Risk_Register.csv` | Covered at concept scope; custom details and exact coupling hub options remain open. |
| Answer critical-thinking questions Q1–Q6 | Report and technical discussion Q&A | Covered. Q1 is labelled as a hypothetical scenario, not a proven failure of the selected candidate. |
| One-page artwork with whole arm view, enlarged actuator, labels, load paths, dimensions, torque/speed and trade-off/open issue | `K_EL01_Concept_Drawing.pdf/.svg/.png` | Covered after adding explicit illustrative forearm-link length. The drawing is schematic, not to scale or for manufacture. |
| Required report, calculation sheet, CAD, drawing, artwork, BOM and organized package | Report PDF/DOCX, workbook/CSVs, STEP/source/macro, drawings, manifest and source brief | Covered. The report is 3 pages, within the 3–5 page expectation. |
| Prepare 10-minute presentation plus 10-minute technical discussion | PPTX/PDF, timed speaker notes, Q&A bank | Preparation materials covered; the candidate must rehearse and deliver the live review. |

## Cross-file consistency and integrity checks

- The nominal static torque and target torque reconcile to 6.0822 N·m and 12.1644 N·m.
- The 45 RPM × 91:1 speed estimate reconciles to 4095 RPM.
- The 40% efficiency screen reconciles to about 0.334 N·m, 143.3 W and 3.64 A. The 30% sensitivity case exceeds the simplified nominal torque/current screen.
- The CAD support spacing and overhang are each 50 mm in the idealized screen. The moment is explicitly converted from N·m to N·mm before mm-based stress formulas.
- The macro COM marker coordinate has been aligned to the STEP builder coordinate.
- The artwork and assembly drawing have been regenerated and visually reviewed; the assembly service note is kept within the drawing panel.
- Workbook imported with `artifact_tool`; the key Dashboard values agree with the report and CSV calculations. The formula-error scan matched zero `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, or `#N/A` cells.
- Python source files and the macro pass syntax parsing; the notebook loads as nbformat 4 with 20 cells. ZIP integrity and checksums are verified for the final archive.

## Official motor-data interpretation

The maxon EC-i 52 product page for part 579165 lists a 180 W class title, nominal speed of 4470 RPM, nominal torque of 0.423 N·m, and a 0.321 RPM/mNm speed/torque-gradient figure. The arithmetic product of the listed nominal torque and speed is about 198 W, so the applicable rated operating point/power convention should be confirmed by maxon. Separately, maxon support explains that EC-i iron-winding speed/torque characteristics are nonlinear and the gradient depends on speed; the published gradient should not be extrapolated as a constant straight-line slope. These are transparent supplier questions, not a silently reconciled assumption.

- Motor product reference: https://www.maxongroup.com/maxon/view/product/motor/ecmotor/EC-i/579165
- Manufacturer guidance on motor data / speed-torque characteristics: https://support.maxongroup.com/hc/en-us/articles/360013761160-Motor-data-and-simulation

## What is genuinely still missing or open

1. **Supplier confirmation**: exact orderable motor/gearhead/encoder/controller combination; torque-speed curve at the 4095 RPM input target and the required load; efficiency and thermal duty; power-rating interpretation; coupling hub compatibility.
2. **Mission requirements absent from the brief**: motion trajectory, acceleration, cycle/dwell, life, impact/stops, link inertia, accuracy/backlash/stiffness budget, ambient/thermal assumptions, and power-loss holding behavior.
3. **Detailed CAD proof**: bearing and cap retention, fastener/tool reach, cable routing, service access, actual interfaces/fits, collision and motion-sweep verification.
4. **Native FreeCAD file**: no `.FCStd` was generated because FreeCAD was not installed in the authoring environment. This is not a missing mandatory assignment deliverable because the brief explicitly permits equivalent CAD; the valid neutral STEP, builder source, macro, and notebook helper are supplied. Run the macro locally and inspect/save `.FCStd` if desired.

## Explicitly not required / not claimed

The original brief says no purchasing, physical prototype, manufacturing-ready drawings, or detailed FEA is required. None is claimed. The package does not claim supplier validation, proven continuous torque-speed performance, thermal proof, verified safety, interference-free assembly, certified design margin, or manufacturing readiness.

## Final judgement

**No mandatory assignment deliverable category is absent from the package.** Component selection and mechanical assembly are only conditionally complete as engineering design decisions because their exact interfaces and vendor operating point remain open. Those gaps are identified and do not get disguised as completed tests. The package is suitable for conceptual review and the assignment discussion, subject to evaluator expectations.
