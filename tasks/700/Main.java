public class Main {
	public static void main(String[] args) {
		long[] b = {25, 23, 21, 19, 17, 15, 13, 11, 9, 7};
		
		double[] x = new double[18];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 18.0 - 9.0;
				
		double[][] k = new double[10][18];
		for (int i = 0; i < k.length; i++) {
			for (int j = 0; j < k[i].length; j++) {
				switch ((int) b[i]) {
					case 17:
						k[i][j] = Math.log(sqrt(Math.acos(x[j]/18)));
						break;
					case 7:
					case 11:
					case 15:
					case 21:
					case 23:
						k[i][j] = Math.sin(Math.cos(Math.pow((2/3*x[j]), 3)));
						break;
					default:
						k[i][j] = Math.pow((2*Math.asin(Math.sin(Math.sin(Math.atan(x[j]/18))))), 2);
						break;
				}
				System.out.printf("%.4f ", k[i][j]);
			}
			System.out.println();
		}
	}
}
