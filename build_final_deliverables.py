from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pptx import Presentation
from pptx.util import Inches as PInches, Pt as PPt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor as PRGB
import csv, shutil, os, textwrap, math

ROOT=Path(__file__).resolve().parent
STAMP='25 October 2026'
NAVY='183247'; TEAL='0E7490'; ORANGE='C97922'; PALE='EAF2F5'; MID='557080'; RED='A52626'; GREEN='2B6E4F'

def shade(cell, fill):
    tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)
def set_cell_text(cell, text, bold=False, color=None, size=8):
    cell.text=''
    p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(0); p.paragraph_format.space_before=Pt(0)
    r=p.add_run(str(text)); r.bold=bold; r.font.name='Aptos'; r.font.size=Pt(size)
    if color: r.font.color.rgb=RGBColor.from_string(color)
    cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER

def setup_doc(title, subtitle=None, small=False):
    d=Document(); sec=d.sections[0]
    sec.top_margin=Inches(0.55 if small else 0.65); sec.bottom_margin=Inches(0.55 if small else 0.65); sec.left_margin=Inches(0.6); sec.right_margin=Inches(0.6)
    styles=d.styles
    styles['Normal'].font.name='Aptos'; styles['Normal'].font.size=Pt(8.8 if small else 9.4); styles['Normal'].font.color.rgb=RGBColor(35,49,58)
    styles['Normal'].paragraph_format.space_after=Pt(3.5); styles['Normal'].paragraph_format.line_spacing=1.03
    for sn,sz,col in [('Title',24,NAVY),('Heading 1',15,NAVY),('Heading 2',11,TEAL),('Heading 3',9,ORANGE)]:
        st=styles[sn]; st.font.name='Aptos Display'; st.font.size=Pt(sz); st.font.bold=True; st.font.color.rgb=RGBColor.from_string(col)
        st.paragraph_format.space_before=Pt(8); st.paragraph_format.space_after=Pt(3)
    header=sec.header.paragraphs[0]; header.text='KRITVA ROBOTICS  |  KR-MECH-INT-001  |  K-EL/01'; header.style='Caption'
    header.runs[0].font.color.rgb=RGBColor.from_string(MID); header.runs[0].font.size=Pt(8)
    footer=sec.footer.paragraphs[0]; footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
    rr=footer.add_run(f'Concept design only • {STAMP} • Not a manufacturing release'); rr.font.size=Pt(7); rr.font.color.rgb=RGBColor.from_string(MID)
    p=d.add_paragraph(); p.style='Title'; p.add_run(title)
    if subtitle:
        p=d.add_paragraph(); p.paragraph_format.space_after=Pt(8); r=p.add_run(subtitle); r.italic=True; r.font.size=Pt(10); r.font.color.rgb=RGBColor.from_string(MID)
    return d

def para(d, text, boldlead=None):
    p=d.add_paragraph()
    if boldlead and text.startswith(boldlead):
        p.add_run(boldlead).bold=True; p.add_run(text[len(boldlead):])
    else: p.add_run(text)
    return p

def bullet(d, text, level=0):
    p=d.add_paragraph(style='List Bullet' if level==0 else 'List Bullet 2'); p.paragraph_format.space_after=Pt(1.5); p.add_run(text); return p

def numbered(d,text):
    p=d.add_paragraph(style='List Number'); p.paragraph_format.space_after=Pt(2); p.add_run(text); return p

def table(d, headers, rows, widths=None, font=7.7):
    t=d.add_table(rows=1, cols=len(headers)); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'
    for j,h in enumerate(headers): set_cell_text(t.rows[0].cells[j],h,True,'FFFFFF',font); shade(t.rows[0].cells[j],NAVY)
    trPr=t.rows[0]._tr.get_or_add_trPr(); repeat=OxmlElement('w:tblHeader'); repeat.set(qn('w:val'),'true'); trPr.append(repeat)
    for ri,row in enumerate(rows):
        cells=t.add_row().cells
        for j,val in enumerate(row):
            set_cell_text(cells[j],val,False,None,font)
            if ri%2==1: shade(cells[j],'F2F6F8')
    if widths:
        for rr in t.rows:
            for i,w in enumerate(widths): rr.cells[i].width=Inches(w)
    d.add_paragraph().paragraph_format.space_after=Pt(0)
    return t

def savepdf(docx_path):
    out=ROOT/'lo_export'; out.mkdir(exist_ok=True)
    os.system(f"libreoffice -env:UserInstallation=file:///tmp/lo_kritva_{os.getpid()} --headless --convert-to pdf --outdir '{out}' '{docx_path}' >/tmp/lo.log 2>&1")
    src=out/(Path(docx_path).stem+'.pdf')
    if src.exists(): shutil.copy2(src, Path(docx_path).with_suffix('.pdf'))
    else: print('PDF export failed',docx_path,open('/tmp/lo.log').read())

