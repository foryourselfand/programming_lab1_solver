public class Main {
	public static void main(String[] args) {
		long[] b = {6, 8, 10, 12, 14, 16, 18, 20, 22};
		
		double[] x = new double[16];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 15.0 - 13.0;
				
		double[][] a = new double[9][16];
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				switch ((int) b[i]) {
					case 12:
						a[i][j] = Math.atan(Math.pow(((x[j]-5.5)/15), 2))/2;
						break;
					case 16:
					case 18:
					case 20:
					case 22:
						a[i][j] = Math.pow((Math.pow(2*Math.E, (Math.cbrt(x[j])))), 2);
						break;
					default:
						a[i][j] = Math.cbrt(Math.pow(Math.E, (Math.atan(1/4*(x[j]-5.5)/15))));
						break;
				}
				System.out.printf("%.2f ", a[i][j]);
			}
			System.out.println();
		}
	}
}
