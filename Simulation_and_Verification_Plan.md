# Simulation and verification plan

This is a proposed future protocol; the assignment expressly does not require detailed FEA or a physical prototype. No simulation or test outcomes beyond the stated CAD geometry validity and calculations are claimed.

| ID | Check | Required evidence | Acceptance approach |
|---|---|---|---|
| V-01 | Requirements/duty | Signed trajectory, acceleration, reversals, dwell, stops/impact, life, temperature, accuracy/backlash and hold requirement | Unknowns answered or formally bounded before freeze |
| V-02 | Static torque | Independent calculation and mass/COM confirmation | Reconcile with 6.0822 N·m static; explicit units |
| V-03 | Drive point | Supplier configured order code, loaded curves and gearhead efficiency | 45 RPM at specified torque and duty concurrently achieved |
| V-04 | Dynamic/thermal | Inertia model, peak/RMS torque, power loss and thermal evidence | Below manufacturer ratings with approved margin |
| V-05 | Coupling | Hub/bore/key part numbers, service factor, speed, stiffness, misalignment | All limits pass for reversing servo duty |
| V-06 | Spindle | Detailed drawing, notch/fatigue, stress, deflection and fit review | Criteria set by project design standard are satisfied |
| V-07 | Bearing/carrier | Modified life calculation, oscillation, axial loads, fits, housing stiffness and fasteners | Life and deflection fit requirement |
| V-08 | CAD assembly | Native assembly, collision sweep, fastener access and cable routing | No unplanned interference through specified motion range |
| V-09 | Optional FEA | Solver files, boundaries, contacts, mesh convergence and sensitivity | Independent reviewer accepts model; does not replace fatigue or vendor checks |
| V-10 | Controls/safety | Safe state, brake/hold architecture, limits, E-stop, regen and encoder setup | Safe power-loss and fault behaviour established |
| V-11 | Bench torque/speed | Calibrated torque/RPM/current/voltage measurements on restrained guarded fixture | Measured operating point meets defined target |
| V-12 | Duty/thermal test | Raw time-series for current, speed and temperature over representative cycle | Steady-state temperatures and ratings remain acceptable |
| V-13 | Backlash/compliance | Bidirectional load steps and output angular/linear measurements | Position error meets explicit budget |
| V-14 | Final review | Reconciled BOM/configuration/deviations/test evidence and approval | All requirements passed or documented waivers approved |

## Minimum future bench safety setup

- Rigid guarded fixture and restrained arm; no person beneath/in the load plane.
- Calibrated torque and RPM instrumentation, current/voltage logging, temperature sensors and uncertainty record.
- Emergency stop, current limit, mechanical stops, cable restraint and safe handling of regenerative energy.
- Test sequence: unloaded direction check; low load; static load points; loaded 45 RPM point; representative cycle; reversal/backlash measurement.
- Predefined abort limits for overcurrent, excess temperature, abnormal movement, noise/vibration, fixture slip or unanticipated motion.