# Update main report with correct coupling architecture and transparent status.
d=setup_doc('K-EL/01 Split-Yoke Elbow Actuator','Concept design report • Revised against the original KR-MECH-INT-001 brief')
para(d,'Purpose. This report documents an assignment-stage elbow actuator concept, the prescribed static gravity calculation, preliminary drive screening, a load-path concept, trade-offs, and unresolved verification tasks. It is deliberately not presented as a production-ready, safety-certified, or physically tested mechanism.')
d.add_heading('1. Requirements and basis',1)
table(d,['Input / brief requirement','Value','Status'],[
('Payload mass and COM radius','1.0 kg at 350 mm from elbow','Specified in brief'),('Forearm + hand mass and COM radius','1.5 kg at 180 mm','Specified in brief'),('Initial configuration','Forearm horizontal; gravity-only static load','Specified in brief'),('Output speed','45 RPM','Specified in brief'),('Motor / transmission / feedback','BLDC/PMSM; planetary preferred; encoder','Specified in brief'),('Upper arm / forearm envelope','300 mm / 350 mm CAD envelopes','Illustrative design assumptions; not brief inputs'),('Preliminary torque multiplier','2.0 × static gravity torque','Engineering assumption only; not a certified safety factor')], [2.3,2.35,2.3],7.5)
d.add_heading('2. Static sizing and speed/power check',1)
para(d,'For a horizontal forearm, each gravity torque is T = m g r. The input masses and centre-of-mass distances are taken directly from the challenge. Link masses beyond the stated forearm/hand mass, inertia, cable forces, impacts and friction are not included.')
table(d,['Term','Calculation','Result'],[
('Payload torque','1.0 kg × 9.81 m/s² × 0.350 m','3.4335 N·m'),('Forearm/hand torque','1.5 kg × 9.81 m/s² × 0.180 m','2.6487 N·m'),('Total static torque','3.4335 + 2.6487','6.0822 N·m'),('Preliminary output target','2.0 × 6.0822','12.1644 N·m'),('Output angular speed','45 × 2π / 60','4.7124 rad/s'),('Ideal output mechanical power','12.1644 × 4.7124','57.32 W'),('Input speed with 91:1','45 RPM × 91','4095 RPM')], [1.65,3.25,1.8],7.7)
para(d,'The 2× multiplier is a preliminary design target only. It is not evidence that acceleration, impacts, stop loads, fatigue or an industry safety factor have been satisfied. A real motion profile and application safety requirements are needed to establish peak and RMS torque.')
d.add_heading('3. Candidate drive and evidence',1)
table(d,['Part / published candidate data','Interpretation and open verification'],[
('maxon EC-i 52, 48 V, part 579165: nominal 4470 RPM, 0.423 N·m, 4.59 A; product page labels it 180 W class.','4095 RPM input target is only 375 RPM below nominal speed (~8.4% headroom). Nominal Tω arithmetic is ~198 W vs the 180 W class label; request the applicable rating point and loaded curve. Maxon says EC-i iron-winding speed/torque characteristics are nonlinear, so the published 0.321 rpm/mNm gradient must not be extrapolated as a constant slope.'),
('maxon GP 52 C, 91:1, candidate part 223094: 30 N·m maximum continuous output torque, 45 N·m intermittent, up to 75% efficiency, ~1° average no-load backlash.','Rated torque appears to exceed 12.16 N·m but efficiency is not guaranteed at the required load/speed/duty. Product is part of a configured combination; exact orderable motor/gearhead/encoder stack remains unfrozen.'),
('maxon ENX16EASY06 encoder candidate: 512 CPT configuration; EPOS4 Disk 60/8 CAN candidate controller.','Encoder option and controller interface/current/thermal/regen integration require configuration confirmation. Motor-side feedback does not measure output-side compliance/backlash.'),
('2 × SKF 6201-2RSH bearings, 12 × 32 × 10 mm; KTR ROTEX GS size 19 flexible coupling with 98 ShA spider candidate.','Envelope/rating data is not a full life or application check. Coupling hub bores, keying, service factor, stiffness, speed and misalignment must be confirmed.')], [3.0,3.7],7.25)
p_sens=para(d,'Efficiency sensitivity at the output target: at assumed 40% reducer efficiency, required motor torque is about 0.334 N·m, idealized motor-side power 143.3 W and a torque-constant current screen ~3.64 A. At 30%, these become ~0.446 N·m, 191.1 W and ~4.85 A; that scenario exceeds the motor’s simple nominal torque/current screen and the 180 W class label. These are screening equations, not a manufacturer torque-speed, temperature or loaded-efficiency prediction.')
p_sens.paragraph_format.keep_together = True
d.add_heading('4. Mechanical concept and load paths',1)
para(d,'K-EL/01 uses a split-yoke bearing carrier with two spaced 6201 bearing envelopes supporting an independent nominal Ø12 mm output spindle. A KTR ROTEX GS size 19 flexible coupling candidate transmits reducer torque to the spindle; the forearm attaches through a concept flange and root-mount plate. Motor, encoder, gearhead, coupling, spindle, bearings, carrier and arm links are represented as simplified CAD envelopes, not vendor-supplied solids or detailed part geometry.')
bullet(d,'Torque path: motor → planetary gearhead → flexible coupling → independent spindle → output flange/root plate → forearm.')
bullet(d,'Radial-load path: forearm/root plate → spindle → two spaced support bearings → split-yoke carrier → upper-arm structure. Gearhead torque rating alone is not treated as proof of cantilever radial-load capability.')
bullet(d,'Proposed service concept (not yet proven in CAD): preassemble spindle/bearings, seat and retain the bearing set in the carrier, align the two coupling hubs, then close the removable access cap. Detailed CAD must demonstrate bearing retention, cap retention, fastener/tool reach, cable access and collision-free servicing; the current envelope model does not verify these interfaces.')
bullet(d,'CAD-derived envelope coordinates put bearing centres at Y=11 and 61 mm (50 mm spacing); the forearm-link centre plane is Y=111 mm, hence a 50 mm overhang beyond the rear bearing centre for the simplified reaction model.')
d.add_heading('5. Structural and backlash screens',1)
table(d,['Check','Screen result','Limit'],[
('Gravity force from stated masses','(1.0 + 1.5) × 9.81 = 24.525 N','Ignores unspecified link mass and dynamics'),('Overhang moment','24.525 N × 50 mm = 1226.25 N·mm = 1.22625 N·m','Idealized beam; coordinates from concept CAD'),('Ideal support reactions','Front/outboard 49.05 N; rear/inboard 24.525 N opposite direction','Static two-support overhung-load approximation'),('Nominal Ø12 mm spindle bending stress','σ = 32 × 1226.25 N·mm / (π × 12³ mm³) = 7.23 MPa','Units explicitly N·mm and mm; stress concentration/dynamic loads omitted'),('Nominal shear at 12.1644 N·m','τ = 16 × (12164.4 N·mm) / (π × 12³ mm³) = 35.85 MPa','Smooth-shaft torsion only; keyway omitted'),('Combined nominal von Mises','√(σ² + 3τ²) ≈ 62.52 MPa','Static nominal screen, not fatigue approval'),('Candidate material basis','17-4PH supplier minimum-yield screen ~758 MPa; yield/stress quotient ~12.1','Not a design factor: heat treatment, certificate, notch, fatigue and impact remain unknown'),('Backlash arc','1° at 350 mm radius ≈ 6.11 mm','Gearhead average no-load backlash; not full closed-loop output error')], [1.7,2.8,2.2],6.95)
para(d,'Explicit unit conversion: use M = 1.22625 N·m × 1000 = 1226.25 N·mm before applying a formula whose diameter is in millimetres. The stress arithmetic is a nominal screen only. The actual spindle/hub/coupling interfaces and section transitions require a detailed drawing, fit and notch/fatigue review.')
d.add_heading('6. BOM, risks and assignment questions',1)
para(d,'The separate BOM.csv lists candidate, custom concept, conditional, and open parts. At minimum the BOM contains the motor and reducer candidates, encoder/controller candidates, two bearings, flexible coupling with two compatible hubs, independent spindle, interface key, split carrier/cap/fasteners, flange/root plate, simplified arm links, 48 V supply and conditional holding brake. Hub bores and shaft details are intentionally listed as open rather than guessed.')
table(d,['Risk / challenge','Mitigation / evidence needed'],[
('Drive may miss speed/thermal target under load.','Obtain configured drive quote, motor torque-speed curve, loaded reducer efficiency and mission profile; calculate peak/RMS current and validate temperature on a supervised bench later.'),
('Output shaft bending/backlash/structural compliance.','Support radial load with spaced bearings; confirm spindle section/keyway/fits, bearing life, carrier stiffness, coupling torsional stiffness and output-position error.')],[2.5,4.2],7.4)
d.add_heading('Critical-thinking answers',2)
for q,a in [
('Q1 — Hypothetical: torque adequate, speed misses.','First check loaded motor speed-torque curve, supply voltage, controller limits and maximum reducer input speed. Test a faster motor/winding or lower ratio only after rechecking torque reserve and thermal duty.'),
('Q2 — Overheats in repeated movement.','Static gravity sizing misses acceleration, deceleration, reversals, RMS torque, copper/iron loss, gearbox friction and heat rejection. Collect current, speed, duty, winding/housing temperature and vendor thermal data over the actual cycle.'),
('Q3 — Gearhead torque rating vs bending.','A torque rating is not a radial-load or cantilever-stiffness rating. Place two separated bearings in the output carrier and route radial force into the structure; calculate shaft stress/deflection and bearing life.'),
('Q4 — Two missing requirements.','Clarify motion profile/duty/acceleration and required output accuracy/backlash/stiffness. Also obtain impact and power-loss hold expectations before design freeze; these may become safety-critical.'),
('Q5 — Low-cost backlash vs stiffness.','For an accurate elbow, tentatively favour low backlash/stiffness if performance requires it, but decide from loaded reversal error, position budget, life, efficiency, noise and budget. The ~1° no-load figure is a warning, not the assembled accuracy.'),
('Q6 — Assumption and validation.','The 2× static multiplier may not cover dynamics or impact. Derive inertia and trajectory, calculate peak/RMS torque, review stop cases and later validate a guarded, supervised duty-cycle test with current and temperature measurements.')]:
    p=d.add_paragraph(); p.paragraph_format.space_after=Pt(2); p.add_run(q+' ').bold=True; p.add_run(a)
