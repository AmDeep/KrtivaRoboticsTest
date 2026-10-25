from pathlib import Path
import cairosvg
from PIL import Image
O=Path(__file__).resolve().parent
svg=r'''<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 1680 1188">
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fbfdff"/><stop offset="1" stop-color="#edf3f7"/></linearGradient>
 <linearGradient id="metal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dce5eb"/><stop offset="0.5" stop-color="#afbec9"/><stop offset="1" stop-color="#718493"/></linearGradient>
 <linearGradient id="dark" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#445b6d"/><stop offset="1" stop-color="#233747"/></linearGradient>
 <linearGradient id="teal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#56c1c8"/><stop offset="1" stop-color="#137e93"/></linearGradient>
 <marker id="arrow" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#0c7690"/></marker>
 <marker id="arrowOrange" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#d66a16"/></marker>
 <marker id="dim" markerWidth="8" markerHeight="8" refX="3.5" refY="3" orient="auto-start-reverse"><path d="M0,0 L6,3 L0,6 Z" fill="#526775"/></marker>
 <style>
 .title{font:700 38px Arial,sans-serif;fill:#20384a}.subtitle{font:17px Arial,sans-serif;fill:#526775}.panel{fill:#fff;stroke:#ccd9e2;stroke-width:2;rx:18}.sect{font:700 20px Arial,sans-serif;fill:#20384a}.label{font:600 14px Arial,sans-serif;fill:#243b4a}.small{font:14px Arial,sans-serif;fill:#435a68}.micro{font:12px Arial,sans-serif;fill:#536a78}.dim{fill:none;stroke:#526775;stroke-width:2;marker-start:url(#dim);marker-end:url(#dim)}.leader{fill:none;stroke:#647b8a;stroke-width:1.5}.load{fill:none;stroke:#d66a16;stroke-width:4;marker-end:url(#arrowOrange)}.torque{fill:none;stroke:#0c7690;stroke-width:4;marker-end:url(#arrow)}.path{fill:none;stroke:#0c7690;stroke-width:3;stroke-dasharray:7 6;marker-end:url(#arrow)}.dimtxt{font:700 15px Arial,sans-serif;fill:#3e5666}.num{font:700 25px Arial,sans-serif;fill:#117e92}.white{fill:#fff}.fine{stroke:#435b6a;stroke-width:2}.dash{stroke-dasharray:7 5}
 </style>
</defs>
<rect width="1680" height="1188" fill="url(#bg)"/>
<rect x="18" y="18" width="1644" height="1152" rx="18" fill="none" stroke="#b9cbd7" stroke-width="2"/>
<text x="48" y="64" class="title">K-EL/01 | Split-Yoke Elbow Actuator</text>
<text x="50" y="93" class="subtitle">Kritva Robotics KR-MECH-INT-001 | Concept artwork and assembly/load-path illustration | Not for manufacture</text>
<rect x="1285" y="37" width="332" height="45" rx="22" fill="#fff0df" stroke="#e6b07e" stroke-width="1.5"/>
<text x="1451" y="65" text-anchor="middle" style="font:700 16px Arial;fill:#984c0b">CONCEPT ONLY - DESIGN GATES OPEN</text>
<!-- Main panels -->
<rect x="38" y="120" width="760" height="765" class="panel"/>
<rect x="818" y="120" width="824" height="765" class="panel"/>
<text x="62" y="158" class="sect">A. Simplified robotic arm - isometric concept</text>
<text x="842" y="158" class="sect">B. Elbow actuator - exploded side concept</text>
<!-- left arm scene -->
<g id="arm">
 <!-- ground/base and upper arm -->
 <path d="M120 780 L190 745 L260 780 L190 817 Z" fill="#718493" stroke="#344b5a" stroke-width="2"/>
 <path d="M155 780 L155 710 L225 674 L225 744 Z" fill="#cad6de" stroke="#536c7c" stroke-width="2"/>
 <path d="M225 674 L254 688 L254 758 L225 744 Z" fill="#859aa8" stroke="#536c7c" stroke-width="2"/>
 <path d="M155 710 L225 674 L254 688 L184 724 Z" fill="#e1e9ee" stroke="#536c7c" stroke-width="2"/>
 <!-- upper arm reaches elbow -->
 <path d="M192 710 L232 630 L312 585 L271 665 Z" fill="#c3d1da" stroke="#536c7c" stroke-width="2.5"/>
 <path d="M232 630 L232 590 L312 546 L312 585 Z" fill="#e5edf2" stroke="#536c7c" stroke-width="2.5"/>
 <path d="M312 546 L351 562 L351 601 L312 585 Z" fill="#8398a6" stroke="#536c7c" stroke-width="2.5"/>
 <path d="M192 710 L271 665 L351 601 L312 585 L232 630 Z" fill="#d7e2e8" stroke="#536c7c" stroke-width="2" opacity="0.35"/>
 <!-- joint -->
 <ellipse cx="331" cy="579" rx="61" ry="51" fill="#9aaebb" stroke="#435b6a" stroke-width="3"/>
 <ellipse cx="331" cy="579" rx="44" ry="37" fill="url(#dark)" stroke="#203746" stroke-width="3"/>
 <ellipse cx="331" cy="579" rx="26" ry="22" fill="url(#teal)" stroke="#0e6375" stroke-width="3"/>
 <ellipse cx="331" cy="579" rx="10" ry="9" fill="#f4f8fb" stroke="#0e6375" stroke-width="2"/>
 <!-- forearm beam with 3D faces -->
 <path d="M365 555 L585 425 L630 442 L410 572 Z" fill="#d7e2e9" stroke="#536c7c" stroke-width="2.5"/>
 <path d="M410 572 L630 442 L630 480 L410 611 Z" fill="#8fa3b1" stroke="#536c7c" stroke-width="2.5"/>
 <path d="M365 555 L410 572 L410 611 L365 594 Z" fill="#526b7b" stroke="#394f5d" stroke-width="2"/>
 <!-- wrist and payload interface -->
 <path d="M585 425 L630 442 L671 418 L626 400 Z" fill="#e7eef3" stroke="#536c7c" stroke-width="2"/>
 <path d="M626 400 L671 418 L671 457 L626 439 Z" fill="#708795" stroke="#536c7c" stroke-width="2"/>
 <path d="M585 425 L626 400 L626 439 L585 464 Z" fill="#becdd7" stroke="#536c7c" stroke-width="2"/>
 <path d="M626 400 L671 418 L709 397 L664 379 Z" fill="#f3f7fa" stroke="#536c7c" stroke-width="2"/>
 <path d="M664 379 L709 397 L709 440 L664 422 Z" fill="#5f7687" stroke="#536c7c" stroke-width="2"/>
 <path d="M626 400 L664 379 L664 422 L626 439 Z" fill="#bdccd6" stroke="#536c7c" stroke-width="2"/>
 <!-- load/COM markers -->
 <circle cx="470" cy="520" r="11" fill="#d66a16" stroke="#fff" stroke-width="3"/>
 <circle cx="650" cy="454" r="11" fill="#d66a16" stroke="#fff" stroke-width="3"/>
 <path d="M470 532 L470 575" class="load"/><path d="M650 466 L650 509" class="load"/>
 <!-- torque arc around joint -->
 <path d="M278 529 A73 61 0 0 1 388 526" class="torque"/>
 <!-- labels -->
 <path d="M210 674 L118 638 L80 638" class="leader"/><text x="78" y="619" class="label">Upper-arm link</text><text x="78" y="638" class="small">300 mm illustrative</text>
 <path d="M458 490 L499 459 L544 459" class="leader"/><text x="493" y="438" class="label">Forearm/hand COM</text><text x="493" y="457" class="small">1.5 kg at 180 mm</text>
 <path d="M654 430 L684 344 L738 344" class="leader"/><text x="623" y="322" class="label">Payload COM</text><text x="623" y="341" class="small">1.0 kg at 350 mm</text>
 <path d="M495 562 L500 658 L603 658" class="leader"/><text x="510" y="681" class="label">Forearm link</text><text x="510" y="701" class="small">350 mm illustrative</text>
 <text x="272" y="648" class="label">Elbow joint</text>
 <!-- COM callouts above provide the required offsets without crowding the arm. -->
 <!-- load path text -->
 <rect x="66" y="823" width="704" height="39" rx="8" fill="#e7f5f7" stroke="#8bc5cc"/>
 <text x="82" y="848" style="font:700 15px Arial;fill:#135b6b">Load path: forearm -> spindle + bearings -> split-yoke -> upper arm</text>
</g>
<!-- right side exploded concept -->
<g id="exploded">
 <!-- horizontal axis and order -->
 <path d="M850 470 L1605 470" stroke="#8a9eaa" stroke-width="1.5" stroke-dasharray="8 8"/>
 <!-- encoder -->
 <rect x="861" y="420" width="52" height="100" rx="9" fill="url(#teal)" stroke="#315966" stroke-width="2"/>
 <circle cx="887" cy="470" r="15" fill="#eaf4f7" stroke="#315966" stroke-width="2"/>
 <!-- motor -->
 <rect x="928" y="388" width="132" height="164" rx="16" fill="url(#dark)" stroke="#273c4b" stroke-width="2.5"/>
 <ellipse cx="928" cy="470" rx="18" ry="82" fill="#536c7d" stroke="#273c4b" stroke-width="2"/>
 <ellipse cx="1060" cy="470" rx="18" ry="82" fill="#314958" stroke="#273c4b" stroke-width="2"/>
 <path d="M953 407 L1033 407 M953 533 L1033 533" stroke="#a7bbc7" stroke-width="3"/>
 <!-- reducer -->
 <rect x="1092" y="400" width="119" height="140" rx="12" fill="url(#metal)" stroke="#506573" stroke-width="2.5"/>
 <ellipse cx="1092" cy="470" rx="18" ry="70" fill="#dbe4ea" stroke="#506573" stroke-width="2.5"/>
 <ellipse cx="1211" cy="470" rx="18" ry="70" fill="#899eac" stroke="#506573" stroke-width="2.5"/>
 <circle cx="1213" cy="470" r="25" fill="#e5edf1" stroke="#506573" stroke-width="2"/>
 <!-- coupling spider and hub -->
 <rect x="1242" y="445" width="62" height="50" rx="11" fill="url(#teal)" stroke="#286b78" stroke-width="2.5"/>
 <rect x="1232" y="437" width="14" height="66" rx="4" fill="#7a8e9b" stroke="#435b6a" stroke-width="2"/>
 <rect x="1301" y="437" width="14" height="66" rx="4" fill="#7a8e9b" stroke="#435b6a" stroke-width="2"/>
 <!-- spindle -->
 <rect x="1317" y="458" width="256" height="24" rx="7" fill="url(#metal)" stroke="#506573" stroke-width="2"/>
 <path d="M1323 462 L1566 462" stroke="#f7fafc" stroke-width="3"/>
 <!-- two bearings -->
 <g transform="translate(1388 470)"><circle r="36" fill="#bccbd4" stroke="#435b6a" stroke-width="2.5"/><circle r="26" fill="#f6fafc" stroke="#738a99" stroke-width="2"/><circle r="16" fill="#879daa" stroke="#435b6a" stroke-width="2"/><circle r="8" fill="#f6fafc" stroke="#435b6a" stroke-width="1.5"/></g>
 <g transform="translate(1464 470)"><circle r="36" fill="#bccbd4" stroke="#435b6a" stroke-width="2.5"/><circle r="26" fill="#f6fafc" stroke="#738a99" stroke-width="2"/><circle r="16" fill="#879daa" stroke="#435b6a" stroke-width="2"/><circle r="8" fill="#f6fafc" stroke="#435b6a" stroke-width="1.5"/></g>
 <!-- yoke bracket top and bottom -->
 <path d="M1350 405 L1502 405 L1502 432 L1350 432 Z" fill="#4b6273" stroke="#293e4d" stroke-width="2"/>
 <path d="M1350 508 L1502 508 L1502 535 L1350 535 Z" fill="#4b6273" stroke="#293e4d" stroke-width="2"/>
 <path d="M1347 405 L1347 535 M1505 405 L1505 535" stroke="#4b6273" stroke-width="10"/>
 <!-- flange and output bracket -->
 <rect x="1583" y="421" width="20" height="98" rx="3" fill="url(#dark)" stroke="#293e4d" stroke-width="2"/>
 <rect x="1555" y="421" width="28" height="98" rx="4" fill="url(#teal)" stroke="#286b78" stroke-width="2.5"/>
 <circle cx="1568" cy="440" r="4" fill="#e8f5f7"/><circle cx="1568" cy="500" r="4" fill="#e8f5f7"/>
 <!-- exploded arrows -->
 <path d="M914 470 L923 470" class="path"/><path d="M1066 470 L1086 470" class="path"/><path d="M1219 470 L1228 470" class="path"/><path d="M1319 470 L1340 470" class="path"/><path d="M1514 470 L1548 470" class="path"/>
 <!-- component labels above -->
 <text x="887" y="335" text-anchor="middle" class="label">Encoder</text><text x="887" y="354" text-anchor="middle" class="small">motor-side</text><path d="M887 360 L887 415" class="leader"/>
 <text x="994" y="335" text-anchor="middle" class="label">BLDC motor</text><text x="994" y="354" text-anchor="middle" class="small">EC-i 52, 48 V</text><path d="M994 360 L994 385" class="leader"/>
 <text x="1138" y="335" text-anchor="middle" class="label">Planetary gearhead</text><text x="1138" y="354" text-anchor="middle" class="small">GP 52 C, 91:1</text><path d="M1138 360 L1138 397" class="leader"/>
 <text x="1283" y="335" text-anchor="middle" class="label">Flexible coupling</text><text x="1283" y="354" text-anchor="middle" class="small">ROTEX GS 19, 98 ShA</text><path d="M1283 360 L1283 436" class="leader"/>
 <text x="1434" y="335" text-anchor="middle" class="label">Independent spindle</text><text x="1434" y="354" text-anchor="middle" class="small">12 mm concept shaft</text><path d="M1434 360 L1434 427" class="leader"/>
 <text x="1568" y="335" text-anchor="middle" class="label">Output flange</text><text x="1568" y="354" text-anchor="middle" class="small">+ root mount plate</text><path d="M1568 360 L1568 419" class="leader"/>
 <!-- lower labels -->
 <text x="1450" y="584" text-anchor="middle" class="label">2 x SKF 6201-2RSH</text><text x="1450" y="605" text-anchor="middle" class="small">12 x 32 x 10 mm envelope</text>
 <path d="M1450 566 L1450 534" class="leader"/>
 <text x="1450" y="647" text-anchor="middle" class="label">Split-yoke carrier</text><text x="1450" y="667" text-anchor="middle" class="small">90 x 90 x 82 mm envelope</text>
 <path d="M1450 637 L1450 535" class="leader"/>
 <text x="1198" y="584" text-anchor="middle" class="label">Torque path</text><text x="1198" y="605" text-anchor="middle" class="small">motor -> reducer -> coupling -> spindle</text>
 <text x="1198" y="647" text-anchor="middle" class="label">Radial-load path</text><text x="1198" y="667" text-anchor="middle" class="small">forearm -> spindle -> bearings -> yoke</text>
 <!-- axial dimensions -->
 <path d="M1388 706 L1464 706" class="dim"/><path d="M1388 681 L1388 716 M1464 681 L1464 716" class="leader"/><text x="1426" y="733" text-anchor="middle" class="dimtxt">50 mm bearing centres</text>
 <path d="M1464 761 L1555 761" class="dim"/><path d="M1464 736 L1464 773 M1555 519 L1555 773" class="leader"/><text x="1510" y="788" text-anchor="middle" class="dimtxt">50 mm load-plane overhang*</text>
 <text x="844" y="838" class="small">*From rear bearing centre (Y=61 mm) to forearm link center plane (Y=111 mm) in this envelope model.</text>
</g>
<!-- bottom calculation and decision strip -->
<rect x="38" y="904" width="1604" height="235" rx="18" fill="#fff" stroke="#ccd9e2" stroke-width="2"/>
<text x="62" y="944" class="sect">C. Design-point calculations and explicit trade-off</text>
<g>
 <rect x="62" y="966" width="260" height="111" rx="12" fill="#eff7fa" stroke="#c5dfe7"/><text x="82" y="994" class="small">Static gravity torque</text><text x="82" y="1036" class="num">6.082 N m</text><text x="82" y="1060" class="micro">1.0 kg x 350 mm + 1.5 kg x 180 mm</text>
 <rect x="338" y="966" width="260" height="111" rx="12" fill="#eff7fa" stroke="#c5dfe7"/><text x="358" y="994" class="small">Preliminary output target</text><text x="358" y="1036" class="num">12.164 N m</text><text x="358" y="1060" class="micro">2.0 x static; assumed margin only</text>
 <rect x="614" y="966" width="260" height="111" rx="12" fill="#eff7fa" stroke="#c5dfe7"/><text x="634" y="994" class="small">Speed and reduction</text><text x="634" y="1036" class="num">45 rpm / 91:1</text><text x="634" y="1060" class="micro">Motor speed screen = 4,095 rpm</text>
 <rect x="890" y="966" width="335" height="111" rx="12" fill="#fff6ec" stroke="#e9c7a6"/><text x="910" y="994" class="small">Backlash trade-off</text><text x="910" y="1036" style="font:700 25px Arial;fill:#a45313">1 degree average</text><text x="910" y="1060" class="micro">At 350 mm radius: about 6.1 mm endpoint arc</text>
 <rect x="1241" y="966" width="372" height="111" rx="12" fill="#f4f7f9" stroke="#d3dfe6"/><text x="1261" y="994" class="small">Mechanical concept assumptions</text><text x="1261" y="1020" class="label">12 mm spindle | 50 mm bearing spacing</text><text x="1261" y="1044" class="label">50 mm axial overhang | key 4 x 4 x 20</text><text x="1261" y="1065" class="micro">All are envelope values; detail design remains open.</text>
</g>
<text x="62" y="1110" class="small">Key unresolved gates: confirmed maxon motor/gearhead/encoder configuration and loaded efficiency; dynamic duty and thermal performance; coupling hub fit/service factor; shaft fatigue/deflection and bearing life; accuracy and safe power-loss behavior.</text>
<text x="62" y="1131" class="micro">Source requirements: Kritva Robotics KR-MECH-INT-001. Component values are preliminary catalogue references. The 2x torque target is not a certified safety factor. No purchase, manufacture, safety certification, FEA, or physical test is claimed.</text>
</svg>'''
p=O/'K_EL01_Concept_Drawing.svg'; p.write_text(svg,encoding='utf-8')
cairosvg.svg2pdf(bytestring=svg.encode(),write_to=str(O/'K_EL01_Concept_Drawing.pdf'))
cairosvg.svg2png(bytestring=svg.encode(),write_to=str(O/'K_EL01_Concept_Drawing.png'),output_width=2800,output_height=1980)
print('created artwork SVG/PDF/PNG')
