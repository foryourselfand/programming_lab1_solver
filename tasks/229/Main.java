public class Main {
	public static void main(String[] args) {
		short[] f = {15, 13, 11, 9, 7, 5, 3};
		
		float[] x = new float[15];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 12.0 - 4.0);
				
		double[][] k = new double[7][15];
		for (int i = 0; i < k.length; i++) {
			for (int j = 0; j < k[i].length; j++) {
				switch ((int) f[i]) {
					case 5:
						k[i][j] = Math.pow((2*Math.cbrt(Math.pow((x[j]), ((x[j]-3/4)/0.25)))), 3);
						break;
					case 7:
					case 9:
					case 11:
						k[i][j] = Math.pow((Math.asin(Math.pow(((x[j]+2)/12), 2))*(3+Math.pow((Math.cbrt(x[j])*(1-Math.cbrt(x[j]))), 2))), (Math.sin(Math.pow((x[j]*(x[j]-Math.PI)), 2))));
						break;
					default:
						k[i][j] = Math.tan(Math.cbrt(Math.pow((2/Math.tan(x[j])), (Math.pow((x[j]), ((x[j]-1)/1/2))))));
						break;
				}
				System.out.printf("%.2f ", k[i][j]);
			}
			System.out.println();
		}
	}
}