d.add_heading('7. Deliverables and primary references',1)
para(d,'Included beside this report: calculation workbook and CSV exports; manufacturer-reference matrix; CAD neutral STEP, parametric builder source and FreeCAD macro; assembly/one-page concept drawing; BOM; traceability, gap, risk and verification registers; simulation/physical-test plan; supplier clarification list; 10-minute slide deck; speaker notes and Q&A preparation; technical QA report; this plan and package manifest. No physical prototype, purchasing, detailed FEA, manufacturing drawings or certification are claimed, consistent with assignment scope.')
d.add_heading('Primary official product references',2)
para(d,'maxon EC-i 52 motor, part 579165: https://www.maxongroup.com/maxon/view/product/motor/ecmotor/EC-i/579165. maxon GP 52 C gearhead, part 223094: https://www.maxongroup.com/maxon/view/product/gear/planetary/gp52/223094. maxon guidance on motor data and the speed/torque characteristic of iron-winding EC-i motors: https://support.maxongroup.com/hc/en-us/articles/360013761160-Motor-data-and-simulation. KTR ROTEX GS assembly guidance: https://www.ktr.com/fileadmin/ktr/media/Manuals/45510en000000.pdf. SKF bearing product reference and the encoder/controller references are listed in Component_Research.csv. Product links confirm catalogue candidates only; the exact drive combination is not supplier-frozen.')
d.add_heading('8. Release boundary',1)
para(d,'Release decision: suitable as a documented conceptual submission subject to evaluator interpretation; not released for manufacture or operation. Open technical gates are recorded in the companion QA and Gap Closure Plan. FreeCAD was not available in this build environment, so a native .FCStd file could not be generated here; execute the supplied macro in FreeCAD to create it. Neutral STEP is the CAD exchange deliverable.')
# fix weird calculation text after initial add? create proper stress row instead by replace doc table cell text later
for t in d.tables:
    for row in t.rows:
        for c in row.cells:
            if '1226.25 N·m? No:' in c.text:
                c.text=c.text.replace('1226.25 N·m? No: 1226.25 N·mm','1226.25 N·mm')
report=ROOT/'Kritva_K_EL01_Design_Report.docx'; d.save(report); savepdf(report)

