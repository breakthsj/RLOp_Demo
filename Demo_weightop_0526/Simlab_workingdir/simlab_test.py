#***************************************************************
#SimLab Version 2021 
#Created at Tue Jun  1 00:05:49 2021
#***************************************************************
#For debugging this python script,Please comment(#) out the line "from hwx import simlab" and uncomment the line "import simlab"
from hwx import simlab
#import simlab


UnitSystem=''' <UnitSystem UUID="3aca8564-4d38-4b0b-887c-6a542d4001c6">
  <SetCurrentDisplaySystem Name="MMKS (mm kg N s)"/>
 </UnitSystem>''';
simlab.execute(UnitSystem);

simlab.newDocument();

UnitSystem=''' <UnitSystem UUID="3aca8564-4d38-4b0b-887c-6a542d4001c6">
  <SetCurrentDisplaySystem Name="MMKS (mm kg N s)"/>
 </UnitSystem>''';
simlab.execute(UnitSystem);

STEP_Import=''' <STEP_Import UUID="e88f2fcc-2430-4e47-9455-78b4dea9b064" CheckBox="ON" gda="" Type="STEP">
  <FileName Value="./../Box.stp" HelpStr="File name to be imported." widget="LineEdit"/>
  <Method Value="SimLab Reader"/>
  <BodyName Value="1"/>
  <ReadPartName Value="0"/>
  <SketchWireframe Value="1"/>
  <Groups Value="1"/>
  <Imprint Value="0"/>
  <Facets Value="1"/>
  <AssemblyStructure Value="1"/>
  <SaveGeometryInDatabase Value="0"/>
 </STEP_Import>''';
simlab.execute(STEP_Import);

AutoHexMesh=''' <AutoHexMesh UUID="f4ce8a5e-4df8-42de-ab98-547a83e9d7c2">
  <InputBodies>
   <Entities>
    <Model>Box.gda</Model>
    <Body></Body>
   </Entities>
  </InputBodies>
  <AverageElementSize Value="5 mm"/>
  <MinimumElementSize Value="2 mm"/>
  <AllowQuadMeshTransition Checked="1"/>
  <CreateMeshInNewModel Checked="0"/>
 </AutoHexMesh>''';
simlab.execute(AutoHexMesh);

CreateSolution=''' <CreateSolution UUID="1210abd7-c815-4f67-8615-6ab616274dcc">
  <tag Value="-1"/>
  <Name Value="Solution"/>
  <SolutionType Value="LINEAR"/>
  <Solver Value="OPTISTRUCT"/>
  <SupportEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body></Body>
   </Entities>
  </SupportEntities>
  <CreateAndSetActiveLC Value="0"/>
  <AutoContact Value="1"/>
  <FluxMagnetoStaticsParameters>
   <Domain Value=""/>
   <DomainDepth Value=""/>
  </FluxMagnetoStaticsParameters>
  <FluxTransientMagneticsParameters>
   <Domain Value=""/>
   <DomainDepth Value=""/>
   <TransientMagneticControlParameter Value=""/>
   <FinalTimeOrAngle Value=""/>
   <TimeOrAngleIncrement Value=""/>
   <ComputeInfinteRegion value="1"/>
  </FluxTransientMagneticsParameters>
 </CreateSolution>''';
simlab.execute(CreateSolution);

BodyMergeRightClick=''' <BodyMergeRightClick UUID="7d2fbe6f-4dd7-4848-8cb5-f8be2d72c418" CheckBox="ON">
  <tag Value="-1"/>
  <ModelId Value=""/>
  <BodyId>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_3","SLBody_4","SLBody_5","SLBody_6","SLBody_7","SLBody_8","SLBody_9","SLBody_10","SLBody_11","SLBody_12","SLBody_13","SLBody_14","SLBody_15","SLBody_16","SLBody_17","SLBody_18","SLBody_19","SLBody_20","SLBody_21","SLBody_22","SLBody_23","SLBody_24","SLBody_25","SLBody_26","SLBody_27","SLBody_28","SLBody_29","SLBody_30","SLBody_31","SLBody_32","SLBody_33","SLBody_34","SLBody_35","SLBody_36","SLBody_37","SLBody_38","SLBody_39","SLBody_40","SLBody_41","SLBody_42","SLBody_43","SLBody_44","SLBody_45","SLBody_46","SLBody_47","SLBody_48","SLBody_49","SLBody_50","SLBody_51","SLBody_52","SLBody_53","SLBody_54","SLBody_55","SLBody_56","SLBody_57","SLBody_58","SLBody_59","SLBody_60","SLBody_61","SLBody_62","SLBody_63","SLBody_64","SLBody_65","SLBody_66",</Body>
   </Entities>
  </BodyId>
  <RedoFlag Value=""/>
  <Output/>
 </BodyMergeRightClick>''';
