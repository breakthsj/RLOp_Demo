#Author-Hong
#Description-test1

import adsk.core, adsk.fusion, adsk.cam, traceback, csv

_commandId = 'com_demo'
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


        commandName = 'com_demo'
        commandDescription = 'MakeBox to a CSV (Comma Separated Values) file\n'
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
    design = app.activeProduct

    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        # ui.messageBox('Hello script')

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        design.designType = adsk.fusion.DesignTypes.DirectDesignType

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create sub occurrence
        occurrences = rootComp.occurrences

        # bRepBody??? ?????? ??????????????????
        bodies = rootComp.bRepBodies
        subOcc = occurrences.addNewComponent(adsk.core.Matrix3D.create())

        # csv ?????? ????????????
        csv_dir = r"C:\Users\break\Downloads\Fusion360_script\Demo\demo_com_0514\demo_com.csv"
        with open(csv_dir, 'r') as f:
            reader = csv.DictReader(f)
            dict_list = []
            for elemt in reader:
                dict_list.append(elemt)

        # ??????????????? ?????? ??????
        bodies.add(makeblock(int(dict_list[0]['X']), int(dict_list[0]['Y']), int(dict_list[0]['Z'])))

        # ?????? ?????? ???????????? ??????
        if rootComp.bRepBodies.count > 49:
            for j in reversed(range(0, rootComp.bRepBodies.count)):
                # ui.messageBox('{}'.format(j))
                body = rootComp.bRepBodies.item(j)
                body.moveToComponent(subOcc)
        else:
            for j in range(0, rootComp.bRepBodies.count):
                body = rootComp.bRepBodies.item(j)
                body.copyToComponent(subOcc)

        # ???????????? ???????????? / ?????? ??????
        phypro = subOcc.getPhysicalProperties()
        com = phypro.centerOfMass
        # ??????????????? ???????????? ?????? ?????????
        origin = adsk.core.Point3D.create()
        comd = int(com.distanceTo(origin))

        # ???????????? ???????????? ???????????? ????????? ??????
        dict_list[0]['C'] = comd

        # csv ?????? ????????????_com ????????? ??????
        field = ['X', 'Y', 'Z', 'C']
        with open(csv_dir, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writeheader()
            writer.writerows(dict_list)

        # ?????? ??????
        folder = 'C:/Users/break/Downloads/Fusion360_script/Demo/demo_com_0514/'

        # Construct the output filename.
        filename = folder + 'Box'

        # Save the file as f3d.
        exportMgr = adsk.fusion.ExportManager.cast(design.exportManager)
        f3dOptions = exportMgr.createFusionArchiveExportOptions(filename, rootComp)
        exportMgr.execute(f3dOptions)

        # ???????????? ??????
        subOcc.deleteMe()

        # # ?????? ????????? 50(??????)?????? ?????? ???????????? ??????
        # if rootComp.bRepBodies.count > 4:
        #     for i in range(0, rootComp.bRepBodies.count):
        #         body = rootComp.bRepBodies.item(i)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def makeblock(X,Y,Z):
    # ???????????? ???????????? ????????? ?????? + ???????????? ?????? ??????
    app = adsk.core.Application.get()
    ui = app.userInterface

    try:
        # Get TemporaryBRepManager
        tempBrepMgr = adsk.fusion.TemporaryBRepManager.get()

        # ?????????, ??????, ??? ??????, ?????? ??????
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

        # Create box
        box = tempBrepMgr.createBox(orientedBoundingBox3D)

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

    return box