# QA review
d=setup_doc('K-EL/01 Technical QA Review','Independent consistency audit against the supplied challenge brief',small=True)
d.add_heading('Executive finding',1)
para(d,'The package covers the assignment-stage deliverables and is more auditable than the earlier release. It is not proof of a validated actuator. Key design values are reproducible from the stated mass/COM inputs; CAD geometry is valid as a neutral concept model; component data are candidates and not a frozen system-level configuration.')
table(d,['Disposition','Meaning'],[
('Covered for assignment','Core calculation, candidate component selection references, simplified arm/elbow STEP, labelled concept artwork, BOM, 3–5 page report, six critical-thinking answers, two risks, and 10-minute presentation prep.'),
('Corrected in this revision','Removed legacy wording about a custom split-clamp sleeve/spindle where CAD uses a flexible coupling; updated encoder option to 512 CPT; explicitly converted N·m to N·mm for the shaft stress equation; recalculated load plane and overhang from CAD coordinates; corrected nominal bending stress to 7.23 MPa; added explicit forearm-link length to artwork and service-access caveat; interpreted EC-i speed/torque-gradient data using Maxon guidance on nonlinear iron-winding characteristics.'),
('Still open by design','Vendor stack configuration, loaded efficiency/torque-speed/thermal point, dynamic/duty profile, brake/hold requirement, coupling hub selection, shaft and carrier detail, fits and life, detailed simulation and physical verification.'),
('Not required by brief','Physical prototype, component purchasing, manufacturing-ready drawings and detailed FEA. No such work is claimed.')],[1.6,5.4],7.5)
d.add_heading('Source-to-submission coverage',1)
rows=[('Section 2: static torque','Calculation sheet and workbook; horizontal-arm calculation explicitly shown.','Pass for assignment calculation; does not cover dynamic inertia.'),('Section 2: speed/reduction','45 RPM × 91 = 4095 RPM; motor nominal 4470 RPM cited.','Preliminary pass; only ~8.4% nominal speed headroom; loaded curve required.'),('Section 3A: torque target/margin','12.1644 N·m using 2× factor.','Transparent assumption; not safety certification.'),('Section 3A: motor + gearbox evidence','Official manufacturer links and exact candidate numbers.','Shortlist only; configured combination not frozen. Ask vendor to clarify nominal Tω arithmetic vs 180 W class label; use actual EC-i speed/torque curve because its gradient is speed-dependent.'),('Section 3B: actuator + arm CAD','STEP neutral model, STEP builder source and FCMacro.','Envelope CAD, not detailed or manufacturing-ready parts; 21 solids in valid STEP.'),('Section 3B: assembly drawing/labelled view','One-page concept artwork plus numbered assembly drawing, each PDF/SVG/PNG.','Required view coverage is present; assembly/service access and bearing retention remain concept-level and must be checked in detailed CAD.'),('Section 3C: BOM and two risks','BOM.csv plus report risk section and risk register.','Covered at conceptual level; custom parts/materials/interfaces remain open.'),('Q1–Q6 critical thinking','Answers included in report and presenter Q&A.','Covered; design choices remain tentative.'),('Section 5 artwork','One-page drawing includes whole arm, enlarged exploded actuator, labels, load paths, dimensions, torque/speed callout and trade-off.','Covered for concept communication; image is not an assembly instruction or to-scale render.'),('Section 6: package organization','README, index, hashes, CSV registers, plan and technical presentation.','Covered; final archive must pass hash and zip integrity checks.'),('Section 8: final review','10-minute presentation + 10-minute tech discussion prep.','Content supplied; actual live review is user-performed.')]
table(d,['Original requirement','Evidence','QA outcome'],rows,[1.8,3.0,2.2],6.9)
d.add_heading('Numerical audit',1)
table(d,['Quantity','Recalculation','Result / interpretation'],[
('Payload torque','1.0 × 9.81 × 0.350','3.4335 N·m'),('Forearm/hand torque','1.5 × 9.81 × 0.180','2.6487 N·m'),('Total / target','6.0822 / 2','12.1644 N·m target'),('Output power at target','12.1644 × 45×2π/60','57.323 W ideal output'),('Motor speed','45×91','4095 RPM; nominal margin 375 RPM'),('Eff. 40% screen','T/(91η); Pout/η; Tm/Kt','0.3342 N·m; 143.3 W; ~3.64 A'),('Eff. 30% screen','Same equations','0.4456 N·m; 191.1 W; ~4.85 A; fails simple continuous screen'),('Overhang moment','24.525N × 50mm','1.22625N·m = 1226.25N·mm'),('Stress','σb=7.228MPa; τ=35.852MPa; VM=62.517MPa','Nominal static only; corrected unit annotation'),('Backlash arc','350mm×π/180','6.109mm at 1° average no-load')],[1.5,3.0,2.5],7.1)
d.add_heading('CAD review',1)
bullet(d,'The exported STEP was re-imported through CadQuery and reported valid geometry; 21 solids were counted. This is a file/geometry sanity check, not a kinematic, interference, strength or assembly validation.')
bullet(d,'Current model uses the ROTEX GS size 19 coupling envelope, independent Ø12 spindle, two 6201 bearing envelopes, split-yoke carrier, root plate, illustrative 300 mm upper-arm and 350 mm forearm envelopes.')
bullet(d,'Bearing centres are Y=11 and 61 mm; forearm link centreline Y=111 mm; spacing and overhang are both 50 mm for the idealized reaction calculation. The model omits detailed seals, fit classes, screw threads, realistic clamp interfaces, cable routing, shoulder mount and detailed encoder installation.')
bullet(d,'Native .FCStd was not generated because FreeCAD is not installed in the current build environment. The supplied .FCMacro is an execution route on a FreeCAD installation; STEP remains a CAD-equivalent neutral format allowed by the brief.')
d.add_heading('Risk and validation verdict',1)
for x in [
'No full motor/gearhead operating point, configured order code or continuous thermal point is available in the files. Ask maxon for a written combination recommendation, rated output curve and explanation of the 180 W class label versus nominal Tω≈198 W arithmetic. Maxon support notes EC-i iron-winding speed/torque characteristics are nonlinear, so the listed 0.321 rpm/mNm gradient should not be extrapolated as a constant slope; it is not by itself evidence of a contradictory spec.',
'No duty cycle/trajectory/acceleration/impact spec is defined. Get requirements, then calculate peak/RMS torque including inertia and worst-case stops; a static factor alone is insufficient.',
'No brake/hold requirement is specified. If the robot must hold gravity after power loss, define a normally engaged brake or external mechanical support with a rated holding torque and safe state.',
'Coupling hub bores, keying, service factor and torsional stiffness are not selected; do not treat size 19/98ShA as a full assembly part number.',
'Shaft, bearing fits/life, axial load, spindle deflection, keyway-notch fatigue, flange fasteners and carrier bolts have only screening calculations or no calculations. Complete detailed drawings and analyses before manufacturing.',
'Backlash may dominate endpoint accuracy: 1° is ~6.1 mm at payload radius before structural deflection and controls. An output-side encoder or lower-backlash reducer may be required depending on tolerance.',
'Physical test, FEA, manufacturing detail and certification are outside this assignment’s stated scope; label them as future validation, not deliverable failures.'
]: bullet(d,x)
d.add_heading('Final QA conclusion',1)
para(d,'The revised report/artwork/registries are internally aligned to one architecture. The deliverable set is assignment-complete as a concept package, with named closure actions for every material open engineering question. It should not be described as a complete engineered actuator release or proven safe design.')
qa=ROOT/'Kritva_K_EL01_Technical_QA_Review.docx'; d.save(qa); savepdf(qa)

