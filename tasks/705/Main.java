public class Main {
	public static void main(String[] args) {
		int[] d = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
		
		float[] x = new float[19];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 13.0 - 10.0);
				
		double[][] k = new double[15][19];
		for (int i = 0; i < k.length; i++) {
			for (int j = 0; j < k[i].length; j++) {
				switch ((int) d[i]) {
					case 15:
						k[i][j] = Math.pow(((0.5-Math.tan(Math.pow((2*x[j]), 2)))/1/2), 3);
						break;
					case 7:
					case 8:
					case 11:
					case 13:
					case 16:
					case 17:
					case 18:
						k[i][j] = Math.cos(Math.cbrt(Math.sin(x[j])));
						break;
					default:
						k[i][j] = Math.asin(Math.pow(Math.E, (Math.cbrt(-Math.abs(Math.pow((0.25/(1-Math.sin(x[j]))), 3))))));
						break;
				}
				System.out.printf("%.3f ", k[i][j]);
			}
			System.out.println();
		}
	}
}
