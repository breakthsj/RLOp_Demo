#Author-Hong
#Description- 단일소재 경량화를 위한 fusion360 바디생성 스크립트

import adsk.core, adsk.fusion, adsk.cam, traceback, csv

_commandId = 'Demo_weightop'
_workspaceToUse = 'FusionSolidEnvironment'
_panelToUse = 'SolidModifyPanel'

_handlers = []

def commandDefinitionById(id):
    app = adsk.core.Application.get()
    ui = app.userInterface
    if not id:
        ui.messageBox('commandDefinition id is not specified')
        return None
    commandDefinitions = ui.commandDefinitions
    commandDefinition = commandDefinitions.itemById(id)
    return commandDefinition

def commandControlByIdForPanel(id):
    app = adsk.core.Application.get()
    ui = app.userInterface
    if not id:
        ui.messageBox('commandControl id is not specified')
        return None
    workspaces = ui.workspaces
    modelingWorkspace = workspaces.itemById(_workspaceToUse)
    toolbarPanels = modelingWorkspace.toolbarPanels
    toolbarPanel = toolbarPanels.itemById(_panelToUse)
    toolbarControls = toolbarPanel.controls
    toolbarControl = toolbarControls.itemById(id)
    return toolbarControl

def destroyObject(uiObj, tobeDeleteObj):
    if uiObj and tobeDeleteObj:
        if tobeDeleteObj.isValid:
            tobeDeleteObj.deleteMe()
        else:
            uiObj.messageBox('tobeDeleteObj is not a valid object')

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface


        commandName = 'Demo_weightop'
        commandDescription = 'Demo_weightop\n'
        commandResources = './resources/command'

        class CommandExecuteHandler(adsk.core.CommandEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:
                    makebox()
                except:
                    if ui:
                        ui.messageBox('command executed failed:\n{}'.format(traceback.format_exc()))

        class CommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
            def __init__(self):
                super().__init__()
            def notify(self, args):
                try:
                    cmd = args.command
                    onExecute = CommandExecuteHandler()
                    cmd.execute.add(onExecute)
                    # keep the handler referenced beyond this function
                    _handlers.append(onExecute)

                except:
                    if ui:
                        ui.messageBox('Panel command created failed:\n{}'.format(traceback.format_exc()))


        commandDefinitions = ui.commandDefinitions

        # check if we have the command definition
        commandDefinition = commandDefinitions.itemById(_commandId)
        if not commandDefinition:
            commandDefinition = commandDefinitions.addButtonDefinition(_commandId, commandName, commandDescription, commandResources)


        onCommandCreated = CommandCreatedHandler()
        commandDefinition.commandCreated.add(onCommandCreated)
        # keep the handler referenced beyond this function
        _handlers.append(onCommandCreated)


        workspaces = ui.workspaces
        modelingWorkspace = workspaces.itemById(_workspaceToUse)
        toolbarPanels = modelingWorkspace.toolbarPanels
        toolbarPanel = toolbarPanels.itemById(_panelToUse)
        toolbarControlsPanel = toolbarPanel.controls
        toolbarControlPanel = toolbarControlsPanel.itemById(_commandId)
        if not toolbarControlPanel:
            toolbarControlPanel = toolbarControlsPanel.addCommand(commandDefinition, '')
            toolbarControlPanel.isVisible = True
            print('The Parameter I/O command was successfully added to the create panel in modeling workspace')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        objArray = []

        commandControlPanel = commandControlByIdForPanel(_commandId)
        if commandControlPanel:
            objArray.append(commandControlPanel)

        commandDefinition = commandDefinitionById(_commandId)
        if commandDefinition:
            objArray.append(commandDefinition)

        for obj in objArray:
            destroyObject(ui, obj)

    except:
        if ui:
            ui.messageBox('AddIn Stop Failed:\n{}'.format(traceback.format_exc()))

def makebox():
    app = adsk.core.Application.get()
    ui = app.userInterface

    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        # ui.messageBox('Hello script')

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        design.designType = adsk.fusion.DesignTypes.DirectDesignType

        # Get the root component of the active design.
        rootComp = design.rootComponent
        bodies = rootComp.bRepBodies

        # # Create sub occurrence
        # occurrences = rootComp.occurrences

        # 처음 파일 돌리는 경우 상,하판 생성 및 새로운 document
        if rootComp.bRepBodies.count == 0:
            doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

            product = app.activeProduct
            design = adsk.fusion.Design.cast(product)
            design.designType = adsk.fusion.DesignTypes.DirectDesignType

            # Get the root component of the active design.
            rootComp = design.rootComponent
            bodies = rootComp.bRepBodies

            # plate 생성
            bodies.add(makeplate(4, 4, 1, 1.5, 1.5, -1.0))
            bodies.add(makeplate(4, 4, 1, 1.5, 1.5, 4))

        # Get the root component of the active design.
        rootComp = design.rootComponent
        bodies = rootComp.bRepBodies

        # # bRepBody를 위한 컴포넌트생성
        # subOcc = occurrences.addNewComponent(adsk.core.Matrix3D.create())

        # csv 파일 받아오기
        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_weightop.csv"
        with open(csv_dir, 'r') as f:
            reader = csv.DictReader(f)
            dict_list = []
            for elemt in reader:
                dict_list.append(elemt)

        # action을 명령이 들어오면 0(비생성) or 1(생성)
        if int(dict_list[0]['G']) == 1:
            # 컴포넌트에 바디 생성
            bodies.add(makeCell(int(dict_list[0]['X']), int(dict_list[0]['Y']), int(dict_list[0]['Z'])))

        # # 생성 바디 컴포넌트 묶음
        # if rootComp.bRepBodies.count > 49:
        #     for j in reversed(range(0, rootComp.bRepBodies.count)):
        #         # ui.messageBox('{}'.format(j))
        #         body = rootComp.bRepBodies.item(j)
        #         body.moveToComponent(subOcc)
        # else:
        #     for j in range(0, rootComp.bRepBodies.count):
        #         body = rootComp.bRepBodies.item(j)
        #         body.copyToComponent(subOcc)

        # 로컬 저장
        folder = "C:/Users/break/Downloads/RLOp_Demo/Demo_weightop_0526/"

        # Construct the output filename.
        filename = folder + 'Box'

        # step파일 형태로 저장
        exportMgr = adsk.fusion.ExportManager.cast(design.exportManager)
        stpOptions = exportMgr.createSTEPExportOptions(filename, rootComp)
        exportMgr.execute(stpOptions)

        # 끝점(3,3,3)에 도달하면 doc 삭제
        if int(dict_list[0]['X']) + int(dict_list[0]['Y']) + int(dict_list[0]['Z']) == 9:
            app.documents.item(1).close(saveChanges=False)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def makeCell(X,Y,Z):
    # 포인트를 받아오면 포인트 기준 + 방향으로 블럭 생성
    app = adsk.core.Application.get()
    ui = app.userInterface

    try:
        # Get TemporaryBRepManager
        tempBrepMgr = adsk.fusion.TemporaryBRepManager.get()

        # 중심점, 길이, 폭 방향, 길이 설정
        centerPoint = adsk.core.Point3D.create(X, Y, Z);
        lengthDir = adsk.core.Vector3D.create(1.0, 0.0, 0.0)
        widthDir = adsk.core.Vector3D.create(0.0, 1.0, 0.0)
        orientedBoundingBox3D = adsk.core.OrientedBoundingBox3D.create(centerPoint,
                                                                       lengthDir,
                                                                       widthDir,
                                                                       1.0,
                                                                       1.0,
                                                                       1.0
                                                                       )

        # Create cell
        cell = tempBrepMgr.createBox(orientedBoundingBox3D)

        # product = app.activeProduct
        # design = adsk.fusion.Design.cast(product)
        # design.designType = adsk.fusion.DesignTypes.DirectDesignType
        #
        # # Get the root component of active design
        # rootComp = design.rootComponent
        #
        # # Get bodies in root component
        # bodies = rootComp.bRepBodies
        #
        # bodies.add(box)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

    return cell


def makeplate(X,Y,Z,cx,cy,cz):
    # 포인트를 받아오면 포인트 기준 + 방향으로 블럭 생성
    app = adsk.core.Application.get()
    ui = app.userInterface

    try:
        # Get TemporaryBRepManager
        tempBrepMgr = adsk.fusion.TemporaryBRepManager.get()

        # 중심점, 길이, 폭 방향, 길이 설정 / centerpoint=(x,y,z)
        centerPoint = adsk.core.Point3D.create(cx,cy,cz);
        lengthDir = adsk.core.Vector3D.create(1.0, 0.0, 0.0)
        widthDir = adsk.core.Vector3D.create(0.0, 1.0, 0.0)
        orientedBoundingBox3D = adsk.core.OrientedBoundingBox3D.create(centerPoint,
                                                                       lengthDir,
                                                                       widthDir,
                                                                       X,
                                                                       Y,
                                                                       Z
                                                                       )

        # Create plate
        plate = tempBrepMgr.createBox(orientedBoundingBox3D)

        # product = app.activeProduct
        # design = adsk.fusion.Design.cast(product)
        # design.designType = adsk.fusion.DesignTypes.DirectDesignType
        #
        # # Get the root component of active design
        # rootComp = design.rootComponent
        #
        # # Get bodies in root component
        # bodies = rootComp.bRepBodies
        #
        # bodies.add(box)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

    return plate