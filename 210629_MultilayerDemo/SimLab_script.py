#***************************************************************
#SimLab Version 2021
#Created at Thu Jun 24 16:31:32 2021
#***************************************************************
#For debugging this python script,Please comment(#) out the line "from hwx import simlab" and uncomment the line "import simlab"

# 실제로 Agent에서 실행되는 파일은 C:\Program Files\Altair\2021\SimLab2021\unity\bin\win64 에 있음
from hwx import simlab
#import simlab

# 디버그용 메시지
simlab.messageBox.popupmsg("작동 이상 없음_from Generator")

def init():
    simlab.newDocument();

    UnitSystem = ''' <UnitSystem UUID="3aca8564-4d38-4b0b-887c-6a542d4001c6">
          <SetCurrentDisplaySystem Name="MMKS (mm kg N s)"/>
         </UnitSystem>''';
    simlab.execute(UnitSystem);

def plate():
    # 처음 시작 시 상,하판 생성
    Box=''' <CreateBox UUID="B219E9B4-B76A-410d-8BF7-C83FC40651FC">
      <BoxDefinition Value="2"/>
      <BodyType Value="Mesh"/>
      <Origin Value="-15 mm,-15 mm,-5 mm"/>
      <BoxDimension X_Length="30 mm" Z_Length="10 mm" Y_Length="30 mm"/>
      <DirectionVector X="1.000000000000,0.000000000000,0.000000000000" Y="0.000000000000,1.000000000000,0.000000000000" Z="0.000000000000,0.000000000000,1.000000000000"/>
      <Mesh>
       <ElementType Value="Hex8"/>
       <NumberOfElements X="1" Y="1" Checked="0" Z="1"/>
       <MeshSize Value="1 mm" Checked="1"/>
      </Mesh>
      <BodyName Value="Lower_Plate"/>
      <Model Value="InitPlate" Existing="0"/>
     </CreateBox>''';
    simlab.execute(Box);

    Box=''' <CreateBox UUID="B219E9B4-B76A-410d-8BF7-C83FC40651FC">
      <BoxDefinition Value="2"/>
      <BodyType Value="Mesh"/>
      <Origin Value="-15 mm,-15 mm,35 mm"/>
      <BoxDimension X_Length="30 mm" Z_Length="10 mm" Y_Length="30 mm"/>
      <DirectionVector X="1.000000000000,0.000000000000,0.000000000000" Y="0.000000000000,1.000000000000,0.000000000000" Z="0.000000000000,0.000000000000,1.000000000000"/>
      <Mesh>
       <ElementType Value="Hex8"/>
       <NumberOfElements X="1" Y="1" Checked="0" Z="1"/>
       <MeshSize Value="1 mm" Checked="1"/>
      </Mesh>
      <BodyName Value="Upper_Plate"/>
      <Model Value="InitPlate.gda" Existing="1"/>
     </CreateBox>''';
    simlab.execute(Box);

    CreateGroup = ''' <CreateGroup UUID="899db3a6-bd69-4a2d-b30f-756c2b2b1954" CheckBox="OFF" isObject="4">
          <tag Value="-1"/>
          <Name Value="sovle_Face" OldValue=""/>
          <SupportEntities>
           <Entities>
            <Model>InitPlate.gda</Model>
            <Face>59,14,</Face>
           </Entities>
          </SupportEntities>
          <Type Value="Face"/>
          <Color Value="255,206,0,"/>
          <Dup Value="0"/>
         </CreateGroup>''';
    simlab.execute(CreateGroup);

    AssignMaterial=''' <AssignMaterial UUID="22fe2ea3-c38e-4992-b9b4-80dbf7b733ac">
      <Material Name="Steel"/>
      <SupportEntities>
       <Entities>
        <Model>InitPlate.gda</Model>
        <Body>"Upper_Plate","Lower_Plate",</Body>
       </Entities>
      </SupportEntities>
     </AssignMaterial>''';
    simlab.execute(AssignMaterial);

