public class Main {
	public static void main(String[] args) {
		long[] g = {22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2};
		
		double[] x = new double[12];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 18.0 - 15.0;
				
		double[][] f = new double[11][12];
		for (int i = 0; i < f.length; i++) {
			for (int j = 0; j < f[i].length; j++) {
				switch ((int) g[i]) {
					case 20:
						f[i][j] = Math.asin(Math.pow(Math.E, (Math.cbrt(-Math.abs(x[j])))));
						break;
					case 2:
					case 4:
					case 8:
					case 10:
					case 18:
						f[i][j] = Math.sin(Math.tan(Math.cbrt(x[j])));
						break;
					default:
						f[i][j] = Math.pow(Math.E, (Math.atan(Math.cos(Math.pow(Math.E, (x[j]/4))))));
						break;
				}
				System.out.printf("%.5f ", f[i][j]);
			}
			System.out.println();
		}
	}
}
