public class Main {
	public static void main(String[] args) {
		long[] g = {19, 17, 15, 13, 11, 9, 7, 5};
		
		float[] x = new float[12];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 17.0 - 5.0);
				
		double[][] d = new double[8][12];
		for (int i = 0; i < d.length; i++) {
			for (int j = 0; j < d[i].length; j++) {
				switch ((int) g[i]) {
					case 11:
						d[i][j] = Math.pow((Math.tan(Math.log(Math.abs(x[j])))), (Math.pow((Math.pow((2/(1-x[j])), (x[j]))/2), 2)));
						break;
					case 5:
					case 9:
					case 13:
					case 17:
						d[i][j] = Math.pow((4/Math.atan(Math.pow(Math.E, (-Math.abs(x[j]))))), 2);
						break;
					default:
						d[i][j] = Math.pow(((Math.pow(1/2-Math.E, (Math.pow(Math.E, (Math.cbrt(x[j]))))))/0.25), 3);
						break;
				}
				System.out.printf("%.5f ", d[i][j]);
			}
			System.out.println();
		}
	}
}
