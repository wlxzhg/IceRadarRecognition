import sys,Ice
import Servant

with Ice.initialize(sys.argv) as communicator:
	adapter = communicator.createObjectAdapterWithEndpoints("RadarUtilAdapter","default -p 10000");
	object = Servant.RadarUtilI()
	adapter.add(object,communicator.stringToIdentity("RadarUtil"))
	adapter.activate()
	communicator.waitForShutdown()