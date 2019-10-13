public class Main {
	public static void main(String[] args) {
		int[] f = {3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25};
		
		double[] x = new double[15];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 14.0 - 6.0;
				
		double[][] l = new double[12][15];
		for (int i = 0; i < l.length; i++) {
			for (int j = 0; j < l[i].length; j++) {
				switch ((int) f[i]) {
					case 19:
						l[i][j] = Math.pow((Math.atan(0.2*(x[j]+1)/14)), (0.25/(Math.asin(Math.pow(Math.E, (-Math.abs(x[j]))))-1)));
						break;
					case 5:
					case 9:
					case 11:
					case 13:
					case 17:
					case 23:
						l[i][j] = Math.cos(Math.cos(Math.cbrt(x[j])));
						break;
					default:
						l[i][j] = Math.pow((0.25-Math.pow((Math.cbrt(Math.pow((x[j]), (x[j]-3/4)))), (3+Math.cos(Math.cbrt(x[j]))))), (Math.asin(Math.pow(Math.E, (Math.cbrt(-Math.pow((4/Math.abs(x[j])), (x[j]))))))));
						break;
				}
				System.out.printf("%.4f ", l[i][j]);
			}
			System.out.println();
		}
	}
}
