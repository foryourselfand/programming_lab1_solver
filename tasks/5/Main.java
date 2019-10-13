public class Main {
	public static void main(String[] args) {
		long[] b = {6, 8, 10, 12, 14, 16, 18, 20, 22};
		
		double[] x = new double[16];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 15.0 - 13.0;
				
		double[][] a = new double[9][16];
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				switch (b[i]) {
					case 12:
						a[i][j] = arctan(((x-5.5)/15)^2)/2;
						break;
					case 16:
					case 18:
					case 20:
					case 22:
						a[i][j] = (2*e^(root(3)(x)))^2;
						break;
					default:
						a[i][j] = root(3)(e^(arctan(1/4*(x-5.5)/15)));
						break;
				}
				System.out.printf("%.2f ", a[i][j]);
			}
			System.out.println();
		}
	}
}