# Comprehensive gap closure plan
d=setup_doc('K-EL/01 Comprehensive Gap Closure Plan','Original-brief review, generation plan, acceptance gates and residual unknowns',small=True)
d.add_heading('1. Purpose and governing principle',1)
para(d,'This plan maps each requirement in KR-MECH-INT-001 to a concrete file/evidence item, states what has been generated, defines how to generate/check anything still missing, and prevents assumptions from being presented as verified facts. The challenge explicitly says this is conceptual work; it does not require physical prototype, purchases, detailed FEA or manufacturing-ready drawings.')
d.add_heading('2. Required deliverables versus generated evidence',1)
rows=[
('1. Calculation sheet','Static torque, target factor, output speed and motor speed/ratio.','Calculations.csv + Engineering Workbook.xlsx + report tables.','Formula and units checked against brief; input cells highlighted in workbook.'),
('2. Component selection','One candidate motor + gearbox with official datasheets/product references.','Component_Research.csv + report with official URLs + Supplier_Clarifications.csv.','Shortlist only; request exact configured combination and loaded curve; not frozen until response.'),
('3. CAD files','Elbow concept and simplified arm assembly; CAD may be FreeCAD/SolidWorks/Fusion/equivalent.','STEP + Build_K_EL01_STEP.py + FCMacro.','STEP re-import valid, 21 solids. Native .FCStd deferred: run macro inside FreeCAD; do not claim macro generated it here.'),
('4. Drawing','One assembly drawing or clearly labelled CAD view.','STEP model plus concept drawing PDF/SVG/PNG.','Views and load paths included; concept dimensions only, no manufacturing tolerances.'),
('5. Draft artwork','One isometric whole arm, enlarged elbow/exploded view, labels/load paths, key dimensions, torque/speed, trade-off note.','K_EL01_Concept_Drawing.pdf/.svg/.png.','One A3 landscape page; perform visual check at full resolution before packaging.'),
('6. BOM','Main components, quantities, manufacturer/model if known.','BOM.csv + workbook BOM sheet.','Separates candidate/catalogue, original concept, conditional and TBD elements; no invented stock number for custom part.'),
('7. Short report','~3–5 pages; assumptions, critical-thinking answers, two risks, rationale.','Kritva_K_EL01_Design_Report.docx/.pdf.','Target 3–5 PDF pages; DOCX rendered and visually inspected before final release.'),
('Critical thinking Q1–Q6','Brief asks brief answers to each.','Report + speaker Q&A.','Answers checked against source framing.'),
('Final review','10-minute presentation then 10-minute technical discussion.','PPTX/PDF + timed speaker notes + technical Q&A.','User must rehearse/deliver; live review itself cannot be performed by deliverable generation.'),
('Original-source audit','Preserve original wording/requirements and show trace.','Original brief PDF included; Assignment_Traceability.csv.','Each original requirement maps to evidence/status; source remains unchanged.')]
table(d,['Requirement','Brief asks','Evidence/generated output','Acceptance / outstanding'],rows,[1.3,1.8,2.35,2.0],6.5)
d.add_heading('3. Remaining technical closure plan (in order)',1)
rows=[
('Gate 0 — Clarify system mission','Obtain duty cycle, trajectory, accelerations, max speed, dwell/reversals, impact/stop cases, ambient temperature, accuracy/backlash, life, cable force, load orientation and power-loss holding.','Project lead answers; revised requirement spec and signed assumption log.','Before motor/reducer design freeze; currently open because brief omits these inputs.'),
('Gate 1 — Supplier configuration','Send exact motor 579165, GP52C ratio 91:1 candidate, encoder 512 CPT, controller 688770 concept to maxon. Ask compatible configured order number, actual torque-speed curve at 4095 rpm, output torque at 45 rpm, loaded efficiency, thermal limits, continuous/intermittent/duty curves, the 180 W versus nominal Tω power arithmetic, maximum input/output loads and regen needs. Do not treat the EC-i 0.321 rpm/mNm gradient as constant; Maxon support describes its iron-winding speed/torque characteristic as nonlinear.','Written vendor response, official datasheet revision, exact order code and performance point saved to Component_Research and Supplier_Clarifications.','Do not release part numbers or claim operational pass before response.'),
('Gate 2 — Transmission interface','Select coupling hubs/bore/key, axial retention, permitted misalignment, peak/reversing torque, service factor, torsional stiffness and speed. Confirm KTR hub compatible with 12 mm spindle and gearhead’s actual keyed output.','Vendor-confirmed coupling assembly and interface sketch.','Current size 19/98ShA is a candidate family only, not full set of order codes.'),
('Gate 3 — CAD native file and assembly','Open STEP in FreeCAD (or accepted CAD), execute K_EL01_Split_Yoke_Concept.FCMacro, save .FCStd. Compare it to STEP; inspect object tree/units/orientation. Add proper constraints/joints only if supported by selected CAD package.','Native file saved from CAD; screenshot of assembly tree and isometric; export refreshed STEP.','FreeCAD unavailable in current authoring environment; user/FreeCAD workstation execution needed.'),
('Gate 4 — Engineering detail','Specify shaft material/condition, shoulders, keyway, hub contact, retaining features, bearing fits, axial load/retention, seals, bolt grades/preload, flange bolt pattern, housing wall thickness, cable route, motor mount, tolerances and assembly access.','Released detailed drawings and calculation notes, reviewed by mechanical designer.','Not required for conceptual assignment; required before building hardware.'),
('Gate 5 — Calculations','Include link inertia, motor rotor/gearhead inertia reflected through ratio, acceleration/deceleration, gravity across full range, impact/stop events, peak and RMS torque/current, output deflection, shaft combined stress with notch/ fatigue, key/hub contact, fasteners, carrier stiffness, bearing L10/oscillation and thermal equilibrium.','Updated calculation workbook; independent engineering review; explicit pass/fail thresholds derived from requirements.','Current static screens are inadequate for final release.'),
('Gate 6 — Digital analysis','Perform CAD interference/motion checks; hand calculations first; FEA for yoke/shaft/flange only if useful, with mesh convergence, boundary-condition rationale and load cases. Use bearing/vendor tools for life and manufacturer reducer sizing tool.','Native model, assumptions, solver/settings, mesh convergence, plots and output tables.','FEA is explicitly not required in assignment; do not manufacture simulation output without running it.'),
('Gate 7 — Safety and controls','Define safe state and power-loss hold. If gravity-load hold required, size normally engaged brake (including margin and release logic) or external support. Validate emergency stop, limits, encoder polarity, regenerative bus and controller derating.','Control concept, brake data or explicit excluded operating envelope, interface schematic and risk assessment.','No brake selected; supervised de-energized setup must remain externally supported.'),
('Gate 8 — Bench verification (future, not assignment task)','Only after component configuration and detailed design: guarded, restrained test stand, no personnel under load, increment torque/speed; measure output torque/speed, current, temperature, backlash and stop response.','Calibrated test setup, protocol, raw logs, uncertainty statement, comparison against requirement thresholds.','No hardware purchased/manufactured; this gate is a future plan, not reported as performed.'),
('Gate 9 — Release decision','Close every requirement and hazard; resolve supplier clarifications; sign drawings/BOM/configuration; archive revision, source, test evidence and review approval.','Design review record and controlled release package.','Current package stays “assignment concept only”.')]
table(d,['Gate','Actions','Evidence / outputs','Entry/exit rule'],rows,[1.25,2.7,2.15,1.5],6.4)
d.add_heading('4. Suggested 5-day execution plan (aligned to brief duration)',1)
table(d,['Day','Activities','End-of-day evidence / acceptance'],[
('Day 1 — Requirements & sizing','Extract brief; establish source/assumption log; torque, power and speed math; identify missing duty/accuracy inputs.','Reviewed calculation sheet and clarification list; all units and assumptions traceable.'),
('Day 2 — Drive shortlist','Compare motor/reducer candidates, official references, ratio, current/power/efficiency sensitivity and controller/encoder options.','Candidate stack and supplier questions; do not call it selected until configured point is validated.'),
('Day 3 — Architecture & CAD','Create support-bearing load path, actuator envelope, simplified arm/wrist, assembly view, link lengths and assembly access review.','Valid STEP, editable builder source/macro, key dimensions and drawing export.'),
('Day 4 — Risk, report and artwork','BOM, six Q answers, two major risks, one-page artwork, traceability, design/verification register.','3–5 page report, drawing PDF/SVG/PNG, risk and gap registers.'),
('Day 5 — QA & presentation','Peer review calculations/files, render every PDF/DOCX page and slides, archive checksums, rehearse 10-minute talk and Q&A.','Integrity-checked release package and clear residual-risk statement.')],[1.35,3.1,3.2],7.0)
d.add_heading('5. Required acceptance checklists',1)
for s in [
'Calculation acceptance: inputs match brief; torque terms independently recomputed; units are visible on every equation; target factor labelled assumption; speed ratio and output power reconcile; sensitivity rows recalculate from formulas.',
'Component acceptance: official part links reachable; revision/date captured; exact order codes and accessories verified; torque-speed-thermal point confirmed; no rated maximum or maximum efficiency represented as guaranteed operating point.',
'CAD acceptance: file opens without warnings; global unit system stated; part coordinates and assembly placement documented; model geometry valid; no overlap/interference assumed merely from STEP validity; native editable source opened in target CAD and re-export round-trip compared.',
'Drawing acceptance: whole-arm isometric and enlarged elbow/exploded view; labels distinguish candidate vendor envelopes from original parts; load-path arrows; COM radii and link lengths; torque and speed callout; at least one trade-off/open issue; text readable at 100%.',
'Report acceptance: 3–5 pages; assumptions and limitations; concise BOM rationale; two risks with mitigations; all Q1–Q6 answered; source URLs; no broken placeholders; consistent spindle/coupling architecture.',
'Presentation acceptance: 10-minute timed presentation, covering torque math, sizing, component evidence, load path, drawing/CAD, trade-offs and next validation; 10-minute discussion question prep; explicitly acknowledge unknowns.',
'Package acceptance: generated source/editable file, PDF preview, named versions, index/hash, archive integrity; no intermediate QA image folders in final zip unless explicitly useful.'
]: bullet(d,s)
d.add_heading('6. Current status and residual open items',1)
para(d,'At the time of this plan, the concept calculations, one-page artwork, candidate component references, STEP model, source CAD builder/macro, report, BOM and registers can be generated and checked. A native FreeCAD .FCStd file, supplier-confirmed drive combination, real thermal/motion proof, manufacturing detail, controlled safety design and physical-test results cannot responsibly be asserted from the provided assignment input. They have explicit routes and acceptance evidence above.')
plan=ROOT/'Kritva_K_EL01_Comprehensive_Gap_Closure_Plan.docx'; d.save(plan); savepdf(plan)

