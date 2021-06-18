#***************************************************************
#SimLab Version 2021 
#Created at Mon Jun  7 19:53:07 2021
#***************************************************************
#For debugging this python script,Please comment(#) out the line "from hwx import simlab" and uncomment the line "import simlab"
from hwx import simlab
#import simlab


UnitSystem=''' <UnitSystem UUID="3aca8564-4d38-4b0b-887c-6a542d4001c6">
  <SetCurrentDisplaySystem Name="MMKS (mm kg N s)"/>
 </UnitSystem>''';
simlab.execute(UnitSystem);

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
