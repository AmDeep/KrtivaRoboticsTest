from pathlib import Path
import csv, json, os
from artifact_tool import Workbook, SpreadsheetFile
R=Path(__file__).resolve().parent
wb=Workbook.create()
NAVY='#183247';TEAL='#0E7490';PALE='#EAF2F5';ORANGE='#C97922';GRAY='#557080'; RED='#A52626'
def setup_sheet(name,title,subtitle=None):
    sh=wb.worksheets.add(name)
    sh.get_range('A1:H1').merge(); sh.get_range('A1').values=[[title]]
    sh.get_range('A1:H1').format={'fill':NAVY,'font':{'bold':True,'color':'#FFFFFF','size':16},'horizontal_alignment':'left','vertical_alignment':'center','row_height':28}
    if subtitle:
        sh.get_range('A2:H2').merge(); sh.get_range('A2').values=[[subtitle]]
        sh.get_range('A2:H2').format={'fill':PALE,'font':{'color':GRAY,'italic':True,'size':9},'wrap_text':True,'row_height':28}
    return sh

def style_header(sh, rng):
    sh.get_range(rng).format={'fill':TEAL,'font':{'bold':True,'color':'#FFFFFF','size':9},'wrap_text':True,'horizontal_alignment':'center','vertical_alignment':'center','row_height':26}
def style_data(sh,rng):
    sh.get_range(rng).format={'font':{'name':'Aptos','size':9,'color':'#23313A'},'wrap_text':True,'vertical_alignment':'center'}

# Dashboard
dash=setup_sheet('Dashboard','K-EL/01 — Engineering Dashboard','Formula-driven screening model • inputs can be edited on Inputs sheet; assumptions are not certified safety factors.')
dash.get_range('A4:C4').values=[['Metric','Calculated value','Units / interpretation']]; style_header(dash,'A4:C4')
rows=[
 ['Static gravity torque','','N·m — prescribed horizontal-arm case'],
 ['Preliminary output target','','N·m — torque factor is an assumption'],
 ['Required motor speed','','RPM — output speed × ratio'],
 ['Ideal target output power','','W — before drive losses'],
 ['Motor nominal speed headroom','','RPM — nominal listing minus kinematic requirement'],
 ['At base efficiency: required motor torque','','N·m — simplified ratio/efficiency screen'],
 ['At base efficiency: motor-side power','','W — ideal output power / assumed efficiency'],
 ['At base efficiency: torque-constant current','','A — current screen; not controller thermal validation'],
 ['Nominal spindle bending stress','','MPa — gravity-only, smooth shaft screen'],
 ['Nominal combined von Mises stress','','MPa — excludes notches/fatigue/dynamics'],
 ['Backlash endpoint arc','','mm — average no-load backlash at 350 mm radius'],
 ['Package / engineering status','Concept stage','Not manufacturing-ready; open gates on Traceability and Risks']]