# Simulation & test plan

d=setup_doc('K-EL/01 Simulation & Verification Plan','Proposed validation protocol — no analyses or physical tests are represented as completed',small=True)
d.add_heading('1. How to use this plan',1)
para(d,'The original challenge explicitly does not require detailed FEA, manufacturing drawings, component purchases or a physical prototype. The plan below is a staged future verification route. Execute only after required mission inputs and supplier configuration are available; retain raw evidence and record failures, not just successful plots.')
rows=[
('V-01','Requirements review','Duty profile, speed range, accelerations, accuracy/backlash, impacts, temperatures, life, power-loss hold.','Project lead and engineering','Signed requirement/assumption register','All key unknowns answered or formally bounded before design freeze.'),
('V-02','Static torque audit','Horizontal-arm torque and all load directions/ranges; confirm mass/COM includes links/attachments.','Mechanical engineer','Calculation workbook and independent check','Numerical results reconcile; input sources and SI units explicit.'),
('V-03','Drive operating point','Motor torque-speed curve at actual voltage; gear ratio/input speed; loaded efficiency; continuous/intermittent output torque.','Supplier + controls engineer','Configured part-number sheet and curves','Output 45 RPM and target torque achieved simultaneously at defined duty.'),
('V-04','Duty/thermal model','Trajectory and reflected inertia; peak/RMS torque; winding and gearhead heating; temperature rise and derating.','Controls/mechanical engineer','Torque profile, loss model, thermal assumptions','Predicted temperatures below manufacturer limits with defined margin.'),
('V-05','Coupling interface','Hub bore/keyway, shaft diameters, torque reversal, speed, offset/angular misalignment, torsional stiffness.','Mechanical engineer + KTR','Selected hub/spider codes and interface drawing','All torque, speed and misalignment limits satisfied including service factor.'),
('V-06','Spindle strength','Bending+torsion, keyway notch, fatigue, shoulders, retaining grooves, deflection, stress concentrations.','Mechanical engineer','Detailed shaft CAD/drawing and checked report','Margin per agreed design standard and peak/duty load cases; no reliance on smooth-shaft screen alone.'),
('V-07','Bearing and carrier','Radial/axial reactions, L10 and oscillation factors, static safety, fits, lubrication, housing stiffness, fasteners.','Mechanical engineer','Bearing tool output, fit table, structural calculations','Life/stiffness/fit requirements met; vendor constraints observed.'),
('V-08','CAD interference & motion','Full assembly clearance, coupling envelope, fastener access, cable bend, arm sweep, stops, collision.','CAD designer','Native assembly, screenshots, interference report','No unplanned interference over specified swept envelope; maintainability demonstrated.'),
('V-09','Finite-element analysis (optional)','Yoke, flange/root plate and spindle only where hand calculations indicate value. Include realistic contacts, preload, load paths and mesh sensitivity.','FEA-capable engineer','Solver file, mesh convergence, BC/load rationale, stress/displacement plots','Convergence and sensitivity accepted; FEA does not replace bearing, fatigue, or supplier checks.'),
('V-10','Control/safety review','Encoder resolution/placement, polarity, controller limits, emergency stop, regen, brake and fault response.','Controls/safety engineer','Block diagram, configuration, hazard review','Safe state defined; power-loss holding behavior is explicitly met or operation externally supported.'),
('V-11','Bench torque/speed test','Guarded restrained fixture; measure torque and RPM at several duty points and current.','Test engineer','Calibration records, raw CSV, protocol','Performance reaches requirements at actual configured operating point.'),
('V-12','Thermal/duty test','Run representative movement cycle to steady state; monitor winding proxy, casing, gearhead, controller, current and speed.','Test engineer','Raw time series and uncertainty statement','Temperatures stabilize within ratings and current limits for stated duty.'),
('V-13','Backlash/deflection','Apply bidirectional load steps; measure output angle/hub displacement and elastic deflection.','Test engineer','Indicator/encoder logs and test report','Measured reversal error and stiffness meet the explicit position-error budget.'),
('V-14','Final review / release','Reconcile deviations, actions, BOM/order codes, drawings, software config and test results.','Design owner + reviewer','Signed design review record','All requirements passed/waived with accountable owner; no open critical hazard.')]
table(d,['ID','Verification','Scope','Owner','Evidence','Acceptance logic'],rows,[0.45,1.25,2.45,1.0,1.25,1.25],6.1)
d.add_heading('2. Minimal later bench setup',1)
for x in ['Rigid guarded base and restrained arm/fixture; no person under or in plane of suspended arm/payload.','Calibrated torque transducer or lever/force arrangement with known uncertainty, RPM measurement, current/voltage logging and temperature sensors.','E-stop, current limits, mechanical travel stops, cable restraint and safe power-disconnect/regeneration management.','Defined test matrix: unloaded run, low-load direction checks, several static torque points, 45-RPM loaded point, representative trajectory and reversal/backlash measurement.','Predefine abort limits for current, vibration, abnormal noise, temperature, unexpected movement and fixture displacement.']: bullet(d,x)
d.add_heading('3. Current evidence versus planned evidence',1)
table(d,['Available now','Not yet available / must not be claimed'],[
('Static calculation from brief inputs; explicit sensitivity analysis; component reference list; valid STEP geometry check; conceptual load/reaction/stress arithmetic.','Supplier-confirmed loaded point, physical torque/speed measurements, thermal steady-state data, measured backlash, detailed FEA, bearing life validation, shaft fatigue assessment, safety certification.'),
('Concept architecture and artwork; BOM and registers identify TBDs.','Manufacturing tolerance stack, full fastener/interface calculations, verified power-loss hold solution, test data from actual components.')],[3.4,3.6],7.2)
sp=ROOT/'Kritva_K_EL01_Simulation_and_Verification_Plan.docx'; d.save(sp); savepdf(sp)

