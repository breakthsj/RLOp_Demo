#***************************************************************
#SimLab Version 2021 
#Created at Mon Jun  7 18:00:02 2021
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

STEP_Import=''' <STEP_Import Type="STEP" UUID="e88f2fcc-2430-4e47-9455-78b4dea9b064" gda="" CheckBox="ON">
  <FileName widget="LineEdit" HelpStr="File name to be imported." Value="./../Box.stp"/>
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
  <AverageElementSize Value="1 mm"/>
  <MinimumElementSize Value="0.1 mm"/>
  <AllowQuadMeshTransition Checked="1"/>
  <CreateMeshInNewModel Checked="0"/>
 </AutoHexMesh>''';
simlab.execute(AutoHexMesh);

BodyMergeRightClick=''' <BodyMergeRightClick UUID="7d2fbe6f-4dd7-4848-8cb5-f8be2d72c418" CheckBox="ON">
  <tag Value="-1"/>
  <ModelId Value=""/>
  <BodyId>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_3","SLBody_4","SLBody_5","SLBody_6","SLBody_7","SLBody_8","SLBody_9","SLBody_10","SLBody_11","SLBody_12","SLBody_13","SLBody_14","SLBody_15","SLBody_16","SLBody_17","SLBody_18","SLBody_19","SLBody_20","SLBody_21","SLBody_22","SLBody_23","SLBody_24","SLBody_25","SLBody_26","SLBody_27","SLBody_28","SLBody_29","SLBody_30","SLBody_31","SLBody_32","SLBody_33","SLBody_34","SLBody_35","SLBody_36","SLBody_37","SLBody_38","SLBody_39","SLBody_40","SLBody_41","SLBody_42","SLBody_43","SLBody_44","SLBody_45","SLBody_46","SLBody_47","SLBody_48","SLBody_49","SLBody_50","SLBody_51","SLBody_52","SLBody_53","SLBody_54","SLBody_55","SLBody_56","SLBody_57","SLBody_58","SLBody_59","SLBody_60","SLBody_61","SLBody_62","SLBody_63","SLBody_64","SLBody_65","SLBody_66","SLBody_67","SLBody_68","SLBody_69","SLBody_70","SLBody_71","SLBody_72","SLBody_73","SLBody_74","SLBody_75","SLBody_76","SLBody_77","SLBody_78","SLBody_79","SLBody_80","SLBody_81","SLBody_82","SLBody_83"</Body>
   </Entities>
  </BodyId>
  <RedoFlag Value=""/>
  <Output/>
 </BodyMergeRightClick>''';
simlab.execute(BodyMergeRightClick);

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
  <AutoContact Value="0"/>
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

ExportOptions=''' <ExportOptions UUID="7a690756-a1f3-4e05-ba73-0bde6a497bd5" pixmap="solution">
  <tag Value="-1"/>
  <Name Value=""/>
  <SolverName Value="OPTISTRUCT"/>
  <FileName Value=""/>
  <Version Value="14"/>
  <SolverSetingType Value=""/>
  <Solution Value="Solution"/>
  <AnalysisType Index="0" Value="LINEAR">
   <Version Value="14"/>
   <SolverName Value="OPTISTRUCT"/>
   <AnalysisType Value="LINEAR">
    <ITEM NAME="Title" DATATYPE="STRING" TYPE="EDITBOX" VALUE="Linear Static Step"/>
    <ITEM NAME="Format" DATATYPE="INT" TYPE="COMBOBOX" VALUE="1"/>
    <ITEM NAME="Numbering" DATATYPE="INT" TYPE="COMBOBOX" VALUE="0"/>
    <ITEM NAME="Write Linear Elements" DATATYPE="BOOL" TYPE="CHECKBOX" VALUE="0"/>
    <ITEM NAME="Spring Element Card Format" DATATYPE="INT" TYPE="COMBOBOX" VALUE="0"/>
    <ITEM NAME="Write Contact Slave Surface as SURF" DATATYPE="BOOL" TYPE="CHECKBOX" VALUE="0"/>
    <ITEM NAME="Write Enforced Displacements as SPCD" DATATYPE="BOOL" TYPE="CHECKBOX" VALUE="1"/>
    <ITEM NAME="Global initial temperature" DATATYPE="DOUBLE" TYPE="CHECKEDITBOX" VALUE="20" STATUS="OFF"/>
    <ITEM NAME="Initial memory allocation (MB)" DATATYPE="DOUBLE" TYPE="CHECKEDITBOX" VALUE="100" STATUS="OFF"/>
    <ITEM NAME="PBUSHFORM" DATATYPE="INT" TYPE="COMBOBOX" VALUE="0"/>
    <ITEM NAME="Write Material" DATATYPE="DOUBLE" TYPE="CHECKBOX" VALUE="1"/>
    <ITEM NAME="External File" DATATYPE="USER" TYPE="EDITBOXWITHBROWSER" VALUE=""/>
    <ITEM NAME="Number of Processors" DATATYPE="INT" TYPE="EDITBOX" VALUE="24"/>
    <ITEM NAME="RAM Allocation" DATATYPE="INT" TYPE="EDITBOX" VALUE="0"/>
    <ITEM NAME="Additional_Arguments" DATATYPE="STRING" TYPE="EDITBOX" VALUE=""/>
   </AnalysisType>
  </AnalysisType>
 </ExportOptions>''';
