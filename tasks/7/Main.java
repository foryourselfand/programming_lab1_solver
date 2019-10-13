public class Main {
	public static void main(String[] args) {
		int[] k = {16, 14, 12, 10, 8, 6, 4};
		
		float[] x = new float[10];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 15.0 - 10.0);
				
		double[][] g = new double[7][10];
		for (int i = 0; i < g.length; i++) {
			for (int j = 0; j < g[i].length; j++) {
				switch ((int) k[i]) {
					case 10:
						g[i][j] = Math.asin(0.2*Math.cos(x[j]));
						break;
					case 8:
					case 12:
					case 14:
						g[i][j] = Math.cos(Math.atan(Math.pow(1/Math.E, (Math.abs(x[j])))));
						break;
					default:
						g[i][j] = Math.sin(Math.pow((Math.asin((x[j]-2.5)/15)*(1-Math.log(Math.abs(x[j])))), (Math.pow((x[j]), (x[j]/2))))/4);
						break;
				}
				System.out.printf("%.5f ", g[i][j]);
			}
			System.out.println();
		}
	}
}
