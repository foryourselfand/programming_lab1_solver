public class Main {
	public static void main(String[] args) {
		int[] e = {6, 8, 10, 12, 14, 16};
		
		float[] x = new float[15];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 24.0 - 9.0);
				
		double[][] f = new double[6][15];
		for (int i = 0; i < f.length; i++) {
			for (int j = 0; j < f[i].length; j++) {
				switch ((int) e[i]) {
					case 8:
						f[i][j] = Math.tan(Math.cbrt(Math.pow((x[j]), (x[j]/1/3))));
						break;
					case 12:
					case 14:
					case 16:
						f[i][j] = Math.atan(Math.pow(1/Math.E, (sqrt(Math.pow(Math.cos(x[j]), 2)))));
						break;
					default:
						f[i][j] = 2*Math.cos(Math.cos(x[j]/(x[j]-1)));
						break;
				}
				System.out.printf("%.2f ", f[i][j]);
			}
			System.out.println();
		}
	}
}
