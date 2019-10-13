public class Main {
	public static void main(String[] args) {
		short[] g = {4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24};
		
		float[] x = new float[12];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 16.0 - 9.0);
				
		double[][] c = new double[11][12];
		for (int i = 0; i < c.length; i++) {
			for (int j = 0; j < c[i].length; j++) {
				switch ((int) g[i]) {
					case 4:
						c[i][j] = Math.atan(Math.cos(Math.pow(Math.E, (Math.pow((2*x[j]), (x[j]))))));
						break;
					case 6:
					case 10:
					case 12:
					case 14:
					case 20:
						c[i][j] = Math.pow(Math.E, (Math.pow(Math.E, (Math.cbrt(x[j])))));
						break;
					default:
						c[i][j] = Math.log(Math.pow((sqrt(Math.pow(Math.sin(x[j]), 2))/2), (Math.tan(Math.tan(x[j])))));
						break;
				}
				System.out.printf("%.4f ", c[i][j]);
			}
			System.out.println();
		}
	}
}