dash.get_range('A5:C16').values=rows
formulas=[['=Calcs!C7'],['=Calcs!C8'],['=Calcs!C10'],['=Calcs!C12'],['=Calcs!C11'],['=Calcs!C8/(Inputs!B11*Inputs!B16)'],['=Calcs!C12/Inputs!B16'],['=B10/Inputs!B15'],['=Calcs!C18'],['=Calcs!C20'],['=Calcs!C22']]
dash.get_range('B5:B15').formulas=formulas
style_data(dash,'A5:C16'); dash.get_range('A5:C16').format.row_height=30
# Inputs
inp=setup_sheet('Inputs','Editable Inputs & Assumptions','Blue/teal input table values feed the calculation sheets. Orange values are design assumptions, not requirements.')
inp.get_range('A4:D4').values=[['Parameter','Value','Unit','Basis / caution']];style_header(inp,'A4:D4')
input_rows=[
 ['Payload mass',1.0,'kg','Specified in original challenge brief'],
 ['Payload COM radius',350,'mm','Specified in original challenge brief'],
 ['Forearm + hand mass',1.5,'kg','Specified in original challenge brief'],
 ['Forearm + hand COM radius',180,'mm','Specified in original challenge brief'],
 ['Gravity',9.81,'m/s²','Conventional engineering value'],
 ['Output speed',45,'RPM','Specified in original challenge brief'],
 ['Gear ratio',91,'ratio','Candidate GP 52 C; exact configuration open'],
 ['Torque multiplier',2.0,'× static','ASSUMPTION; not a certified safety factor'],
 ['Motor nominal speed',4470,'RPM','Candidate EC-i 52 part 579165 published data'],
 ['Motor nominal torque',0.423,'N·m','Candidate published nominal data; loaded point open'],
 ['Motor torque constant',0.0919,'N·m/A','Published candidate value; current screen only'],
 ['Base reducer efficiency',0.40,'fraction','ASSUMPTION for screening; not a guaranteed value'],
 ['Spindle diameter',12,'mm','Concept envelope, nominal; keyway details omitted'],
 ['Bearing centre spacing',50,'mm','CAD-derived concept geometry'],
 ['Load plane overhang',50,'mm','CAD-derived concept geometry'],
 ['Bearing dynamic rating C',7280,'N','Candidate SKF 6201-2RSH catalogue value'],
 ['Bearing static rating C0',3100,'N','Candidate SKF 6201-2RSH catalogue value'],
 ['Average no-load backlash',1.0,'degree','Candidate GP52C catalogue average, not assembled joint error'],
 ['Shaft candidate yield basis',758,'MPa','17-4PH supplier data screen; condition/certificate not frozen'],
 ['Motor continuous current',4.59,'A','Candidate EC-i52 published value; current screen only'],
]
inp.get_range('A5:D24').values=input_rows; style_data(inp,'A5:D24'); inp.get_range('B5:B24').format={'fill':'#DCECF7','font':{'color':'#164E83','bold':True},'horizontal_alignment':'right'}
inp.get_range('A12:D12').format={'fill':'#FFF2CC','font':{'color':ORANGE,'bold':True},'wrap_text':True}
inp.get_range('A16:D16').format={'fill':'#FFF2CC','font':{'color':ORANGE,'bold':True},'wrap_text':True}
inp.get_range('B5:B24').format.number_format='0.0000'
# Calcs
cal=setup_sheet('Calcs','Calculated Mechanics & Drive Screens','Formulas are unit-labelled below. Inputs are linked from Inputs; structural results are simplified static screens only.')
cal.get_range('A4:D4').values=[['Calculation','Formula / linked expression','Value','Units / limit']];style_header(cal,'A4:D4')
calc_rows=[
 ['Payload gravity torque','m_payload × g × r_payload','','N·m'],
 ['Forearm/hand gravity torque','m_forearm × g × r_forearm','','N·m'],
 ['Total static torque','T_payload + T_forearm','','N·m'],
 ['Preliminary target torque','T_static × assumed multiplier','','N·m; multiplier is not certified safety factor'],
 ['Output angular velocity','rpm × 2π / 60','','rad/s'],
 ['Required motor speed','output rpm × ratio','','RPM; kinematic, loaded curve not verified'],
 ['Nominal motor speed headroom','motor nominal − required speed','','RPM'],
 ['Ideal output power at target','target torque × angular velocity','','W before losses'],
 ['Combined gravity force','(payload + forearm/hand) × g','','N; omitted link masses/dynamics'],
 ['Overhang bending moment','force × overhang(mm) / 1000','','N·m'],
 ['Outboard/front reaction','F × (1 + e/L)','','N; ideal overhung two-support model'],
 ['Inboard/rear reaction magnitude','F × e/L','','N; opposite direction in idealized model'],
 ['Moment in N·mm','M(N·m) × 1000','','N·mm; explicit unit conversion'],
 ['Nominal bending stress','32 × M(N·mm) / (π × d³)','','MPa; smooth solid shaft'],
 ['Nominal torsional shear','16 × T_target(N·m)×1000 / (π × d³)','','MPa; keyway omitted'],
 ['Combined von Mises','sqrt(σb² + 3τ²)','','MPa; nominal static only'],
 ['Yield/stress quotient','candidate yield basis / nominal von Mises','','ratio; not a design factor'],
 ['Backlash endpoint arc','radius(mm) × backlash(deg) × π/180','','mm; no-load average only'],
 ['Bearing dynamic-rating ratio','C / front reaction','','ratio; not bearing life'],
 ['Bearing static-rating ratio','C0 / front reaction','','ratio; not a full static check'],
]
cal.get_range('A5:D24').values=calc_rows
cal_formulas=[
 ['=Inputs!B5*Inputs!B9*(Inputs!B6/1000)'],
 ['=Inputs!B7*Inputs!B9*(Inputs!B8/1000)'],
 ['=C5+C6'],
 ['=C7*Inputs!B12'],
 ['=Inputs!B10*2*PI()/60'],
 ['=Inputs!B10*Inputs!B11'],
 ['=Inputs!B13-C10'],
 ['=C8*C9'],
 ['=(Inputs!B5+Inputs!B7)*Inputs!B9'],
 ['=C13*Inputs!B19/1000'],
 ['=C13*(1+Inputs!B19/Inputs!B18)'],
 ['=C13*Inputs!B19/Inputs!B18'],
 ['=C14*1000'],
 ['=32*C17/(PI()*Inputs!B17^3)'],
 ['=16*C8*1000/(PI()*Inputs!B17^3)'],
 ['=SQRT(C18^2+3*C19^2)'],
 ['=Inputs!B23/C20'],
 ['=Inputs!B6*Inputs!B22*PI()/180'],
 ['=Inputs!B20/C15'],
 ['=Inputs!B21/C15'],
]
cal.get_range('C5:C24').formulas=cal_formulas
style_data(cal,'A5:D24'); cal.get_range('A5:D24').format.row_height=29; cal.get_range('C5:C24').format.number_format='0.0000'
# Sensitivity
sen=setup_sheet('Sensitivity','Reducer Efficiency Sensitivity','Efficiency values are scenario assumptions. Calculations use target output torque / (ratio × efficiency) and ideal output power / efficiency.')
sen.get_range('A4:G4').values=[['Assumed efficiency','Required motor torque (N·m)','Input power screen (W)','Current screen (A)','Simple capacity reserve (N·m)','Torque/current screen','180 W label screen']];style_header(sen,'A4:G4')
effs=[0.75,0.60,0.50,0.40,0.35,0.32,0.30]
sen.get_range('A5:A11').values=[[x] for x in effs]
sen.get_range('B5:F11').formulas=[[f'=Calcs!C8/(Inputs!B11*A{r})',f'=Calcs!C12/A{r}',f'=B{r}/Inputs!B15',f'=MIN(Inputs!B14,Inputs!B15*Inputs!B24)-B{r}',f'=IF(B{r}<=MIN(Inputs!B14,Inputs!B15*Inputs!B24),"PASS SCREEN","FAIL SCREEN")'] for r in range(5,12)]
sen.get_range('G5:G11').formulas=[[f'=IF(C{r}<=180,"WITHIN 180 W LABEL","OVER 180 W LABEL")'] for r in range(5,12)]
style_data(sen,'A5:G11'); sen.get_range('A5:A11').format.number_format='0%';sen.get_range('B5:E11').format.number_format='0.000';sen.get_range('F5:G11').format.horizontal_alignment='center'
sen.get_range('A13:G15').merge();sen.get_range('A13').values=[['Interpretation: this is a first-order ratio/efficiency screen only. It is not a loaded motor torque-speed curve, validated motor power rating, gearbox loss model, thermal prediction, or duty-cycle analysis. Actual vendor curves and configured stack are required.']];sen.get_range('A13:G15').format={'fill':'#FFF2CC','font':{'color':ORANGE,'size':10},'wrap_text':True,'vertical_alignment':'center'}
# Import CSV tabs
csv_tabs=[('BOM','BOM.csv','BOM — candidate, custom concept, conditional and TBD parts'),('Components','Component_Research.csv','Component Research & Official References'),('Traceability','Assignment_Traceability.csv','Original Brief Requirement Traceability'),('Risks','Risk_Register.csv','Risk Register and Mitigations'),('Validation Plan','Simulation_and_Test_Plan.csv','Future Simulation / Verification Plan'),('Gap Register','Gap_Closure_Register.csv','Gap Closure Register'),('Supplier Queries','Supplier_Clarifications.csv','Supplier Clarifications Required')]
for name,filename,title in csv_tabs:
    sh=setup_sheet(name,title,'Imported from the current register; see status/caveat columns and do not treat shortlist data as a release.')
    with open(R/filename,encoding='utf-8-sig',newline='') as f: data=list(csv.reader(f))
    sh.get_range_by_indexes(3,0,len(data),max(len(x) for x in data)).values=[x+['']*(max(len(y) for y in data)-len(x)) for x in data]
    if data:
        ncol=max(len(x) for x in data); from_cols='A4:'+chr(64+ncol)+'4';style_header(sh,from_cols)
        if len(data)>1: style_data(sh,f'A5:{chr(64+ncol)}{3+len(data)}')
        sh.get_range(f'A4:{chr(64+ncol)}{3+len(data)}').format.wrap_text=True
        sh.get_range(f'A4:{chr(64+ncol)}{3+len(data)}').format.vertical_alignment='top'
        sh.get_range(f'A4:{chr(64+ncol)}{3+len(data)}').format.row_height=45
