# Comprehensive gap closure plan — K-EL/01

## Principle

Use the supplied challenge brief as the requirement baseline. Generate evidence where possible now, and define a specific closure method for every missing technical input. Do not silently convert assumptions to requirements or present future tests/simulations as completed work.

## Original brief coverage map

| Requirement | Deliverable / evidence | Current status |
|---|---|---|
| Static torque, target and margin, motor speed/ratio | `Calculations.csv`, workbook `Inputs`/`Calcs`/`Sensitivity`, concise report | Generated and numerically checked; 2× is an assumption, not a certified factor |
| Motor + gearhead commercial candidate and official references | `Component_Research.csv`, report, supplier query register | Candidate shortlist supported by official product references; configured stack and loaded point open |
| Actuator CAD + integrated simplified arm | STEP, `Build_K_EL01_STEP.py`, `.FCMacro` | Equivalent neutral CAD generated; valid geometry, 21 solids; detailed manufacturing CAD not claimed |
| Labelled assembly drawing | `K_EL01_Assembly_Drawing.pdf/.svg/.png` | Generated as A3 concept drawing with numbered item key/load paths/spacing/overhang |
| One-page artwork | `K_EL01_Concept_Drawing.pdf/.svg/.png` | Generated; complete arm plus exploded elbow, labels, dimensions, torque/speed and open trade-off |
| BOM | `BOM.csv`, workbook BOM tab | Generated; candidates vs custom/TBD/conditional are marked |
| 3–5 page short report, assumptions, Q1–Q6, two risks | 3-page PDF + editable DOCX | Complete at assignment scope |
| 10-minute presentation + 10-minute technical discussion | 8-slide PPTX/PDF, timed speaker notes, technical Q&A | Prep materials supplied; candidate must present/practice live |
| Scope and uncertainty | QA report, verification plan, this plan and source brief | No prototype/purchases/manufacturing-ready drawings/detailed FEA claimed |

## Ordered closure gates

### Gate 0 — confirm requirements with project lead
Obtain duty cycle, trajectory, peak speed, acceleration/deceleration, reversals, dwell, stops/impact assumptions, life, ambient temperature, allowed endpoint error/backlash/stiffness, cable force, full link/attachment mass/inertia and power-loss holding/safe state. Produce a signed requirement and assumption log. **Exit:** unknowns are answered or explicitly bounded.

### Gate 1 — freeze drive configuration with supplier
Ask maxon for a configured orderable motor/gearhead/encoder/controller stack; actual speed/torque curve at 4095 RPM and 45 RPM output; continuous/intermittent curves; efficiency at design torque/speed; thermal limits; allowable radial/axial loading; regen limits; and interpretation of the 180 W class label versus 0.423 N·m × 4470 RPM ≈198 W arithmetic. Maxon states that EC-i iron-winding speed/torque characteristics are not a single straight line, so do not extrapolate the 0.321 rpm/mNm gradient as constant. **Evidence:** supplier response, data sheet revision, exact order codes. No supplier freeze is claimed before this.

### Gate 2 — complete coupling and shaft interfaces
Confirm two ROTEX GS hub models/bore/keyway, spider size, service factor for reversing servo duty, max speed, torsional stiffness and misalignment; match the gearhead output interface. Finalize spindle material/condition, keyway, shoulders, retention, runout, fits, bearing journals and hub engagement. **Evidence:** controlled interface drawing, approved vendor selection and recalculated strength.

### Gate 3 — native CAD and detailed assembly
Open STEP in FreeCAD or an accepted CAD tool; execute the macro if using FreeCAD; save native file if useful; re-export STEP and compare geometry/orientation. Import official supplier CAD where available. Add mount details, fasteners, cable route, verified removable access, bearing seats/retention, stop features and required joint motion. Verify fastener/tool reach and service sequence. **Evidence:** native assembly, object tree, screenshots, interference/access report. FreeCAD is not installed in the current environment, so native `.FCStd` generation is tool-gated; equivalent STEP is already included.

### Gate 4 — analytical validation
Calculate reflected rotor/link inertia, gravity torque across range, peak and RMS torque/current from trajectory, stop/impact cases, thermal losses, shaft combined stress with notches/fatigue/deflection, key/hub contact, fastener and flange loads, bearing modified L10 life/oscillation, carrier stiffness and output position error. **Evidence:** workbook and signed independent calculation review.

### Gate 5 — simulation only where useful
Run CAD interference and motion sweep first. If detailed geometry and boundary conditions are defined, use FEA on yoke/root plate/flange/spindle with mesh convergence and realistic contacts/preload/load cases. Use supplier sizing tools for bearings and reducer. **Evidence:** native analysis files, assumptions, solver settings, mesh sensitivity, plots and review. Detailed FEA is not required by the assignment and has not been run/claimed.

### Gate 6 — safe control/hold design
Define emergency stop and power-loss safe state. If gravity load must be held, size a normally engaged brake/counterbalance/support and confirm controller current/thermal/regen limits. Define feedback placement, encoder polarity/resolution, end stops and fault response. **Evidence:** reviewed control block diagram and safety/risk assessment.

### Gate 7 — controlled future bench validation
Only if later authorized and after configuration freeze: use a guarded restrained fixture, calibrated torque/RPM measurement, voltage/current logging, thermocouples, E-stop, limits and defined abort thresholds. Progress unloaded → low load → static points → loaded 45 RPM → representative duty cycle → backlash/deflection/reversal checks. **Evidence:** protocol, raw CSV, calibrated instrumentation, uncertainty and acceptance comparison. No such test has been performed.

### Gate 8 — review and release
Close all requirement/hazard rows, supplier queries, drawing/BOM configuration and test deviations. Archive revisions, sources, code, analysis and approvals. **Current disposition:** concept submission package, not a design/manufacturing release.

## 5-day plan suggested by the brief

1. Requirements, assumption log and static sizing.
2. Candidate drive research, official data and supplier questions.
3. CAD architecture, load path, access and assembly drawing.
4. BOM, risks, critical-thinking answers, one-page artwork and 3–5 page report.
5. Independent calculation/file review, rendered visual QA, package index/checksum and timed presentation rehearsal.

## Acceptance checks

- Calculations have explicit units, source or assumption for each input, and formulas reconcile.
- Component evidence is official and the exact configured stack is not misrepresented as frozen.
- CAD opens and has documented units/orientation; file validity is not called structural verification.
- Artwork includes specified views, labels, dimensions, load arrows, torque/speed and a trade-off note.
- Report contains all six critical thinking answers, two risks and concise assumptions.
- Presentation is timed to 10 minutes and discussion prep answers likely questions without overclaiming.
- Package has index/hashes, original source brief and successful ZIP integrity test.