simlab.execute(ExportOptions);

AssignMaterial=''' <AssignMaterial UUID="22fe2ea3-c38e-4992-b9b4-80dbf7b733ac">
  <Material Name="Steel"/>
  <SupportEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_2","SLBody_1",</Body>
   </Entities>
  </SupportEntities>
 </AssignMaterial>''';
simlab.execute(AssignMaterial);

AssignMaterial=''' <AssignMaterial UUID="22fe2ea3-c38e-4992-b9b4-80dbf7b733ac">
  <Material Name="Aluminium"/>
  <SupportEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_3",</Body>
   </Entities>
  </SupportEntities>
 </AssignMaterial>''';
simlab.execute(AssignMaterial);

DefineContact=''' <Contact customselection="1" UUID="3b4a24b5-6aea-49d3-b74a-82bf5b3ec193" pixmap="sizemeshcontrol" BCType="Contact" isObject="2" CheckBox="ON">
  <tag Value="-1"/>
  <Name Value="SLBody_2_SLBody_3"/>
  <New Value="1"/>
  <Entity Index="0" Value="Body"/>
  <MasterEntity>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_2",</Body>
   </Entities>
  </MasterEntity>
  <SlaveEntity>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_3",</Body>
   </Entities>
  </SlaveEntity>
  <IgnoreEdges EntityTypes="" ModelIds="" Value=""/>
  <MasterSet Value=""/>
  <SlaveSet Value=""/>
  <ContactBodyPairList/>
  <Trim Value="None"/>
  <SurfaceInteraction Index="0" Value="None"/>
  <PressFit Index="0" Value="None"/>
  <ContactFaceType Value="All"/>
  <Tolerance Value="0.1 mm"/>
  <UserContactName value="" Value="0"/>
  <SolverStackIndex Value="OptiStruct"/>
  <Export Value="0"/>
  <FileName Value=""/>
  <AutoContact Value="0"/>
  <RadiossContact>
   <RadiossContactType Index="4" Value="TIE"/>
   <ShellOrientation Index="0" Value="OPENGAP"/>
   <RadiossSurfaceToSurface Value="1"/>
   <Tolerance Check="1" Value="0 mm"/>
   <Adjust Index="1" Value="AUTO"/>
   <SlaveSurfaceCornerTreatmentBreakAngle Index="0" Value="NO"/>
   <PadThickness Value="THICK"/>
   <GapStiffness Value="AUTO"/>
   <FrictionCoefficient Value="0.0"/>
   <RadiossSlidingType Index="0" Value="Small Sliding"/>
   <FrictionElasticSlip Value=""/>
   <Conductance Value="Default"/>
   <Separation Value=""/>
   <bClearance Value="0"/>
   <Clearance Value="0 mm"/>
   <OverClosure Value="None"/>
   <ExpOverClosureZeroPressure Value="AUTO"/>
   <ExpPressure Value="AUTO"/>
   <QuadOverClosureZeroPressure Value="0.0"/>
   <UpperQuadLimit Value="AUTO"/>
   <LowerQuadLimit Value="AUTO"/>
   <StiffnessRatio Value="AUTO"/>
   <bGapConductanceTable Value=""/>
   <GapConductanceTable Value=""/>
   <TiedSlaveNodeSet Value=""/>
   <FrictionCoefficientTable Value=""/>
   <NonLinearParameters>
    <ExplicitContactType Value=""/>
    <StiffnessFactor Value=""/>
    <CoulombFrictionCoefficient Value=""/>
    <ImpactActivationGap Value=""/>
    <ContactDeletionFlag Value=""/>
    <HandleInitialPenetration Value=""/>
    <ContactType Value=""/>
    <StartTime Value=""/>
    <EndTime Value=""/>
   </NonLinearParameters>
   <ExplicitParameters>
    <SymmetricContactFlag Value=""/>
    <EdgeGenerationFlag Value=""/>
    <FeatureAngle Value=""/>
    <GapDefinition Value=""/>
    <ContactStiffnessDefinition Value=""/>
    <UserDefinedStiffness Value=""/>
    <MinimumStiffness Value=""/>
    <MaximumStiffness Value=""/>
    <StiffnessDamping Value=""/>
    <FrictionDamping Value=""/>
    <SortingFactor Value=""/>
    <DeactivationFlag Value=""/>
    <MaximumAvgNo Value=""/>
    <FrictionFormulation Value=""/>
    <FrictionPenalty Value=""/>
    <FrictionFilter Value=""/>
    <FrictionFilteringFactor Value=""/>
    <FrictionCoefficients c5="" c6="" c1="" c4="" c2="" c3=""/>
   </ExplicitParameters>
   <Type24Parameters>
    <StiffnessFactor Value=""/>
    <CoulombFrictionCoefficient Value=""/>
    <MaxSlaveGap Value=""/>
    <MaxMasterGap Value=""/>
    <HandleInitialPenetration Value=""/>
    <GapModification Value=""/>
    <InitialPenetrationDetection Value=""/>
    <MaxInitialPenetration Value=""/>
    <MinInitialPenetration Value=""/>
    <StartTime Value=""/>
    <EndTime Value=""/>
   </Type24Parameters>
  </RadiossContact>
 </Contact>''';
