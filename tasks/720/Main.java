public class Main {
	public static void main(String[] args) {
		short[] g = {3, 5, 7, 9, 11, 13, 15, 17, 19};
		
		double[] x = new double[15];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 21.0 - 12.0;
				
		double[][] g = new double[9][15];
		for (int i = 0; i < g.length; i++) {
			for (int j = 0; j < g[i].length; j++) {
				switch ((int) g[i]) {
					case 5:
						g[i][j] = (2/3+Math.pow((Math.cos(x[j])/1/3), 2))/2;
						break;
					case 7:
					case 9:
					case 11:
					case 13:
						g[i][j] = Math.tan(Math.cbrt(Math.log(Math.abs(x[j]))));
						break;
					default:
						g[i][j] = Math.pow(((Math.pow(2/3-Math.E, (Math.pow(Math.E, (Math.pow((1/3*(x[j]+1)), (x[j])))))))/1/4), 2);
						break;
				}
				System.out.printf("%.4f ", g[i][j]);
			}
			System.out.println();
		}
	}
}