# Width and freeze all
for name in ['Dashboard','Inputs','Calcs','Sensitivity','BOM','Components','Traceability','Risks','Validation Plan','Gap Register','Supplier Queries']:
    sh=wb.worksheets.get_item(name)
    sh.freeze_panes.freeze_rows(4)
    sh.get_range('A:A').format.column_width=31
    if name=='Dashboard':
        sh.get_range('B:B').format.column_width=23;sh.get_range('C:C').format.column_width=49
    elif name=='Inputs':
        sh.get_range('B:B').format.column_width=16;sh.get_range('C:C').format.column_width=17;sh.get_range('D:D').format.column_width=67
    elif name=='Calcs':
        sh.get_range('B:B').format.column_width=44;sh.get_range('C:C').format.column_width=16;sh.get_range('D:D').format.column_width=50
    elif name=='Sensitivity':
        sh.get_range('A:G').format.column_width=24
    else:
        sh.get_range('B:Z').format.column_width=28
# Add a read me / status page if supported just a text sheet
status=setup_sheet('Read Me','Workbook Use & Limitations','Model revision: 25 October 2026')
status.get_range('A4:B10').values=[['Topic','Instructions'],['Purpose','Editable first-order conceptual calculations and registers for KR-MECH-INT-001.'],['Edit inputs','Change blue cells on Inputs; orange rows are assumptions that may also be varied. Linked formulas feed Dashboard and Calcs; the sensitivity table shows fixed scenarios.'],['Known inputs','Payload/forearm-hand mass and COM radii; output speed; motor/transmission technology are from original brief.'],['Assumptions','2× target multiplier, reducer efficiency scenarios, link lengths and shaft diameter are design assumptions or CAD envelope values.'],['Not modelled','Dynamic inertia, peak/RMS duty, temperature, loaded torque-speed curve, detailed shaft fatigue, fit, life, FEA, backlash control error or safety certification.'],['Document links','See the companion report, QA review, gap closure plan and supplier clarification register.']]
style_header(status,'A4:B4');style_data(status,'A5:B10');status.get_range('A:A').format.column_width=27;status.get_range('B:B').format.column_width=95;status.get_range('A4:B10').format.wrap_text=True;status.get_range('A4:B10').format.row_height=36
status.freeze_panes.freeze_rows(4)
# Export xlsx
xlsx=R/'K_EL01_Engineering_Workbook.xlsx'
SpreadsheetFile.export_xlsx(wb).save(str(xlsx))
print('Saved',xlsx)
# Export formula snapshot and render key sheets for visual QA
for sheet in ['Dashboard','Inputs','Calcs','Sensitivity']:
    try:
        img=wb.render({'sheet_name':sheet,'auto_crop':'all','scale':1})
        img.save(str(R/f'_qa_render/{sheet}_workbook_preview.png'))
        print('Rendered',sheet)
    except Exception as e: print('Render skipped',sheet,repr(e))
try:
 print(wb.inspect({'kind':'sheet','include':'id,name'}).ndjson)
 print(wb.inspect({'kind':'formula','sheet_id':wb.worksheets.get_item('Calcs').id}).ndjson[:1000])
except Exception as e: print('inspect note',repr(e))