# Presentation
prs=Presentation(); prs.slide_width=PInches(13.333); prs.slide_height=PInches(7.5)
blank=prs.slide_layouts[6]
def add_bg(slide, color='FFFFFF'):
    sh=slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,0,0,prs.slide_width,prs.slide_height); sh.fill.solid(); sh.fill.fore_color.rgb=PRGB.from_string(color); sh.line.fill.background()
    # push shape back (created first)
    slide.shapes._spTree.remove(sh._element); slide.shapes._spTree.insert(2,sh._element)
def title(slide,txt,sub=None):
    box=slide.shapes.add_textbox(PInches(.55),PInches(.35),PInches(12.2),PInches(.65)); p=box.text_frame.paragraphs[0]; p.text=txt; p.font.name='Aptos Display'; p.font.size=PPt(28); p.font.bold=True; p.font.color.rgb=PRGB.from_string(NAVY)
    if sub:
        b=slide.shapes.add_textbox(PInches(.58),PInches(1.03),PInches(12),PInches(.35)); pp=b.text_frame.paragraphs[0]; pp.text=sub; pp.font.size=PPt(12); pp.font.color.rgb=PRGB.from_string(MID)
def bulletbox(slide, items, x=.8,y=1.55,w=11.7,h=5.2, fs=22):
    sh=slide.shapes.add_textbox(PInches(x),PInches(y),PInches(w),PInches(h)); tf=sh.text_frame; tf.word_wrap=True; tf.clear()
    for i,item in enumerate(items):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.text=item; p.level=0; p.font.name='Aptos'; p.font.size=PPt(fs); p.font.color.rgb=PRGB.from_string('23313A'); p.space_after=PPt(13)
def footer(slide, n):
    b=slide.shapes.add_textbox(PInches(.58),PInches(7.16),PInches(12),PInches(.2)); p=b.text_frame.paragraphs[0]; p.text=f'K-EL/01 • Concept only • {STAMP}                                                       {n}/8'; p.font.size=PPt(8); p.font.color.rgb=PRGB.from_string(MID)