def unitcell(x, y, z, cell_cnt):
    if cell_cnt == 1:
        Box=''' <CreateBox UUID="B219E9B4-B76A-410d-8BF7-C83FC40651FC">
          <BoxDefinition Value="2"/>
          <BodyType Value="Mesh"/>
          <Origin Value="{} mm,{} mm,{} mm"/>
          <BoxDimension X_Length="10 mm" Z_Length="10 mm" Y_Length="10 mm"/>
          <DirectionVector X="1.000000000000,0.000000000000,0.000000000000" Y="0.000000000000,1.000000000000,0.000000000000" Z="0.000000000000,0.000000000000,1.000000000000"/>
          <Mesh>
           <ElementType Value="Tri3"/>
           <NumberOfElements X="1" Y="1" Checked="0" Z="1"/>
           <MeshSize Value="1 mm" Checked="1"/>
          </Mesh>
          <BodyName Value="UnitCell{}"/>
          <Model Value="Unitcell" Existing="0"/>
         </CreateBox>'''.format(x, y, z, cell_cnt);
        simlab.execute(Box);
    else:
        Box=''' <CreateBox UUID="B219E9B4-B76A-410d-8BF7-C83FC40651FC">
          <BoxDefinition Value="2"/>
          <BodyType Value="Mesh"/>
          <Origin Value="{} mm,{} mm,{} mm"/>
          <BoxDimension X_Length="10 mm" Z_Length="10 mm" Y_Length="10 mm"/>
          <DirectionVector X="1.000000000000,0.000000000000,0.000000000000" Y="0.000000000000,1.000000000000,0.000000000000" Z="0.000000000000,0.000000000000,1.000000000000"/>
          <Mesh>
           <ElementType Value="Tri3"/>
           <NumberOfElements X="1" Y="1" Checked="0" Z="1"/>
           <MeshSize Value="1 mm" Checked="1"/>
          </Mesh>
          <BodyName Value="UnitCell{}"/>
          <Model Value="Unitcell.gda" Existing="1"/>
         </CreateBox>'''.format(x, y, z, cell_cnt);
        simlab.execute(Box);


