#***************************************************************
#SimLab Version 2021
#Created at Thu Jun 24 16:31:32 2021
#***************************************************************
#For debugging this python script,Please comment(#) out the line "from hwx import simlab" and uncomment the line "import simlab"
from hwx import simlab
#import simlab

simlab.messageBox.popupmsg("작동 이상 없음")
def generate():
    UnitSystem=''' <UnitSystem UUID="3aca8564-4d38-4b0b-887c-6a542d4001c6">
      <SetCurrentDisplaySystem Name="MMKS (mm kg N s)"/>
     </UnitSystem>''';
    simlab.execute(UnitSystem);

    Box=''' <CreateBox UUID="B219E9B4-B76A-410d-8BF7-C83FC40651FC">
      <BoxDefinition Value="2"/>
      <BodyType Value="Mesh"/>
      <Origin Value="-15 mm,-15 mm,-5 mm"/>
      <BoxDimension X_Length="30 mm" Z_Length="10 mm" Y_Length="30 mm"/>
      <DirectionVector X="1.000000000000,0.000000000000,0.000000000000" Y="0.000000000000,1.000000000000,0.000000000000" Z="0.000000000000,0.000000000000,1.000000000000"/>
      <Mesh>
       <ElementType Value="Hex8"/>
       <NumberOfElements X="1" Y="1" Checked="1" Z="1"/>
       <MeshSize Value="0 mm" Checked="0"/>
      </Mesh>
      <BodyName Value="Plate1"/>
      <Model Value="Box_Mesh1" Existing="0"/>
     </CreateBox>''';
    simlab.execute(Box);

    Box=''' <CreateBox UUID="B219E9B4-B76A-410d-8BF7-C83FC40651FC">
      <BoxDefinition Value="2"/>
      <BodyType Value="Mesh"/>
      <Origin Value="-15 mm,-15 mm,15 mm"/>
      <BoxDimension X_Length="30 mm" Z_Length="10 mm" Y_Length="30 mm"/>
      <DirectionVector X="1.000000000000,0.000000000000,0.000000000000" Y="0.000000000000,1.000000000000,0.000000000000" Z="0.000000000000,0.000000000000,1.000000000000"/>
      <Mesh>
       <ElementType Value="Hex8"/>
       <NumberOfElements X="1" Y="1" Checked="1" Z="1"/>
       <MeshSize Value="0 mm" Checked="0"/>
      </Mesh>
      <BodyName Value="Upper_Plate"/>
      <Model Value="Box_Mesh1.gda" Existing="1"/>
     </CreateBox>''';
    simlab.execute(Box);

    Box=''' <CreateBox UUID="B219E9B4-B76A-410d-8BF7-C83FC40651FC">
      <BoxDefinition Value="2"/>
      <BodyType Value="Mesh"/>
      <Origin Value="-5 mm,-5 mm,5 mm"/>
      <BoxDimension X_Length="10 mm" Z_Length="10 mm" Y_Length="10 mm"/>
      <DirectionVector X="1.000000000000,0.000000000000,0.000000000000" Y="0.000000000000,1.000000000000,0.000000000000" Z="0.000000000000,0.000000000000,1.000000000000"/>
      <Mesh>
       <ElementType Value="Hex8"/>
       <NumberOfElements X="1" Y="1" Checked="1" Z="1"/>
       <MeshSize Value="0 mm" Checked="0"/>
      </Mesh>
      <BodyName Value="UnitCell"/>
      <Model Value="Box_Mesh1.gda" Existing="1"/>
     </CreateBox>''';
    simlab.execute(Box);

    Box=''' <CreateBox UUID="B219E9B4-B76A-410d-8BF7-C83FC40651FC">
      <BoxDefinition Value="2"/>
      <BodyType Value="Mesh"/>
      <Origin Value="-15 mm,-15 mm,5 mm"/>
      <BoxDimension X_Length="10 mm" Z_Length="10 mm" Y_Length="10 mm"/>
      <DirectionVector X="1.000000000000,0.000000000000,0.000000000000" Y="0.000000000000,1.000000000000,0.000000000000" Z="0.000000000000,0.000000000000,1.000000000000"/>
      <Mesh>
       <ElementType Value="Hex8"/>
       <NumberOfElements X="1" Y="1" Checked="1" Z="1"/>
       <MeshSize Value="0 mm" Checked="0"/>
      </Mesh>
      <BodyName Value="UnitCell2"/>
      <Model Value="Box_Mesh1.gda" Existing="1"/>
     </CreateBox>''';
    simlab.execute(Box);

    BodyMergeRightClick=''' <BodyMergeRightClick UUID="7d2fbe6f-4dd7-4848-8cb5-f8be2d72c418" CheckBox="ON">
      <tag Value="-1"/>
      <ModelId Value=""/>
      <BodyId>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Body>"UnitCell","UnitCell2",</Body>
       </Entities>
      </BodyId>
      <RedoFlag Value=""/>
      <Output/>
     </BodyMergeRightClick>''';
    simlab.execute(BodyMergeRightClick);

    DropTestParameters=''' <DropTestParameters UUID="467f776e-febc-4c63-8fde-b4a01fbb61c9">
      <InputBodies>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Body>"UnitCell",</Body>
       </Entities>
      </InputBodies>
      <MeshType Value=""/>
      <MeshSize Value=""/>
      <MinimumElementSize Value=""/>
      <Material Name="Aluminium"/>
      <QualitySpec Name=""/>
     </DropTestParameters>''';
    simlab.execute(DropTestParameters);

    AssignMaterial=''' <AssignMaterial UUID="22fe2ea3-c38e-4992-b9b4-80dbf7b733ac">
      <Material Name="Steel"/>
      <SupportEntities>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Body>"Upper_Plate","Plate1",</Body>
       </Entities>
      </SupportEntities>
     </AssignMaterial>''';
    simlab.execute(AssignMaterial);

    CreateSolution=''' <CreateSolution UUID="1210abd7-c815-4f67-8615-6ab616274dcc">
      <tag Value="-1"/>
      <Name Value="Solution"/>
      <SolutionType Value="LINEAR"/>
      <Solver Value="OPTISTRUCT"/>
      <SupportEntities>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
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

    ForceandMoment=''' <Force UUID="af4acb9c-542e-47aa-9ddc-ca6001e13175" BCType="Force">
      <tag Value="-1"/>
      <Name Value="Force_2"/>
      <ForceEntities>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Face>59,</Face>
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

    FixedConstraint=''' <Fixed UUID="f5ecfc0a-a238-477c-928c-e81c22353a69" isObject="2" BCType="Constraint">
      <tag Value="-1"/>
      <Name Value="Face_Constraint_3"/>
      <FixedEntities>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Face>14,</Face>
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
        <ITEM TYPE="EDITBOX" VALUE="Linear Static Step" NAME="Title" DATATYPE="STRING"/>
        <ITEM TYPE="COMBOBOX" VALUE="1" NAME="Format" DATATYPE="INT"/>
        <ITEM TYPE="COMBOBOX" VALUE="0" NAME="Numbering" DATATYPE="INT"/>
        <ITEM TYPE="CHECKBOX" VALUE="0" NAME="Write Linear Elements" DATATYPE="BOOL"/>
        <ITEM TYPE="COMBOBOX" VALUE="0" NAME="Spring Element Card Format" DATATYPE="INT"/>
        <ITEM TYPE="CHECKBOX" VALUE="0" NAME="Write Contact Slave Surface as SURF" DATATYPE="BOOL"/>
        <ITEM TYPE="CHECKBOX" VALUE="1" NAME="Write Enforced Displacements as SPCD" DATATYPE="BOOL"/>
        <ITEM TYPE="CHECKEDITBOX" VALUE="20" STATUS="OFF" NAME="Global initial temperature" DATATYPE="DOUBLE"/>
        <ITEM TYPE="CHECKEDITBOX" VALUE="100" STATUS="OFF" NAME="Initial memory allocation (MB)" DATATYPE="DOUBLE"/>
        <ITEM TYPE="COMBOBOX" VALUE="0" NAME="PBUSHFORM" DATATYPE="INT"/>
        <ITEM TYPE="CHECKBOX" VALUE="1" NAME="Write Material" DATATYPE="DOUBLE"/>
        <ITEM TYPE="EDITBOXWITHBROWSER" VALUE="" NAME="External File" DATATYPE="USER"/>
        <ITEM TYPE="EDITBOX" VALUE="24" NAME="Number of Processors" DATATYPE="INT"/>
        <ITEM TYPE="EDITBOX" VALUE="0" NAME="RAM Allocation" DATATYPE="INT"/>
        <ITEM TYPE="EDITBOX" VALUE="" NAME="Additional_Arguments" DATATYPE="STRING"/>
       </AnalysisType>
      </AnalysisType>
     </ExportOptions>''';
    simlab.execute(ExportOptions);

    CreateResponseNew=''' <CreateResponseNew UUID="a7326802-d869-41d4-a46d-d4d5c159d938">
      <tag Value="-1"/>
      <Name Value="Stress"/>
      <Response LoadCase="" ModeIndex="" Type="Stress" Component="Von Mises"/>
      <AllBodies Value="0"/>
      <SupportEntities>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Body>"UnitCell",</Body>
       </Entities>
      </SupportEntities>
      <Sets Value=""/>
      <Interested_Regions/>
      <Ignore_Regions/>
      <ValueType Value="Maximum"/>
      <SolutionName Value="Solution"/>
     </CreateResponseNew>''';
    simlab.execute(CreateResponseNew);

    ExportMassProperties=''' <ExportMassProperties UUID="0fd1f4ae-0e76-4125-a915-ef18f37b0e08">
      <tag Value="-1"/>
      <SupportEntities>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Body>"UnitCell",</Body>
       </Entities>
      </SupportEntities>
      <FileName Value="./Mass_Properties_Export.csv"/>
      <CoordID Value="Global"/>
      <Mass Value=""/>
     </ExportMassProperties>''';
    simlab.execute(ExportMassProperties);

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
      <SupportEntities Value="" ModelIds="" EntityTypes=""/>
      <UnitSystem Value="MKS (m kg N s)"/>
     </ExportStaticSolverInput>''';
    simlab.execute(ExportandSolve);

    DefineContact=''' <Contact UUID="3b4a24b5-6aea-49d3-b74a-82bf5b3ec193" isObject="2" CheckBox="ON" pixmap="sizemeshcontrol" customselection="1" BCType="Contact">
      <tag Value="-1"/>
      <Name Value="Upper_Plate_UnitCell"/>
      <New Value="1"/>
      <Entity Index="0" Value="Body"/>
      <MasterEntity>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Body>"Upper_Plate",</Body>
       </Entities>
      </MasterEntity>
      <SlaveEntity>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Body>"UnitCell",</Body>
       </Entities>
      </SlaveEntity>
      <IgnoreEdges Value="" ModelIds="" EntityTypes=""/>
      <MasterSet Value=""/>
      <SlaveSet Value=""/>
      <ContactBodyPairList/>
      <Trim Value="None"/>
      <SurfaceInteraction Index="0" Value="None"/>
      <PressFit Index="0" Value="None"/>
      <ContactFaceType Value="All"/>
      <Tolerance Value="1.44444 mm"/>
      <UserContactName Value="0" value=""/>
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
        <FrictionCoefficients c5="" c4="" c3="" c1="" c6="" c2=""/>
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

    DefineContact=''' <Contact UUID="3b4a24b5-6aea-49d3-b74a-82bf5b3ec193" isObject="2" CheckBox="ON" pixmap="sizemeshcontrol" customselection="1" BCType="Contact">
      <tag Value="-1"/>
      <Name Value="Plate1_UnitCell"/>
      <New Value="1"/>
      <Entity Index="0" Value="Body"/>
      <MasterEntity>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Body>"Plate1",</Body>
       </Entities>
      </MasterEntity>
      <SlaveEntity>
       <Entities>
        <Model>Box_Mesh1.gda</Model>
        <Body>"UnitCell",</Body>
       </Entities>
      </SlaveEntity>
      <IgnoreEdges Value="" ModelIds="" EntityTypes=""/>
      <MasterSet Value=""/>
      <SlaveSet Value=""/>
      <ContactBodyPairList/>
      <Trim Value="None"/>
      <SurfaceInteraction Index="0" Value="None"/>
      <PressFit Index="0" Value="None"/>
      <ContactFaceType Value="All"/>
      <Tolerance Value="1.44444 mm"/>
      <UserContactName Value="0" value=""/>
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
        <FrictionCoefficients c5="" c4="" c3="" c1="" c6="" c2=""/>
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
      <SupportEntities Value="" ModelIds="" EntityTypes=""/>
      <UnitSystem Value="MKS (m kg N s)"/>
     </ExportStaticSolverInput>''';
    simlab.execute(ExportandSolve);

    ExportandSolve=''' <ExportStaticSolverInput UUID="f009bc99-991f-43b7-8c87-cc606ef9c443" pixmap="solution">
      <tag Value="-1"/>
      <Name Value=""/>
      <SolverName Value=""/>
      <FileName Value="./Stress_Export.fem"/>
      <Solution Value="Solution"/>
      <WriteMode ValueText="Default" Value="0"/>
      <LoadCase Value=""/>
      <Renumber Value="0"/>
      <RunSolver Value="0"/>
      <DataCheck Value="0"/>
      <RemoveOrphanNodes Value="1"/>
      <AnalysisType Index="" Value=""/>
      <Version Value="14"/>
      <ExportOptionsVersion Value="1"/>
      <RemoteSolve Value="0"/>
      <CopyIncludeFiles Value="1"/>
      <SupportEntities Value="" ModelIds="" EntityTypes=""/>
      <UnitSystem Value="MKS (m kg N s)"/>
     </ExportStaticSolverInput>''';
    simlab.execute(ExportandSolve);
