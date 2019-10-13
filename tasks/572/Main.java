public class Main {
	public static void main(String[] args) {
		int[] k = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19};
		
		double[] x = new double[13];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 17.0 - 14.0;
				
		double[][] g = new double[18][13];
		for (int i = 0; i < g.length; i++) {
			for (int j = 0; j < g[i].length; j++) {
				switch ((int) k[i]) {
					case 9:
						g[i][j] = Math.pow((Math.pow((Math.pow((x[j]), (2*x[j]))-1), 3/1/3)), 2);
						break;
					case 2:
					case 4:
					case 7:
					case 8:
					case 12:
					case 15:
					case 17:
					case 18:
					case 19:
						g[i][j] = Math.pow(((Math.tan(Math.pow((Math.PI/x[j]), 3))+1)/Math.pow((Math.sin(x[j])), ((Math.pow(1-Math.E, (x[j])))/Math.PI))), (Math.tan(Math.pow((1-x[j]), (x[j])))));
						break;
					default:
						g[i][j] = Math.cos(Math.cos(Math.log(Math.pow(Math.tan, 2)(x[j]))));
						break;
				}
				System.out.printf("%.3f ", g[i][j]);
			}
			System.out.println();
		}
	}
}