simlab.execute(BodyMergeRightClick);

AssignMaterial=''' <AssignMaterial UUID="22fe2ea3-c38e-4992-b9b4-80dbf7b733ac">
  <Material Name="Steel"/>
  <SupportEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_1","SLBody_2",</Body>
   </Entities>
  </SupportEntities>
 </AssignMaterial>''';
simlab.execute(AssignMaterial);

DropTestParameters=''' <DropTestParameters UUID="467f776e-febc-4c63-8fde-b4a01fbb61c9">
  <InputBodies>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_3",</Body>
   </Entities>
  </InputBodies>
  <MeshType Value=""/>
  <MeshSize Value=""/>
  <MinimumElementSize Value=""/>
  <Material Name="Aluminium"/>
  <QualitySpec Name=""/>
 </DropTestParameters>''';
simlab.execute(DropTestParameters);

ForceandMoment=''' <Force UUID="af4acb9c-542e-47aa-9ddc-ca6001e13175" BCType="Force">
  <tag Value="-1"/>
  <Name Value="Force_178"/>
  <ForceEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Face>10,</Face>
   </Entities>
  </ForceEntities>
  <Distribute Value="Shape function"/>
  <CoordinateAxisID Value="Global" Index="0"/>
  <AmpFieldData Value="None" Index="0"/>
  <ForceFieldData Value="None" Index="0"/>
  <Force-Fx Value="0 N"/>
  <Force-Fy Value="0 N"/>
  <Force-Fz Value="1000 N"/>
  <Moment-Mx Value="0 N*mm"/>
  <Moment-My Value="0 N*mm"/>
  <Moment-Mz Value="0 N*mm"/>
 </Force>''';
simlab.execute(ForceandMoment);

FixedConstraint=''' <Fixed UUID="f5ecfc0a-a238-477c-928c-e81c22353a69" BCType="Constraint" isObject="2">
  <tag Value="-1"/>
  <Name Value="Face_Constraint_179"/>
  <FixedEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Face>58,</Face>
   </Entities>
  </FixedEntities>
  <CoordinateAxisID Value="Global" Index="0"/>
  <UseParameter Value="0"/>
  <Parameter Value="111000"/>
  <Tx Value="1"/>
  <Ty Value="1"/>
  <Tz Value="1"/>
  <Rx Value="0"/>
  <Ry Value="0"/>
  <Rz Value="0"/>
 </Fixed>''';
simlab.execute(FixedConstraint);