# 1
s=prs.slides.add_slide(blank); add_bg(s,NAVY)
b=s.shapes.add_textbox(PInches(.9),PInches(1.05),PInches(11.5),PInches(1.4)); p=b.text_frame.paragraphs[0]; p.text='K-EL/01 Split-Yoke Elbow Actuator'; p.font.size=PPt(34); p.font.bold=True; p.font.color.rgb=PRGB(255,255,255)
b=s.shapes.add_textbox(PInches(.95),PInches(2.6),PInches(11),PInches(1)); p=b.text_frame.paragraphs[0]; p.text='Conceptual mechanical design • KR-MECH-INT-001'; p.font.size=PPt(20); p.font.color.rgb=PRGB(200,224,232)
img=ROOT/'K_EL01_Concept_Drawing.png'
if img.exists(): s.shapes.add_picture(str(img),PInches(6.7),PInches(3.3),width=PInches(5.7))
b=s.shapes.add_textbox(PInches(.95),PInches(4.1),PInches(5.2),PInches(1.6)); p=b.text_frame.paragraphs[0]; p.text='10-minute design walkthrough\nPresenter: Candidate\n25 October 2026'; p.font.size=PPt(18); p.font.color.rgb=PRGB(255,255,255)
footer(s,1)
# 2
s=prs.slides.add_slide(blank); add_bg(s); title(s,'1. Problem & design basis','Use the brief inputs without silently inventing a full mission profile')
bulletbox(s,['Payload: 1.0 kg at 350 mm from elbow axis','Forearm + hand: 1.5 kg at 180 mm','Horizontal forearm is the initial gravity-only case','Output target 45 RPM; BLDC/PMSM + encoder; planetary preferred','Illustrative link envelope: 300 mm upper arm / 350 mm forearm','No duty cycle, acceleration, position accuracy, impact or power-loss holding requirement was supplied.'],fs=20); footer(s,2)
# 3
s=prs.slides.add_slide(blank); add_bg(s); title(s,'2. Static torque & preliminary target','Gravity-only result is a baseline, not a complete motion design')
tabledata=[('Payload','1.0 × 9.81 × 0.350','3.4335 N·m'),('Forearm/hand','1.5 × 9.81 × 0.180','2.6487 N·m'),('Static total','3.4335 + 2.6487','6.0822 N·m'),('Preliminary target','2.0 × static','12.1644 N·m'),('Ideal output power','12.1644 × 45×2π/60','57.32 W')]
tb=s.shapes.add_table(len(tabledata)+1,3,PInches(.8),PInches(1.65),PInches(8.2),PInches(3.5)).table
for j,h in enumerate(['Term','Formula','Result']): tb.cell(0,j).text=h
for i,row in enumerate(tabledata,1):
 for j,val in enumerate(row): tb.cell(i,j).text=val
for row in tb.rows:
 for cell in row.cells:
  for p in cell.text_frame.paragraphs:
   p.font.size=PPt(15)
   if row==tb.rows[0]: p.font.bold=True; p.font.color.rgb=PRGB(255,255,255)
  if row==tb.rows[0]: cell.fill.solid(); cell.fill.fore_color.rgb=PRGB.from_string(NAVY)
bulletbox(s,['The 2× multiplier is an assumption, not a certified safety factor.','Dynamics and inertia can dominate peak/RMS sizing.'],x=9.3,y=1.8,w=3.3,h=3.5,fs=16); footer(s,3)
# 4
s=prs.slides.add_slide(blank); add_bg(s); title(s,'3. Drive candidate & key caution','A shortlist is not a frozen supplier configuration')
bulletbox(s,['Motor candidate: maxon EC-i 52, 48 V, part 579165; nominal 4470 RPM, 0.423 N·m, 4.59 A.','Gearhead candidate: maxon GP 52 C, 91:1, part 223094; nominal input speed required = 4095 RPM.','At assumed 40% gearhead efficiency: ~0.334 N·m motor torque, ~143 W input screen, ~3.64 A torque-constant current screen.','At assumed 30% efficiency, simple continuous torque/current screen fails.','180 W class vs nominal T×ω ≈198 W: clarify rating point with maxon. EC-i curve is nonlinear; use actual curve, not a constant gradient.'],fs=18); footer(s,4)
# 5
s=prs.slides.add_slide(blank); add_bg(s); title(s,'4. Mechanical load path','Torque transmission and radial support are deliberately separated')
if img.exists(): s.shapes.add_picture(str(img),PInches(.6),PInches(1.45),width=PInches(8.0))
bulletbox(s,['Torque: motor → GP52C → ROTEX GS coupling → independent spindle → flange/root plate → forearm.','Radial load: forearm → spindle → two 6201 bearings → split yoke → upper arm.','Bearing centres 50 mm apart; forearm load plane is 50 mm beyond rear-bearing centre.','STEP is simplified envelope CAD: 21 solids, valid geometry; not proof of no interference or strength.'],x=8.8,y=1.55,w=3.9,h=4.8,fs=16); footer(s,5)
# 6
s=prs.slides.add_slide(blank); add_bg(s); title(s,'5. Structural & accuracy screens','Useful for concept decisions; not final verification')
bulletbox(s,['Gravity force from specified masses: 24.525 N; overhang moment: 1.22625 N·m = 1226.25 N·mm.','Ø12 mm nominal spindle: bending 7.23 MPa; torsional shear 35.85 MPa; von Mises ~62.52 MPa.','Stress screens omit keyway/notch factors, fatigue, shock, dynamic loads, detailed spindle geometry and deflection.','At 1° average no-load backlash, payload-radius arc is ~6.11 mm at 350 mm.','The final position error also includes compliance, controller/encoder, assembly and load effects.'],fs=19); footer(s,6)
# 7
s=prs.slides.add_slide(blank); add_bg(s); title(s,'6. Major risks & next evidence','Close mission requirements and vendor evidence before freezing hardware')
bulletbox(s,['Thermal/duty risk: define trajectory, acceleration, cycles and ambient; obtain loaded motor curve and gearhead efficiency; calculate peak/RMS torque.','Mechanical risk: confirm coupling hubs/keying, spindle section/fits, bearing life, carrier stiffness and fasteners.','Safety risk: clarify gravity hold during power loss; add rated normally-engaged brake or explicitly limit to externally supported supervised use.','Accuracy risk: 1° no-load backlash may be too high; define output-position tolerance and evaluate lower-backlash reducer/output feedback.','Validate with a guarded supervised test only after the configuration is confirmed.'],fs=18); footer(s,7)
# 8
s=prs.slides.add_slide(blank); add_bg(s); title(s,'7. Conclusion & status','Concept submission complete; engineering release is intentionally not claimed')
bulletbox(s,['Static target: 6.0822 N·m required; 12.1644 N·m preliminary target.','Candidate 91:1 drive is kinematically plausible but needs supplier-confirmed loaded operation and thermal validation.','Included package: report, workbook/CSVs, BOM, official reference matrix, STEP/source/macro, concept artwork, QA/gap plan, verification plan, presentation and discussion notes.','Native .FCStd was not created because FreeCAD is unavailable in this environment; run included macro on FreeCAD to create it.','No purchase, manufacture, FEA, physical test or certification is claimed.'],fs=18); footer(s,8)
pptx=ROOT/'Kritva_K_EL01_Final_Review_Presentation.pptx'; prs.save(pptx)
print('Generated docs and PPTX')
