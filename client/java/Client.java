public class Client {
	public static void main(String[] args) {
		try(com.zeroc.Ice.Communicator communicator = com.zeroc.Ice.Util.initialize(args)) {
			com.zeroc.Ice.ObjectPrx base = communicator.stringToProxy("RadarUtil:default -p 10000");
			xidianRadar.RadarUtilPrx radarUtil = xidianRadar.RadarUtilPrx.checkedCast(base);
			if(radarUtil == null) {
				throw new Error("Invalid proxy");
			}
			int[][] r = {{1,1},{1,2}};
			int[] ret = radarUtil.recognitionRadar();
			for(int i : ret) {
				System.out.print(i + " ");
			}
		}
	}
}