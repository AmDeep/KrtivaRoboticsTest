# Change log

## Comprehensive revision — 25 October 2026

- Re-reviewed all three pages of the original challenge and mapped explicit requirements, critical questions, artwork contents, and final-review expectations to deliverables.
- Rebuilt the concise design report to align the written architecture with the CAD: ROTEX GS flexible coupling + independent Ø12 mm spindle + spaced bearing support, not a custom clamp-sleeve design.
- Corrected encoder text to ENX16EASY06 / 512 CPT candidate.
- Re-derived bearing/load-plane coordinates from current STEP: bearing centres Y=11 and 61 mm; forearm centre plane Y=111 mm; 50 mm overhang and spacing.
- Wrote shaft stress unit conversion explicitly (M from N·m to N·mm) and made stress results reproducible: 7.228 MPa bending, 35.852 MPa torsional shear, 62.517 MPa von Mises nominal static screen.
- Added a formula-driven workbook with input cells, calculation formulas, efficiency sensitivity, 180 W label screen, component/BOM and risk/traceability/gap/verification/supplier tabs.
- Added a separate A3 numbered assembly drawing and retained the one-page full-arm concept artwork.
- Added gap-closure plan, simulation/verification plan, technical QA review, 8-slide presentation, timed speaking script and anticipated technical Q&A.
- Preserved original brief and documented that no FCStd file could be generated because FreeCAD is unavailable; STEP + source + macro provided.
- Explicitly retained supplier configuration, loaded point/thermal duty, coupling interface, detailed shaft/bearing/fastener verification, power-loss holding and physical testing as open gates.


## Audit follow-up — 25 October 2026

- Added the illustrative 350 mm forearm-link length to the artwork because COM radius alone is not the same as physical link length.
- Added an explicit proposed assembly/service sequence and stated that bearing/cap retention, tool reach, cabling and service access remain unverified in the envelope CAD.
- Corrected the motor-data interpretation: Maxon guidance says the EC-i iron-winding speed/torque characteristic is nonlinear and its gradient is speed-dependent; the catalogue gradient is not a constant straight-line slope. The distinct 180 W class versus nominal Tω arithmetic is still a supplier question.
- Aligned the macro's COM marker coordinates with the STEP builder.
- Added the optional FreeCAD notebook to the release and synced artwork/assembly files before regenerating the delivery index and checksum manifest.
