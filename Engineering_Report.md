# K-EL/01 Split-Yoke Elbow Actuator

**Kritva Robotics KR-MECH-INT-001 — concept design report**  
**Revision:** 25 October 2026  
**Status:** Concept only; not a manufacturing release.

## Requirements and assumptions

The challenge specifies payload mass 1.0 kg at 350 mm, forearm/hand mass 1.5 kg at 180 mm, horizontal arm for the initial static case, output 45 RPM, BLDC/PMSM motor technology, planetary preferred, and encoder feedback. The 300 mm upper-arm link, 350 mm forearm envelope, 12 mm spindle, 50 mm bearing spacing/overhang, and 2× target multiplier are assumptions or concept geometry, not additional requirements. The multiplier is not a certified safety factor.

## Static sizing

- Payload: `T = 1.0 × 9.81 × 0.350 = 3.4335 N·m`.
- Forearm/hand: `T = 1.5 × 9.81 × 0.180 = 2.6487 N·m`.
- Total static gravity torque: `6.0822 N·m`.
- Preliminary target at assumed 2×: `12.1644 N·m`.
- Output angular speed: `45 × 2π/60 = 4.7124 rad/s`.
- Ideal output mechanical power at target torque: `12.1644 × 4.7124 = 57.32 W` before drive losses.
- Required motor speed with 91:1: `45 × 91 = 4095 RPM`.

This does not include link masses not supplied, dynamic inertias, cable forces, impacts, friction, stop events or duty-cycle thermal loads.

## Candidate drive and sensitivity

The shortlist is maxon EC-i 52, 48 V part 579165; maxon GP 52 C, 91:1 candidate part 223094; ENX16EASY06 encoder candidate configured at 512 CPT; EPOS4 Disk 60/8 CAN candidate; two SKF 6201-2RSH bearings; and a KTR ROTEX GS size 19/98 ShA flexible coupling candidate. The exact configured stack is not frozen.

At assumed 40% reducer efficiency the first-order motor-side screen is 0.334 N·m, 143.3 W and 3.64 A. At 30%, this becomes 0.446 N·m, 191.1 W and about 4.85 A, exceeding the simple continuous torque/current and 180 W-label screens. This is sensitivity arithmetic, not a manufacturer loaded operating prediction. The motor listing is titled 180 W class while nominal torque × speed gives about 198 W by arithmetic; ask the supplier to clarify the applicable rating point and conditions. Maxon support notes the EC-i iron-winding speed/torque characteristic is nonlinear and speed-dependent, so do not extrapolate the published 0.321 rpm/mNm gradient as a constant slope: https://support.maxongroup.com/hc/en-us/articles/360013761160-Motor-data-and-simulation.

## Mechanical concept

The split-yoke carrier supports an independent nominal Ø12 mm spindle with two spaced 6201 bearing envelopes. The motor/gearhead transmits torque through a KTR ROTEX GS flexible coupling candidate to the spindle. A concept flange and root plate attach the forearm. Radial load is routed through the spindle and bearing pair into the yoke/upper arm rather than relying on the reducer torque rating alone.

CAD envelope coordinates: bearing centres Y=11 mm and Y=61 mm; forearm link centre plane Y=111 mm; hence 50 mm bearing spacing and 50 mm overhang. A gravity-only radial force of 24.525 N gives `M = 24.525 × 50 = 1226.25 N·mm = 1.22625 N·m`. Explicitly converting moment to N·mm for an mm-based formula gives nominal smooth Ø12 mm shaft bending stress 7.23 MPa; nominal torsional shear at target torque is 35.85 MPa; combined nominal von Mises is about 62.52 MPa. This excludes notch factors, fatigue, impact, dynamics, fits and deflection. The yield/stress quotient is only a screening ratio, not a design factor.

Average no-load backlash of 1° corresponds to about 6.11 mm arc at a 350 mm radius. It may be unacceptable if the output-position budget is tight; define the position-error requirement before finalizing reducer/feedback choices.

## Critical-thinking answers

**Q1:** If speed is low, first check loaded torque-speed curve, voltage/drive limit and gearhead input-speed limit; then test a faster winding/motor or lower ratio while rechecking torque reserve and thermal margin.

**Q2:** Repeated overheating can come from acceleration, reversals, RMS torque, winding losses, gearbox friction, poor thermal path or excessive duty. Collect current, speed, duty, winding/housing temperature and vendor thermal curves for the actual movement cycle.

**Q3:** Gearhead torque rating is not proof of cantilever radial-load capacity. Use independent spaced bearings and calculate shaft stress/deflection, bearing life and carrier stiffness.

**Q4:** Clarify full motion/duty profile and output accuracy/backlash/stiffness. Also clarify impact/stop cases and power-loss hold/safe state before a real design freeze.

**Q5:** Prefer low-backlash/stiffness only if required by the position budget. Compare loaded reversal error, stiffness, life, efficiency, noise and cost; 1° no-load backlash is a warning, not full assembled error.

**Q6:** The 2× static target could be inadequate for dynamic or impact loads. Add link/rotor inertia and trajectory, calculate peak/RMS torque, derive worst-case stops, then run a guarded supervised duty test with current/temperature logging if hardware is later authorized.

## Risks and release boundary

Main risks: thermal/duty mismatch and mechanical stiffness/shaft support. Mitigations are a supplier-confirmed operating point and mission-profile sizing, plus detailed coupling/spindle/bearing/fastener/structural validation. Power-loss holding is not specified; de-energized gravity load must be externally supported unless a rated normally engaged brake or equivalent is designed and validated.

A valid STEP export is not a strength/interference/manufacturing proof. This package includes neutral STEP, CadQuery builder, FreeCAD macro, drawings, report, workbook, BOM, traceability, gap register, QA and future verification plan. Proposed service access is not verified in the envelope model: bearing retention, cap retention, fastener/tool reach, cable routing and collision-free maintenance require detailed CAD. A native `.FCStd` file was not generated because FreeCAD is unavailable in this environment. No hardware purchase, manufacture, FEA, physical test or certification is claimed.
