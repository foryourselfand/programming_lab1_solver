public class Main {
	public static void main(String[] args) {
		short[] g = {21, 19, 17, 15, 13, 11, 9, 7, 5};
		
		float[] x = new float[14];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 20.0 - 15.0);
				
		double[][] g = new double[9][14];
		for (int i = 0; i < g.length; i++) {
			for (int j = 0; j < g[i].length; j++) {
				switch ((int) g[i]) {
					case 15:
						g[i][j] = Math.cos(Math.sin(Math.pow((x[j]), (3/4*(x[j]+1/4)))));
						break;
					case 5:
					case 7:
					case 9:
					case 13:
						g[i][j] = Math.pow((Math.cos(Math.pow((1/4/(1-x[j])), 3))), (0.5*Math.log(Math.acos((x[j]-5)/2E+1))));
						break;
					default:
						g[i][j] = Math.cbrt(Math.tan(Math.cbrt(Math.pow((x[j]), (x[j])))));
						break;
				}
				System.out.printf("%.2f ", g[i][j]);
			}
			System.out.println();
		}
	}
}
