public class Main {
	public static void main(String[] args) {
		long[] d = {19, 17, 15, 13, 11, 9, 7, 5, 3, 1};
		
		float[] x = new float[10];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 19.0 - 14.0);
				
		double[][] k = new double[10][10];
		for (int i = 0; i < k.length; i++) {
			for (int j = 0; j < k[i].length; j++) {
				switch ((int) d[i]) {
					case 11:
						k[i][j] = Math.tan(Math.sin(Math.tan(x[j])));
						break;
					case 3:
					case 5:
					case 9:
					case 15:
					case 17:
						k[i][j] = Math.sin(Math.sin(Math.pow(Math.E, (x[j]))));
						break;
					default:
						k[i][j] = Math.cos(Math.pow((1-Math.atan(Math.sin(x[j]))), (Math.sin(x[j]*(1/2+x[j])))));
						break;
				}
				System.out.printf("%.5f ", k[i][j]);
			}
			System.out.println();
		}
	}
}
