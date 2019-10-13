public class Main {
	public static void main(String[] args) {
		long[] g = {19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5};
		
		double[] x = new double[17];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 19.0 - 6.0;
				
		double[][] f = new double[15][17];
		for (int i = 0; i < f.length; i++) {
			for (int j = 0; j < f[i].length; j++) {
				switch ((int) g[i]) {
					case 13:
						f[i][j] = Math.atan(Math.pow(Math.E, (Math.cbrt(-Math.pow((3/Math.abs(x[j])), (x[j]))))));
						break;
					case 5:
					case 6:
					case 8:
					case 11:
					case 17:
					case 18:
					case 19:
						f[i][j] = Math.pow((2/Math.pow((Math.cbrt(x[j])/2), (x[j]/2/3))), (Math.cbrt(Math.tan(x[j]))));
						break;
					default:
						f[i][j] = Math.pow((Math.pow((Math.cbrt(x[j])/2), (Math.sin(x[j])))), 2);
						break;
				}
				System.out.printf("%.3f ", f[i][j]);
			}
			System.out.println();
		}
	}
}
