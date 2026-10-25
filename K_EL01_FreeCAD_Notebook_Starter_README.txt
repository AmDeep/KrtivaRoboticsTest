K-EL/01 FreeCAD Notebook Starter

Contents
- K_EL01_Run_and_View_FreeCAD_Macro.ipynb: inspect the macro source, view a rotatable STEP preview, detect a local FreeCAD installation and run a temporary copy of the macro.
- K_EL01_Split_Yoke_Concept.FCMacro: source macro. It has been aligned to the STEP builder's COM-marker coordinates; original macro is not altered by the notebook when it runs.
- K_EL01_Split_Yoke_Concept.step: neutral CAD envelope model for notebook preview or import into FreeCAD.
- Build_K_EL01_STEP.py: CadQuery source used to build the neutral STEP concept.

Requirements and limits
1. The interactive STEP preview uses CadQuery and Plotly. Install into your local Jupyter environment with: python -m pip install cadquery plotly
2. Actual .FCMacro execution requires a local desktop FreeCAD installation on the same computer as local Jupyter/JupyterLab. Set FREECAD_EXECUTABLE in the notebook cell if auto-detection misses it.
3. Hosted Colab can preview after the input files and dependencies are available, but generally cannot open the local desktop FreeCAD GUI; run the macro locally.
4. The macro can generate a native .FCStd model in the local environment. Inspect the object tree and geometry before saving/using it. This is conceptual envelope CAD, not manufacturing-ready geometry.
5. The STEP model has passed a geometry-validity check. That does not prove interference-free assembly, real bearing retention, fits, load capacity, thermal performance or safety.
