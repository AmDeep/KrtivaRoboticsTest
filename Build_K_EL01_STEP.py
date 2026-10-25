"""Build K_EL01_Split_Yoke_Concept.step with CadQuery.
All sizes are mm. Catalogue parts are simplified envelope solids, not vendor STEP models.
Run: python Build_K_EL01_STEP.py
"""
from pathlib import Path
import cadquery as cq
from cadquery import Vector
OUT=Path(__file__).resolve().parent
A=cq.Assembly(name='K_EL01_Split_Yoke_ECi52_GP52C_Concept')
C={'metal':cq.Color(0.72,0.77,0.81),'dark':cq.Color(0.20,0.29,0.36),'blue':cq.Color(0.08,0.48,0.62),'teal':cq.Color(0.18,0.68,0.72),'orange':cq.Color(0.88,0.48,0.12),'light':cq.Color(0.87,0.91,0.94),'bearing':cq.Color(0.55,0.63,0.69)}
def add(n,s,c='metal'): A.add(s,name=n,color=C[c])
def box(n,d,b,c='metal'): add(n,cq.Solid.makeBox(*d,Vector(*b)),c)
def cy(n,r,l,y,c='metal',x=0,z=0): add(n,cq.Solid.makeCylinder(r,l,Vector(x,y,z),Vector(0,1,0)),c)
def tube(n,ro,ri,l,y,c='metal',x=0,z=0):
    o=cq.Solid.makeCylinder(ro,l,Vector(x,y,z),Vector(0,1,0)); i=cq.Solid.makeCylinder(ri,l+2,Vector(x,y-1,z),Vector(0,1,0)); s=o.cut(i)
    if len(s.Solids())!=1: raise RuntimeError(n)
    add(n,s,c)
# Links are illustrative. Axis conventions: elbow axis Y, arm plane X-Z, gravity -Z.
box('UpperArmLink_300mm_Illustrative',(58,48,300),(-29,-24,-325),'light')
carrier=cq.Solid.makeBox(90,82,90,Vector(-45,0,-45)).cut(cq.Solid.makeCylinder(16,84,Vector(0,-1,0),Vector(0,1,0)))
add('SplitYoke_BearingCarrier_Envelope',carrier,'metal')
box('Removable_BearingCarrier_Cap',(90,12,14),(-45,35,45),'dark')
cy('ECi52_579165_Motor_Envelope_D52x80',26,80,-198.5,'dark')
cy('ENX16EASY06_512CPT_Configurable_Encoder_Envelope_D32x12',16,12,-210.5,'teal')
cy('GP52C_223094_91to1_Gearhead_Envelope_D52x78p5',26,78.5,-118.5,'metal')
tube('KTR_ROTEX_GS_Size19_98ShA_Coupling_Envelope',19,6.25,40,-40,'teal')
cy('Independent_Output_Spindle_12mm_Assumed',6,175,-82,'metal')
tube('SKF_6201_2RSH_Bearing_A_12x32x10',16,6,10,6,'bearing')
tube('SKF_6201_2RSH_Bearing_B_12x32x10',16,6,10,56,'bearing')
tube('Optional_Output_Encoder_Target_Ring_Not_Selected',13.5,6.2,4,68,'teal')
box('Optional_Output_Encoder_Sensor_PCB_Envelope_Not_Selected',(6,12,18),(14,66,-9),'orange')
tube('Spindle_Retainer_A_Envelope_Detail_TBD',8,6.05,2,17,'dark')
tube('Spindle_Retainer_B_Envelope_Detail_TBD',8,6.05,2,67,'dark')
cy('Forearm_Output_Flange_Envelope',34,10,82,'teal')
# Root plate bridges the offset between the shaft flange face and arm beam envelope.
box('Forearm_Root_Mount_Plate_Concept',(100,8,62),(-35,92,-31),'dark')
box('Forearm_Link_350mm_Illustrative',(350,48,52),(0,87,-26),'light')
box('Wrist_Payload_Interface_Illustrative',(32,56,45),(325,83,-22.5),'dark')
box('Payload_1kg_Envelope_CenterAt350mm',(45,45,45),(327.5,88.5,-22.5),'blue')
cy('Payload_COM_Marker_350mm',3.5,4.5,108.75,'orange',x=350)
cy('ForearmHand_COM_Marker_180mm',3.5,4.5,108.75,'orange',x=180)
path=OUT/'K_EL01_Split_Yoke_Concept.step'
A.save(str(path),exportType='STEP')
print('Saved',path)
