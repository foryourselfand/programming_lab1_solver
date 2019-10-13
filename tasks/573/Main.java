public class Main {
	public static void main(String[] args) {
		short[] c = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19};
		
		float[] x = new float[12];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 10.0 - 2.0);
				
		double[][] g = new double[18][12];
		for (int i = 0; i < g.length; i++) {
			for (int j = 0; j < g[i].length; j++) {
				switch ((int) c[i]) {
					case 10:
						g[i][j] = Math.pow(((1-Math.cbrt(Math.log(Math.abs(x[j]))))/2), (Math.log(Math.abs(x[j])/2)));
						break;
					case 3:
					case 5:
					case 6:
					case 7:
					case 8:
					case 9:
					case 13:
					case 14:
					case 15:
						g[i][j] = Math.tan(Math.tan(Math.log(Math.abs(x[j]))));
						break;
					default:
						g[i][j] = Math.cbrt(Math.atan(Math.sin(Math.log(Math.abs(x[j])))));
						break;
				}
				System.out.printf("%.4f ", g[i][j]);
			}
			System.out.println();
		}
	}
}
