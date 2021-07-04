#***************************************************************
#SimLab Version 2021 
#Created at Fri Jul  2 04:35:24 2021
#***************************************************************
#For debugging this python script,Please comment(#) out the line "from hwx import simlab" and uncomment the line "import simlab"
from hwx import simlab
#import simlab


UnitSystem=''' <UnitSystem UUID="3aca8564-4d38-4b0b-887c-6a542d4001c6">
  <SetCurrentDisplaySystem Name="MMKS (mm kg N s)"/>
 </UnitSystem>''';
simlab.execute(UnitSystem);
