public class Main {
	public static void main(String[] args) {
		long[] f = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19};
		
		float[] x = new float[16];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 23.0 - 12.0);
				
		double[][] n = new double[14][16];
		for (int i = 0; i < n.length; i++) {
			for (int j = 0; j < n[i].length; j++) {
				switch ((int) f[i]) {
					case 13:
						n[i][j] = Math.pow((3/4/(Math.pow((Math.sin(x[j])*(Math.pow((x[j]), ((x[j]+1)/x[j]))-1/2)), 2-1))), 2);
						break;
					case 6:
					case 8:
					case 9:
					case 11:
					case 15:
					case 16:
					case 19:
						n[i][j] = Math.pow((Math.pow((Math.log(Math.abs(x[j]))*(0.25+Math.asin((x[j]-0.5)/23))), (Math.pow(((1/2+x[j])/x[j]), 3)))), (Math.pow(Math.E, (Math.pow((2*x[j]), 3)))));
						break;
					default:
						n[i][j] = 2*Math.pow((Math.tan(Math.pow((x[j]), 2))/(Math.cbrt(Math.pow((Math.PI/(x[j]+1)), (x[j])))-1)), 3);
						break;
				}
				System.out.printf("%.4f ", n[i][j]);
			}
			System.out.println();
		}
	}
}
