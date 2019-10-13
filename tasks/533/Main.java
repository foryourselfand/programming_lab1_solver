public class Main {
	public static void main(String[] args) {
		short[] g = {5, 7, 9, 11, 13, 15, 17, 19};
		
		double[] x = new double[17];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 17.0 - 7.0;
				
		double[][] k = new double[8][17];
		for (int i = 0; i < k.length; i++) {
			for (int j = 0; j < k[i].length; j++) {
				switch ((int) g[i]) {
					case 9:
						k[i][j] = Math.cos(Math.pow(Math.E, (Math.pow((4*x[j]), 3))));
						break;
					case 11:
					case 13:
					case 15:
					case 19:
						k[i][j] = Math.tan(Math.asin(Math.sin(x[j])));
						break;
					default:
						k[i][j] = Math.log(Math.pow((Math.abs(x[j])/2), 2*)(Math.pow(2+Math.tan, 2)(Math.pow(Math.E, (Math.sin(x[j]))))));
						break;
				}
				System.out.printf("%.5f ", k[i][j]);
			}
			System.out.println();
		}
	}
}