ExportOptions=''' <ExportOptions UUID="7a690756-a1f3-4e05-ba73-0bde6a497bd5" pixmap="solution">
  <tag Value="-1"/>
  <Name Value=""/>
  <SolverName Value="OPTISTRUCT"/>
  <FileName Value=""/>
  <Version Value="14"/>
  <SolverSetingType Value=""/>
  <Solution Value="Solution"/>
  <AnalysisType Value="LINEAR" Index="0">
   <Version Value="14"/>
   <SolverName Value="OPTISTRUCT"/>
   <AnalysisType Value="LINEAR">
    <ITEM NAME="Title" DATATYPE="STRING" VALUE="Linear Static Step" TYPE="EDITBOX"/>
    <ITEM NAME="Format" DATATYPE="INT" VALUE="1" TYPE="COMBOBOX"/>
    <ITEM NAME="Numbering" DATATYPE="INT" VALUE="0" TYPE="COMBOBOX"/>
    <ITEM NAME="Write Linear Elements" DATATYPE="BOOL" VALUE="0" TYPE="CHECKBOX"/>
    <ITEM NAME="Spring Element Card Format" DATATYPE="INT" VALUE="0" TYPE="COMBOBOX"/>
    <ITEM NAME="Write Contact Slave Surface as SURF" DATATYPE="BOOL" VALUE="0" TYPE="CHECKBOX"/>
    <ITEM NAME="Write Enforced Displacements as SPCD" DATATYPE="BOOL" VALUE="1" TYPE="CHECKBOX"/>
    <ITEM NAME="Global initial temperature" STATUS="OFF" DATATYPE="DOUBLE" VALUE="20" TYPE="CHECKEDITBOX"/>
    <ITEM NAME="Initial memory allocation (MB)" STATUS="OFF" DATATYPE="DOUBLE" VALUE="100" TYPE="CHECKEDITBOX"/>
    <ITEM NAME="PBUSHFORM" DATATYPE="INT" VALUE="0" TYPE="COMBOBOX"/>
    <ITEM NAME="Write Material" DATATYPE="DOUBLE" VALUE="1" TYPE="CHECKBOX"/>
    <ITEM NAME="External File" DATATYPE="USER" VALUE="" TYPE="EDITBOXWITHBROWSER"/>
    <ITEM NAME="Number of Processors" DATATYPE="INT" VALUE="24" TYPE="EDITBOX"/>
    <ITEM NAME="RAM Allocation" DATATYPE="INT" VALUE="0" TYPE="EDITBOX"/>
    <ITEM NAME="Additional_Arguments" DATATYPE="STRING" VALUE="" TYPE="EDITBOX"/>
   </AnalysisType>
  </AnalysisType>
 </ExportOptions>''';
simlab.execute(ExportOptions);

CreateResponseNew=''' <CreateResponseNew UUID="a7326802-d869-41d4-a46d-d4d5c159d938">
  <tag Value="-1"/>
  <Name Value="Stress"/>
  <Response Component="Von Mises" ModeIndex="" LoadCase="" Type="Stress"/>
  <AllBodies Value="1"/>
  <SupportEntities/>
  <Sets Value=""/>
  <Interested_Regions/>
  <Ignore_Regions/>
  <ValueType Value="Maximum"/>
  <SolutionName Value="Solution"/>
 </CreateResponseNew>''';
simlab.execute(CreateResponseNew);

ExportandSolve=''' <ExportStaticSolverInput UUID="f009bc99-991f-43b7-8c87-cc606ef9c443" pixmap="solution">
  <tag Value="-1"/>
  <Name Value=""/>
  <SolverName Value=""/>
  <FileName Value=""/>
  <Solution Value="Solution"/>
  <WriteMode Value="0" ValueText="Default"/>
  <LoadCase Value=""/>
  <Renumber Value="0"/>
  <RunSolver Value="1"/>
  <DataCheck Value="0"/>
  <RemoveOrphanNodes Value="1"/>
  <AnalysisType Value="" Index=""/>
  <Version Value="14"/>
  <ExportOptionsVersion Value="1"/>
  <RemoteSolve Value="0"/>
  <CopyIncludeFiles Value="1"/>
  <SupportEntities Value="" ModelIds="" EntityTypes=""/>
  <UnitSystem Value="MKS (m kg N s)"/>
 </ExportStaticSolverInput>''';
simlab.execute(ExportandSolve);

ExportResponses=''' <ExportResponses UUID="eb262d06-c529-4545-9596-c109bc7067e0">
  <FileName Value="./../demo_simlabstress.csv"/>
  <SolutionName Value="Solution"/>
 </ExportResponses>''';
simlab.execute(ExportResponses);

ExportMassProperties=''' <ExportMassProperties UUID="0fd1f4ae-0e76-4125-a915-ef18f37b0e08">
  <tag Value="-1"/>
  <SupportEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_3",</Body>
   </Entities>
  </SupportEntities>
  <FileName Value="./../demo_simlabweight.csv"/>
  <CoordID Value="Global"/>
  <Mass Value=""/>
 </ExportMassProperties>''';
simlab.execute(ExportMassProperties);

ExportSlb=''' <ExportSlb UUID="a155cd6e-8ae6-4720-8ab4-1f50d4a34d1c">
  <tag Value="-1"/>
  <Name Value=""/>
  <Option Value="0"/>
  <Duplicate Value="0"/>
  <FileName Value="./../Demo_Simlab_result.slb"/>
 </ExportSlb>''';
simlab.execute(ExportSlb);

simlab.closeActiveDocument();
