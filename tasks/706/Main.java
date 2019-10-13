public class Main {
	public static void main(String[] args) {
		short[] f = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17};
		
		float[] x = new float[15];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 21.0 - 6.0);
				
		double[][] k = new double[15][15];
		for (int i = 0; i < k.length; i++) {
			for (int j = 0; j < k[i].length; j++) {
				switch ((int) f[i]) {
					case 15:
						k[i][j] = Math.tan(Math.pow((2*(x[j]+1)), 3/0.25));
						break;
					case 4:
					case 6:
					case 9:
					case 10:
					case 13:
					case 14:
					case 16:
						k[i][j] = Math.pow((2/3*Math.cos(Math.pow((x[j]), (x[j]/3/4)))), 2);
						break;
					default:
						k[i][j] = Math.tan(Math.sin(Math.cbrt(Math.pow((x[j]/3), 2))));
						break;
				}
				System.out.printf("%.3f ", k[i][j]);
			}
			System.out.println();
		}
	}
}
