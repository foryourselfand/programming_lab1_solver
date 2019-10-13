public class Main {
	public static void main(String[] args) {
		short[] k = {20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6};
		
		double[] x = new double[10];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 20.0 - 8.0;
				
		double[][] b = new double[15][10];
		for (int i = 0; i < b.length; i++) {
			for (int j = 0; j < b[i].length; j++) {
				switch ((int) k[i]) {
					case 20:
						b[i][j] = Math.cbrt(Math.pow((Math.cos(x[j])*(2-x[j]-1)), (Math.pow(((0.5+x[j])/3), (x[j])))));
						break;
					case 8:
					case 9:
					case 11:
					case 12:
					case 17:
					case 18:
					case 19:
						b[i][j] = Math.atan(Math.sin(Math.tan(Math.sin(x[j]))));
						break;
					default:
						b[i][j] = Math.cos(Math.tan(Math.pow((Math.PI/(Math.pow(Math.E, (x[j]))-Math.PI)), (Math.cbrt(x[j])))));
						break;
				}
				System.out.printf("%.3f ", b[i][j]);
			}
			System.out.println();
		}
	}
}
