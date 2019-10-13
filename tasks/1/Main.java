public class Main {
	public static void main(String[] args) {
		int[] f = {3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25};
		
		double[] x = new double[15];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 14.0 - 6.0;
				
		double[][] l = new double[12][15];
		for (int i = 0; i < l.length; i++) {
			for (int j = 0; j < l[i].length; j++) {
				switch (f[i]) {
					case 19:
						l[i][j] = (arctan(0.2*(x+1)/14))^(0.25/(arcsin(e^(-abs(x)))-1));
						break;
					case 5:
					case 9:
					case 11:
					case 13:
					case 17:
					case 23:
						l[i][j] = cos(cos(root(3)(x)));
						break;
					default:
						l[i][j] = (0.25-(root(3)((x)^(x-3/4)))^(3+cos(root(3)(x))))^(arcsin(e^(root(3)(-(4/abs(x))^(x)))));
						break;
				}
				System.out.printf("%.4f ", l[i][j]);
			}
			System.out.println();
		}
	}
}
