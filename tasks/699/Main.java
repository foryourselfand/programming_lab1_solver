public class Main {
	public static void main(String[] args) {
		long[] k = {19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
		
		float[] x = new float[18];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 24.0 - 14.0);
				
		double[][] d = new double[19][18];
		for (int i = 0; i < d.length; i++) {
			for (int j = 0; j < d[i].length; j++) {
				switch ((int) k[i]) {
					case 14:
						d[i][j] = (Math.pow((Math.pow((x[j]*(x[j]+2)), 3)), 2-1))/Math.cos(4+x[j]);
						break;
					case 4:
					case 7:
					case 8:
					case 10:
					case 11:
					case 12:
					case 15:
					case 18:
					case 19:
						d[i][j] = Math.log(Math.pow(Math.E, (Math.pow((Math.pow((x[j]), (x[j]*(x[j]-4)))), (Math.pow((2*x[j]), 2*)(Math.pow((0.25/(x[j]+2/3)), 3+1)))))));
						break;
					default:
						d[i][j] = Math.cbrt(Math.pow(Math.E, (Math.cbrt(Math.pow((2*x[j]), 2)))));
						break;
				}
				System.out.printf("%.5f ", d[i][j]);
			}
			System.out.println();
		}
	}
}