simlab.execute(DefineContact);

DefineContact=''' <Contact customselection="1" UUID="3b4a24b5-6aea-49d3-b74a-82bf5b3ec193" pixmap="sizemeshcontrol" BCType="Contact" isObject="2" CheckBox="ON">
  <tag Value="-1"/>
  <Name Value="SLBody_1_SLBody_3"/>
  <New Value="1"/>
  <Entity Index="0" Value="Body"/>
  <MasterEntity>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_1",</Body>
   </Entities>
  </MasterEntity>
  <SlaveEntity>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_3",</Body>
   </Entities>
  </SlaveEntity>
  <IgnoreEdges EntityTypes="" ModelIds="" Value=""/>
  <MasterSet Value=""/>
  <SlaveSet Value=""/>
  <ContactBodyPairList/>
  <Trim Value="None"/>
  <SurfaceInteraction Index="0" Value="None"/>
  <PressFit Index="0" Value="None"/>
  <ContactFaceType Value="All"/>
  <Tolerance Value="0.1 mm"/>
  <UserContactName value="" Value="0"/>
  <SolverStackIndex Value="OptiStruct"/>
  <Export Value="0"/>
  <FileName Value=""/>
  <AutoContact Value="0"/>
  <RadiossContact>
   <RadiossContactType Index="4" Value="TIE"/>
   <ShellOrientation Index="0" Value="OPENGAP"/>
   <RadiossSurfaceToSurface Value="1"/>
   <Tolerance Check="1" Value="0 mm"/>
   <Adjust Index="1" Value="AUTO"/>
   <SlaveSurfaceCornerTreatmentBreakAngle Index="0" Value="NO"/>
   <PadThickness Value="THICK"/>
   <GapStiffness Value="AUTO"/>
   <FrictionCoefficient Value="0.0"/>
   <RadiossSlidingType Index="0" Value="Small Sliding"/>
   <FrictionElasticSlip Value=""/>
   <Conductance Value="Default"/>
   <Separation Value=""/>
   <bClearance Value="0"/>
   <Clearance Value="0 mm"/>
   <OverClosure Value="None"/>
   <ExpOverClosureZeroPressure Value="AUTO"/>
   <ExpPressure Value="AUTO"/>
   <QuadOverClosureZeroPressure Value="0.0"/>
   <UpperQuadLimit Value="AUTO"/>
   <LowerQuadLimit Value="AUTO"/>
   <StiffnessRatio Value="AUTO"/>
   <bGapConductanceTable Value=""/>
   <GapConductanceTable Value=""/>
   <TiedSlaveNodeSet Value=""/>
   <FrictionCoefficientTable Value=""/>
   <NonLinearParameters>
    <ExplicitContactType Value=""/>
    <StiffnessFactor Value=""/>
    <CoulombFrictionCoefficient Value=""/>
    <ImpactActivationGap Value=""/>
    <ContactDeletionFlag Value=""/>
    <HandleInitialPenetration Value=""/>
    <ContactType Value=""/>
    <StartTime Value=""/>
    <EndTime Value=""/>
   </NonLinearParameters>
   <ExplicitParameters>
    <SymmetricContactFlag Value=""/>
    <EdgeGenerationFlag Value=""/>
    <FeatureAngle Value=""/>
    <GapDefinition Value=""/>
    <ContactStiffnessDefinition Value=""/>
    <UserDefinedStiffness Value=""/>
    <MinimumStiffness Value=""/>
    <MaximumStiffness Value=""/>
    <StiffnessDamping Value=""/>
    <FrictionDamping Value=""/>
    <SortingFactor Value=""/>
    <DeactivationFlag Value=""/>
    <MaximumAvgNo Value=""/>
    <FrictionFormulation Value=""/>
    <FrictionPenalty Value=""/>
    <FrictionFilter Value=""/>
    <FrictionFilteringFactor Value=""/>
    <FrictionCoefficients c5="" c6="" c1="" c4="" c2="" c3=""/>
   </ExplicitParameters>
   <Type24Parameters>
    <StiffnessFactor Value=""/>
    <CoulombFrictionCoefficient Value=""/>
    <MaxSlaveGap Value=""/>
    <MaxMasterGap Value=""/>
    <HandleInitialPenetration Value=""/>
    <GapModification Value=""/>
    <InitialPenetrationDetection Value=""/>
    <MaxInitialPenetration Value=""/>
    <MinInitialPenetration Value=""/>
    <StartTime Value=""/>
    <EndTime Value=""/>
   </Type24Parameters>
  </RadiossContact>
 </Contact>''';