def solve():
    Unitcells = simlab.getChildrenInAssembly("Unitcell.gda", "Unitcell.gda", "ALLBODIES")
    Unitcells = str(Unitcells).strip("()").replace("'",'"')

    Fuse = ''' <Fuse UUID="5796af66-2083-48aa-9fdb-3c15223838cb">
      <Entity>
       <Entities>
        <Model>Unitcell.gda</Model>
        <Body>'''+Unitcells+''',</Body>
       </Entities>
      </Entity>
      <Meshsize Value="1.00588 mm"/>
      <Tolerance Value="1 mm"/>
      <ScaleFactor Value="1.5"/>
      <PreserveInternalFace Value="1"/>
     </Fuse>''';
    simlab.execute(Fuse);

    ModelNames = simlab.getAllRootModelNames("FEM")

    MergeBodies = ''' <BodyMerge UUID="FA9128EE-5E6C-49af-BADF-4016E5622020" gda="">
      <tag Value="-1"/>
      <Name Value="BodyMerge7"/>
      <SupportEntities>
       <Entities>
        <Model>{}</Model>
        <Body></Body>
       </Entities>
      </SupportEntities>
      <Delete_Shared_Faces Value="0"/>
      <Output_Body_Name Value=""/>
      <RedoFlag Value=""/>
      <Output/>
     </BodyMerge>'''.format(ModelNames[0]);
    simlab.execute(MergeBodies);

    AssignMaterial = ''' <AssignMaterial UUID="22fe2ea3-c38e-4992-b9b4-80dbf7b733ac">
      <Material Name="Aluminium"/>
      <SupportEntities>
       <Entities>
        <Model>{}</Model>
        <Body></Body>
       </Entities>
      </SupportEntities>
     </AssignMaterial>'''.format(ModelNames[0]);
    simlab.execute(AssignMaterial);

    TetMesh = ''' <TetMesher UUID="83822e68-12bb-43b9-b2ac-77e0b9ea5149">
      <tag Value="-1"/>
      <Name Value="TetMesher19"/>
      <SupportEntities>
       <Entities>
        <Model>{}</Model>
        <Body></Body>
       </Entities>
      </SupportEntities>
      <MeshType Value="Tet4"/>
      <AverageElemSize Value="1 mm"/>
      <MaxElemSize Checked="0" Value="0"/>
      <InternalGrading Value="4"/>
      <MinQuality Value="0.1"/>
      <LinearQuality Value="0"/>
      <MaxQuality Value="1"/>
      <QuadMinQuality Value="0.001"/>
      <QuadQuality Value="0"/>
      <QuadMaxQuality Value="1"/>
      <CadBody Value="0"/>
      <IdentifyFeaturesAndMeshOnCAD Value="0"/>
      <AdvancedOptions>
       <MeshDensity Value="0"/>
       <CreateNewMeshModel Checked="0"/>
       <OutputModelName Value=""/>
       <Assembly Value="0"/>
       <PreserveFaceMesh Value="0"/>
       <MeshAsSingleBody Value="0"/>
       <Retain2DSurfaceBodies Value="0"/>
       <PreserveSurfaceSkew Checked="0" Value="55"/>
       <MixedMesh Value="0"/>
       <FillCavity Value="1"/>
      </AdvancedOptions>
     </TetMesher>'''.format(ModelNames[0]);
    simlab.execute(TetMesh);

    DeleteModel = ''' <DeleteModel updategraphics="0" CheckBox="ON" UUID="AE031126-6421-4633-8FAE-77C8DE10C18F">
      <ModelName Value="Unitcell.gda"/>
     </DeleteModel>''';
    simlab.execute(DeleteModel);

    MergeModels = ''' <MergeModels gda="" UUID="D630B49E-5180-456e-A2BF-58688DC76D4A">
      <tag Value="-1"/>
      <Name Value="Model"/>
      <SupportEntities EntityTypes="" ModelIds="" Value=""/>
      <Output/>
     </MergeModels>''';
    simlab.execute(MergeModels);

    Unitcells = simlab.getChildrenInAssembly("Merged_Model.gda", "Merged_Model.gda", "ALLBODIES")
    Unitcells = str(Unitcells).strip("()").replace("'", '"')

    CreateSolution = ''' <CreateSolution UUID="1210abd7-c815-4f67-8615-6ab616274dcc">
      <tag Value="-1"/>
      <Name Value="Solution"/>
      <SolutionType Value="LINEAR"/>
      <Solver Value="OPTISTRUCT"/>
      <SupportEntities>
       <Entities>
        <Model>Merged_Model.gda</Model>
        <Body>'''+Unitcells+''',,</Body>
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

    lodafaceArray = simlab.getEntityFromGroup('sovle_Face')

    FixedConstraint = ''' <Fixed isObject="2" BCType="Constraint" UUID="f5ecfc0a-a238-477c-928c-e81c22353a69">
      <tag Value="-1"/>
      <Name Value="Face_Constraint_4"/>
      <FixedEntities>
       <Entities>
        <Model>Merged_Model.gda</Model>
        <Face>{},</Face>
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
     </Fixed>'''.format(str(lodafaceArray[1]));
    simlab.execute(FixedConstraint);

    ForceandMoment = ''' <Force BCType="Force" UUID="af4acb9c-542e-47aa-9ddc-ca6001e13175">
      <tag Value="-1"/>
      <Name Value="Force_5"/>
      <ForceEntities>
       <Entities>
        <Model>Merged_Model.gda</Model>
        <Face>{},</Face>
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
     </Force>'''.format(str(lodafaceArray[0]));
    simlab.execute(ForceandMoment);

    ExportOptions = ''' <ExportOptions UUID="7a690756-a1f3-4e05-ba73-0bde6a497bd5" pixmap="solution">
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

    CreateResponseNew = ''' <CreateResponseNew UUID="a7326802-d869-41d4-a46d-d4d5c159d938">
          <tag Value="-1"/>
          <Name Value="Stress"/>
          <Response ModeIndex="" Component="Von Mises" LoadCase="" Type="Stress"/>
          <AllBodies Value="0"/>
          <SupportEntities>
           <Entities>
            <Model>Merged_Model.gda</Model>
            <Body></Body>
           </Entities>
          </SupportEntities>
          <Sets Value=""/>
          <Interested_Regions/>
          <Ignore_Regions/>
          <ValueType Value="Maximum"/>
          <SolutionName Value="Solution"/>
         </CreateResponseNew>''';
    simlab.execute(CreateResponseNew);

    ExportandSolve = ''' <ExportStaticSolverInput UUID="f009bc99-991f-43b7-8c87-cc606ef9c443" pixmap="solution">
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
          <SupportEntities EntityTypes="" ModelIds="" Value=""/>
          <UnitSystem Value="MKS (m kg N s)"/>
         </ExportStaticSolverInput>''';
    simlab.execute(ExportandSolve);

    ExportResponses = ''' <ExportResponses UUID="eb262d06-c529-4545-9596-c109bc7067e0">
          <FileName Value="./SimLab_response.csv"/>
          <SolutionName Value="Solution"/>
         </ExportResponses>''';
    simlab.execute(ExportResponses);

    # simlab.closeActiveDocument();


init()
plate()
unitcell(-15, -15, 5, 1)
unitcell(-5, -5, 15, 2)
unitcell(5, 5, 25, 3)
solve()
simlab.messageBox.popupmsg("작동 이상 없음_from Generator3")