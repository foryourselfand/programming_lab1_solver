public class Main {
	public static void main(String[] args) {
		int[] g = {3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25};
		
		double[] x = new double[15];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 14.0 - 6.0;
				
		double[][] d = new double[14][20];
		for (int i = 0; i < d.length; i++) {
			for (int j = 0; j < d[i].length; j++) {
				switch ((int) b[i]) {
					case 7:
						d[i][j] = Math.asin(Math.pow(Math.E, Math.cbrt(- Math.pow(Math.sin(x[j]), 2))));
						break;
					case 5:
					case 6:
					case 8:
					case 9:
					case 15:
					case 16:
					case 17:
						d[i][j] = Math.sin(Math.pow(3 * (Math.cos(x[j]) - 1), Math.pow(3 * x[j], 3)));
						break;
					default:
						d[i][j] = Math.pow(Math.E, Math.pow(Math.E, 4 * ((1 / 2) + x[j])));
						break;
				}
				System.out.printf("%.3f ", d[i][j]);
			}
			System.out.println();
		}
	}
}