simlab.execute(DefineContact);

ForceandMoment=''' <Force BCType="Force" UUID="af4acb9c-542e-47aa-9ddc-ca6001e13175">
  <tag Value="-1"/>
  <Name Value="Force_34"/>
  <ForceEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Face>58,</Face>
   </Entities>
  </ForceEntities>
  <Distribute Value="Shape function"/>
  <CoordinateAxisID Index="0" Value="Global"/>
  <AmpFieldData Index="0" Value="None"/>
  <ForceFieldData Index="0" Value="None"/>
  <Force-Fx Value="0 N"/>
  <Force-Fy Value="0 N"/>
  <Force-Fz Value="-10000 N"/>
  <Moment-Mx Value="0 N*mm"/>
  <Moment-My Value="0 N*mm"/>
  <Moment-Mz Value="0 N*mm"/>
 </Force>''';
simlab.execute(ForceandMoment);

FixedConstraint=''' <Fixed isObject="2" BCType="Constraint" UUID="f5ecfc0a-a238-477c-928c-e81c22353a69">
  <tag Value="-1"/>
  <Name Value="Face_Constraint_35"/>
  <FixedEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Face>10,</Face>
   </Entities>
  </FixedEntities>
  <CoordinateAxisID Index="0" Value="Global"/>
  <UseParameter Value="0"/>
  <Parameter Value="111000"/>
  <Tx Value="1"/>
  <Ty Value="1"/>
  <Tz Value="1"/>
  <Rx Value="1"/>
  <Ry Value="1"/>
  <Rz Value="1"/>
 </Fixed>''';
simlab.execute(FixedConstraint);

CreateResponseNew=''' <CreateResponseNew UUID="a7326802-d869-41d4-a46d-d4d5c159d938">
  <tag Value="-1"/>
  <Name Value="Stress"/>
  <Response Type="Stress" ModeIndex="" Component="Von Mises" LoadCase=""/>
  <AllBodies Value="0"/>
  <SupportEntities>
   <Entities>
    <Model>Box1_VM.gda</Model>
    <Body>"SLBody_3",</Body>
   </Entities>
  </SupportEntities>
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
  <WriteMode ValueText="Default" Value="0"/>
  <LoadCase Value=""/>
  <Renumber Value="0"/>
  <RunSolver Value="1"/>
  <DataCheck Value="0"/>
  <RemoveOrphanNodes Value="1"/>
  <AnalysisType Index="" Value=""/>
  <Version Value="14"/>
  <ExportOptionsVersion Value="1"/>
  <RemoteSolve Value="0"/>
  <CopyIncludeFiles Value="1"/>
  <SupportEntities EntityTypes="" ModelIds="" Value=""/>
  <UnitSystem Value="MKS (m kg N s)"/>
 </ExportStaticSolverInput>''';
simlab.execute(ExportandSolve);

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

ExportResponses=''' <ExportResponses UUID="eb262d06-c529-4545-9596-c109bc7067e0">
  <FileName Value="./../demo_simlabstress.csv"/>
  <SolutionName Value="Solution"/>
 </ExportResponses>''';
simlab.execute(ExportResponses);

ExportSlb=''' <ExportSlb UUID="a155cd6e-8ae6-4720-8ab4-1f50d4a34d1c">
  <tag Value="-1"/>
  <Name Value=""/>
  <Option Value="1"/>
  <Duplicate Value="0"/>
  <FileName Value="./../Demo_Simlab_result.slb"/>
 </ExportSlb>''';
simlab.execute(ExportSlb);
